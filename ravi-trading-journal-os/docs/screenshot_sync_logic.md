# Screenshot Sync Service v1 Logic

## Goal

Read Notion Trades screenshot slots, validate them, download valid images, rename them, upload them to Google Drive, create screenshot records, and update the original trade.

## Trigger

Only process trades where:

```text
Screenshot Sync Status = Ready to Sync
```

## Required Trade Fields

- Trade ID
- Date
- Pair
- Direction

Missing required fields mark the trade as Needs Manual Check.

## Slot Rules

Each trade has five optional screenshot slots.

```text
Screenshot Slot 1 Type + Screenshot Slot 1 File
Screenshot Slot 2 Type + Screenshot Slot 2 File
Screenshot Slot 3 Type + Screenshot Slot 3 File
Screenshot Slot 4 Type + Screenshot Slot 4 File
Screenshot Slot 5 Type + Screenshot Slot 5 File
```

Rules:

```text
Type empty + File empty = ignore
Type selected + File empty = Pending Upload
Type empty + File uploaded = Needs Manual Check
Type selected + File uploaded = process
```

## Filename Rule

```text
{Trade ID}_{Pair}_{Date}_{Timeframe}_{Image Type}.{extension}
```

Example:

```text
TRD-20260516-0001_XAUUSD_2026-05-16_5M_ENTRY.png
```

## Duplicate Prevention

Use source key:

```text
Trade ID | Slot Number | Slot Type | Original File Name
```

Before uploading, check if that source key already exists in Trade Screenshots.

## Drive Destination

```text
01_Trades/YYYY/YYYY-MM/{Trade ID}_{Pair}_{Direction}/
├── 01_context
├── 02_entry
├── 03_exit
├── 04_review
├── 05_mistakes
└── 99_extra
```

## Final Status Priority

```text
1. Error
2. Needs Manual Check
3. Synced to Drive
4. Pending Upload
5. Not Started
```
