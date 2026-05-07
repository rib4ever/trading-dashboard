# 07 Entry Confluence Engine — Connection Notes

This note explains how the smart key-level block should connect to Ravi's existing v1.4 entry logic.

## Source block

```text
03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine
```

## New output booleans from the smart key-level block

```pine
smartAnyKeyTouched
smartBullKeyReaction
smartBearKeyReaction
smartBullLiquidityTouched
smartBearLiquidityTouched
smartBuyLiquidityTarget
smartSellLiquidityTarget
```

## Safe connection points in v1.4

In the master v1.4 logic, the existing key-touch section currently defines:

```pine
anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched
keyLevelTouchOk = not requireKeyLevelTouch or anyExistingKeyLevelTouched
```

When integrating the smart key-level block, this should become conceptually:

```pine
anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched or smartAnyKeyTouched
keyLevelTouchOk = not requireKeyLevelTouch or anyExistingKeyLevelTouched
```

## Bull reaction connection

Existing v1.4 bull reaction logic should keep all original terms and only add the smart bull reaction as an extra OR condition:

```pine
bullKeyReaction = keyLevelTouchOk and (
     original_v1_4_bull_conditions or
     smartBullKeyReaction)
```

## Bear reaction connection

Existing v1.4 bear reaction logic should keep all original terms and only add the smart bear reaction as an extra OR condition:

```pine
bearKeyReaction = keyLevelTouchOk and (
     original_v1_4_bear_conditions or
     smartBearKeyReaction)
```

## Important rule

Do not replace existing v1.4 logic. Only extend it.

The master should keep:
- current swing key touch
- PD/PW/PM touch
- current OB/FVG touch
- HTF 1/2 swing touch
- HTF 1/2 OB/FVG touch

Then add the smart key-level fallback as an extra validation source.

## TP connection — later only

The block also exposes:

```pine
smartBuyLiquidityTarget
smartSellLiquidityTarget
```

These are reserved for later TP logic and should not be forced into v1.5 until the entry validation is proven stable.

Recommended setting:

```pine
useSmartKeyForTP = false
```

## Current integration status

- Patch 02 isolated visual test was confirmed by Ravi.
- Block 06 was created from Patch 02 and cleaned for master integration.
- Next step is to assemble a v1.5 candidate carefully, using this note as the connection guide.
