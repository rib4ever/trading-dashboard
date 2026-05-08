# Patch 15 — Premium Visual Hierarchy & Chart Cleanup

## Purpose

Improve the chart appearance and usability after v1.8 Fibonacci POI integration.

This patch is visual-only. It must not change entries, alerts, risk logic, SMC logic, SATS logic, or backtest behavior.

## Problem observed

With all visuals enabled, the chart becomes too dense:

- too many right-side labels
- too many equally visible zones
- OB/FVG/Fib/HTF labels compete for attention
- Fibonacci POI is useful but needs a cleaner premium style
- status panel is useful but too block-like / debug-like

## Core design principle

Create visual hierarchy:

```text
Tier 1 = current actionable visual context
Tier 2 = important structural context
Tier 3 = background / historic context
Tier 4 = debug-only visuals
```

## Visual priority order

```text
1. Strongest POI
2. Active Fibonacci 61.8%-80% zone
3. Nearest active OB/FVG
4. Key HTF levels
5. Liquidity / smart key levels
6. Historic OB/FVG zones
7. Debug labels
```

## Proposed visual modes

Replace or extend existing visual mode behavior into:

```text
Clean
Analyst
Premium
Debug
```

### Clean
Show only:
- strongest POI box
- active fib band
- nearest key level
- minimal status panel
- optional SL/TP if entries are enabled

### Analyst
Show:
- active fib band
- strongest POI
- nearest OB/FVG
- key HTF levels
- compact status panel
- limited labels

### Premium
Show:
- active fib band with soft fill
- strongest POI with gold/amber accent
- nearest OB/FVG with elegant borders
- faded secondary zones
- compact table panel
- clean right-side labels

### Debug
Show everything:
- all labels
- all zones
- setup internals
- fib diagnostics
- full workflow visibility

## Fibonacci visual rules

The Fibonacci engine should display as a premium overlay:

- one soft 61.8%-80% retracement band
- one emphasized 70.5% line
- optional 61.8 / 78.6 / 80 lines as subtle dashed lines
- one compact POI badge only
- no excessive numeric labels
- POI box uses unique amber/gold accent

Recommended label text:

```text
Fib POI
Bull / Bear
OB / FVG
Score xx.x
```

## OB/FVG visual rules

OB/FVG zones should not all appear equally important.

### Active / nearest zone
- stronger border
- medium transparent fill
- label visible

### Secondary zone
- lighter border
- more transparent fill
- label optional

### Historic zone
- very faint fill
- no label unless Debug mode

## Label cleanup rules

Right-side label clutter must be reduced.

Rules:
- Only strongest POI label is always allowed.
- HTF labels limited by visual mode.
- OB/FVG labels only for active/nearest zones in Clean/Premium.
- Debug mode can show all labels.

## Status panel rules

Status panel should be a compact table, not a large paragraph block.

Suggested layout:

```text
SMC + SATS
Mode       Full
Preset     XAUUSD
Bias       Bull
Entry TF   3M/5M
TQI/ER     .60/.35
POI        YES
```

## Suggested settings

Add or reuse settings:

```text
Visual Mode: Clean / Analyst / Premium / Debug
Label Density: Minimal / Balanced / Full
Zone Priority: Active Only / Active + Nearby / All
Show Historic Zones: true / false
POI Accent Style: Gold / Theme / Contrast
Fib Detail Level: Band Only / Band + Key Lines / Full
```

## Object management rules

- Use persistent `var` object IDs for key visuals.
- Delete and redraw only selected premium visuals on `barstate.islast`.
- Cap visible labels/boxes.
- Avoid creating unnecessary new labels every bar.

## Implementation strategy

### Phase 1 — planning only
Create this patch blueprint.

### Phase 2 — visual engine block
Create:

```text
03_SCRIPT_BLOCKS/12_premium_visual_hierarchy_engine.pine
```

This block should define:

```text
premiumVisualMode
premiumLabelDensity
premiumZonePriority
premiumShowHistoricZones
premiumFibDetailLevel
premiumPoiAccentColor
visualIsClean
visualIsAnalyst
visualIsPremium
visualIsDebug
```

### Phase 3 — v1.9 candidate
Create:

```text
03_SCRIPT_BLOCKS/98_assemble_v1_9_premium_visual_candidate.py
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.9-premium-visual-candidate.pine
.github/workflows/build-pine-v19-premium-visual-candidate.yml
```

### Phase 4 — TradingView test
Test with:

```text
BTCUSD 15M
XAUUSD 3M / 5M
NAS100 5M / 15M
```

## Non-negotiable safety rule

Patch 15 must not modify:

```text
entry booleans
alert booleans
risk calculations
SL/TP calculations
SMC calculations
SATS calculations
```

## Status

Blueprint created. Implementation should happen in v1.9 candidate only, based on v1.8 candidate and v1.7 confirmed working checkpoint.
