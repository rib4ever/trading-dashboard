from dotenv import load_dotenv
from src.services.trade_maintenance_service import fill_missing_trade_ids


if __name__ == "__main__":
    load_dotenv()
    fill_missing_trade_ids()
