# 03_SCRIPT_BLOCKS — Modular Pine Script Assembly Workspace

This folder is the modular working area for the Master SMC + SATS Sniper System.

TradingView Pine Script must ultimately be pasted as one complete `.pine` file, but this folder lets us design, review, and troubleshoot the system block by block before assembling a master candidate.

## Purpose

- Keep Ravi's v1.4 base logic protected.
- Split future work into small, understandable blocks.
- Make every change easier to debug in isolation.
- Avoid large direct merges that create many Pine compiler errors at once.
- Maintain a clean path from idea → patch → block → candidate → final release.

## Planned block order

| Order | Planned file | Contains |
|---|---|---|
| 00 | `00_header_and_groups.pine` | Version header, indicator declaration, group constants, color constants. |
| 01 | `01_inputs_and_presets.pine` | Master presets, SMC inputs, visual inputs, HTF/key-level inputs, risk/alert inputs. |
| 02 | `02_types_and_utilities.pine` | Custom types, helper functions, safe math, mapping/clamp functions. |
| 03 | `03_core_smc_engine.pine` | Swings, structure, OB/FVG, sweep/reclaim base calculations. |
| 04 | `04_mtf_bias_engine.pine` | Multi-timeframe SMC requests, bias scoring, strong HTF bull/bear logic. |
| 05 | `05_sats_engine.pine` | SATS adaptive trend-quality engine: ER, TQI, ATR bands, trend flips. |
| 06 | `06_smart_key_level_engine.pine` | Strongest historical support/resistance, EQH/EQL liquidity, PD/PW/PM integration. |
| 07 | `07_entry_confluence_engine.pine` | Setup, opportunity, sniper, and ultra-sniper conditions. |
| 08 | `08_risk_tp_sl_engine.pine` | SL, TP, dynamic R, liquidity target selection, risk state. |
| 09 | `09_visual_engine.pine` | Lines, boxes, labels, mini status panel, chart visual objects. |
| 10 | `10_alert_engine.pine` | Alert messages, webhook JSON, setup/opportunity/sniper alerts. |
| 99 | `99_final_assembly_notes.md` | Assembly order, known dependencies, and candidate promotion checklist. |

## Non-negotiable rules

1. The protected v1.4 base remains in `01_BASE_WORKING_VERSION/` and must not be overwritten.
2. Every new feature starts in `08_PATCHES/` or an isolated block first.
3. Each block must use unique variable prefixes when adding new logic.
4. Do not paste GitHub HTML/page content into TradingView. Always copy raw Pine text.
5. After every important change, update:
   - `09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md`
   - `PROJECT_NETWORK_MAP.md`

## Current focus

Current development focus: split the project into reusable script blocks, then convert the tested Patch 02 Smart Key Level / Liquidity Engine into `06_smart_key_level_engine.pine` before assembling a v1.5 master candidate.
