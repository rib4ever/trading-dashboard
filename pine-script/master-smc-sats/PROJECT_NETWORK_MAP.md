# Project Network Map — Master SMC + SATS Sniper System

This file maps Ravi's Pine Script project folders, active build chain, and confirmed working version.

## Root project path

```text
pine-script/master-smc-sats/
```

Main workspace for Ravi's TradingView Pine Script project: `Master SMC + SATS Sniper System [Ravi Custom 01]`.

## Current confirmed working version

```text
v1.7 CONFIRMED WORKING
```

Confirmed working candidate:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.7-settings-ui-cleanup-candidate.pine
```

Confirmed by Ravi after testing:

```text
It works perfectly as it supposed. Built with love and care by 2 experts.
```

## Version lineage

```text
v1.4 = protected working base
v1.5 = smart key levels + entry workflow
v1.6 = theme engine + chart color collections
v1.7 = settings UI cleanup + premium theme pack + OB/FVG visibility fix — CONFIRMED WORKING
```

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
| `00_MASTER_COMPILED/` | Final full Pine Script versions after TradingView confirmation. | Promote v1.7 here as the confirmed master. |
| `01_BASE_WORKING_VERSION/` | Protected backup of the older confirmed working Pine Script. | Do not edit directly. Current protected base remains v1.4. |
| `02_SMC_CORE/` | Swings, structure, BOS/CHoCH, OB, FVG, sweep/reclaim base logic. | Keep core market-structure logic separate from entries and visuals. |
| `03_SCRIPT_BLOCKS/` | Modular Pine blocks and assembly automation. | Develop blocks here first, then assemble candidates. Blocks are not standalone unless stated. |
| `03_MASTER_CANDIDATES/` | Candidate merged master versions before final confirmation. | v1.7 is now confirmed working. Future candidates should build from v1.7. |
| `03_KEY_LEVEL_ENGINE/` | HTF levels, smart fallback levels, equal highs/lows, support/resistance strength scoring. | Key-level logic should be designed here or in matching script blocks first. |
| `04_SATS_ENGINE/` | SATS adaptive trend-quality engine: TQI, ER, ATR adaptation, trend direction. | Keep SATS calculations independent. |
| `05_ENTRY_RULES/` | Setup, opportunity, sniper, normal, key-level, and ultra entry conditions. | Must respect Ravi's no-random-entry confluence model and workflow mode. |
| `06_RISK_TP_SL/` | Stop loss, take profit, liquidity targets, R-multiple logic, risk lines. | Smart liquidity TP integration remains future work. |
| `07_VISUALS_ALERTS/` | Labels, boxes, lines, status panel, alerts, webhook JSON. | Keep chart noise controlled with settings. |
| `08_PATCHES/` | Patch plans, isolated tests, failed attempts, fixes, and implementation notes. | Every new feature starts here before integration. |
| `09_PROJECT_MEMORY/` | ChatGPT project memory prompts and session update notes. | Update after important sessions so work can continue safely. |

## Modular script-block plan

```text
03_SCRIPT_BLOCKS/
├── README.md
├── 06_smart_key_level_engine.pine
├── 07_entry_workflow_engine.pine
├── 09a_theme_engine.pine
├── 97_audit_settings_usage.py
├── 98_assemble_v1_5_candidate.py
├── 98_assemble_v1_6_theme_candidate.py
├── 98_assemble_v1_7_settings_ui_candidate.py
└── 99_final_assembly_notes.md
```

## Important active files

| File | Description | Status |
|---|---|---|
| `01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine` | Protected older working Pine v6 master script. | Do not edit directly. |
| `03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine` | Smart key-level / liquidity block. | Active. Not standalone. |
| `03_SCRIPT_BLOCKS/07_entry_workflow_engine.pine` | Entry workflow controller. | Active. Not standalone. |
| `03_SCRIPT_BLOCKS/09a_theme_engine.pine` | Theme engine, chart color collections, premium themes, OB/FVG visibility colors. | Active. Not standalone. |
| `03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py` | Builds v1.5 from v1.4 + smart key + entry workflow. | Active build layer. |
| `03_SCRIPT_BLOCKS/98_assemble_v1_6_theme_candidate.py` | Builds v1.6 from v1.5 + theme engine. | Active build layer. |
| `03_SCRIPT_BLOCKS/98_assemble_v1_7_settings_ui_candidate.py` | Builds v1.7 from v1.6 + settings UI cleanup + OB/FVG theme visibility patch. | Current confirmed build layer. |
| `03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.7-settings-ui-cleanup-candidate.pine` | Latest confirmed working TradingView candidate. | CONFIRMED WORKING by Ravi. |
| `08_PATCHES/patch-10-theme-engine-plan.md` | Theme engine plan. | Completed. |
| `08_PATCHES/patch-11-settings-architecture-audit.md` | Settings connectivity audit plan. | Completed. |
| `08_PATCHES/patch-12-settings-ui-cleanup-plan.md` | Settings UI cleanup plan. | Completed. |
| `08_PATCHES/patch-13-creative-premium-theme-pack.md` | Creative premium theme pack plan. | Completed. |
| `09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md` | Latest project continuation prompt. | Updated to v1.7 confirmed working. |
| `09_PROJECT_MEMORY/session-update-2026-05-08-v1.7-confirmed-working.md` | Session note for v1.7 confirmation. | Created. |

## Key logic relationships

```text
Protected v1.4 base
   ↓
03_SCRIPT_BLOCKS/06_smart_key_level_engine
   ↓ provides smartAnyKeyTouched, smartBullKeyReaction, smartBearKeyReaction,
     smartBullLiquidityTouched, smartBearLiquidityTouched,
     smartBuyLiquidityTarget, smartSellLiquidityTarget
03_SCRIPT_BLOCKS/07_entry_workflow_engine
   ↓ provides entryWorkflowMode, enableSetupWarningsFinal,
     enableOpportunityEntriesFinal, enableNormalEntriesFinal,
     enableSniperEntriesFinal, enableUltraEntriesFinal,
     enableKeyLevelEntriesFinal, confirmedEntryTfOk, entryVisualWindowOk
03_SCRIPT_BLOCKS/09a_theme_engine
   ↓ provides themePreset, themeBaseBull, themeBaseBear,
     themeOBBull, themeOBBear, themeFVGBull, themeFVGBear,
     themePanelBg, themePanelText, themeLiquidity, themeKeyLevel
03_SCRIPT_BLOCKS/98_assemble_v1_7_settings_ui_candidate.py
   ↓ creates the confirmed v1.7 candidate
03_MASTER_CANDIDATES/v1.7 settings UI cleanup candidate
   ↓ confirmed by Ravi after TradingView testing
00_MASTER_COMPILED
   ↓ final confirmed copies after promotion
```

## Entry workflow modes

```text
- Market Structure Only
- Setups Only
- Opportunity Mode
- Confirmed Entries
- Full Mode
- Manual Custom
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

## Theme system status

Theme engine includes original collections and premium creative variants.

Original collection themes:

```text
Claude, Onyx, Bone, Lavender, Arctic, Night, ICT V2, Glass
```

Premium creative themes:

```text
Bone Luxe, Lavender Mist, Arctic Frost, Night Phantom, Onyx Gold,
Diamond Ice, Forest Temple, Ember Smoke, Ocean Glass, Royal Burgundy
```

Recommended themes:

```text
Default: Night Phantom
XAUUSD premium: Onyx Gold
Modern luxury: Diamond Ice
Clean light mode: Bone Luxe
```

Important theme rule:
- Candle/signal colors can be aesthetic.
- OB/FVG zones use dedicated darker/readable functional colors.
- Light themes must not make OB/FVG disappear.

## GitHub Actions

Active workflows:

```text
.github/workflows/build-pine-v15-candidate.yml
.github/workflows/build-pine-v16-theme-candidate.yml
.github/workflows/build-pine-v17-settings-ui-candidate.yml
.github/workflows/audit-pine-settings.yml
```

v1.6 and v1.7 workflows were hardened against non-fast-forward push errors using pull/rebase and concurrency.

Recommended build path now:

```text
GitHub → Actions → Build Pine v1.7 Settings UI Candidate → Run workflow → main
```

## Known Pine Script safety rules

- Do not modify global variables inside functions.
- Avoid duplicate input variable names.
- Declare variables before referencing them.
- Keep modular blocks without `//@version` and without `indicator()`.
- Guard arrays before using `array.get()` when arrays can be empty.
- Pine indentation matters.
- Do not paste GitHub webpage HTML into TradingView; always copy from `Raw`.
- Avoid combining logic changes and visual changes in the same patch unless unavoidable.

## Project memory loop

After each important update:
1. Add a session update in `09_PROJECT_MEMORY/`.
2. Update `chatgpt_project_memory_prompt.md`.
3. Update `PROJECT_NETWORK_MAP.md` when structure, workflow, or active version changes.
4. Keep the last confirmed working version clearly identified.

## Next recommended action

Promote v1.7 into `00_MASTER_COMPILED/` as the confirmed working master version, then build future patches from v1.7.
