# Patch 02 — Smart Historical Key-Level + Liquidity Engine

## Status
Planning / next implementation patch.

## Base script
Protected base:

```text
01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine
```

Do not edit this protected base directly.

## Purpose
Add a LuxAlgo-inspired but Pine v6-safe smart key-level engine to the existing Master SMC + SATS script.

The engine must solve Ravi's open-space problem:

> When price is at a new area and there is no obvious historical level immediately on the left, the script should search historical candles and find meaningful support/resistance or liquidity levels above/below price.

## Main rule
Prefer the strongest level, not the nearest level.

## Required features

1. Smart fallback support and resistance levels.
2. Historical scan above and below current price.
3. Strength scoring based on touches/reactions.
4. Liquidity inclusion:
   - equal highs,
   - equal lows,
   - previous day/week/month highs and lows,
   - current/HTF swing highs and lows.
5. Optional visual lines and labels.
6. Noise control through minimum touches, ATR tolerance, and maximum visible levels.
7. Safe connection into existing logic:
   - `anyExistingKeyLevelTouched`
   - `bullKeyReaction`
   - `bearKeyReaction`
   - future TP/liquidity targeting.

## Pine v6 safety rules

Avoid the previous error pattern.

- Do not modify global variables inside functions.
- Do not reuse existing input variable names.
- Prefix all new variables with `sk` or `smart`.
- Declare variables before using them.
- Keep the patch isolated first.
- Do not paste the full LuxAlgo script into the master script.
- Use a small number of line/label objects to avoid chart noise and object-limit issues.

## Proposed settings

```pinescript
showSmartKeyLevels      = input.bool(true, "Show Smart Key Levels", group = GRP_HTFLVL)
enableSmartKeyFallback  = input.bool(true, "Enable Smart Historical Fallback Levels", group = GRP_HTFLVL)
smartKeyLookbackBars    = input.int(1500, "Smart Key Search Lookback", minval = 100, maxval = 5000, group = GRP_HTFLVL)
smartKeyPivotLen        = input.int(5, "Smart Key Pivot Length", minval = 2, maxval = 20, group = GRP_HTFLVL)
smartKeyMinTouches      = input.int(2, "Smart Key Minimum Touches", minval = 1, maxval = 10, group = GRP_HTFLVL)
smartKeyAtrTolerance    = input.float(0.25, "Smart Key Touch Tolerance xATR", minval = 0.05, maxval = 2.0, step = 0.05, group = GRP_HTFLVL)
smartKeyMaxVisible      = input.int(2, "Smart Key Max Visible Each Side", minval = 1, maxval = 5, group = GRP_HTFLVL)
smartKeyUseLiquidity    = input.bool(true, "Include Liquidity in Smart Key Levels", group = GRP_HTFLVL)
smartKeyPreferStrongest = input.bool(true, "Prefer Strongest Level", group = GRP_HTFLVL)
```

## Strength scoring idea

A level should gain score from:

- number of touches/reactions,
- recent-but-not-too-recent relevance,
- swing high/low origin,
- equal high/equal low liquidity,
- PD/PW/PM liquidity alignment,
- proximity within a reasonable ATR band.

Nearest level should not automatically win. If `smartKeyPreferStrongest = true`, strongest score wins.

## Integration plan

### Step 1 — Isolated engine
Create calculations only:

```text
smartSupportLevel
smartResistanceLevel
smartSupportTouched
smartResistanceTouched
smartBullLiquidityTouched
smartBearLiquidityTouched
```

### Step 2 — Visuals
Add optional clean lines:

```text
Smart Support
Smart Resistance
Smart Bull Liquidity
Smart Bear Liquidity
```

### Step 3 — Entry confluence connection
Extend existing booleans:

```pinescript
anyExistingKeyLevelTouched := anyExistingKeyLevelTouched or smartSupportTouched or smartResistanceTouched

bullKeyReaction := bullKeyReaction or smartSupportTouched or smartBullLiquidityTouched
bearKeyReaction := bearKeyReaction or smartResistanceTouched or smartBearLiquidityTouched
```

Final integration must be done carefully because the current script uses direct assignments, not `:=`, for some booleans. The safest method is to create new extended variables:

```pinescript
anyKeyLevelTouchedExtended = anyExistingKeyLevelTouched or smartSupportTouched or smartResistanceTouched
bullKeyReactionExtended = bullKeyReaction or smartSupportTouched or smartBullLiquidityTouched
bearKeyReactionExtended = bearKeyReaction or smartResistanceTouched or smartBearLiquidityTouched
```

Then replace entry conditions to use the extended variables.

## First implementation target
Create an isolated Pine v6 patch file in this folder first. After TradingView confirms it compiles, merge into:

```text
00_MASTER_COMPILED/master-smc-sats-ravi-custom-01-v1.5-smart-key-levels.pine
```

## Validation checklist

- Script compiles with zero errors.
- No undeclared identifiers.
- No duplicate variables.
- No global variable mutation inside functions.
- Smart key lines are visible when enabled.
- Smart key lines disappear when disabled.
- Clean mode remains clean.
- Existing entries do not disappear unless the smart key fallback is required by settings.
- Base v1.4 remains untouched.
