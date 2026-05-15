# Google Drive Structure

Root folder required:

```text
Trading Journal OS
```

## Folder Tree

```text
Trading Journal OS/
├── 00_System/
│   ├── config/
│   ├── logs/
│   │   ├── screenshot_sync_logs/
│   │   ├── trade_import_logs/
│   │   ├── dashboard_export_logs/
│   │   ├── metrics_logs/
│   │   └── backup_logs/
│   └── error_exports/
│       ├── failed_screenshot_sync/
│       ├── failed_trade_imports/
│       ├── needs_manual_check/
│       └── failed_dashboard_exports/
├── 01_Trades/
│   └── 2026/
│       ├── 2026-01/
│       ├── 2026-02/
│       ├── 2026-03/
│       ├── 2026-04/
│       ├── 2026-05/
│       ├── 2026-06/
│       ├── 2026-07/
│       ├── 2026-08/
│       ├── 2026-09/
│       ├── 2026-10/
│       ├── 2026-11/
│       └── 2026-12/
├── 02_Imports/
│   ├── MT5_CSV/
│   │   ├── pending/
│   │   ├── processed/
│   │   └── failed/
│   ├── Broker_Exports/
│   │   ├── pending/
│   │   ├── processed/
│   │   └── failed/
│   └── Manual_CSV/
│       ├── pending/
│       ├── processed/
│       └── failed/
├── 03_Reviews/
│   ├── Daily/2026/
│   ├── Weekly/2026/
│   └── Monthly/2026/
├── 04_Backtesting/
│   ├── XAUUSD/
│   ├── BTCUSD/
│   ├── NAS100/
│   ├── Forex/
│   ├── Crypto/
│   └── Other/
├── 05_Dashboard_Exports/
│   ├── json/
│   ├── csv/
│   └── snapshots/
├── 06_Reports/
│   ├── Daily_AI_Reports/
│   ├── Weekly_AI_Reports/
│   ├── Monthly_Reports/
│   ├── Mistake_Reports/
│   └── Setup_Reports/
├── 07_Playbook_Examples/
└── 99_Backups/
    ├── notion_exports/
    ├── drive_index_exports/
    ├── github_data_backups/
    ├── database_schema_backups/
    └── emergency_exports/
```

## Trade Folder Rule

```text
01_Trades/YYYY/YYYY-MM/{Trade ID}_{Pair}_{Direction}/
├── 01_context/
├── 02_entry/
├── 03_exit/
├── 04_review/
├── 05_mistakes/
└── 99_extra/
```

The Python automation will create individual trade folders and subfolders dynamically when the Google Drive API credentials are connected.
