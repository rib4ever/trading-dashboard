import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from src.clients.notion_client import NotionClient

TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")
ROOT_DIR = Path(__file__).resolve().parents[2]
SYMBOL_SETTINGS_PATH = ROOT_DIR / "config" / "symbol_profit_settings.json"
PARIS_TZ = ZoneInfo("Europe/Paris")


def load_symbol_settings() -> dict[str, Any]:
    if not SYMBOL_SETTINGS_PATH.exists():
        return {"symbols": {}}
    return json.loads(SYMBOL_SETTINGS_PATH.read_text(encoding="utf-8"))


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
    return {"rich_text": [{"text": {"content": value[:1900]}}]}


def number(value: float) -> dict[str, Any]:
    return {"number": round(float(value), 4)}


def select(value: str) -> dict[str, Any]:
    return {"select": {"name": value}}


def checkbox(value: bool) -> dict[str, Any]:
    return {"checkbox": value}


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=PARIS_TZ)
        return dt
    except Exception:
        return None


def paris_datetime(value: str | None) -> datetime | None:
    dt = parse_datetime(value)
    if not dt:
        return None
    return dt.astimezone(PARIS_TZ)


def time_24h(value: str | None) -> str:
    dt = paris_datetime(value)
    return dt.strftime("%H:%M") if dt else ""


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


def date_token(page: dict[str, Any]) -> str:
    entry_dt = paris_datetime(get_text(page, "Entry DateTime"))
    if entry_dt:
        return entry_dt.strftime("%Y%m%d")
    raw = get_text(page, "Date") or page.get("created_time")
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


def estimate_gross_pl(page: dict[str, Any], symbol_settings: dict[str, Any]) -> tuple[float | None, str | None]:
    pair = get_text(page, "Pair")
    direction = get_text(page, "Direction")
    entry = get_number(page, "Entry Price")
    exit_price = get_number(page, "Exit Price")
    lot = get_number(page, "Lot Size")

    if not all([pair, direction]) or entry is None or exit_price is None or lot is None:
        return None, None

    symbol = symbol_settings.get("symbols", {}).get(pair)
    if not symbol:
        return None, f"Gross P/L not estimated: missing symbol settings for {pair}."

    contract_size = float(symbol.get("contract_size", 1))
    direction_multiplier = 1 if direction == "Buy" else -1
    gross = (exit_price - entry) * lot * contract_size * direction_multiplier
    note = f"Gross P/L estimated from Entry/Exit/Lot using {pair} contract_size={contract_size}. Broker/MT5 value should be final truth."
    return gross, note


def get_missing_fields(page: dict[str, Any]) -> list[str]:
    required = ["Trade ID", "Date", "Pair", "Direction"]
    missing = [field for field in required if not get_text(page, field)]
    kpi_required = ["Result", "Net P/L", "Result R"]
    for field in kpi_required:
        value = get_text(page, field) if field == "Result" else get_number(page, field)
        if value is None or value == "":
            missing.append(field)
    return missing


def build_maintenance_updates(page: dict[str, Any], symbol_settings: dict[str, Any]) -> dict[str, Any]:
    updates: dict[str, Any] = {}
    notes: list[str] = []

    if not get_text(page, "Trade ID"):
        trade_id = generate_trade_id(page)
        updates["Trade ID"] = rich_text(trade_id)
        notes.append(f"Generated Trade ID: {trade_id}")

    entry_dt = paris_datetime(get_text(page, "Entry DateTime"))
    exit_dt = paris_datetime(get_text(page, "Exit DateTime"))
    entry_time = time_24h(get_text(page, "Entry DateTime"))
    exit_time = time_24h(get_text(page, "Exit DateTime"))
    auto_session = session_from_paris_time(entry_dt)
    auto_killzone = killzone_from_paris_time(entry_dt)

    if entry_time and get_text(page, "Broker Entry Time") != entry_time:
        updates["Broker Entry Time"] = rich_text(entry_time)
        notes.append(f"Broker Entry Time set from Entry DateTime Paris time: {entry_time}")
    if exit_time and get_text(page, "Broker Exit Time") != exit_time:
        updates["Broker Exit Time"] = rich_text(exit_time)
        notes.append(f"Broker Exit Time set from Exit DateTime Paris time: {exit_time}")
    if auto_session and get_text(page, "Auto Session") != auto_session:
        updates["Auto Session"] = select(auto_session)
        notes.append(f"Auto Session calculated from broker entry time: {auto_session}")
    if auto_killzone and get_text(page, "Killzone") != auto_killzone:
        updates["Killzone"] = select(auto_killzone)
        notes.append(f"Killzone calculated from broker entry time: {auto_killzone}")

    if get_number(page, "Commission") is None:
        updates["Commission"] = number(0)
        notes.append("Commission blank → set to 0")
    if get_number(page, "Swap / Fees") is None:
        updates["Swap / Fees"] = number(0)
        notes.append("Swap / Fees blank → set to 0")

    pair = get_text(page, "Pair")
    direction = get_text(page, "Direction")
    entry = get_number(page, "Entry Price")
    exit_price = get_number(page, "Exit Price")
    stop = get_number(page, "Stop Loss")
    target = get_number(page, "Take Profit")

    if get_number(page, "Price Move") is None and entry is not None and exit_price is not None and direction:
        multiplier = 1 if direction == "Buy" else -1
        updates["Price Move"] = number((exit_price - entry) * multiplier)
        notes.append("Price Move calculated from Entry/Exit/Direction")

    gross = get_number(page, "Gross P/L")
    if gross is None:
        estimated_gross, gross_note = estimate_gross_pl(page, symbol_settings)
        if estimated_gross is not None:
            gross = estimated_gross
            updates["Gross P/L"] = number(gross)
            notes.append(gross_note or "Gross P/L estimated")

    commission = get_number(page, "Commission")
    if commission is None:
        commission = 0.0
    fees = get_number(page, "Swap / Fees")
    if fees is None:
        fees = 0.0

    net = get_number(page, "Net P/L")
    if net is None and gross is not None:
        net = gross - commission - fees
        updates["Net P/L"] = number(net)
        notes.append("Net P/L calculated as Gross P/L - Commission - Swap/Fees")

    risk_amount = get_number(page, "Risk Amount")
    if get_number(page, "Result R") is None and net is not None and risk_amount not in (None, 0):
        updates["Result R"] = number(net / abs(risk_amount))
        notes.append("Result R calculated from Net P/L and Risk Amount")

    if get_number(page, "Planned R") is None and entry is not None and stop is not None and target is not None:
        risk_per_unit = abs(entry - stop)
        reward_per_unit = abs(target - entry)
        if risk_per_unit > 0:
            updates["Planned R"] = number(reward_per_unit / risk_per_unit)
            notes.append("Planned R calculated from Entry, SL, TP")

    if not get_text(page, "Result") and net is not None:
        if net > 0:
            updates["Result"] = select("Win")
        elif net < 0:
            updates["Result"] = select("Loss")
        else:
            updates["Result"] = select("Break Even")
        notes.append("Result calculated from Net P/L")

    if get_number(page, "Trade Duration Minutes") is None and entry_dt and exit_dt:
        duration_minutes = (exit_dt - entry_dt).total_seconds() / 60
        if duration_minutes >= 0:
            updates["Trade Duration Minutes"] = number(duration_minutes)
            notes.append("Trade Duration calculated from Entry/Exit DateTime")

    missing = get_missing_fields(page)
    if "Trade ID" in missing and "Trade ID" in updates:
        missing.remove("Trade ID")
    if "Net P/L" in missing and ("Net P/L" in updates or net is not None):
        missing.remove("Net P/L")
    if "Result R" in missing and "Result R" in updates:
        missing.remove("Result R")
    if "Result" in missing and "Result" in updates:
        missing.remove("Result")

    updates["Dashboard Ready"] = checkbox(len(missing) == 0)
    updates["Missing Required Fields"] = rich_text(", ".join(missing) if missing else "None")
    updates["Calculation Status"] = select("Complete" if not missing else ("Partial" if notes else "Needs Manual Input"))

    if notes:
        updates["Auto Calculation Notes"] = rich_text(" | ".join([n for n in notes if n]))
    elif missing:
        updates["Auto Calculation Notes"] = rich_text("No automatic calculation applied. Missing required source fields.")
    else:
        updates["Auto Calculation Notes"] = rich_text("Checked. No changes needed.")

    return updates


def run_trade_maintenance() -> int:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    notion = NotionClient()
    symbol_settings = load_symbol_settings()
    pages = notion.query_database_all(TRADES_DATABASE_ID, {})
    updated = 0
    for page in pages:
        updates = build_maintenance_updates(page, symbol_settings)
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
