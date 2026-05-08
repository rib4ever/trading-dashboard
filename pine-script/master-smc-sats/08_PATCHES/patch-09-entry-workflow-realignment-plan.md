# Patch 09 — Entry Workflow Realignment Plan

## Objective

Revisit and realign every entry layer so the indicator can be used in three clean modes:

1. **Market Structure Only**
   - No entry labels.
   - No TP/SL lines.
   - Only SMC, OB/FVG, smart key levels, HTF levels, and status panel.

2. **Analysis + Warning Mode**
   - Setup warnings allowed.
   - Opportunity warnings optional.
   - No confirmed entry labels unless enabled.

3. **Full Entry Mode**
   - Confirmed entries enabled only when the selected entry model is active.
   - Entries should respect execution timeframe, HTF bias, key level touch, liquidity sweep/reclaim, execution OB/FVG or structure confirmation, and SATS quality.

## Problem Found

The current candidate can still show old historical confirmed entry labels on higher timeframes. This is not aligned with the intended Ravi Custom 01 scalping workflow.

For the Ravi Custom 01 model:

- 15M, 1H, and 4H should mainly guide bias and POI context.
- Confirmed entries should normally print only on execution charts such as 3M or 5M.
- Higher timeframe entries should be disabled by default.
- Old historical entry lines should not remain dragged into the current chart unless the user enables historical mode.

## New Entry Workflow Settings To Add

### Master Entry Mode

Input name:

```text
Entry Workflow Mode
```

Options:

```text
Market Structure Only
Setups Only
Opportunity Mode
Confirmed Entries
Full Mode
Manual Custom
```

Expected behavior:

| Mode | SMC visuals | Setup warnings | Opportunity entries | Normal entries | Sniper entries | Ultra entries | TP/SL lines |
|---|---:|---:|---:|---:|---:|---:|---:|
| Market Structure Only | yes | no | no | no | no | no | no |
| Setups Only | yes | yes | no | no | no | no | no |
| Opportunity Mode | yes | yes | yes | no | no | no | optional |
| Confirmed Entries | yes | optional | optional | yes | yes | no | yes |
| Full Mode | yes | yes | yes | yes | yes | yes | yes |
| Manual Custom | user controlled | user controlled | user controlled | user controlled | user controlled | user controlled | user controlled |

### Individual Toggles

Only active when Entry Workflow Mode = Manual Custom, or used internally by the preset mode.

```text
Enable Setup Warnings
Enable Opportunity Entries
Enable Normal Entries
Enable Sniper Entries
Enable Ultra Entries
Enable Key-Level Entries
Show Entry Labels
Show Historical Entry Labels/Lines
Show TP/SL For Entries
Show TP/SL For Opportunity Entries
```

### Timeframe Control

```text
Restrict Confirmed Entries To Execution TF
Max Confirmed Entry TF Minutes
Allow Higher Timeframe Entries
```

Recommended default:

```text
Restrict Confirmed Entries To Execution TF = true
Max Confirmed Entry TF Minutes = 5
Allow Higher Timeframe Entries = false
```

Meaning:

- 1M / 3M / 5M can produce confirmed entries.
- 15M / 1H / 4H can show structure, POIs, key levels, and setup context, but no confirmed entries by default.

## Entry Model Definitions

### Setup Warning

Purpose: early warning only.

Minimum conditions:

```text
HTF POI context
Key level touch/reaction
Liquidity sweep/reclaim if enabled
Basic TQI/ER quality if enabled
```

Not required:

```text
Full SATS confirmation
Full HTF directional alignment
TP/SL drawing
```

### Opportunity Entry

Purpose: earlier/lower-confidence entry.

Minimum conditions:

```text
Setup warning is active
Execution timeframe allowed, if required
Structure confirmation
SATS directional confirmation
Basic TQI/ER quality
Optional killzone
Optional volume filter
```

Should not override confirmed entry logic.

### Normal Entry

Purpose: normal confirmed entry, less strict than sniper.

Minimum conditions:

```text
Execution timeframe allowed
HTF bias agrees with direction
HTF POI context
Key level touch/reaction
Liquidity sweep/reclaim
Execution OB/FVG OR structure confirmation
SATS confirmation
TQI/ER minimums
Volume and volatility filters
Killzone filter if enabled
```

### Sniper Entry

Purpose: strict high-confluence entry.

Minimum conditions:

```text
Execution timeframe allowed
HTF bias agrees with direction
Opposite HTF bias must not be active
HTF POI context
Key level touch/reaction
Liquidity sweep/reclaim
Execution OB/FVG required
Execution structure confirmation required
SATS confirmation
TQI/ER minimums
Volume and volatility filters
Killzone filter
Confirmed candle only
```

Important rule:

```text
HTF POI override can help setup warnings, but should not create confirmed sniper entries by itself.
```

### Ultra Entry

Purpose: strongest entry type.

Minimum conditions:

```text
Valid sniper entry
Strong HTF bias
Ultra TQI threshold
Liquidity sweep from major level
Execution OB and FVG confluence
Optional smart key liquidity touch
```

### Key-Level Entry

Purpose: optional entry model based mainly on smart support/resistance or HTF levels.

Minimum conditions:

```text
Execution timeframe allowed
Smart/HTF key level touch
Directional rejection/reclaim
HTF bias agreement
SATS confirmation
Liquidity sweep/reclaim if enabled
```

This should be optional and separate from sniper.

## Historical Display Rules

Default:

```text
Show Historical Entry Labels/Lines = false
```

When disabled:

- Old entry labels should not clutter the chart.
- TP/SL lines should not remain dragged from old signals.
- Only current/recent valid entry context should be displayed.

Optional setting:

```text
Historical Entry Lookback Bars = 500
```

## Implementation Plan

1. Create a new modular entry workflow block:

```text
03_SCRIPT_BLOCKS/07_entry_workflow_engine.pine
```

2. Keep current v1.4 entry logic untouched in the base file.

3. Update the assembler:

```text
03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py
```

4. The assembler should inject the workflow settings and replace only the entry decision section.

5. Rebuild v1.5 candidate.

6. Test TradingView on:

```text
XAUUSD / GOLD 3M
XAUUSD / GOLD 5M
XAUUSD / GOLD 15M
XAUUSD / GOLD 1H
```

Expected result:

- 1H should not print confirmed entries by default.
- 3M/5M can print entries only when all enabled conditions match.
- Market Structure Only mode should show zero entries.

## Status

Planned. Not yet merged into the v1.5 candidate.
