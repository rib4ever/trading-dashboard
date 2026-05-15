from dotenv import load_dotenv
from src.services.metrics_service import run_metrics_refresh


if __name__ == "__main__":
    load_dotenv()
    run_metrics_refresh()
