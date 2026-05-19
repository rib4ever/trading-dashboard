# Current Project State — Ravi Trading Journal OS

## Confirmed Working Loop

```text
Notion Trade screenshot slot
→ Screenshot Sync GitHub Action
→ Python sync service
→ Google Drive upload using Google OAuth
→ Trade Screenshots record
→ Trade status updated to Synced to Drive
```

## Working Test Trade

```text
Trade Name: TEST XAUUSD Buy Screenshot Sync
Trade ID: TRD-20260516-TEST01
Result: Successfully synced 1 screenshot
```

## Active Notion Pages

```text
📊 Ravi Trading Journal OS
Trading Dashboard
Trade Entry Workspace Guide
```

## Active Notion Databases

```text
📘 Trades
🖼 Trade Screenshots
🧠 Trading Setups / Playbooks
📝 Daily Review
⚙️ Dashboard Metrics
```

## Active Google Drive Root

```text
Trading Journal OS
https://drive.google.com/drive/folders/1xTKxCN4EKnwMMKdidF6NET4V57Fh4Rfl
```

## GitHub Workflow

```text
.github/workflows/ravi_screenshot_sync.yml
```

Runs:

```text
Manual workflow_dispatch
Automatic every 15 minutes
```

## GitHub Secrets Required

```text
NOTION_TOKEN
NOTION_TRADES_DATABASE_ID
NOTION_SCREENSHOTS_DATABASE_ID
GOOGLE_DRIVE_ROOT_FOLDER_ID
GOOGLE_OAUTH_CLIENT_ID
GOOGLE_OAUTH_CLIENT_SECRET
GOOGLE_OAUTH_REFRESH_TOKEN
GOOGLE_SERVICE_ACCOUNT_JSON
```

OAuth is preferred. Service account is fallback only.

## Screenshot Sync Status Logic

```text
Ready to Sync: picked up by automation
Synced to Drive: successful sync
Pending Upload: slot type selected but file missing
Needs Manual Check: file uploaded but slot type missing or required data incomplete
Error: sync failed
Not Started: no screenshot slots used or sync not requested
```

## Duplicate Logic

Screenshot source key:

```text
Trade ID | Slot Number | Slot Type | Original File Name
```

The system:

```text
- skips exact duplicates
- reuses existing Drive trade folders
- never overwrites screenshots
- never deletes screenshots
- allows later added screenshots by setting trade back to Ready to Sync
```

## Notion Views Created

Inside Trades:

```text
📥 Manual Trade Entry
🚦 Ready to Sync
Pending Upload
Needs Manual Check
Sync Errors
Synced to Drive
```

Inside Trading Dashboard:

```text
Dashboard - Ready to Sync
Dashboard - Pending Upload
Dashboard - Needs Manual Check
Dashboard - Sync Errors
Dashboard - Recently Synced
```

## Next Planned Work

1. Improve trade record structure and properties for better manual journaling.
2. Create dashboard metric views and later automated metric refresh.
3. Build MT5 CSV import later.
