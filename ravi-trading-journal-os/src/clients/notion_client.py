import os
import time
import requests

NOTION_VERSION = "2022-06-28"
RETRY_STATUS_CODES = {429, 500, 502, 503, 504}


class NotionClient:
    """Minimal Notion API client for Ravi Trading Journal OS with retry support."""

    def __init__(self):
        self.token = os.environ.get("NOTION_TOKEN")
        if not self.token:
            raise RuntimeError("Missing NOTION_TOKEN")
        self.max_retries = int(os.environ.get("NOTION_MAX_RETRIES", "5"))
        self.timeout_seconds = int(os.environ.get("NOTION_TIMEOUT_SECONDS", "120"))
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        }

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Request wrapper that retries transient Notion/API gateway errors.

        This protects the GitHub Actions pipeline from temporary Notion 429/5xx/504
        failures, especially when querying larger databases.
        """
        last_response = None
        last_exc = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = requests.request(
                    method,
                    url,
                    headers=self.headers,
                    timeout=self.timeout_seconds,
                    **kwargs,
                )
                last_response = response
                if response.status_code not in RETRY_STATUS_CODES:
                    response.raise_for_status()
                    return response

                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    wait_seconds = min(float(retry_after), 60)
                else:
                    wait_seconds = min(8 * attempt, 60)
                print(
                    f"Notion temporary error {response.status_code} on attempt "
                    f"{attempt}/{self.max_retries}. Retrying in {wait_seconds:.0f}s."
                )
                if attempt < self.max_retries:
                    time.sleep(wait_seconds)
                    continue
                response.raise_for_status()
            except requests.RequestException as exc:
                last_exc = exc
                wait_seconds = min(8 * attempt, 60)
                print(
                    f"Notion request exception on attempt {attempt}/{self.max_retries}: "
                    f"{exc}. Retrying in {wait_seconds:.0f}s."
                )
                if attempt < self.max_retries:
                    time.sleep(wait_seconds)
                    continue
                raise

        if last_response is not None:
            last_response.raise_for_status()
        if last_exc:
            raise last_exc
        raise RuntimeError("Notion request failed without response")

    def query_database(self, database_id: str, payload: dict | None = None) -> list[dict]:
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = self._request("POST", url, json=payload or {})
        return response.json().get("results", [])

    def query_database_all(self, database_id: str, payload: dict | None = None) -> list[dict]:
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        request_payload = dict(payload or {})
        results: list[dict] = []
        while True:
            response = self._request("POST", url, json=request_payload)
            data = response.json()
            results.extend(data.get("results", []))
            if not data.get("has_more"):
                break
            request_payload["start_cursor"] = data.get("next_cursor")
        return results

    def create_page(self, database_id: str, properties: dict) -> dict:
        url = "https://api.notion.com/v1/pages"
        payload = {"parent": {"database_id": database_id}, "properties": properties}
        response = self._request("POST", url, json=payload)
        return response.json()

    def update_page(self, page_id: str, properties: dict) -> dict:
        url = f"https://api.notion.com/v1/pages/{page_id}"
        response = self._request("PATCH", url, json={"properties": properties})
        return response.json()
