import mimetypes
import os
from typing import Any

import requests

from src.clients.google_drive_client import GoogleDriveClient
from src.clients.notion_client import NotionClient
from src.utils.config_loader import load_json_config
from src.utils.date_utils import format_trade_date, get_year_month, now_iso
from src.utils.duplicate_utils import generate_screenshot_source_key
from src.utils.filename_utils import generate_screenshot_filename, get_extension


TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")
SCREENSHOTS_DATABASE_ID = os.environ.get("NOTION_SCREENSHOTS_DATABASE_ID")
GOOGLE_DRIVE_ROOT_FOLDER_ID = os.environ.get("GOOGLE_DRIVE_ROOT_FOLDER_ID")
AUTO_MARK_AI_READY_AFTER_SCREENSHOT_SYNC = os.environ.get("AUTO_MARK_AI_READY_AFTER_SCREENSHOT_SYNC", "false").lower() == "true"

SLOT_CONFIG = [
    (1, "Screenshot Slot 1 Type", "Screenshot Slot 1 File"),
    (2, "Screenshot Slot 2 Type", "Screenshot Slot 2 File"),
    (3, "Screenshot Slot 3 Type", "Screenshot Slot 3 File"),
    (4, "Screenshot Slot 4 Type", "Screenshot Slot 4 File"),
    (5, "Screenshot Slot 5 Type", "Screenshot Slot 5 File"),
]

STATUS_READY = "Ready to Sync"
STATUS_SYNCED = "Synced to Drive"
STATUS_PENDING = "Pending Upload"
STATUS_MANUAL = "Needs Manual Check"
STATUS_ERROR = "Error"
STATUS_NOT_STARTED = "Not Started"
AI_STATUS_READY = "Ready for AI Review"
AI_STATUS_COMPLETE = "AI Review Complete"
AI_STATUS_ERROR = "AI Review Error"


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
    if prop_type == "status" and prop.get("status"):
        return prop["status"].get("name")
    return None


def get_date(page: dict[str, Any], name: str) -> str | None:
    prop = _prop(page, name)
    if not prop or prop.get("type") != "date" or not prop.get("date"):
        return None
    return prop["date"].get("start")


def get_files(page: dict[str, Any], name: str) -> list[dict[str, Any]]:
    prop = _prop(page, name)
    if not prop or prop.get("type") != "files":
        return []
    return prop.get("files", [])


def notion_rich_text(value: str) -> dict[str, Any]:
    return {"rich_text": [{"text": {"content": value[:1900]}}]}


def notion_title(value: str) -> dict[str, Any]:
    return {"title": [{"text": {"content": value[:1900]}}]}


def notion_select(value: str) -> dict[str, Any]:
    return {"select": {"name": value}}


def notion_date(value: str) -> dict[str, Any]:
    return {"date": {"start": value}}


def extract_file_info(notion_file: dict[str, Any]) -> tuple[str, str]:
    name = notion_file.get("name", "screenshot.png")
    file_type = notion_file.get("type")
    if file_type == "file":
        return name, notion_file["file"]["url"]
    if file_type == "external":
        return name, notion_file["external"]["url"]
    raise ValueError(f"Unsupported Notion file type: {file_type}")


def download_file(url: str) -> bytes:
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.content


def should_mark_ready_for_ai(page: dict[str, Any], status: str, processed: bool) -> tuple[bool, str | None]:
    if not AUTO_MARK_AI_READY_AFTER_SCREENSHOT_SYNC:
        return False, None
    if status != STATUS_SYNCED or not processed:
        return False, None
    raw_story = get_text(page, "Raw Journal Story")
    if not raw_story:
        return False, "AI auto-ready skipped: Raw Journal Story is blank."
    current_ai_status = get_text(page, "AI Review Status")
    if current_ai_status in [AI_STATUS_COMPLETE, AI_STATUS_ERROR]:
        return False, f"AI Review Status unchanged because current status is {current_ai_status}."
    return True, "AI Review Status auto-set to Ready for AI Review by full pipeline."


def update_trade_status(notion: NotionClient, page: dict[str, Any], status: str, notes: str, processed: bool, folder_url: str | None = None) -> None:
    props: dict[str, Any] = {
        "Screenshot Sync Status": notion_select(status),
        "Screenshot Sync Notes": notion_rich_text(notes),
        "Last Screenshot Sync Time": notion_date(now_iso()),
        "Screenshots Processed": {"checkbox": processed},
    }
    if folder_url:
        props["Google Drive Trade Folder"] = {"url": folder_url}
    mark_ai_ready, ai_note = should_mark_ready_for_ai(page, status, processed)
    if mark_ai_ready:
        props["AI Review Status"] = notion_select(AI_STATUS_READY)
        props["AI Review Mode"] = notion_select("Contact Sheet")
    if ai_note:
        props["Screenshot Sync Notes"] = notion_rich_text(f"{notes} | {ai_note}")
    notion.update_page(page["id"], props)


def query_ready_trades(notion: NotionClient) -> list[dict[str, Any]]:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    payload = {"filter": {"property": "Screenshot Sync Status", "select": {"equals": STATUS_READY}}}
    return notion.query_database(TRADES_DATABASE_ID, payload)


def screenshot_source_exists(notion: NotionClient, source_key: str) -> bool:
    if not SCREENSHOTS_DATABASE_ID:
        raise RuntimeError("Missing NOTION_SCREENSHOTS_DATABASE_ID")
    payload = {"filter": {"property": "Screenshot Source Key", "rich_text": {"equals": source_key}}}
    return bool(notion.query_database(SCREENSHOTS_DATABASE_ID, payload))


def create_screenshot_record(
    notion: NotionClient,
    trade_page_id: str,
    trade_id: str,
    pair: str,
    trade_date: str,
    slot_number: int,
    slot_type: str,
    mapping: dict[str, Any],
    source_key: str,
    original_url: str,
    drive_file: dict[str, Any],
    target_folder: dict[str, Any],
    final_file_name: str,
) -> None:
    if not SCREENSHOTS_DATABASE_ID:
        raise RuntimeError("Missing NOTION_SCREENSHOTS_DATABASE_ID")

    image_type = mapping["image_type"]
    timeframe = mapping["timeframe"]
    category = mapping.get("category", mapping.get("drive_subfolder", "EXTRA"))
    screenshot_name = f"{trade_id} — {timeframe} {image_type}"

    properties = {
        "Screenshot Name": notion_title(screenshot_name),
        "Screenshot ID": notion_rich_text(f"IMG-{trade_date.replace('-', '')}-{slot_number:02d}"),
        "Trade ID": notion_rich_text(trade_id),
        "Pair": notion_select(pair if pair else "Other"),
        "Trade Date": notion_date(trade_date),
        "Slot Number": {"number": slot_number},
        "Source Slot Type": notion_select(slot_type),
        "Image Type": notion_select(image_type),
        "Timeframe": notion_select(timeframe),
        "Category": notion_select(category),
        "Original Notion File URL": {"url": original_url},
        "Google Drive URL": {"url": drive_file.get("webViewLink")},
        "Google Drive File ID": notion_rich_text(drive_file.get("id", "")),
        "Google Drive Folder URL": {"url": target_folder.get("webViewLink")},
        "Final File Name": notion_rich_text(final_file_name),
        "Screenshot Source Key": notion_rich_text(source_key),
        "Sync Status": notion_select("Synced"),
        "Processed Time": notion_date(now_iso()),
    }
    notion.create_page(SCREENSHOTS_DATABASE_ID, properties)


def process_trade(page: dict[str, Any], notion: NotionClient, drive: GoogleDriveClient, slot_mapping: dict[str, Any]) -> None:
    trade_id = get_text(page, "Trade ID")
    trade_date_raw = get_date(page, "Date")
    pair = get_text(page, "Pair")
    direction = get_text(page, "Direction")

    missing = [name for name, value in [("Trade ID", trade_id), ("Date", trade_date_raw), ("Pair", pair), ("Direction", direction)] if not value]
    if missing:
        update_trade_status(notion, page, STATUS_MANUAL, "Missing required fields: " + ", ".join(missing), False)
        return

    trade_date = format_trade_date(trade_date_raw)
    year, month = get_year_month(trade_date_raw)

    if not GOOGLE_DRIVE_ROOT_FOLDER_ID:
        raise RuntimeError("Missing GOOGLE_DRIVE_ROOT_FOLDER_ID")

    trades_root = drive.get_or_create_folder("01_Trades", GOOGLE_DRIVE_ROOT_FOLDER_ID)
    year_folder = drive.get_or_create_folder(year, trades_root["id"])
    month_folder = drive.get_or_create_folder(month, year_folder["id"])
    trade_folder = drive.get_or_create_folder(f"{trade_id}_{pair}_{direction}".upper(), month_folder["id"])

    subfolders = {name: drive.get_or_create_folder(name, trade_folder["id"]) for name in ["01_context", "02_entry", "03_exit", "04_review", "05_mistakes", "99_extra"]}

    processed = 0
    skipped_empty = 0
    skipped_duplicates = 0
    notes: list[str] = []
    has_manual = False
    has_pending = False
    has_error = False
    attempted_slots = 0

    for slot_number, type_prop, file_prop in SLOT_CONFIG:
        slot_type = get_text(page, type_prop)
        files = get_files(page, file_prop)

        if not slot_type and not files:
            skipped_empty += 1
            continue
        attempted_slots += 1
        if slot_type and not files:
            has_pending = True
            notes.append(f"Slot {slot_number}: type selected but no file")
            continue
        if files and not slot_type:
            has_manual = True
            notes.append(f"Slot {slot_number}: file uploaded but no type selected")
            continue
        if slot_type not in slot_mapping:
            has_manual = True
            notes.append(f"Slot {slot_number}: unknown type {slot_type}")
            continue

        mapping = slot_mapping[slot_type]
        original_name, original_url = extract_file_info(files[0])
        source_key = generate_screenshot_source_key(trade_id, slot_number, slot_type, original_name)

        if screenshot_source_exists(notion, source_key):
            skipped_duplicates += 1
            notes.append(f"Slot {slot_number}: duplicate skipped")
            continue

        try:
            extension = get_extension(original_name)
            final_file_name = generate_screenshot_filename(trade_id=trade_id, pair=pair, trade_date=trade_date, timeframe=mapping["timeframe"], image_type=mapping["image_type"], extension=extension)
            file_bytes = download_file(original_url)
            mime_type = mimetypes.guess_type(final_file_name)[0] or "image/png"
            target_folder = subfolders[mapping["drive_subfolder"]]
            drive_file = drive.upload_bytes(file_bytes, final_file_name, target_folder["id"], mime_type)
            create_screenshot_record(notion, page["id"], trade_id, pair, trade_date, slot_number, slot_type, mapping, source_key, original_url, drive_file, target_folder, final_file_name)
            processed += 1
        except Exception as exc:
            has_error = True
            notes.append(f"Slot {slot_number}: {exc}")

    if has_error:
        final_status = STATUS_ERROR
    elif has_manual:
        final_status = STATUS_MANUAL
    elif processed > 0:
        final_status = STATUS_SYNCED
    elif skipped_duplicates > 0 and not has_pending:
        final_status = STATUS_SYNCED
    elif has_pending:
        final_status = STATUS_PENDING
    elif attempted_slots == 0:
        final_status = STATUS_NOT_STARTED
    else:
        final_status = STATUS_NOT_STARTED

    processed_flag = processed > 0 or skipped_duplicates > 0
    summary = f"Processed: {processed}. Duplicate skipped: {skipped_duplicates}. Empty skipped: {skipped_empty}. Notes: {' | '.join(notes) if notes else 'No issues.'}"
    update_trade_status(notion, page, final_status, summary, processed_flag, trade_folder.get("webViewLink"))


def run_screenshot_sync() -> None:
    slot_mapping = load_json_config("config/screenshot_slot_mapping.json")
    notion = NotionClient()
    drive = GoogleDriveClient()
    trades = query_ready_trades(notion)
    print(f"Trades ready for screenshot sync: {len(trades)}")
    for page in trades:
        try:
            process_trade(page, notion, drive, slot_mapping)
        except Exception as exc:
            print(f"Failed to process trade page {page.get('id')}: {exc}")
