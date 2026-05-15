from dotenv import load_dotenv

from src.services.screenshot_sync_service import run_screenshot_sync


if __name__ == "__main__":
    load_dotenv()
    run_screenshot_sync()
