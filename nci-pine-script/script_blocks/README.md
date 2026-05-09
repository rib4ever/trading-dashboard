# NCI Script Blocks

This folder stores isolated Pine Script blocks before they are merged into the master indicator.

## Workflow

Each feature must be developed and tested as a separate script block first.

After testing, the approved block is merged into:

```text
candidate/NCI_Master_Indicator_candidate.pine
```

Only after candidate testing is successful, it is promoted to:

```text
pine/NCI_Master_Indicator_latest.pine
```

## Planned blocks

```text
01_preset_engine.pine
02_candle_engine.pine
03_market_structure_engine.pine
04_key_level_engine.pine
05_supply_demand_engine.pine
06_strongest_obsolete_sd_engine.pine
07_breakout_pullback_engine.pine
08_entry_model_engine.pine
09_mtf_engine.pine
10_visual_dashboard_engine.pine
11_alert_engine.pine
```

## Rule

Do not directly add complex new logic to the latest master script. Build, test, and approve each block first.
