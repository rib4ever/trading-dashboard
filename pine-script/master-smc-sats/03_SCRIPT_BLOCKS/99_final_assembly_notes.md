# Final Assembly Notes — Master SMC + SATS

This document defines how modular blocks should be assembled into one TradingView Pine Script file.

## Important Pine limitation

TradingView Pine Script does not support importing separate local files. The block files in this folder are for project organization only.

The final result must be one complete `.pine` file in:

```text
pine-script/master-smc-sats/03_MASTER_CANDIDATES/
```

After TradingView compile confirmation, the final validated version can later be copied to:

```text
pine-script/master-smc-sats/00_MASTER_COMPILED/
```

## Assembly order

Use this order when building a candidate:

```text
00_header_and_groups
01_inputs_and_presets
02_types_and_utilities
03_core_smc_engine
04_mtf_bias_engine
05_sats_engine
06_smart_key_level_engine
07_entry_confluence_engine
08_risk_tp_sl_engine
09_visual_engine
10_alert_engine
```

## Dependency rules

- `06_smart_key_level_engine` must be placed before `07_entry_confluence_engine` because entry rules need key-touch booleans.
- `08_risk_tp_sl_engine` must be placed after entry signals are defined.
- `09_visual_engine` must be placed after all levels/signals/risk variables exist.
- `10_alert_engine` must be last because it depends on entry/risk/status variables.

## Candidate checklist

Before creating a new master candidate:

- Confirm the first line is exactly `//@version=6`.
- Confirm there is only one `indicator()` declaration.
- Confirm no duplicate input variable names exist.
- Confirm no global variables are modified inside functions.
- Confirm all new variables are declared before use.
- Confirm no GitHub HTML or webpage text is copied into the `.pine` file.
- Confirm the protected v1.4 base is not overwritten.
- Update project memory and network map after the candidate is created.

## Current target

Current target candidate:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine
```

This candidate should eventually connect the tested smart key-level engine into:

- `anyExistingKeyLevelTouched`
- `keyLevelTouchOk`
- `bullKeyReaction`
- `bearKeyReaction`
- future TP liquidity target selection
