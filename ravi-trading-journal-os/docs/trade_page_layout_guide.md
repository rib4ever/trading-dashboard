# Trade Page Layout Guide

This document mirrors the Notion page `📘 Trade Page Layout Guide` and defines how Ravi should use the opened trade page and database views.

## Quick Rule

Fill only the manual sections first. Let `Ravi Full Pipeline` handle automation, calculations, screenshot sync, AI review, dashboard export, and dashboard deployment.

Normal one-button process:

1. Fill manual trade details.
2. Fill execution/KPI inputs if available.
3. Upload screenshots in all relevant screenshot slots.
4. Set `Screenshot Sync Status` to `Ready to Sync`.
5. Write `Raw Journal Story`.
6. Run `GitHub → Actions → Ravi Full Pipeline → Run workflow`.

## 01 — Manual Trade Input

User-filled fields:

- Trade Name
- Date
- Pair
- Direction
- Account
- Session
- Setup Model
- Raw Journal Story
- Followed Rules
- Mistake Type
- Trade Quality

Recommended view: `01 Manual Required Input`

## 02 — Execution / KPI Input

User-filled or future MT5-import fields:

- Entry DateTime
- Exit DateTime
- Entry Price
- Exit Price
- Lot Size
- Stop Loss
- Take Profit
- Risk Amount
- Risk %
- Commission
- Swap / Fees

Automation defaults blank `Commission` and `Swap / Fees` to 0.

Recommended view: `02 Execution KPI Input`

## 03 — Screenshots / Evidence Upload — All 5 Slots

Each screenshot slot needs both type and file.

- Screenshot Slot 1 Type / File
- Screenshot Slot 2 Type / File
- Screenshot Slot 3 Type / File
- Screenshot Slot 4 Type / File
- Screenshot Slot 5 Type / File

Recommended usage:

- Slot 1: Before 4H or higher timeframe context
- Slot 2: Before 1H or liquidity/context
- Slot 3: Entry 5M or Entry 3M
- Slot 4: Exit 5M or management screenshot
- Slot 5: Review, Mistake, or Extra

Before running pipeline, set `Screenshot Sync Status = Ready to Sync`.

Recommended view: `03 Screenshot Upload - All 5 Slots`

## 04 — AI Review Fields

Normally automation owns these fields:

- AI Review Status
- AI Review Mode
- AI Review
- AI Reality Check
- AI Evidence Warning
- AI Mistake Diagnosis
- AI Future Rules
- AI Review Confidence
- AI Reviewed Time
- AI Estimated Cost

The full pipeline can automatically set `AI Review Status = Ready for AI Review` after successful screenshot sync when `Raw Journal Story` is filled.

Recommended view: `05 AI Review Fields`

## 05 — Auto Calculated Fields

Automation-maintained fields:

- Trade ID
- Dashboard Ready
- Missing Required Fields
- Calculation Status
- Auto Calculation Notes
- Price Move
- Gross P/L
- Net P/L
- Planned R
- Result R
- Result
- Trade Duration Minutes

Recommended view: `04 Auto Calculated Fields`

## 06 — System / Debug Fields

Debug/future import fields:

- Import Source
- Import Status
- Import Unique Key
- Import Batch ID
- Last Import Time
- Broker Ticket ID
- Broker Position ID
- Original Symbol
- Last Edited Time
- Created Time

Use only for troubleshooting or future MT5 import work.
