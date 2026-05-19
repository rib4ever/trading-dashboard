import hashlib
import os
from datetime import datetime
from typing import Any

from src.clients.notion_client import NotionClient

TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")


def _prop(page: dict[str, Any], name: str) -> dict[str, Any] | None:
    return page.get("properties", {}).get(name)


def get_text(page: dict[str, Any], name: str) -> str | None:
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


def get_number(page: dict[str, Any], name: str) -> float | None:
    prop = _prop(page, name)
    if not prop or prop.get("type") != "number":
        return None
    value = prop.get("number")
    return float(value) if value is not None else None


def rich_text(value: str) -> dict[str, Any]:
    return {"rich_text": [{"text": {"content": value}}]}


def number(value: float) -> dict[str, Any]:
    return {"number": round(float(value), 4)}


def select(value: str) -> dict[str, Any]:
    return {"select": {"name": value}}


def date_token(page: dict[str, Any]) -> str:
    raw = get_text(page, "Date") or get_text(page, "Entry DateTime") or page.get("created_time")
    if not raw:
        return datetime.utcnow().strftime("%Y%m%d")
    return str(raw)[:10].replace("-", "")


def generate_trade_id(page: dict[str, Any]) -> str:
    date_part = date_token(page)
    seed = "|".join([
        page.get("id", ""),
        str(get_text(page, "Trade Name") or ""),
        str(get_text(page, "Pair") or ""),
        str(get_text(page, "Direction") or ""),
        str(get_text(page, "Date") or ""),
    ])
    suffix = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:6].upper()
    return f"TRD-{date_part}-{suffix}"


def build_maintenance_updates(page: dict[str, Any]) -> dict[str, Any]:
    updates: dict[str, Any] = {}

    if not get_text(page, "Trade ID"):
        updates["Trade ID"] = rich_text(generate_trade_id(page))

    gross = get_number(page, "Gross P/L")
    commission = get_number(page, "Commission") or 0.0
    fees = get_number(page, "Swap / Fees") or 0.0
    net = get_number(page, "Net P/L")

    if net is None and gross is not None:
        net = gross - commission - fees
        updates["Net P/L"] = number(net)

    risk_amount = get_number(page, "Risk Amount")
    result_r = get_number(page, "Result R")
    if result_r is None and net is not None and risk_amount not in (None, 0):
        updates["Result R"] = number(net / abs(risk_amount))

    entry = get_number(page, "Entry Price")
    stop = get_number(page, "Stop Loss")
    target = get_number(page, "Take Profit")
    planned_r = get_number(page, "Planned R")
    if planned_r is None and entry is not None and stop is not None and target is not None:
        risk_per_unit = abs(entry - stop)
        reward_per_unit = abs(target - entry)
        if risk_per_unit > 0:
            updates["Planned R"] = number(reward_per_unit / risk_per_unit)

    result = get_text(page, "Result")
    if not result and net is not None:
        if net > 0:
            updates["Result"] = select("Win")
        elif net < 0:
            updates["Result"] = select("Loss")
        else:
            updates["Result"] = select("Break Even")

    return updates


def run_trade_maintenance() -> int:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    notion = NotionClient()
    pages = notion.query_database_all(TRADES_DATABASE_ID, {})
    updated = 0
    for page in pages:
        updates = build_maintenance_updates(page)
        if not updates:
            continue
        notion.update_page(page["id"], updates)
        updated += 1
        print(f"Maintained trade page {page['id']}: {list(updates.keys())}")
    print(f"Trade maintenance complete. Updated {updated} trade(s).")
    return updated


def fill_missing_trade_ids() -> int:
    return run_trade_maintenance()


if __name__ == "__main__":
    run_trade_maintenance()
