# Master SMC + SATS Sniper System — Ravi Custom 01

This folder is dedicated to the TradingView Pine Script project.

## Goal
Build and maintain the `Master SMC + SATS Sniper System [Ravi Custom 01]` as a clean, modular project instead of trying to edit one very large script in chat.

## Current strategy
We keep the last working Pine Script as the protected base version, then add new features in small controlled patches.

Main feature currently planned:

- Historical / fallback key-level search when price is in open space and there is no clean historical level above or below current price.
- Strongest level preference instead of nearest level.
- Liquidity inclusion in the historical key-level engine.
- Visual display options for fallback key levels.
- Noise filtering to avoid too many weak levels.

## Folder map

```text
pine-script/master-smc-sats/
├── README.md                         Main project overview
├── PROJECT_NETWORK_MAP.md            Folder/script network with descriptions
├── 00_MASTER_COMPILED/               Final complete merged Pine scripts
├── 01_BASE_WORKING_VERSION/          Last confirmed working script backups
├── 02_SMC_CORE/                      Market structure, swing, BOS/CHoCH, OB, FVG logic
├── 03_KEY_LEVEL_ENGINE/              HTF levels, fallback key levels, liquidity levels
├── 04_SATS_ENGINE/                   SATS trend-quality engine
├── 05_ENTRY_RULES/                   Setup, opportunity, sniper, ultra sniper rules
├── 06_RISK_TP_SL/                    SL, TP, liquidity targets, risk display
├── 07_VISUALS_ALERTS/                Labels, lines, boxes, status panel, alerts
├── 08_PATCHES/                       Incremental patch notes and implementation plans
└── 09_PROJECT_MEMORY/                ChatGPT project memory prompt and update template
```

## Important files

```text
PROJECT_NETWORK_MAP.md
09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md
09_PROJECT_MEMORY/session_update_template.md
```

## Working rule
Do not modify the base working version directly. Every change should be made as a patch first, tested, then merged into the compiled master script.

## Integration principle
The LuxAlgo-style logic should not be blindly pasted into the master script. The useful parts should be adapted into our existing v6 structure:

1. Strong/weak swing high/low tracking.
2. Historical MTF high/low search using bar-time arrays.
3. Equal high / equal low liquidity detection.
4. Optional visual lines and labels.
5. Confluence with existing key-touch, sweep, HTF POI, SATS, volume, volatility and killzone rules.

## Memory loop
After each important project update, update:

1. `09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md`
2. `PROJECT_NETWORK_MAP.md` when folder/file responsibilities change
3. Relevant patch notes in `08_PATCHES/`

The goal is to let a future ChatGPT conversation continue from the correct project state without losing context.
