import io
import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


class GoogleDriveClient:
    """Minimal Google Drive API client for folders and uploads."""

    def __init__(self):
        raw_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
        if not raw_json:
            raise RuntimeError("Missing GOOGLE_SERVICE_ACCOUNT_JSON")

        info = json.loads(raw_json)
        scopes = ["https://www.googleapis.com/auth/drive"]
        credentials = service_account.Credentials.from_service_account_info(info, scopes=scopes)
        self.service = build("drive", "v3", credentials=credentials)

    def get_or_create_folder(self, name: str, parent_id: str) -> dict:
        safe_name = name.replace("'", "\\'")
        query = (
            f"name = '{safe_name}' and "
            f"mimeType = 'application/vnd.google-apps.folder' and "
            f"'{parent_id}' in parents and trashed = false"
        )
        result = self.service.files().list(q=query, fields="files(id,name,webViewLink)", supportsAllDrives=True).execute()
        files = result.get("files", [])
        if files:
            return files[0]

        metadata = {"name": name, "mimeType": "application/vnd.google-apps.folder", "parents": [parent_id]}
        return self.service.files().create(body=metadata, fields="id,name,webViewLink", supportsAllDrives=True).execute()

    def upload_bytes(self, file_bytes: bytes, filename: str, parent_folder_id: str, mime_type: str) -> dict:
        media = MediaIoBaseUpload(io.BytesIO(file_bytes), mimetype=mime_type, resumable=False)
        metadata = {"name": filename, "parents": [parent_folder_id]}
        return self.service.files().create(
            body=metadata,
            media_body=media,
            fields="id,name,webViewLink,webContentLink",
            supportsAllDrives=True,
        ).execute()
