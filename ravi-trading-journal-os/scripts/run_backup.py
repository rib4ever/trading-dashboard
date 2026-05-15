from dotenv import load_dotenv
from src.services.backup_service import run_backup


if __name__ == "__main__":
    load_dotenv()
    run_backup()
