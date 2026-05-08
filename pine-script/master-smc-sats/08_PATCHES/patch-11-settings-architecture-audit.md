# Patch 11 — Settings Architecture and Functional Connectivity Audit

## Purpose

Make sure every TradingView setting is meaningful, connected, and functional before any deeper UI cleanup.

This patch is focused on settings safety, not strategy changes.

## Non-negotiable rule

Do not remove or rename a functional input until its downstream usage is confirmed.

## Scope

Patch 11 should check:

- which settings are user-facing inputs
- which internal variables each input creates
- whether each input variable is referenced later in the script
- which settings are pure visual controls
- which settings change entry logic
- which settings change risk / TP / SL logic
- which settings are advanced/manual controls
- which settings are redundant, confusing, or only useful in Manual Custom mode

## Safe cleanup approach

1. Audit all `input.*` variables.
2. Count downstream references for each input variable.
3. Classify each setting as one of:
   - Logic-critical
   - Visual-only
   - Risk-only
   - Alert-only
   - Theme-only
   - Manual-only
   - Candidate for rename
   - Candidate for advanced group
   - Candidate for removal only after proof
4. Keep all functions intact.
5. Reorganize groups only after the audit is clear.

## Proposed future settings groups

```text
01 Quick Start
02 Theme Engine
03 Core Entry Filters
04 Setup / Opportunity Logic
05 SMC Engine
06 SATS Engine
07 Key Levels
08 Visual Display
09 Risk / TP / SL
10 Alerts
11 Advanced Manual Preset
12 Developer / Debug
```

## Important note

Pine Script settings cannot be dynamically hidden based on another setting. For example, Manual Theme colors will still appear even when Theme Preset is not Manual Custom. Therefore, the labels must clearly say they are custom/manual controls.

## Current recommendation

Do not remove settings yet. First generate a settings usage report from the current candidate.
