# Ravi Trading Journal OS — Field Source-of-Truth Map

This document defines the clean field architecture for the Trading Journal OS. The goal is to avoid duplicate fields, prevent manual overload, and keep Notion, GitHub scripts, Google Drive evidence, AI review, dashboard export, and GitHub Pages aligned.

## Core principle

Each field must have one clear role:

1. Manual input — Ravi fills it.
2. Automation calculated — scripts fill it.
3. AI judged — AI fills it after screenshot/story review.
4. System/debug — workflow uses it, but Ravi normally ignores it.
5. Evidence/storage — screenshots/files and Drive links.

No field should exist only because it looks useful. If it is not used by Notion workflow, AI review, dashboard, KPI, Google Drive, or future MT5 import, it should be hidden first and later removed after confirmation.

---

## A. Manual input fields Ravi should care about

These are the fields Ravi should fill or verify when creating a trade manually.

| Field | Purpose | Source of truth | Notes |
|---|---|---|---|
| Trade Name | Human readable name | Manual | Keep simple and descriptive. |
| Pair | Instrument | Manual / future MT5 | Required for filtering and dashboard. |
| Direction | Buy/Sell | Manual / future MT5 | Required for analysis. |
| Account | Trading account | Manual / future MT5 | Useful for account-level analysis. |
| Entry DateTime | Broker entry date/time | Manual / future MT5 | MAIN time source. Store broker time correctly in Paris display. |
| Exit DateTime | Broker exit date/time | Manual / future MT5 | Used for duration and management. |
| Entry Price | Execution entry price | Manual / future MT5 | Required for trade analytics. |
| Exit Price | Execution exit price | Manual / future MT5 | Required after close. |
| Lot Size | Position size | Manual / future MT5 | Required for future calculation checks. |
| Stop Loss | Planned/actual SL | Manual | Used for risk/R validation. |
| Take Profit | Planned TP | Manual | Used for planned R/target logic. |
| Setup Model | Ravi's selected setup model | Manual, AI can challenge | AI Verdict/score becomes final judgment if selected setup is wrong. |
| Raw Journal Story | Ravi's own trade explanation | Manual | Required for AI review. |
| Screenshot Slot 1–5 Type/File | Chart evidence | Manual upload | Five slots retained for MTF evidence. |
| Net P/L | Final net broker P/L | Manual / future MT5 | Broker value is final truth. |
| Gross P/L | Gross broker P/L | Manual / future MT5 | Optional if net is available. |
| Commission | Broker commission | Manual / future MT5 / automation default | Blank should become 0 only when no commission exists. |
| Swap / Fees | Swap/fees/charges | Manual / future MT5 / automation default | Blank should become 0 if none. |

---

## B. Automation-calculated fields

These should be filled by `run_trade_maintenance.py` and not manually edited in normal use.

| Field | Purpose | Script |
|---|---|---|
| Trade ID | Stable trade identifier | trade_maintenance_service.py |
| Broker Entry Time | 24h display helper from Entry DateTime | trade_maintenance_service.py |
| Broker Exit Time | 24h display helper from Exit DateTime | trade_maintenance_service.py |
| Auto Session | Session from broker entry time | trade_maintenance_service.py |
| Killzone | Killzone from broker entry time | trade_maintenance_service.py |
| Price Move | Direction-adjusted price movement | trade_maintenance_service.py |
| Planned R | Planned reward/risk from Entry/SL/TP | trade_maintenance_service.py |
| Result R | Net P/L / Risk Amount when risk exists | trade_maintenance_service.py |
| Result | Win/Loss/BE from Net P/L if blank | trade_maintenance_service.py |
| Trade Duration Minutes | Exit DateTime - Entry DateTime | trade_maintenance_service.py |
| Dashboard Ready | Data quality flag | trade_maintenance_service.py |
| Missing Required Fields | Missing-source report | trade_maintenance_service.py |
| Calculation Status | Complete/Partial/Needs Manual Input | trade_maintenance_service.py |
| Auto Calculation Notes | What automation changed | trade_maintenance_service.py |

Important: Dashboard P/L cards should not depend on Dashboard Ready. A valid Net P/L + Result can be counted, while Dashboard Ready separately measures data quality.

---

## C. AI-judged fields

These are populated by `run_ai_trade_review.py`. Ravi should not manually score trades.

| Field | Purpose | Source |
|---|---|---|
| AI Review Status | Review workflow status | AI review service |
| AI Review | Short strict summary | AI review service |
| AI Story Review | Full structured review | AI review service |
| AI Reality Check | Journal vs screenshot validation | AI review service |
| AI Mistake Diagnosis | Strict mistake explanation | AI review service |
| AI Future Rules | Future rules for this exact error | AI review service |
| AI Evidence Warning | Missing evidence + score reasoning | AI review service |
| AI Review Confidence | 0–1 confidence | AI review service |
| AI Reviewed Time | Review timestamp | AI review service |
| AI Verdict | Final AI validity verdict | AI review service |
| AI Trade Score | Overall strict score 0–100 | AI review service |
| AI HTF Context Score | HTF/context score | AI review service |
| AI Setup Quality Score | Setup/POI/FVG/OB quality | AI review service |
| AI Entry Execution Score | Entry timing/confirmation score | AI review service |
| AI Risk Management Score | SL/TP/management score | AI review service |
| AI Journal Accuracy Score | Story vs chart truth score | AI review service |
| AI Screenshot Evidence Score | Evidence quality score | AI review service |
| AI Discipline Score | Rules/patience/emotion score | AI review service |

AI Verdict and AI Trade Score replace manual scoring. If Ravi selects the wrong Setup Model, AI must challenge it in AI Verdict, AI Review, and the score breakdown.

---

## D. Evidence and storage fields

| Field | Purpose | Source |
|---|---|---|
| Google Drive Trade Folder | Main Drive folder for trade evidence | screenshot_sync_service.py |
| Last Screenshot Sync Time | Screenshot sync timestamp | screenshot_sync_service.py |
| Screenshot Sync Status | Sync state | screenshot_sync_service.py |
| AI Story Screenshots | Optional mapping/debug for story screenshot alignment | AI/dashboard export |
| Trade Screenshots database | Normalized screenshot records | screenshot_sync_service.py |
| Dashboard screenshot assets | Local persistent copies in GitHub Pages | dashboard_export_service.py |

Google Drive remains the long-term original screenshot storage. GitHub Pages stores only dashboard-optimized persistent copies to prevent broken previews.

---

## E. System/import/debug fields

These should stay at the bottom or be hidden from the manual entry view.

| Field | Purpose | Keep? |
|---|---|---|
| Broker Position ID | Future MT5 position matching | Keep hidden |
| Broker Ticket ID | Future MT5 ticket matching | Keep hidden |
| Import Source | Future import/source tracking | Keep hidden |
| Import Status | Future import state | Keep hidden |
| Import Batch ID | Batch tracking | Keep hidden |
| Import Unique Key | Duplicate prevention | Keep hidden |
| Last Import Time | Import timestamp | Keep hidden |
| Created Time | Notion system field | Keep hidden |
| Last Edited Time | Notion system field | Keep hidden |
| Daily Review | Relation to daily review DB | Keep if daily review remains active |
| Place | Not useful currently | Candidate remove/hide |
| Original Symbol | Future MT5 raw symbol | Keep hidden if MT5 import planned |

---

## F. Merge / hide / remove candidates

Do not delete directly. First hide, verify no code/dashboard dependency, then remove after confirmation.

| Current field | Recommendation | Reason |
|---|---|---|
| Date | Keep but hide from manual entry | Entry DateTime is source of truth. Date can be fallback only. |
| Broker Entry Time | Keep as automation display helper, hide if too noisy | Derived from Entry DateTime. Useful for quick mobile view. |
| Broker Exit Time | Keep as automation display helper, hide if too noisy | Derived from Exit DateTime. |
| Session | Keep as manual/session expectation for now | AI can compare against Auto Session. Later may merge. |
| Auto Session | Keep automation field | Dashboard/session KPI can use this reliably. |
| Followed Rules | Keep as self-check, but not final truth | AI Verdict/AI Score is final judgment. |
| Trade Quality | Candidate remove/hide | Replaced by AI Trade Score. |
| Notes | Candidate hide/merge into Raw Journal Story | Avoid duplicate journal text. |
| AI Estimated Cost | Keep hidden | Useful for API spend tracking if populated later. |
| AI Review Mode | Keep hidden/default | Useful for controlling API cost. |
| AI Story Screenshots | Keep hidden/debug | Only if dashboard uses story screenshot alignment. |
| Place | Candidate remove | Not used by trading KPI/AI currently. |

---

## G. Pipeline mapping

Main workflow: `.github/workflows/ravi_full_pipeline.yml`

1. `run_trade_maintenance.py`
   - Fills automation fields.
   - Calculates time/session/killzone and P/L helper fields.

2. `run_screenshot_sync.py`
   - Reads screenshot slots.
   - Creates Drive folders/files.
   - Writes normalized screenshot records.
   - Can mark AI status ready.

3. `run_ai_trade_review.py`
   - Reads trade context + screenshot records.
   - Sends contact sheet to OpenAI.
   - Writes strict AI review + AI score fields.

4. `run_trade_maintenance.py` again
   - Final cleanup after AI review.

5. `run_dashboard_export.py`
   - Exports Notion trade fields + AI scores + screenshots to `ravi-dashboard/data/trades.json`.
   - Downloads persistent screenshot assets to `ravi-dashboard/assets/screenshots`.

6. GitHub Pages deploy
   - Publishes `ravi-dashboard`.

---

## H. Dashboard mapping

Dashboard should use:

| Dashboard area | Field source |
|---|---|
| Calendar day | `date` exported from Entry DateTime Paris-local date |
| P/L KPI cards | Net P/L + Result, not Dashboard Ready |
| Session charts | Auto Session preferred; Session fallback if needed |
| Killzone analytics | Killzone |
| Trade detail modal | Entry/Exit Price, Lot, SL, TP, AI Verdict, AI Score |
| AI score cards | AI Trade Score and score breakdown |
| Screenshot display | Persistent local screenshot asset first, Drive thumbnail fallback |

---

## I. Cleanup rule before deletion

Before dropping any Notion property:

1. Search GitHub for the exact field name.
2. Confirm it is not exported in dashboard_export_service.py.
3. Confirm it is not read/written by maintenance, screenshot sync, or AI review service.
4. Confirm it is not used in a dashboard view/KPI.
5. Hide it first, run the full pipeline once, then delete only after Ravi confirms.
