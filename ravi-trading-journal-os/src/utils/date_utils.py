from datetime import datetime


def now_iso() -> str:
    return datetime.utcnow().isoformat()


def format_trade_date(date_value: str) -> str:
    if not date_value:
        raise ValueError("Missing trade date")
    return date_value[:10]


def get_year_month(date_value: str) -> tuple[str, str]:
    trade_date = format_trade_date(date_value)
    return trade_date[:4], trade_date[:7]
