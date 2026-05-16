import io
import json
import os

from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


class GoogleDriveClient:
    """Google Drive API client for Ravi Trading Journal OS.

    Preferred for personal Gmail Drive: OAuth refresh token.
    Fallback for Workspace Shared Drives: service account JSON.
    """

    def __init__(self):
        credentials = self._build_credentials()
        self.service = build("drive", "v3", credentials=credentials)

    def _build_credentials(self):
        scopes = ["https://www.googleapis.com/auth/drive"]

        oauth_client_id = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        oauth_client_secret = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")
        oauth_refresh_token = os.environ.get("GOOGLE_OAUTH_REFRESH_TOKEN")

        if oauth_client_id and oauth_client_secret and oauth_refresh_token:
            return Credentials(
                token=None,
                refresh_token=oauth_refresh_token,
                token_uri="https://oauth2.googleapis.com/token",
                client_id=oauth_client_id,
                client_secret=oauth_client_secret,
                scopes=scopes,
            )

        raw_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
        if raw_json:
            info = json.loads(raw_json)
            return service_account.Credentials.from_service_account_info(info, scopes=scopes)

        raise RuntimeError(
            "Missing Google Drive credentials. Add OAuth secrets GOOGLE_OAUTH_CLIENT_ID, "
            "GOOGLE_OAUTH_CLIENT_SECRET, GOOGLE_OAUTH_REFRESH_TOKEN, or fallback GOOGLE_SERVICE_ACCOUNT_JSON."
        )

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
