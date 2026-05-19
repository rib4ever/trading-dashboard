import hashlib
import os
from datetime import datetime
from typing import Any

from src.clients.notion_client import NotionClient

TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")


def _prop(page: dict[str, Any], name: str) -> dict[str, Any] | None:
    return page.get("properties", {}).get(name)


def get_value(page: dict[str, Any], name: str) -> Any:
    prop = _prop(page, name)
    if not prop:
        return None
    t = prop.get("type")
    if t == "title":
        return "".join(x.get("plain_text", "") for x in prop.get("title", [])) or None
    if t == "rich_text":
        return "".join(x.get("plain_text", "") for x in prop.get("rich_text", [])) or None
    if t == "date" and prop.get("date"):
        return prop["date"].get("start")
    if t == "select" and prop.get("select"):
        return prop["select"].get("name")
    return None


def rich_text(value: str) -> dict[str, Any]:
    return {"rich_text": [{"text": {"content": value}}]}


def date_token(page: dict[str, Any]) -> str:
    raw = get_value(page, "Date") or get_value(page, "Entry DateTime") or page.get("created_time")
    if not raw:
        return datetime.utcnow().strftime("%Y%m%d")
    return str(raw)[:10].replace("-", "")


def generate_trade_id(page: dict[str, Any]) -> str:
    date_part = date_token(page)
    seed = "|".join([
        page.get("id", ""),
        str(get_value(page, "Trade Name") or ""),
        str(get_value(page, "Pair") or ""),
        str(get_value(page, "Direction") or ""),
        str(get_value(page, "Date") or ""),
    ])
    suffix = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:6].upper()
    return f"TRD-{date_part}-{suffix}"


def fill_missing_trade_ids() -> int:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    notion = NotionClient()
    pages = notion.query_database_all(TRADES_DATABASE_ID, {})
    updated = 0
    for page in pages:
        current = get_value(page, "Trade ID")
        if current:
            continue
        trade_id = generate_trade_id(page)
        notion.update_page(page["id"], {"Trade ID": rich_text(trade_id)})
        updated += 1
        print(f"Filled Trade ID {trade_id} for page {page['id']}")
    print(f"Trade ID maintenance complete. Updated {updated} trade(s).")
    return updated


if __name__ == "__main__":
    fill_missing_trade_ids()
