# Patch 001 — Historical Fallback Key Levels + Liquidity

## Problem
The current master script can block signals when price is in open space and the current visible chart has no obvious historical key level above or below price.

Example case: price reaches a fresh area where there is no nearby historical level on the left side of the chart. Ravi manually draws a light-blue key level, but the script does not detect it.

## Required behavior
When there is no valid existing key level above or below current price, the script should search historical price action on the left and identify a meaningful level.

Ravi confirmed preference:

- Use the **strongest** valid level, not simply the nearest level.
- Include liquidity levels.
- Show these levels visually on chart as an optional setting.
- Reduce noise.
- Keep alignment with the existing master script entry conditions.

## Source logic inspiration
From LuxAlgo Smart Money Concepts, useful concepts are:

1. Strong / weak high and low.
2. MTF high and low line drawing based on actual historical high/low time.
3. EQH / EQL liquidity detection.
4. Swing structure pivots.
5. Present vs historical object management.

## Do not directly copy
The open source script is Pine v5 and uses different type names and object lifecycle patterns.

Direct copy caused errors before:

- Undeclared identifiers.
- Duplicate type/function names.
- Logic placement issues.
- Pine v5/v6 mismatch problems.

## Integration plan

### Step 1 — Add new settings under `GRP_HTFLVL`
Planned settings:

```pine
showFallbackKeyLevels = input.bool(true, "Show Historical Fallback Key Levels", group = GRP_HTFLVL)
useFallbackKeyLevelsForEntries = input.bool(true, "Use Fallback Key Levels For Entries", group = GRP_HTFLVL)
fallbackSearchBars = input.int(1500, "Fallback Search Bars", minval = 100, maxval = 5000, group = GRP_HTFLVL)
fallbackPivotLen = input.int(20, "Fallback Pivot Strength", minval = 3, maxval = 100, group = GRP_HTFLVL)
fallbackMinTouches = input.int(2, "Fallback Min Touches", minval = 1, maxval = 10, group = GRP_HTFLVL)
fallbackMergeAtr = input.float(0.35, "Fallback Merge Distance xATR", minval = 0.05, maxval = 2.0, step = 0.05, group = GRP_HTFLVL)
fallbackStrongestMode = input.string("Strongest", "Fallback Level Selection", options = ["Strongest", "Nearest Strong"], group = GRP_HTFLVL)
```

### Step 2 — Create isolated fallback engine
The fallback engine should calculate:

- fallback support below price.
- fallback resistance above price.
- level strength score.
- whether current price touched/rejected that fallback level.

### Step 3 — Integrate into current key reaction logic
Current logic:

```pine
anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched
```

Planned logic:

```pine
fallbackKeyTouched = useFallbackKeyLevelsForEntries and (fallbackSupportTouched or fallbackResistanceTouched)
anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched or fallbackKeyTouched
```

Directional reactions:

```pine
bullKeyReaction = keyLevelTouchOk and (... existing bullish reactions ... or fallbackSupportTouched)
bearKeyReaction = keyLevelTouchOk and (... existing bearish reactions ... or fallbackResistanceTouched)
```

### Step 4 — Add visuals
Only draw on `barstate.islast` to avoid noise and object overload.

Visuals:

- Fallback support line below price.
- Fallback resistance line above price.
- Labels showing strength score and touch count.

### Step 5 — Add mini status information
Add:

```text
Fallback B/S: B✓ / S×
```

## Important safety rule
This patch must not weaken the sniper-entry system. Fallback levels should only help the script identify a valid key level. Sniper entries must still require the existing confluences:

- HTF OB/FVG context.
- Liquidity sweep/reclaim.
- Execution OB/FVG or structure confirmation.
- SATS TQI/ER quality.
- Volume / volatility filters.
- Killzone filter.
