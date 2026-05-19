import json
import os
import time
from typing import Any

import requests

from src.clients.google_drive_client import GoogleDriveClient
from src.clients.notion_client import NotionClient
from src.utils.config_loader import load_text_config
from src.utils.contact_sheet import build_contact_sheet, image_bytes_to_data_url
from src.utils.date_utils import now_iso

TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")
SCREENSHOTS_DATABASE_ID = os.environ.get("NOTION_SCREENSHOTS_DATABASE_ID")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_TRADE_REVIEW_MODEL", "gpt-4.1-mini")

AI_STATUS_READY = "Ready for AI Review"
AI_STATUS_COMPLETE = "AI Review Complete"
AI_STATUS_MORE_SCREENSHOTS = "Needs More Screenshots"
AI_STATUS_ERROR = "AI Review Error"

MAX_SCREENSHOTS = int(os.environ.get("AI_REVIEW_MAX_SCREENSHOTS", "3"))
OPENAI_MAX_RETRIES = int(os.environ.get("OPENAI_MAX_RETRIES", "3"))


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
    return notion.query_database(
        TRADES_DATABASE_ID,
        {"filter": {"property": "AI Review Status", "select": {"equals": AI_STATUS_READY}}},
    )


def query_screenshot_records(notion: NotionClient, trade_id: str) -> list[dict[str, Any]]:
    if not SCREENSHOTS_DATABASE_ID:
        raise RuntimeError("Missing NOTION_SCREENSHOTS_DATABASE_ID")
    return notion.query_database(
        SCREENSHOTS_DATABASE_ID,
        {"filter": {"property": "Trade ID", "rich_text": {"equals": trade_id}}},
    )


def build_trade_context(page: dict[str, Any]) -> dict[str, str | None]:
    fields = [
        "Trade Name", "Trade ID", "Date", "Pair", "Direction", "Account", "Session", "Setup Model",
        "Result", "Trade Quality", "Followed Rules", "Mistake Type", "Entry Price", "Exit Price",
        "Stop Loss", "Take Profit", "Risk %", "Risk Amount", "Planned R", "Result R", "Net P/L",
        "Raw Journal Story", "Notes", "Google Drive Trade Folder",
    ]
    return {name: get_text(page, name) for name in fields}


def build_screenshot_context(pages: list[dict[str, Any]]) -> list[dict[str, str | None]]:
    rows = []
    for page in pages[:MAX_SCREENSHOTS]:
        rows.append({
            "Screenshot Name": get_text(page, "Screenshot Name"),
            "Slot Number": get_text(page, "Slot Number"),
            "Source Slot Type": get_text(page, "Source Slot Type"),
            "Image Type": get_text(page, "Image Type"),
            "Timeframe": get_text(page, "Timeframe"),
            "Category": get_text(page, "Category"),
            "Google Drive URL": get_text(page, "Google Drive URL"),
            "Google Drive File ID": get_text(page, "Google Drive File ID"),
            "Final File Name": get_text(page, "Final File Name"),
        })
    return rows


def download_drive_file_bytes(drive: GoogleDriveClient, file_id: str) -> bytes:
    return drive.service.files().get_media(fileId=file_id, supportsAllDrives=True).execute()


def build_review_contact_sheet_data_url(drive: GoogleDriveClient, trade_id: str, screenshots: list[dict[str, str | None]]) -> tuple[str, int]:
    items = []
    for s in screenshots[:MAX_SCREENSHOTS]:
        file_id = s.get("Google Drive File ID")
        if not file_id:
            continue
        label = f"{s.get('Source Slot Type') or 'Screenshot'} | {s.get('Timeframe') or ''} | {s.get('Final File Name') or ''}"
        items.append({"label": label, "bytes": download_drive_file_bytes(drive, file_id)})

    if not items:
        raise RuntimeError("No downloadable Google Drive screenshots found for AI review")

    sheet_bytes, mime_type = build_contact_sheet(items, f"AI Review Packet — {trade_id}")
    return image_bytes_to_data_url(sheet_bytes, mime_type), len(items)


def _format_openai_error(response: requests.Response) -> str:
    try:
        body = response.json()
    except Exception:
        body = response.text
    return f"OpenAI API error {response.status_code}: {json.dumps(body, ensure_ascii=False)[:1500]}"


def _post_openai_with_retries(payload: dict[str, Any]) -> dict[str, Any]:
    if not OPENAI_API_KEY:
        raise RuntimeError("Missing OPENAI_API_KEY")

    last_error = "Unknown OpenAI error"
    for attempt in range(1, OPENAI_MAX_RETRIES + 1):
        response = requests.post(
            "https://api.openai.com/v1/responses",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
            json=payload,
            timeout=180,
        )
        if response.ok:
            return response.json()
        last_error = _format_openai_error(response)
        if response.status_code == 429 and attempt < OPENAI_MAX_RETRIES:
            wait_seconds = min(10 * attempt, 30)
            print(f"OpenAI 429 on attempt {attempt}/{OPENAI_MAX_RETRIES}. Retrying in {wait_seconds}s.")
            time.sleep(wait_seconds)
            continue
        raise RuntimeError(last_error)
    raise RuntimeError(last_error)


def call_openai_review(prompt: str, trade_context: dict[str, Any], screenshots: list[dict[str, str | None]], contact_sheet_url: str, image_count: int) -> dict[str, Any]:
    user_text = {
        "task": "Review this trade and return the required JSON only.",
        "review_mode": "single compressed contact sheet",
        "trade_context": trade_context,
        "screenshot_records": screenshots,
        "image_count_in_contact_sheet": image_count,
        "model": OPENAI_MODEL,
    }

    payload = {
        "model": OPENAI_MODEL,
        "input": [{
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_text", "text": json.dumps(user_text, ensure_ascii=False, indent=2)},
                {"type": "input_image", "image_url": contact_sheet_url},
            ],
        }],
        "temperature": 0.2,
    }

    data = _post_openai_with_retries(payload)
    output_text = data.get("output_text")
    if not output_text:
        parts = []
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
    props = {
        "AI Review Status": notion_select(AI_STATUS_MORE_SCREENSHOTS if needs_more else AI_STATUS_COMPLETE),
        "AI Review": notion_rich_text(str(review.get("summary", ""))),
        "AI Reality Check": notion_rich_text(str(review.get("reality_check", ""))),
        "AI Mistake Diagnosis": notion_rich_text(str(review.get("mistake_diagnosis", ""))),
        "AI Future Rules": notion_rich_text(str(review.get("future_rules", ""))),
        "AI Review Confidence": notion_number(max(0.0, min(confidence, 1.0))),
        "AI Reviewed Time": notion_date(now_iso()),
    }
    notion.update_page(page_id, props)


def update_trade_error(notion: NotionClient, page_id: str, message: str) -> None:
    notion.update_page(page_id, {
        "AI Review Status": notion_select(AI_STATUS_ERROR),
        "AI Review": notion_rich_text(message),
        "AI Reviewed Time": notion_date(now_iso()),
    })


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
        update_trade_review(notion, page_id, {
            "summary": "AI review cannot be completed because no synced screenshot records were found.",
            "reality_check": "No screenshots are available to compare against the journal story.",
            "mistake_diagnosis": "Missing visual evidence.",
            "future_rules": "Upload and sync chart screenshots before requesting AI review.",
            "confidence": 0.1,
            "needs_more_screenshots": True,
        })
        return

    contact_sheet_url, image_count = build_review_contact_sheet_data_url(drive, trade_id, screenshots)
    review = call_openai_review(prompt, trade_context, screenshots, contact_sheet_url, image_count)
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
