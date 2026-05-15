import re
from pathlib import Path


def clean_text(value: str) -> str:
    if not value:
        return "UNKNOWN"
    value = value.strip().upper()
    value = re.sub(r"[^A-Z0-9_\-]+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_")


def get_extension(file_name: str, default: str = "png") -> str:
    if not file_name:
        return default
    suffix = Path(file_name).suffix.replace(".", "").lower()
    return suffix or default


def generate_screenshot_filename(trade_id: str, pair: str, trade_date: str, timeframe: str, image_type: str, extension: str) -> str:
    parts = [clean_text(trade_id), clean_text(pair), trade_date]
    if timeframe and timeframe != "AUTO":
        parts.append(clean_text(timeframe))
    parts.append(clean_text(image_type))
    return "_".join(parts) + f".{extension.lower()}"
