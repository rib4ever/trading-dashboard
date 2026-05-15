from dotenv import load_dotenv
from src.services.trade_import_service import run_trade_import


if __name__ == "__main__":
    load_dotenv()
    run_trade_import()
