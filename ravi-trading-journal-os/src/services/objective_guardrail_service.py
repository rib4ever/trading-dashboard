import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests

ROOT_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = ROOT_DIR.parent
CONFIG_PATH = ROOT_DIR / "config" / "trading_objectives.json"
DASHBOARD_DATA_DIR = REPO_ROOT / "ravi-dashboard" / "data"
TRADES_EXPORT_PATH = DASHBOARD_DATA_DIR / "trades.json"
OBJECTIVE_STATUS_PATH = DASHBOARD_DATA_DIR / "objective_status.json"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_date(value: str | None, tz: ZoneInfo) -> datetime | None:
    if not value:
        return None
    text = str(value)
    try:
        if len(text) == 10:
            y, m, d = [int(x) for x in text.split("-")]
            return datetime(y, m, d, tzinfo=tz)
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=tz)
        return dt.astimezone(tz)
    except Exception:
        return None


def period_bounds(now: datetime) -> dict[str, tuple[datetime, datetime]]:
    day_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    week_start = day_start - timedelta(days=day_start.weekday())
    month_start = day_start.replace(day=1)
    if month_start.month == 12:
        next_month = month_start.replace(year=month_start.year + 1, month=1)
    else:
        next_month = month_start.replace(month=month_start.month + 1)
    return {
        "daily": (day_start, day_start + timedelta(days=1)),
        "weekly": (week_start, week_start + timedelta(days=7)),
        "monthly": (month_start, next_month),
    }


def is_loss(trade: dict[str, Any]) -> bool:
    result = str(trade.get("result") or "").lower()
    return "loss" in result or float(trade.get("net") or 0) < 0


def pct(value: float, target: float) -> float:
    if not target:
        return 0.0
    return round((value / target) * 100, 2)


def loss_pct(value: float, max_loss: float) -> float:
    if not max_loss:
        return 0.0
    if value >= 0:
        return 0.0
    return round((abs(value) / abs(max_loss)) * 100, 2)


def status_level(progress: float, warning_at: float, breached: bool) -> str:
    if breached:
        return "breached"
    if progress >= warning_at:
        return "warning"
    return "ok"


def evaluate_period(name: str, trades: list[dict[str, Any]], config: dict[str, Any]) -> dict[str, Any]:
    period_cfg = config.get(name, {})
    alerts_cfg = config.get("alerts", {})
    net = round(sum(float(t.get("net") or 0) for t in trades), 2)
    count = len(trades)
    losing = sum(1 for t in trades if is_loss(t))
    profit_target = float(period_cfg.get("profitTarget") or 0)
    max_loss = float(period_cfg.get("maxLoss") or 0)
    max_trades = int(period_cfg.get("maxTrades") or 0)
    max_losing_trades = int(period_cfg.get("maxLosingTrades") or 0)

    profit_progress = pct(net, profit_target) if profit_target else 0.0
    loss_progress = loss_pct(net, max_loss) if max_loss else 0.0
    trade_progress = pct(count, max_trades) if max_trades else 0.0
    losing_trade_progress = pct(losing, max_losing_trades) if max_losing_trades else 0.0

    profit_hit = profit_target > 0 and net >= profit_target
    max_loss_hit = max_loss < 0 and net <= max_loss
    max_trades_hit = max_trades > 0 and count >= max_trades
    max_losing_trades_hit = max_losing_trades > 0 and losing >= max_losing_trades

    warnings = []
    breaches = []
    if profit_hit:
        warnings.append(f"{name.title()} profit target reached")
    if max_loss_hit:
        breaches.append(f"{name.title()} max loss reached")
    if max_trades_hit:
        breaches.append(f"{name.title()} max trade count reached")
    if max_losing_trades_hit:
        breaches.append(f"{name.title()} max losing trades reached")
    if not breaches:
        if loss_progress >= float(alerts_cfg.get("warnAtLossPercent") or 80):
            warnings.append(f"{name.title()} loss limit is close")
        if trade_progress >= float(alerts_cfg.get("warnAtTradeCountPercent") or 80):
            warnings.append(f"{name.title()} trade count limit is close")
        if losing_trade_progress >= float(alerts_cfg.get("warnAtLosingTradeCountPercent") or 80):
            warnings.append(f"{name.title()} losing trade limit is close")
        if profit_progress >= float(alerts_cfg.get("warnAtProgressPercent") or 80):
            warnings.append(f"{name.title()} profit target is close")

    action = "CONTINUE"
    if max_loss_hit or max_trades_hit or max_losing_trades_hit:
        action = "STOP TRADING"
    elif warnings:
        action = "CAUTION"

    return {
        "period": name,
        "net": net,
        "trades": count,
        "losingTrades": losing,
        "profitTarget": profit_target,
        "maxLoss": max_loss,
        "maxTrades": max_trades,
        "maxLosingTrades": max_losing_trades,
        "profitProgressPercent": profit_progress,
        "lossProgressPercent": loss_progress,
        "tradeProgressPercent": trade_progress,
        "losingTradeProgressPercent": losing_trade_progress,
        "profitTargetHit": profit_hit,
        "maxLossHit": max_loss_hit,
        "maxTradesHit": max_trades_hit,
        "maxLosingTradesHit": max_losing_trades_hit,
        "level": "breached" if breaches else ("warning" if warnings else "ok"),
        "action": action,
        "warnings": warnings,
        "breaches": breaches,
    }


def build_message(status: dict[str, Any]) -> str:
    currency = status.get("currency", "EUR")
    lines = ["🚦 Ravi Trading Guardrail Update", f"Profile: {status.get('profile', '-')}"]
    for name in ["daily", "weekly", "monthly"]:
        p = status["periods"].get(name, {})
        lines.append(
            f"\n{name.title()}: {p.get('action')} | Net {p.get('net')} {currency} | "
            f"Trades {p.get('trades')}/{p.get('maxTrades')} | Losses {p.get('losingTrades')}/{p.get('maxLosingTrades')}"
        )
        for b in p.get("breaches", []):
            lines.append(f"❌ {b}")
        for w in p.get("warnings", []):
            lines.append(f"⚠️ {w}")
    return "\n".join(lines)


def should_alert(status: dict[str, Any]) -> bool:
    if not status.get("alerts", {}).get("enabled", False):
        return False
    for p in status.get("periods", {}).values():
        if p.get("breaches") or p.get("warnings"):
            return True
    return not bool(status.get("alerts", {}).get("sendOnlyWhenBreachedOrWarning", True))


def send_telegram(message: str) -> bool:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Telegram alert skipped: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID missing")
        return False
    response = requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={"chat_id": chat_id, "text": message},
        timeout=30,
    )
    if not response.ok:
        print(f"Telegram alert failed: {response.status_code} {response.text[:500]}")
        return False
    return True


def run_objective_guardrails() -> None:
    config = load_json(CONFIG_PATH)
    tz = ZoneInfo(config.get("timezone") or "Europe/Paris")
    now = datetime.now(tz)
    trades_export = load_json(TRADES_EXPORT_PATH)
    trades = trades_export.get("trades", [])
    bounds = period_bounds(now)

    periods = {}
    for name, (start, end) in bounds.items():
        scoped = []
        for trade in trades:
            dt = parse_date(trade.get("date"), tz)
            if dt and start <= dt < end:
                scoped.append(trade)
        periods[name] = evaluate_period(name, scoped, config)

    status = {
        "generatedAt": now.isoformat(),
        "profile": config.get("profile", "Default"),
        "currency": config.get("currency", "EUR"),
        "timezone": config.get("timezone", "Europe/Paris"),
        "objectives": {k: config.get(k, {}) for k in ["daily", "weekly", "monthly"]},
        "alerts": config.get("alerts", {}),
        "periods": periods,
    }
    DASHBOARD_DATA_DIR.mkdir(parents=True, exist_ok=True)
    OBJECTIVE_STATUS_PATH.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Objective guardrails exported to {OBJECTIVE_STATUS_PATH}")

    if config.get("alerts", {}).get("telegramEnabled", False) and should_alert(status):
        sent = send_telegram(build_message(status))
        print(f"Telegram alert sent: {sent}")


if __name__ == "__main__":
    run_objective_guardrails()
