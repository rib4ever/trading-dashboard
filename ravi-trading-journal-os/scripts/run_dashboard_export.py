from dotenv import load_dotenv
from src.services.dashboard_export_service import run_dashboard_export


if __name__ == "__main__":
    load_dotenv()
    run_dashboard_export()
