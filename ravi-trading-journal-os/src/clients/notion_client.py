import os
import requests

NOTION_VERSION = "2022-06-28"


class NotionClient:
    """Minimal Notion API client for Ravi Trading Journal OS."""

    def __init__(self):
        self.token = os.environ.get("NOTION_TOKEN")
        if not self.token:
            raise RuntimeError("Missing NOTION_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def query_database(self, database_id: str, payload: dict | None = None) -> list[dict]:
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.post(url, headers=self.headers, json=payload or {})
        response.raise_for_status()
        return response.json().get("results", [])

    def create_page(self, database_id: str, properties: dict) -> dict:
        url = "https://api.notion.com/v1/pages"
        payload = {"parent": {"database_id": database_id}, "properties": properties}
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def update_page(self, page_id: str, properties: dict) -> dict:
        url = f"https://api.notion.com/v1/pages/{page_id}"
        response = requests.patch(url, headers=self.headers, json={"properties": properties})
        response.raise_for_status()
        return response.json()
