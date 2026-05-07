# Project Network Map — Master SMC + SATS Sniper System

This file maps the Pine Script project folders and explains what each path should contain.

## Root project path

```text
pine-script/master-smc-sats/
```

Main workspace for Ravi's TradingView Pine Script project: `Master SMC + SATS Sniper System [Ravi Custom 01]`.

## Folder and script network

```text
pine-script/master-smc-sats/
├── README.md
├── PROJECT_NETWORK_MAP.md
├── 00_MASTER_COMPILED/
├── 01_BASE_WORKING_VERSION/
├── 02_SMC_CORE/
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
| `README.md` | Main project overview, high-level strategy, and workflow rules. | Keep short and clear. Update only when the project strategy changes. |
| `PROJECT_NETWORK_MAP.md` | This file. Describes the folder/script network and where each logic block belongs. | Update whenever a new folder, important file, or workflow is added. |
| `00_MASTER_COMPILED/` | Final full Pine Script versions after validated patches are merged. | Only place scripts here after they are expected to compile as one complete indicator. |
| `01_BASE_WORKING_VERSION/` | Protected backups of the last confirmed working Pine Script. | Do not directly modify. This is the fallback restore point. |
| `02_SMC_CORE/` | Market structure logic: swings, HH/HL/LH/LL, BOS/CHoCH, OB, FVG, sweep/reclaim base logic. | Keep core structure logic separate from entries and visuals where possible. |
| `03_MASTER_CANDIDATES/` | Candidate merged master versions before they become the new protected base. | Use for v1.5+ candidates. Do not treat these as confirmed until TradingView compiles them. |
| `03_KEY_LEVEL_ENGINE/` | HTF levels, smart fallback historical key levels, equal high/low liquidity, support/resistance strength scoring. | New LuxAlgo-inspired key-level logic belongs here first before master merge. |
| `04_SATS_ENGINE/` | SATS adaptive trend-quality engine: TQI, ER, ATR adaptation, SuperTrend-style direction. | Keep SATS calculations independent so they can be tested separately. |
| `05_ENTRY_RULES/` | Setup, opportunity, sniper, and ultra-sniper entry conditions. | Entry rules must respect Ravi's no-random-entry confluence model. |
| `06_RISK_TP_SL/` | Stop loss, take profit, liquidity target selection, R-multiple logic, risk lines. | Later smart liquidity levels can be plugged here for TP selection. |
| `07_VISUALS_ALERTS/` | Labels, boxes, lines, status panel, alerts, webhook JSON formatting. | Keep chart noise controlled with settings. |
| `08_PATCHES/` | Patch plans, failed attempts, fixes, and implementation notes. | Every new feature should start here before becoming part of the compiled master. |
| `09_PROJECT_MEMORY/` | ChatGPT memory prompt and session update template. | Update after each important project session so future chats can continue safely. |

## Important active files

| File | Description | Status |
|---|---|---|
| `01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine` | Protected last working Pine v6 master script. | Do not edit directly. |
| `03_MASTER_CANDIDATES/README.md` | Candidate workflow rulebook. | Created. |
| `08_PATCHES/patch-02-smart-key-level-engine-plan.md` | Written implementation plan for strongest historical key-level and liquidity engine. | Planning document created. |
| `08_PATCHES/patch-02-smart-key-level-engine-isolated-v0.1.pine` | Standalone Pine v6 isolated indicator for smart support/resistance and liquidity testing. | TradingView visual test confirmed by Ravi. |
| `08_PATCHES/patch-03-master-v1.5-integration-map.md` | Exact merge map for connecting Patch 02 into the master v1.4 logic as v1.5 candidate. | Created. |

## Key logic relationships

```text
02_SMC_CORE
   ↓ provides structure, OB/FVG, sweep/reclaim
03_KEY_LEVEL_ENGINE
   ↓ provides key-level touch/reaction and liquidity levels
04_SATS_ENGINE
   ↓ provides trend quality, TQI, ER, adaptive trend direction
05_ENTRY_RULES
   ↓ combines SMC + key levels + SATS + filters into signals
06_RISK_TP_SL
   ↓ calculates SL/TP using SMC/liquidity/R-multiple logic
07_VISUALS_ALERTS
   ↓ displays signals, levels, status, and alerts
03_MASTER_CANDIDATES
   ↓ holds testable merged candidates before confirmation
00_MASTER_COMPILED
   ↓ final integrated Pine Script version
```

## Current protected base

The latest protected working base remains:

```text
01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine
```

Rules:
- Never overwrite the base working version directly.
- Build patches first.
- Test in TradingView.
- Merge only when the patch compiles and does not break existing conditions.

## Current active feature plan

Smart historical fallback key-level and liquidity engine:

- Use LuxAlgo-style concepts, but do not paste the LuxAlgo v5 script directly.
- Adapt the useful logic safely into Pine v6.
- Prefer strongest key level, not nearest.
- Include liquidity levels such as equal highs/lows and previous highs/lows.
- Add optional visual settings.
- Reduce noise with strength/touch filters.
- Connect to existing `anyExistingKeyLevelTouched`, `bullKeyReaction`, and `bearKeyReaction` after isolated testing.

## Patch 02 isolated testing result

Test file:

```text
08_PATCHES/patch-02-smart-key-level-engine-isolated-v0.1.pine
```

Observed result from Ravi:
- Smart Support / EQL line displayed.
- Smart Resistance / EQH line displayed.
- The isolated patch appears visually correct on TradingView.

## Patch 03 merge objective

Use this file as the merge map:

```text
08_PATCHES/patch-03-master-v1.5-integration-map.md
```

Target candidate file:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine
```

Important:
- Do not paste GitHub webpage HTML into TradingView.
- Open the `.pine` file, tap/click `Raw`, then copy the raw Pine text.
- The first line must be `//@version=6`.

## Suggested next enhancement ideas

After Patch 03 / v1.5 compiles and visually behaves correctly:

1. Add previous day/week/month highs and lows into the smart score.
2. Add HTF smart levels from 15M and 1H using `request.security`.
3. Use smart resistance/support as optional TP liquidity targets.
4. Add a debug table showing why a level was selected: touches, distance, recency, liquidity.
5. Add strict toggle: `Require Smart Key Level When No HTF Level Exists`.

## Known Pine Script safety rules

- Do not modify global variables inside functions.
- Avoid duplicate input variable names.
- Use unique prefixes for new patch variables, for example `smart` or `sk`.
- Declare variables before referencing them.
- Avoid huge direct merges.
- Keep each patch small and testable.

## Project memory loop

The memory loop is stored in:

```text
09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md
09_PROJECT_MEMORY/session_update_template.md
```

After each major update:
1. Summarize what changed.
2. Update the memory prompt.
3. Update this network map if paths or responsibilities changed.
4. Keep the last working script clearly identified.
