# Ravi Trading Journal OS — Core Network Map

## Purpose

This document is the permanent operating map for the Trading Journal OS project. It exists so the project can be resumed without losing context.

## High-Level Architecture

```text
Notion = trade input, journal, screenshots, AI review output, system status
Google Drive = permanent screenshot/file archive
GitHub Actions = automation engine
OpenAI API = AI Trade Supervisor
GitHub Repository = code, workflows, exported dashboard data
GitHub Pages = live visual dashboard
```

## Core Data Loop

```text
1. User creates or updates trade in Notion
2. User uploads screenshots into Notion screenshot slots
3. Screenshot Sync workflow reads Notion
4. Python uploads screenshots to Google Drive
5. Python creates Trade Screenshots records in Notion
6. Python updates trade sync status
7. User writes simple Raw Journal Story
8. AI Trade Review workflow reads trade + screenshots
9. AI writes review, reality check, mistakes, and future rules to Notion
10. Dashboard Export workflow reads Notion trades
11. Dashboard Export writes ravi-dashboard/data/trades.json
12. GitHub Pages deploys visual dashboard
```

## Main Notion Databases

### Trades

Main source of truth for all trades.

Used for:

```text
Manual trade entry
Execution/KPI data
Screenshot slots
AI review status
Dashboard source data
```

Important views:

```text
Daily Entry - Minimal
Execution & KPI Input
Clean Trade Journal
AI Supervisor - Clean
Automation Debug - System Fields
KPI Source - Completed Trades
KPI Missing Execution Data
KPI - By Pair
KPI - By Setup
KPI - By Session
KPI - Mistake Tracker
KPI - Rule Following
```

### Trade Screenshots

Permanent Notion index of synced screenshot files.

Used for:

```text
Google Drive file references
Screenshot slot metadata
AI image retrieval
Audit trail
```

### Trading Setups / Playbooks

Strategy library for trading models and playbooks.

### Daily Review

Daily psychological and review tracking.

### Dashboard Metrics

Future metrics cache for advanced dashboard calculations.

## Google Drive Structure

Root folder:

```text
Trading Journal OS
```

Purpose:

```text
Permanent screenshot archive
Trade-level folders
Import files
Processed/failed files later for MT5 import
```

## GitHub Workflows

### Ravi Screenshot Sync

File:

```text
.github/workflows/ravi_screenshot_sync.yml
```

Purpose:

```text
Notion screenshot slot → Google Drive upload → Notion screenshot record → Notion status update
```

### Ravi AI Trade Review

File:

```text
.github/workflows/ravi_ai_trade_review.yml
```

Purpose:

```text
Raw Journal Story + synced screenshots → OpenAI review → Notion AI review fields
```

Uses contact sheet mode to reduce cost:

```text
Up to 3 screenshots → one compressed contact sheet → OpenAI API
```

### Ravi Dashboard Export

File:

```text
.github/workflows/ravi_dashboard_export.yml
```

Purpose:

```text
Notion Trades → normalized JSON → ravi-dashboard/data/trades.json
```

### Ravi Dashboard Pages

File:

```text
.github/workflows/ravi_dashboard_pages.yml
```

Purpose:

```text
Deploy ravi-dashboard/ to GitHub Pages
```

## Live Dashboard

Expected URL:

```text
https://rib4ever.github.io/trading-dashboard/
```

Dashboard sections:

```text
System Map
Analytics
Calendar
Trade Log
```

## Key Automation Status Fields

### Screenshot Sync Status

```text
Not Started
Ready to Sync
Pending Upload
Needs Manual Check
Error
Synced to Drive
```

### AI Review Status

```text
Not Requested
Ready for AI Review
AI Review Complete
Needs More Screenshots
AI Review Error
```

## Trade ID Rule

Trade ID is required for stable linking between:

```text
Trades
Trade Screenshots
Google Drive folders
Dashboard JSON
AI review process
```

Recommended format:

```text
TRD-YYYYMMDD-XXXX
```

Example:

```text
TRD-20260516-TEST01
TRD-20260519-8A4F
```

If Trade ID is blank, automation maintenance should fill it before screenshot sync, AI review, or dashboard export.

## Current MVP Status

Working:

```text
Screenshot sync
Google Drive OAuth upload
AI Trade Supervisor
Contact sheet AI review mode
Dashboard data export
GitHub Pages visual dashboard
Calendar analytics tab
Clean Notion views
KPI source views
```

Planned later:

```text
MT5 CSV import
Deeper KPI calculations
Private/protected dashboard hosting
Advanced trade detail drawer
Screenshot preview in dashboard
AI cost tracking per trade
```
