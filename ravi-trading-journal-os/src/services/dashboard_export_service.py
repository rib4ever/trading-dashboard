import json
import os
from pathlib import Path
from typing import Any

from src.clients.notion_client import NotionClient

TRADES_DATABASE_ID = os.environ.get("NOTION_TRADES_DATABASE_ID")
ROOT_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = ROOT_DIR.parent
DASHBOARD_DATA_DIR = REPO_ROOT / "ravi-dashboard" / "data"
EXPORT_PATH = DASHBOARD_DATA_DIR / "trades.json"


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
    return None


def num(page: dict[str, Any], name: str) -> float:
    try:
        return float(value(page, name) or 0)
    except Exception:
        return 0.0


def normalize_trade(page: dict[str, Any]) -> dict[str, Any]:
    trade_id = value(page, "Trade ID") or page.get("id")
    return {
        "id": trade_id,
        "notionPageId": page.get("id"),
        "notionUrl": page.get("url"),
        "name": value(page, "Trade Name") or trade_id,
        "date": value(page, "Date") or value(page, "Entry DateTime") or page.get("created_time", "")[:10],
        "entryDateTime": value(page, "Entry DateTime"),
        "exitDateTime": value(page, "Exit DateTime"),
        "pair": value(page, "Pair") or "Unknown",
        "direction": value(page, "Direction") or "Unknown",
        "setup": value(page, "Setup Model") or "Unknown",
        "session": value(page, "Session") or "Unknown",
        "result": value(page, "Result") or "",
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
        "rules": bool(value(page, "Followed Rules")),
        "quality": value(page, "Trade Quality") or "",
        "mistakes": value(page, "Mistake Type") or [],
        "ai": value(page, "AI Review Status") or "Not Requested",
        "aiConfidence": num(page, "AI Review Confidence"),
        "aiReview": value(page, "AI Review") or "",
        "aiRealityCheck": value(page, "AI Reality Check") or "",
        "aiMistakeDiagnosis": value(page, "AI Mistake Diagnosis") or "",
        "aiFutureRules": value(page, "AI Future Rules") or "",
        "driveFolder": value(page, "Google Drive Trade Folder") or "",
        "screenshotSyncStatus": value(page, "Screenshot Sync Status") or "",
    }


def run_dashboard_export() -> None:
    if not TRADES_DATABASE_ID:
        raise RuntimeError("Missing NOTION_TRADES_DATABASE_ID")
    notion = NotionClient()
    pages = notion.query_database_all(TRADES_DATABASE_ID, {"sorts": [{"property": "Date", "direction": "descending"}]})
    trades = [normalize_trade(page) for page in pages]
    DASHBOARD_DATA_DIR.mkdir(parents=True, exist_ok=True)
    EXPORT_PATH.write_text(json.dumps({"trades": trades, "count": len(trades)}, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Exported {len(trades)} trades to {EXPORT_PATH}")


if __name__ == "__main__":
    run_dashboard_export()
