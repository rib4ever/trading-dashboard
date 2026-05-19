# Ravi Trading Journal OS — Future Phase Backlog

## Purpose

This document stores important future-phase improvements so the project can continue without losing context.

## Phase: Settings / Parameters Layer

Create a dedicated settings/config layer so Ravi can adjust important system behavior without editing code.

Recommended settings:

```text
Default Account
Default Risk %
Dashboard Base Currency
Trading session time ranges
Default screenshot slots
AI review max screenshots
AI review model
Dashboard privacy mode
Dashboard theme default
MT5 import account mapping
Broker symbol normalization rules
```

## Phase: Stronger Field Calculation System

Current automation calculates selected blank fields:

```text
Trade ID
Net P/L
Planned R
Result R
Result
```

Future improvements:

```text
Trade Duration
Risk/Reward in points
Price Move
Profit Factor
Expectancy
Average Win
Average Loss
Win/Loss Ratio
Daily P/L rollup
Monthly P/L rollup
Pair-level P/L rollup
Session-level P/L rollup
Setup-level P/L rollup
```

## Phase: MT5 Import

Build MT5 CSV import to auto-fill execution fields:

```text
Entry DateTime
Exit DateTime
Entry Price
Exit Price
Lot Size
Commission
Swap / Fees
Gross P/L
Net P/L
Broker Ticket ID
Broker Position ID
Original Symbol
Import Unique Key
Import Batch ID
```

Rules:

```text
Do not duplicate already imported trades.
Use Import Unique Key for duplicate detection.
Preserve manual journal notes and screenshots.
Allow manual correction if imported broker data needs adjustment.
```

## Phase: Advanced Dashboard

Enhance GitHub Pages dashboard with deeper insights:

```text
Advanced calendar analytics
Equity curve by account
Drawdown
Profit factor
Expectancy
Best/worst pair
Best/worst session
Best/worst setup
Rule-followed vs rule-broken performance
Mistake cost analysis
AI-detected evidence mismatch list
Trade detail drawer
Screenshot preview panel
Google Drive screenshot links
AI review cards
```

## Phase: AI Supervisor Enhancements

Improve AI review with:

```text
AI Evidence Warning auto-fill
AI Estimated Cost per review
AI Model Used
AI Review Token Usage
AI repeated-mistake memory
AI checklist scoring
AI pre-trade checklist later
```

## Phase: Privacy / Deployment

Current dashboard can be deployed publicly through GitHub Pages.

Future options:

```text
Make GitHub repo private if available
Move dashboard to private Vercel/Netlify/Cloudflare deployment
Add simple password gate
Separate public UI from private data file
```

## Current Reminder

Keep the field mapping audit in mind for all future work:

```text
ravi-trading-journal-os/docs/trades_field_mapping_audit.md
```

Do not add new fields randomly. Every new field should have:

```text
Owner: Manual / Automation / Calculated / Future Import / System
Purpose
Source
Dashboard usage
Automation impact
```
