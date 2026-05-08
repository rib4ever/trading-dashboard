# Project Network Map — Master SMC + SATS Sniper System

This file maps the Pine Script project folders and explains what each path contains.

## Root project path

```text
pine-script/master-smc-sats/
```

Main workspace for Ravi's TradingView Pine Script project: `Master SMC + SATS Sniper System [Ravi Custom 01]`.

## Folder network

```text
pine-script/master-smc-sats/
├── README.md
├── PROJECT_NETWORK_MAP.md
├── 00_MASTER_COMPILED/
├── 01_BASE_WORKING_VERSION/
├── 02_SMC_CORE/
├── 03_SCRIPT_BLOCKS/
├── 03_MASTER_CANDIDATES/
├── 03_KEY_LEVEL_ENGINE/
├── 04_SATS_ENGINE/
├── 05_ENTRY_RULES/
├── 06_RISK_TP_SL/
├── 07_VISUALS_ALERTS/
├── 08_PATCHES/
└── 09_PROJECT_MEMORY/
```

## Path descriptions

| Path | Purpose | Current rule |
|---|---|---|
| `00_MASTER_COMPILED/` | Final full Pine Script versions after validated patches are merged. | Only promote here after TradingView compile/runtime testing is confirmed. |
| `01_BASE_WORKING_VERSION/` | Protected backup of the last confirmed working Pine Script. | Do not edit directly. Current protected base is v1.4. |
| `02_SMC_CORE/` | Swings, structure, BOS/CHoCH, OB, FVG, sweep/reclaim base logic. | Keep core market-structure logic separate from entries and visuals. |
| `03_SCRIPT_BLOCKS/` | Modular Pine block workspace and assembly automation. | Develop blocks here first, then assemble candidates. Blocks are not standalone unless stated. |
| `03_MASTER_CANDIDATES/` | Candidate merged master versions before final confirmation. | Test candidates here before promoting to final. |
| `03_KEY_LEVEL_ENGINE/` | HTF levels, smart fallback levels, equal highs/lows, support/resistance strength scoring. | Key-level logic should be designed here or in the matching script block first. |
| `04_SATS_ENGINE/` | SATS adaptive trend-quality engine: TQI, ER, ATR adaptation, trend direction. | Keep SATS calculations independent. |
| `05_ENTRY_RULES/` | Setup, opportunity, sniper, normal, key-level, and ultra entry conditions. | Must respect Ravi's no-random-entry confluence model and workflow mode. |
| `06_RISK_TP_SL/` | Stop loss, take profit, liquidity targets, R-multiple logic, risk lines. | Smart liquidity TP integration remains future work. |
| `07_VISUALS_ALERTS/` | Labels, boxes, lines, status panel, alerts, webhook JSON. | Keep chart noise controlled with settings. |
| `08_PATCHES/` | Patch plans, isolated tests, failed attempts, fixes, and implementation notes. | Every new feature starts here before master integration. |
| `09_PROJECT_MEMORY/` | ChatGPT project memory prompts and session update notes. | Update after important sessions so work can continue safely. |

## Modular script-block plan

```text
03_SCRIPT_BLOCKS/
├── README.md
├── 00_header_and_groups.pine
├── 01_inputs_and_presets.pine
├── 02_types_and_utilities.pine
├── 03_core_smc_engine.pine
├── 04_mtf_bias_engine.pine
├── 05_sats_engine.pine
├── 06_smart_key_level_engine.pine
├── 07_entry_workflow_engine.pine
├── 07_entry_confluence_engine.pine
├── 07_entry_confluence_engine_connection_notes.md
├── 08_risk_tp_sl_engine.pine
├── 09_visual_engine.pine
├── 10_alert_engine.pine
├── 98_assemble_v1_5_candidate.py
└── 99_final_assembly_notes.md
```

Purpose of this modular plan:
- Keep every engine isolated and easier to troubleshoot.
- Preserve the GitHub structure while preparing one final TradingView `.pine` file.
- Maintain the repeatable loop: patch → block → candidate → TradingView test → final release.

## Important active files

| File | Description | Status |
|---|---|---|
| `01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine` | Protected last working Pine v6 master script. | Do not edit directly. |
| `03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine` | Modular smart key-level block. Supports selectable source: Current chart, HTF1, HTF2, Current + HTF1, Current + HTF2, HTF1 + HTF2, Current + HTF1 + HTF2. | Updated. Not standalone. |
| `03_SCRIPT_BLOCKS/07_entry_workflow_engine.pine` | Modular entry workflow controller. Adds Market Structure Only, Setups Only, Opportunity Mode, Confirmed Entries, Full Mode, and Manual Custom. | Created. Not standalone. |
| `03_SCRIPT_BLOCKS/07_entry_confluence_engine_connection_notes.md` | Exact connection notes showing how smart hooks extend v1.4 key logic. | Created. |
| `03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py` | Assembly script that reads v1.4 base plus Block 06 and Block 07 and writes the generated v1.5 candidate. | Active. Uses full-block OB/FVG indentation-safe replacements and workflow-controlled entry gating. |
| `03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine` | Generated v1.5 candidate from v1.4 + Smart Key Levels + Entry Workflow. | Must be rebuilt after latest assembler/block changes. |
| `03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-candidate-smart-key-levels.pine` | Safe placeholder/warning script. | Warning uses selectable table position instead of price-level label. |
| `08_PATCHES/patch-02-smart-key-level-engine-isolated-v0.1.pine` | Standalone Pine v6 isolated indicator for smart key-level testing. | Ravi visually confirmed Smart Support / Smart Resistance. |
| `08_PATCHES/patch-03-master-v1.5-integration-map.md` | Merge map for connecting Patch 02 into v1.4 as v1.5 candidate. | Created. |
| `08_PATCHES/patch-09-entry-workflow-realignment-plan.md` | Patch plan for re-evaluating and controlling all entry models. | Created. |
| `.github/workflows/build-pine-v15-candidate.yml` | GitHub Action to assemble the v1.5 candidate. | Active. Manual run supported; push path trigger added. |
| `09_PROJECT_MEMORY/session-update-2026-05-08-v1.5-runtime-placeholder-fix.md` | Session note documenting the 5M runtime error and placeholder display fix. | Created. |

## Key logic relationships

```text
02_SMC_CORE
   ↓ provides structure, OB/FVG, sweep/reclaim
03_SCRIPT_BLOCKS/06_smart_key_level_engine
   ↓ provides smartAnyKeyTouched, smartBullKeyReaction, smartBearKeyReaction,
     smartBullLiquidityTouched, smartBearLiquidityTouched,
     smartBuyLiquidityTarget, smartSellLiquidityTarget
03_SCRIPT_BLOCKS/07_entry_workflow_engine
   ↓ provides entryWorkflowMode, enableSetupWarningsFinal,
     enableOpportunityEntriesFinal, enableNormalEntriesFinal,
     enableSniperEntriesFinal, enableUltraEntriesFinal,
     enableKeyLevelEntriesFinal, confirmedEntryTfOk, entryVisualWindowOk
04_SATS_ENGINE
   ↓ provides trend quality, TQI, ER, adaptive trend direction
05_ENTRY_RULES / entry confluence
   ↓ combines workflow mode + SMC + key levels + SATS + filters into signals
06_RISK_TP_SL
   ↓ calculates SL/TP using SMC/liquidity/R-multiple logic
07_VISUALS_ALERTS
   ↓ displays signals, levels, status, and alerts
03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py
   ↓ creates v1.5 candidate from protected v1.4 + Block 06 + Block 07
03_MASTER_CANDIDATES
   ↓ holds testable merged candidates before confirmation
00_MASTER_COMPILED
   ↓ final integrated Pine Script version after TradingView confirmation
```

## Entry workflow modes

New workflow controller:

```text
Entry Workflow Mode:
- Market Structure Only
- Setups Only
- Opportunity Mode
- Confirmed Entries
- Full Mode
- Manual Custom
```

Default direction for Ravi Custom 01:

```text
15M / 1H / 4H = bias, POI, structure, key levels only
3M / 5M = execution entries only when enabled
Historical entry labels/lines = OFF by default
```

Expected behavior:

| Mode | Setup warnings | Opportunity | Normal | Sniper | Ultra | Key-level | TP/SL |
|---|---:|---:|---:|---:|---:|---:|---:|
| Market Structure Only | no | no | no | no | no | no | no |
| Setups Only | yes | no | no | no | no | no | no |
| Opportunity Mode | yes | yes | no | no | no | no | optional |
| Confirmed Entries | yes | optional | yes | yes | no | no | yes |
| Full Mode | yes | yes | yes | yes | yes | yes | yes |
| Manual Custom | user choice | user choice | user choice | user choice | user choice | user choice | user choice |

## Current protected base

```text
01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine
```

Rules:
- Never overwrite the base working version directly.
- Build patches first.
- Convert validated patches into modular blocks.
- Assemble candidates only after each block is checked.
- Test in TradingView before promoting any candidate.

## v1.5 candidate status

Current generated test file:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine
```

Current v1.5 feature:
- Adds smart historical support/resistance and EQH/EQL liquidity as an extension of v1.4 key-level logic.
- Adds entry workflow control layer.
- Does not replace the original v1.4 SMC engine.
- Extends:
  - `anyExistingKeyLevelTouched`
  - `bullKeyReaction`
  - `bearKeyReaction`
  - `bullSniperEntry`
  - `bearSniperEntry`
  - `bullOpportunityEntry`
  - `bearOpportunityEntry`
  - `bullUltraEntry`
  - `bearUltraEntry`
  - risk line signal gating
- Adds normal and key-level entry booleans.

Validated by Ravi:
- 5M runtime array error was fixed after adding array guards in the assembler.
- Smart levels appear on 3M, 5M, and 15M.

Latest compile/debug update:
- Created `03_SCRIPT_BLOCKS/07_entry_workflow_engine.pine`.
- Updated `03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py` to inject Block 07 and gate all entry families.
- Candidate must be rebuilt via GitHub Action before TradingView testing.

## Placeholder status

File:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-candidate-smart-key-levels.pine
```

Purpose:
- Warning/reference only.
- Not the final master code.
- Updated so its warning appears in a selectable table position instead of directly on the price level.

## GitHub Action workflow

File:

```text
.github/workflows/build-pine-v15-candidate.yml
```

Recommended manual run path:

```text
GitHub → Actions → Build Pine v1.5 Candidate → Run workflow → main
```

After successful green run:
1. Open the generated v1.5 candidate file.
2. Tap/click `Raw`.
3. Copy raw Pine text.
4. Paste into TradingView.
5. Test 3M, 5M, 15M, and 1H.

## Known Pine Script safety rules

- Do not modify global variables inside functions.
- Avoid duplicate input variable names.
- Declare variables before referencing them.
- Avoid blindly merging LuxAlgo v5 into the v6 master.
- Keep new patch variables uniquely prefixed, preferably `smart`, `sk`, or workflow-specific names.
- Guard arrays before using `array.get()` when the array can be empty.
- Pine indentation matters: after adding an `if` before a `for`, the full nested loop body must be indented one additional level.
- Do not paste GitHub webpage HTML into TradingView; always copy from `Raw`.
- Isolated scripts may have `//@version` and `indicator()`, but modular blocks must not.

## Project memory loop

Stored in:

```text
09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md
09_PROJECT_MEMORY/session_update_template.md
09_PROJECT_MEMORY/session-update-2026-05-08-v1.5-runtime-placeholder-fix.md
```

After each important update:
1. Summarize what changed.
2. Update the memory prompt or add a session note.
3. Update this network map when paths, workflows, responsibilities, or active files change.
4. Keep the last working script clearly identified.

## Latest session update

- Created Patch 09 plan for full entry workflow realignment.
- Created `03_SCRIPT_BLOCKS/07_entry_workflow_engine.pine`.
- Updated `03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py` to inject entry workflow controls.
- Updated this network map.
- Next action: run GitHub Action again, copy rebuilt Raw candidate into TradingView, and test first in `Market Structure Only`, then `Setups Only`, then `Confirmed Entries` on 3M/5M only.
