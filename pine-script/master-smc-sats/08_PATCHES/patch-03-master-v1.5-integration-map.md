# Patch 03 — Master v1.5 Integration Map

## Objective
Merge the working isolated Smart Historical Key Level + Liquidity Engine into the existing master v1.4 Pine Script without breaking the current SMC + SATS sniper logic.

## Current confirmed state
- Base working script: `pine-script/master-smc-sats/01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine`
- Working isolated patch: `pine-script/master-smc-sats/08_PATCHES/patch-02-smart-key-level-engine-isolated-v0.1.pine`
- Patch 02 visually works in TradingView: Smart Support / EQL and Smart Resistance / EQH levels are drawn correctly.

## Merge rule
Do not paste the full isolated patch directly into the master script. Only merge the reusable engine components:
1. Smart key level inputs
2. Smart key level arrays/storage
3. Pivot clustering logic
4. Strongest support/resistance scoring logic
5. Touch/liquidity booleans
6. Clean visual lines/labels
7. Entry-condition connections

## Exact master connection points

### 1. Inputs
Add the Patch 02 inputs inside the existing `GRP_HTFLVL = "🧭 HTF Key Levels"` group.

Keep existing v1.4 inputs unchanged:
- `showHtfKeyLevels`
- `htfKeyTf1`
- `htfKeyTf2`
- `showHtfSwingHL`
- `showHtfPoiLevels`
- `requireKeyLevelTouch`
- `keyLevelTouchAtrBuffer`

Add new smart key inputs with unique names only:
- `showSmartKeyLevels`
- `enableSmartKeyFallback`
- `smartKeyPreferStrongest`
- `smartKeyPivotLen`
- `smartKeyMaxStored`
- `smartKeyMinTouches`
- `smartKeyAtrLen`
- `smartKeyAtrTolerance`
- `smartKeyTouchBuffer`
- `smartKeyExtendBars`
- `showSmartLabels`
- `smartSupportColor`
- `smartResistanceColor`
- `smartLiquidityColor`

### 2. Storage
Add the arrays after the `nearLevel()` helper or before the Zone + Key Level Confluence block.

Required arrays:
- `skSupportLevels`
- `skSupportHits`
- `skSupportBars`
- `skResistanceLevels`
- `skResistanceHits`
- `skResistanceBars`

### 3. Smart calculations
The smart engine must remain in main/global scope. Do not place global array mutation inside functions. This avoids Pine errors such as:
- Cannot modify global variable in function
- Undeclared identifier
- Return type mismatch

### 4. Entry connection
Update the existing v1.4 key-level booleans as follows:

`anyExistingKeyLevelTouched` must include:
- existing current swing / PD / PW / PM / HTF OB/FVG touches
- `smartSupportTouched`
- `smartResistanceTouched`

`bullKeyReaction` must include:
- existing bull reactions
- `smartSupportTouched`
- `smartBullLiquidityTouched`

`bearKeyReaction` must include:
- existing bear reactions
- `smartResistanceTouched`
- `smartBearLiquidityTouched`

### 5. TP/SL connection
For now, do not replace the existing TP logic. Later optional improvement:
- Buy TP can use `smartResistanceLevel` if above price.
- Sell TP can use `smartSupportLevel` if below price.

This should be Patch 04, not Patch 03.

### 6. Visuals
Add smart support/resistance line objects near the existing HTF key level visual section.

Use last-bar-only drawing:
- delete old smart lines/labels on `barstate.islast`
- draw only current strongest support and resistance
- keep the chart clean

### 7. Mini status label
Add to the existing mini status label:

`Smart Key: B✓/S✓`

Where:
- B✓ = `smartBullLiquidityTouched` or `smartSupportTouched`
- S✓ = `smartBearLiquidityTouched` or `smartResistanceTouched`

## Validation checklist
After creating master v1.5:
1. Paste into TradingView Pine Editor.
2. Confirm no compile errors.
3. Test on XAUUSD 3M, 5M, 15M.
4. Confirm Smart Support / Smart Resistance lines show.
5. Confirm master labels still work.
6. Confirm no random entries appear without key-level reaction.
7. Confirm status label shows smart key condition.

## Naming recommendation
Create the merged candidate as:

`pine-script/master-smc-sats/03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine`

Do not overwrite the base v1.4 working script until v1.5 is tested in TradingView.
