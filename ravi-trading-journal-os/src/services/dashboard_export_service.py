import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from src.clients.google_drive_client import GoogleDriveClient
from src.clients.notion_client import NotionClient

TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")
SCREENSHOTS_DATABASE_ID = os.environ.get("NOTION_SCREENSHOTS_DATABASE_ID")
ROOT_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = ROOT_DIR.parent
DASHBOARD_DIR = REPO_ROOT / "ravi-dashboard"
DASHBOARD_DATA_DIR = DASHBOARD_DIR / "data"
SCREENSHOT_ASSET_DIR = DASHBOARD_DIR / "assets" / "screenshots"
EXPORT_PATH = DASHBOARD_DATA_DIR / "trades.json"
PARIS_TZ = ZoneInfo("Europe/Paris")
UTC_TZ = ZoneInfo("UTC")

SLOT_CONFIG = [
    (1, "Screenshot Slot 1 Type", "Screenshot Slot 1 File"),
    (2, "Screenshot Slot 2 Type", "Screenshot Slot 2 File"),
    (3, "Screenshot Slot 3 Type", "Screenshot Slot 3 File"),
    (4, "Screenshot Slot 4 Type", "Screenshot Slot 4 File"),
    (5, "Screenshot Slot 5 Type", "Screenshot Slot 5 File"),
]


def _prop(page: dict[str, Any], name: str) -> dict[str, Any] | None:
    return page.get("properties", {}).get(name)


def value(page: dict[str, Any], name: str) -> Any:
    prop = _prop(page, name)
    if not prop:
        return None
    t = prop.get("type")
    if t == "title":
        return "".join(x.get("plain_text", "") for x in prop.get("title", [])) or None
    if t == "rich_text":
        return "".join(x.get("plain_text", "") for x in prop.get("rich_text", [])) or None
    if t == "select" and prop.get("select"):
        return prop["select"].get("name")
    if t == "multi_select":
        return [x.get("name") for x in prop.get("multi_select", []) if x.get("name")]
    if t == "checkbox":
        return bool(prop.get("checkbox"))
    if t == "number":
        return prop.get("number")
    if t == "url":
        return prop.get("url")
    if t == "date" and prop.get("date"):
        return prop["date"].get("start")
    if t == "files":
        return prop.get("files", [])
    return None


def num(page: dict[str, Any], name: str) -> float:
    try:
        return float(value(page, name) or 0)
    except Exception:
        return 0.0


def parse_notion_datetime(raw: str | None) -> datetime | None:
    if not raw:
        return None
    try:
        dt = datetime.fromisoformat(str(raw).replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=PARIS_TZ)
        return dt
    except Exception:
        return None


def paris_datetime(raw: str | None) -> datetime | None:
    dt = parse_notion_datetime(raw)
    if not dt:
        return None
    return dt.astimezone(PARIS_TZ)


def format_paris_time(raw: str | None) -> str:
    dt = paris_datetime(raw)
    return dt.strftime("%H:%M") if dt else ""


def format_paris_datetime(raw: str | None) -> str:
    dt = paris_datetime(raw)
    return dt.strftime("%Y-%m-%d %H:%M") if dt else ""


def trade_date_from_entry(page: dict[str, Any]) -> str:
    """Dashboard reporting date based on broker entry time in Europe/Paris.

    This prevents UTC conversion from moving a trade to the previous/next calendar day.
    """
    entry_dt = paris_datetime(value(page, "Entry DateTime"))
    if entry_dt:
        return entry_dt.date().isoformat()
    notion_date = value(page, "Date")
    if notion_date:
        return str(notion_date)[:10]
    created_dt = paris_datetime(page.get("created_time"))
    return created_dt.date().isoformat() if created_dt else page.get("created_time", "")[:10]


def session_from_paris_time(dt: datetime | None) -> str:
    if not dt:
        return "Unknown"
    minutes = dt.hour * 60 + dt.minute
    if 0 <= minutes < 8 * 60:
        return "Asian"
    if 8 * 60 <= minutes < 13 * 60 + 30:
        return "London"
    if 13 * 60 + 30 <= minutes < 22 * 60:
        return "New York"
    return "Off Session"


def killzone_from_paris_time(dt: datetime | None) -> str:
    if not dt:
        return "Unknown"
    minutes = dt.hour * 60 + dt.minute
    if 8 * 60 <= minutes < 11 * 60:
        return "London Killzone"
    if 13 * 60 + 30 <= minutes < 16 * 60:
        return "New York AM Killzone"
    if 19 * 60 <= minutes < 21 * 60:
        return "New York PM Killzone"
    return "Off Killzone"


def safe_filename(text: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip())
    clean = re.sub(r"-+", "-", clean).strip("-._")
    return clean or "screenshot"


def file_extension(name: str) -> str:
    suffix = Path(name or "").suffix.lower()
    return suffix if suffix in {".png", ".jpg", ".jpeg", ".webp"} else ".png"


def file_url(file_obj: dict[str, Any]) -> str:
    if not file_obj:
        return ""
    if file_obj.get("type") == "file":
        return file_obj.get("file", {}).get("url", "")
    if file_obj.get("type") == "external":
        return file_obj.get("external", {}).get("url", "")
    return ""


def category_from_slot_type(slot_type: str) -> str:
    text = (slot_type or "").lower()
    if any(x in text for x in ["4h", "1h", "15m", "before", "context", "htf"]):
        return "context"
    if any(x in text for x in ["entry", "5m", "3m", "execution"]):
        return "entry"
    if any(x in text for x in ["exit", "management", "close"]):
        return "exit"
    if any(x in text for x in ["review", "mistake"]):
        return "review"
    return "extra"


def fallback_screenshots_from_trade_page(page: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for slot_number, type_prop, file_prop in SLOT_CONFIG:
        slot_type = value(page, type_prop) or ""
        files = value(page, file_prop) or []
        if not files:
            continue
        first_file = files[0]
        url = file_url(first_file)
        name = first_file.get("name") or f"Screenshot Slot {slot_number}"
        if not url:
            continue
        rows.append({
            "name": name,
            "slot": slot_number,
            "slotType": slot_type,
            "imageType": slot_type,
            "timeframe": slot_type,
            "category": category_from_slot_type(slot_type),
            "driveUrl": url,
            "fileId": "",
            "thumbnailUrl": url,
            "localUrl": "",
            "fileName": name,
            "source": "trade_page_slot_temporary_fallback",
        })
    return rows


def query_screenshots_for_trade(notion: NotionClient, trade_id: str) -> list[dict[str, Any]]:
    if not SCREENSHOTS_DATABASE_ID or not trade_id:
        return []
    pages = notion.query_database(
        SCREENSHOTS_DATABASE_ID,
        {"filter": {"property": "Trade ID", "rich_text": {"equals": trade_id}}},
    )
    rows = []
    for page in pages:
        file_id = value(page, "Google Drive File ID") or ""
        rows.append({
            "name": value(page, "Screenshot Name") or value(page, "Final File Name") or "Screenshot",
            "slot": num(page, "Slot Number"),
            "slotType": value(page, "Source Slot Type") or "",
            "imageType": value(page, "Image Type") or "",
            "timeframe": value(page, "Timeframe") or "",
            "category": value(page, "Category") or "",
            "driveUrl": value(page, "Google Drive URL") or "",
            "fileId": file_id,
            "thumbnailUrl": f"https://drive.google.com/thumbnail?id={file_id}&sz=w1600" if file_id else "",
            "localUrl": "",
            "fileName": value(page, "Final File Name") or "",
            "source": "trade_screenshots_db",
        })
    return sorted(rows, key=lambda x: x.get("slot") or 99)


def persist_dashboard_screenshots(screenshots: list[dict[str, Any]], trade_id: str) -> list[dict[str, Any]]:
    if not screenshots:
        return screenshots
    SCREENSHOT_ASSET_DIR.mkdir(parents=True, exist_ok=True)
    drive = None
    enriched: list[dict[str, Any]] = []
    for shot in screenshots:
        slot = int(float(shot.get("slot") or 0)) if str(shot.get("slot") or "").replace(".", "", 1).isdigit() else 0
        source_name = shot.get("fileName") or shot.get("name") or f"slot-{slot}.png"
        ext = file_extension(source_name)
        file_id = shot.get("fileId") or ""
        stable_key = file_id or f"slot-{slot}-{safe_filename(source_name)}"
        asset_name = safe_filename(f"{trade_id}_slot-{slot}_{stable_key}") + ext
        asset_path = SCREENSHOT_ASSET_DIR / asset_name
        local_url = f"./assets/screenshots/{asset_name}"
        if file_id and not asset_path.exists():
            try:
                if drive is None:
                    drive = GoogleDriveClient()
                asset_path.write_bytes(drive.download_bytes(file_id))
                print(f"Downloaded dashboard screenshot asset: {asset_name}")
            except Exception as exc:
                print(f"Warning: could not download Drive screenshot {file_id}: {exc}")
        if asset_path.exists():
            shot["localUrl"] = local_url
            shot["thumbnailUrl"] = local_url
            shot["stableAsset"] = True
        else:
            shot["stableAsset"] = False
        enriched.append(shot)
    return enriched


def normalize_trade(page: dict[str, Any], screenshots: list[dict[str, Any]]) -> dict[str, Any]:
    trade_id = value(page, "Trade ID") or page.get("id")
    entry_raw = value(page, "Entry DateTime")
    exit_raw = value(page, "Exit DateTime")
    entry_paris = paris_datetime(entry_raw)
    dashboard_ready = bool(value(page, "Dashboard Ready"))
    missing_fields = value(page, "Missing Required Fields") or ""
    calculation_status = value(page, "Calculation Status") or "Not Checked"
    ai_story = value(page, "AI Story Review") or ""
    auto_session = session_from_paris_time(entry_paris)
    auto_killzone = killzone_from_paris_time(entry_paris)
    fallback_story = "\n\n".join([
        value(page, "AI Review") or "",
        value(page, "AI Reality Check") or "",
        value(page, "AI Mistake Diagnosis") or "",
        value(page, "AI Future Rules") or "",
    ]).strip()
    return {
        "id": trade_id,
        "notionPageId": page.get("id"),
        "notionUrl": page.get("url"),
        "name": value(page, "Trade Name") or trade_id,
        "date": trade_date_from_entry(page),
        "dateSource": "Entry DateTime Paris" if entry_raw else ("Date" if value(page, "Date") else "Notion created_time Paris"),
        "entryDateTime": entry_raw,
        "exitDateTime": exit_raw,
        "entryDateTimeParis": format_paris_datetime(entry_raw),
        "exitDateTimeParis": format_paris_datetime(exit_raw),
        "entryTime": format_paris_time(entry_raw),
        "exitTime": format_paris_time(exit_raw),
        "pair": value(page, "Pair") or "Unknown",
        "direction": value(page, "Direction") or "Unknown",
        "setup": value(page, "Setup Model") or "Unknown",
        "session": value(page, "Session") or auto_session,
        "autoSession": auto_session,
        "killzone": auto_killzone,
        "result": value(page, "Result") or "Incomplete",
        "net": num(page, "Net P/L"),
        "gross": num(page, "Gross P/L"),
        "commission": num(page, "Commission"),
        "fees": num(page, "Swap / Fees"),
        "r": num(page, "Result R"),
        "plannedR": num(page, "Planned R"),
        "riskAmount": num(page, "Risk Amount"),
        "riskPercent": num(page, "Risk %"),
        "entryPrice": num(page, "Entry Price"),
        "exitPrice": num(page, "Exit Price"),
        "lotSize": num(page, "Lot Size"),
        "stopLoss": num(page, "Stop Loss"),
        "takeProfit": num(page, "Take Profit"),
        "priceMove": num(page, "Price Move"),
        "durationMinutes": num(page, "Trade Duration Minutes"),
        "dashboardReady": dashboard_ready,
        "missingRequiredFields": missing_fields,
        "calculationStatus": calculation_status,
        "autoCalculationNotes": value(page, "Auto Calculation Notes") or "",
        "rules": bool(value(page, "Followed Rules")),
        "quality": value(page, "Trade Quality") or "",
        "mistakes": value(page, "Mistake Type") or [],
        "rawJournalStory": value(page, "Raw Journal Story") or "",
        "ai": value(page, "AI Review Status") or "Not Requested",
        "aiConfidence": num(page, "AI Review Confidence"),
        "aiReview": value(page, "AI Review") or "",
        "aiStoryReview": ai_story or fallback_story,
        "aiRealityCheck": value(page, "AI Reality Check") or "",
        "aiMistakeDiagnosis": value(page, "AI Mistake Diagnosis") or "",
        "aiFutureRules": value(page, "AI Future Rules") or "",
        "driveFolder": value(page, "Google Drive Trade Folder") or "",
        "screenshotSyncStatus": value(page, "Screenshot Sync Status") or "",
        "screenshots": screenshots,
    }


def run_dashboard_export() -> None:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    notion = NotionClient()
    pages = notion.query_database_all(TRADES_DATABASE_ID, {"sorts": [{"property": "Entry DateTime", "direction": "descending"}, {"property": "Date", "direction": "descending"}]})
    trades = []
    for page in pages:
        trade_id = value(page, "Trade ID") or page.get("id")
        screenshots = query_screenshots_for_trade(notion, trade_id)
        if screenshots:
            screenshots = persist_dashboard_screenshots(screenshots, trade_id)
        else:
            screenshots = fallback_screenshots_from_trade_page(page)
        trades.append(normalize_trade(page, screenshots))
    DASHBOARD_DATA_DIR.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.write_text(json.dumps({"trades": trades, "count": len(trades)}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(trades)} trades to {EXPORT_PATH}")


if __name__ == "__main__":
    run_dashboard_export()
