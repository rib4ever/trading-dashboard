# Trades Database — Field Mapping Audit

## Purpose

This document defines how every important field in the Notion `📘 Trades` database should be used, who owns it, and how it feeds automation, AI review, and the visual dashboard.

## Field Ownership Types

```text
Manual = Ravi fills it directly in Notion.
Automation = GitHub/Python fills or updates it.
Calculated = automation calculates when enough source inputs are available.
Future Import = MT5 CSV import will fill it later.
System = Notion-created read-only field.
```

## Core Required Fields

| Field | Type | Owner | Required For | Rule |
|---|---|---:|---|---|
| Trade Name | Title | Manual | All views | Short readable name of the trade. |
| Trade ID | Text | Automation | Screenshot sync, AI review, dashboard | Auto-generated if blank. Format: TRD-YYYYMMDD-XXXXXX. |
| Date | Date | Manual | Dashboard/calendar | Main trade date. If blank, automation may fall back to Entry DateTime or created time. |
| Pair | Select | Manual / Future Import | Dashboard grouping, AI context | Example: XAUUSD, BTCUSD, NAS100. |
| Direction | Select | Manual / Future Import | Dashboard grouping, AI context | Buy or Sell. |
| Account | Select | Manual / Future Import | Account-level reporting | IC Markets, FTMO, Demo, etc. |
| Session | Select | Manual | Session analytics | London, New York, Asia, Overlap, etc. |
| Setup Model | Select | Manual | Setup performance | SMC, FVG, OB, NCI, etc. |

## Execution / KPI Fields

| Field | Type | Owner | Calculation Rule |
|---|---|---:|---|
| Entry DateTime | Date | Manual / Future Import | Used for time analysis and trade duration later. |
| Exit DateTime | Date | Manual / Future Import | Used for time analysis and trade duration later. |
| Entry Price | Number | Manual / Future Import | Source field. |
| Exit Price | Number | Manual / Future Import | Source field. |
| Lot Size | Number | Manual / Future Import | Source field. |
| Stop Loss | Number | Manual | Source field for Planned R. |
| Take Profit | Number | Manual | Source field for Planned R. |
| Risk % | Number | Manual | Used for risk dashboard. |
| Risk Amount | Number | Manual / Future Import | Source for Result R calculation. |
| Gross P/L | Number | Manual / Future Import | Source for Net P/L calculation. |
| Commission | Number | Manual / Future Import | Defaults to 0 when blank. |
| Swap / Fees | Number | Manual / Future Import | Defaults to 0 when blank. |
| Net P/L | Number | Calculated / Manual | If blank and Gross P/L exists: Net P/L = Gross P/L - Commission - Swap/Fees. |
| Planned R | Number | Calculated / Manual | If blank and Entry, SL, TP exist: Planned R = abs(TP - Entry) / abs(Entry - SL). |
| Result R | Number | Calculated / Manual | If blank and Net P/L + Risk Amount exist: Result R = Net P/L / abs(Risk Amount). |
| Result | Select | Calculated / Manual | If blank and Net P/L exists: Win if >0, Loss if <0, Break Even if =0. |

## Review / Psychology Fields

| Field | Type | Owner | Purpose |
|---|---|---:|---|
| Trade Quality | Select | Manual / AI later | Subjective quality rating. |
| Followed Rules | Checkbox | Manual | Key discipline metric. |
| Mistake Type | Multi-select | Manual / AI later | Mistake tracking and dashboard grouping. |
| Raw Journal Story | Text | Manual | Ravi writes simple trade story here. |
| Notes | Text | Manual | Optional extra notes. |

## Screenshot Fields

| Field | Type | Owner | Rule |
|---|---|---:|---|
| Screenshot Slot 1 Type/File | Select/File | Manual | Upload screenshot and choose its role. |
| Screenshot Slot 2 Type/File | Select/File | Manual | Optional. |
| Screenshot Slot 3 Type/File | Select/File | Manual | Optional. |
| Screenshot Slot 4 Type/File | Select/File | Manual | Optional. |
| Screenshot Slot 5 Type/File | Select/File | Manual | Optional. |
| Screenshot Sync Status | Select | Manual + Automation | User sets Ready to Sync. Automation updates result. |
| Screenshot Sync Notes | Text | Automation | Processing result and errors. |
| Last Screenshot Sync Time | Date | Automation | Updated after sync. |
| Screenshots Processed | Checkbox | Automation | Checked after successful sync. |
| Google Drive Trade Folder | URL | Automation | Drive folder for the trade. |

## AI Review Fields

| Field | Type | Owner | Rule |
|---|---|---:|---|
| AI Review Status | Select | Manual + Automation | User sets Ready for AI Review. Automation updates result. |
| AI Review | Text | AI Automation | Summary of trade. |
| AI Reality Check | Text | AI Automation | Checks journal vs screenshots. |
| AI Mistake Diagnosis | Text | AI Automation | Main mistakes/weaknesses. |
| AI Future Rules | Text | AI Automation | Rules to avoid repeated mistakes. |
| AI Review Confidence | Number | AI Automation | 0.0 to 1.0 confidence. |
| AI Reviewed Time | Date | AI Automation | Timestamp. |
| AI Review Mode | Select | AI Automation / Manual | Contact Sheet is default. |
| AI Evidence Warning | Text | AI Automation / future | Evidence mismatch warnings. |
| AI Estimated Cost | Number | Future Automation | Estimated cost per review later. |

## Import Fields

| Field | Type | Owner | Purpose |
|---|---|---:|---|
| Import Source | Select | Manual / Future Import | Manual, MT5 CSV, Python Script, Backtest. |
| Import Status | Select | Future Import | Import processing result. |
| Import Unique Key | Text | Future Import | Duplicate detection key. |
| Import Batch ID | Text | Future Import | CSV batch/run identifier. |
| Last Import Time | Date | Future Import | Import timestamp. |
| Broker Ticket ID | Text | Future Import | MT5/broker ticket. |
| Broker Position ID | Text | Future Import | MT5/broker position. |
| Original Symbol | Text | Future Import | Raw broker symbol before normalization. |

## Current Automation Calculation Behavior

The `Ravi Trade Maintenance` workflow now fills:

```text
Trade ID
Net P/L
Planned R
Result R
Result
```

It only fills calculation fields when they are blank and enough source data exists. It does not overwrite existing manual values.

## Calculation Requirements

### Net P/L

Required source fields:

```text
Gross P/L
Commission optional
Swap / Fees optional
```

Formula:

```text
Net P/L = Gross P/L - Commission - Swap / Fees
```

### Planned R

Required source fields:

```text
Entry Price
Stop Loss
Take Profit
```

Formula:

```text
Planned R = abs(Take Profit - Entry Price) / abs(Entry Price - Stop Loss)
```

### Result R

Required source fields:

```text
Net P/L
Risk Amount
```

Formula:

```text
Result R = Net P/L / abs(Risk Amount)
```

### Result

Required source field:

```text
Net P/L
```

Logic:

```text
Net P/L > 0 → Win
Net P/L < 0 → Loss
Net P/L = 0 → Break Even
```

## Required Settings / Parameters

Recommended user-level settings to add later:

```text
Default Account
Default Risk %
Dashboard Base Currency
Default screenshot slots
Default timezone
Trading sessions time ranges
AI review max screenshots
AI review model
```

Current code-level defaults:

```text
AI review mode: Contact Sheet
AI max screenshots: 3
Dashboard theme: Dark Professional
Dashboard source: ravi-dashboard/data/trades.json
```

## Main Recommendations

1. Keep manual entry simple. Ravi should use `Daily Entry - Minimal` and `Execution & KPI Input`.
2. Do not manually fill system fields unless debugging.
3. Let maintenance automation fill Trade ID and blank KPI calculations.
4. Keep Net P/L, Result R, and Result editable for manual correction, but only when necessary.
5. Later, when MT5 CSV import is built, import should become the primary source for execution fields.
6. Add a settings/config database later for risk model, dashboard currency, and session time logic.
