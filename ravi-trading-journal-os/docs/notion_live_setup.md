# Notion Live Setup

## Parent Page Needed

The Notion connector requires an existing parent page ID or URL before it can create databases.

Manual action needed from Ravi:
1. Create or open a Notion page.
2. Recommended title: Ravi Trading Journal OS.
3. Share/send the page URL.

## Databases to Create Under Parent Page

1. Trades
2. Trade Screenshots
3. Trading Setups / Playbooks
4. Daily Review
5. Dashboard Metrics

## Screenshot Slot Logic

Each trade has 5 optional screenshot slots:
- Screenshot Slot 1 Type + File
- Screenshot Slot 2 Type + File
- Screenshot Slot 3 Type + File
- Screenshot Slot 4 Type + File
- Screenshot Slot 5 Type + File

Rules:
- Empty slot: ignored
- Type without file: Pending Upload
- File without type: Needs Manual Check
- Type + file: processed by automation

## Main Automation Statuses

Screenshot Sync Status:
- Not Started
- Pending Upload
- Ready to Sync
- Processing
- Synced to Drive
- Needs Manual Check
- Error
