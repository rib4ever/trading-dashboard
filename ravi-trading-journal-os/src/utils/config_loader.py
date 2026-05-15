import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]


def load_json_config(relative_path: str) -> dict:
    path = ROOT_DIR / relative_path
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
