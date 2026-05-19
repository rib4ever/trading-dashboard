import base64
import json
import mimetypes
import os
from typing import Any

import requests

from src.clients.google_drive_client import GoogleDriveClient
from src.clients.notion_client import NotionClient
from src.utils.config_loader import load_text_config
from src.utils.date_utils import now_iso


TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")
SCREENSHOTS_DATABASE_ID = os.environ.get("NOTION_SCREENSHOTS_DATABASE_ID")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_TRADE_REVIEW_MODEL", "gpt-4.1-mini")

AI_STATUS_READY = "Ready for AI Review"
AI_STATUS_COMPLETE = "AI Review Complete"
AI_STATUS_MORE_SCREENSHOTS = "Needs More Screenshots"
AI_STATUS_ERROR = "AI Review Error"

MAX_SCREENSHOTS = int(os.environ.get("AI_REVIEW_MAX_SCREENSHOTS", "5"))


def _prop(page: dict[str, Any], name: str) -> dict[str, Any] | None:
    return page.get("properties", {}).get(name)


def get_text(page: dict[str, Any], name: str) -> str | None:
    prop = _prop(page, name)
    if not prop:
        return None
    prop_type = prop.get("type")
    if prop_type == "title":
        return "".join(x.get("plain_text", "") for x in prop.get("title", [])) or None
    if prop_type == "rich_text":
        return "".join(x.get("plain_text", "") for x in prop.get("rich_text", [])) or None
    if prop_type == "select" and prop.get("select"):
        return prop["select"].get("name")
    if prop_type == "multi_select":
        return ", ".join(x.get("name", "") for x in prop.get("multi_select", [])) or None
    if prop_type == "status" and prop.get("status"):
        return prop["status"].get("name")
    if prop_type == "number":
        value = prop.get("number")
        return str(value) if value is not None else None
    if prop_type == "checkbox":
        return "Yes" if prop.get("checkbox") else "No"
    if prop_type == "date" and prop.get("date"):
        return prop["date"].get("start")
    if prop_type == "url":
        return prop.get("url")
    return None


def notion_rich_text(value: str) -> dict[str, Any]:
    return {"rich_text": [{"text": {"content": value[:1900]}}]}


def notion_select(value: str) -> dict[str, Any]:
    return {"select": {"name": value}}


def notion_number(value: float) -> dict[str, Any]:
    return {"number": value}


def notion_date(value: str) -> dict[str, Any]:
    return {"date": {"start": value}}


def query_ready_trades(notion: NotionClient) -> list[dict[str, Any]]:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    payload = {
        "filter": {
            "property": "AI Review Status",
            "select": {"equals": AI_STATUS_READY},
        }
    }
    return notion.query_database(TRADES_DATABASE_ID, payload)


def query_screenshot_records(notion: NotionClient, trade_id: str) -> list[dict[str, Any]]:
    if not SCREENSHOTS_DATABASE_ID:
        raise RuntimeError("Missing NOTION_SCREENSHOTS_DATABASE_ID")
    payload = {
        "filter": {
            "property": "Trade ID",
            "rich_text": {"equals": trade_id},
        }
    }
    return notion.query_database(SCREENSHOTS_DATABASE_ID, payload)


def build_trade_context(page: dict[str, Any]) -> dict[str, str | None]:
    fields = [
        "Trade Name",
        "Trade ID",
        "Date",
        "Pair",
        "Direction",
        "Account",
        "Session",
        "Setup Model",
        "Result",
        "Trade Quality",
        "Followed Rules",
        "Mistake Type",
        "Entry Price",
        "Exit Price",
        "Stop Loss",
        "Take Profit",
        "Risk %",
        "Risk Amount",
        "Planned R",
        "Result R",
        "Net P/L",
        "Raw Journal Story",
        "Notes",
        "Google Drive Trade Folder",
    ]
    return {name: get_text(page, name) for name in fields}


def build_screenshot_context(screenshot_pages: list[dict[str, Any]]) -> list[dict[str, str | None]]:
    rows: list[dict[str, str | None]] = []
    for page in screenshot_pages[:MAX_SCREENSHOTS]:
        rows.append(
            {
                "Screenshot Name": get_text(page, "Screenshot Name"),
                "Slot Number": get_text(page, "Slot Number"),
                "Source Slot Type": get_text(page, "Source Slot Type"),
                "Image Type": get_text(page, "Image Type"),
                "Timeframe": get_text(page, "Timeframe"),
                "Category": get_text(page, "Category"),
                "Google Drive URL": get_text(page, "Google Drive URL"),
                "Google Drive File ID": get_text(page, "Google Drive File ID"),
                "Final File Name": get_text(page, "Final File Name"),
            }
        )
    return rows


def download_drive_file_as_data_url(drive: GoogleDriveClient, file_id: str, filename: str | None = None) -> str:
    request = drive.service.files().get_media(fileId=file_id, supportsAllDrives=True)
    file_bytes = request.execute()
    mime_type = mimetypes.guess_type(filename or "screenshot.png")[0] or "image/png"
    encoded = base64.b64encode(file_bytes).decode("utf-8")
    return f"data:{mime_type};base64,{encoded}"


def collect_image_inputs(drive: GoogleDriveClient, screenshots: list[dict[str, str | None]]) -> list[dict[str, Any]]:
    image_inputs: list[dict[str, Any]] = []
    for screenshot in screenshots:
        file_id = screenshot.get("Google Drive File ID")
        if not file_id:
            continue
        data_url = download_drive_file_as_data_url(drive, file_id, screenshot.get("Final File Name"))
        label = f"{screenshot.get('Source Slot Type') or 'Screenshot'} | {screenshot.get('Timeframe') or ''} | {screenshot.get('Final File Name') or ''}"
        image_inputs.append({"label": label, "data_url": data_url})
    return image_inputs


def call_openai_review(prompt: str, trade_context: dict[str, Any], screenshots: list[dict[str, str | None]], image_inputs: list[dict[str, Any]]) -> dict[str, Any]:
    if not OPENAI_API_KEY:
        raise RuntimeError("Missing OPENAI_API_KEY")

    user_text = {
        "task": "Review this trade and return the required JSON only.",
        "trade_context": trade_context,
        "screenshot_records": screenshots,
        "image_count": len(image_inputs),
    }

    content: list[dict[str, Any]] = [
        {"type": "input_text", "text": prompt},
        {"type": "input_text", "text": json.dumps(user_text, ensure_ascii=False, indent=2)},
    ]
    for image in image_inputs:
        content.append({"type": "input_text", "text": f"Screenshot: {image['label']}"})
        content.append({"type": "input_image", "image_url": image["data_url"]})

    payload = {
        "model": OPENAI_MODEL,
        "input": [
            {
                "role": "user",
                "content": content,
            }
        ],
        "temperature": 0.2,
    }

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
        json=payload,
        timeout=180,
    )
    response.raise_for_status()
    data = response.json()

    output_text = data.get("output_text")
    if not output_text:
        parts: list[str] = []
        for item in data.get("output", []):
            for content_item in item.get("content", []):
                if content_item.get("type") == "output_text":
                    parts.append(content_item.get("text", ""))
        output_text = "\n".join(parts).strip()

    if not output_text:
        raise RuntimeError("OpenAI response did not contain output text")

    cleaned = output_text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    return json.loads(cleaned.strip())


def update_trade_review(notion: NotionClient, page_id: str, review: dict[str, Any]) -> None:
    needs_more = bool(review.get("needs_more_screenshots"))
    confidence = float(review.get("confidence", 0.0) or 0.0)
    final_status = AI_STATUS_MORE_SCREENSHOTS if needs_more else AI_STATUS_COMPLETE

    props = {
        "AI Review Status": notion_select(final_status),
        "AI Review": notion_rich_text(str(review.get("summary", ""))),
        "AI Reality Check": notion_rich_text(str(review.get("reality_check", ""))),
        "AI Mistake Diagnosis": notion_rich_text(str(review.get("mistake_diagnosis", ""))),
        "AI Future Rules": notion_rich_text(str(review.get("future_rules", ""))),
        "AI Review Confidence": notion_number(max(0.0, min(confidence, 1.0))),
        "AI Reviewed Time": notion_date(now_iso()),
    }
    notion.update_page(page_id, props)


def update_trade_error(notion: NotionClient, page_id: str, message: str) -> None:
    props = {
        "AI Review Status": notion_select(AI_STATUS_ERROR),
        "AI Review": notion_rich_text(message),
        "AI Reviewed Time": notion_date(now_iso()),
    }
    notion.update_page(page_id, props)


def process_trade(page: dict[str, Any], notion: NotionClient, drive: GoogleDriveClient, prompt: str) -> None:
    page_id = page["id"]
    trade_context = build_trade_context(page)
    trade_id = trade_context.get("Trade ID")
    raw_story = trade_context.get("Raw Journal Story") or trade_context.get("Notes")

    if not trade_id:
        update_trade_error(notion, page_id, "Missing Trade ID. Cannot perform AI review.")
        return
    if not raw_story:
        update_trade_error(notion, page_id, "Missing Raw Journal Story. Add your simple journal notes before AI review.")
        return

    screenshot_pages = query_screenshot_records(notion, trade_id)
    screenshots = build_screenshot_context(screenshot_pages)
    if not screenshots:
        review = {
            "summary": "AI review cannot be completed because no synced screenshot records were found.",
            "reality_check": "No screenshots are available to compare against the journal story.",
            "mistake_diagnosis": "Missing visual evidence. Sync at least one HTF/context and one entry screenshot.",
            "future_rules": "Upload and sync chart screenshots before requesting AI review.",
            "confidence": 0.1,
            "needs_more_screenshots": True,
            "missing_evidence": ["Synced screenshot records"],
        }
        update_trade_review(notion, page_id, review)
        return

    image_inputs = collect_image_inputs(drive, screenshots)
    review = call_openai_review(prompt, trade_context, screenshots, image_inputs)
    update_trade_review(notion, page_id, review)


def run_ai_trade_review() -> None:
    prompt = load_text_config("config/ai_trade_review_prompt.md")
    notion = NotionClient()
    drive = GoogleDriveClient()
    trades = query_ready_trades(notion)
    print(f"Trades ready for AI review: {len(trades)}")
    for page in trades:
        try:
            process_trade(page, notion, drive, prompt)
        except Exception as exc:
            print(f"Failed AI review for trade page {page.get('id')}: {exc}")
            try:
                update_trade_error(notion, page["id"], str(exc))
            except Exception as update_exc:
                print(f"Failed to update AI review error status: {update_exc}")
