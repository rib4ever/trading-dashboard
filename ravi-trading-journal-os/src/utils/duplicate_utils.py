def generate_screenshot_source_key(trade_id: str, slot_number: int, slot_type: str, original_file_name: str) -> str:
    return f"{trade_id}|{slot_number}|{slot_type}|{original_file_name}"
