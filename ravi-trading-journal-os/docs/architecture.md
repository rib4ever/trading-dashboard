# Ravi Trading Journal OS Architecture

## Core Network Mapping

```text
Notion = user interface and journal database
Google Drive = permanent storage for screenshots, CSVs, reports, backups
GitHub = automation code, config, workflows, future dashboard
Python = sync/import/metrics/export/backup engine
GitHub Actions = scheduled and manual automation runner
```

## MVP Flow

```text
1. Trade is created manually or imported from MT5 CSV into Notion Trades.
2. Ravi uploads screenshots into one of five Notion screenshot slots.
3. Ravi selects the screenshot slot type.
4. Screenshot Sync reads trades marked Ready to Sync.
5. Valid screenshots are downloaded from Notion temporary URLs.
6. Images are renamed using Trade ID, pair, date, timeframe, and image type.
7. Images are uploaded permanently into Google Drive.
8. Trade Screenshots records are created in Notion.
9. Trades are updated with sync status and Drive folder URL.
10. Metrics service reads trades and updates Dashboard Metrics.
11. Dashboard export service prepares JSON/CSV for future GitHub Pages app.
```

## Build Priority

1. Notion core databases
2. GitHub scaffold and config
3. Google Drive root/folder IDs
4. Screenshot Sync Service v1
5. MT5 CSV Import Service
6. Metrics Refresh Service
7. Dashboard Export Service
8. Backup Service
9. AI Review Service

## Safety Rules

- Do not process all trades blindly.
- Only process trades marked Ready to Sync.
- Do not overwrite existing Drive files in v1.
- Do not store API tokens in repo.
- Store secrets only in GitHub Secrets.
- Empty screenshot slots are ignored.
- File without selected type is Needs Manual Check.
- Type without file is Pending Upload.
