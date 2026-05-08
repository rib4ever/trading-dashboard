# Updated Project Memory Prompt — Master SMC + SATS [2026-05-08 / v1.5 Candidate Runtime + Mini Status Patch]

Copy and paste this prompt into a new ChatGPT conversation whenever the project needs to continue from the correct state.

```text
You are continuing Ravi's TradingView Pine Script project: Master SMC + SATS Sniper System [Ravi Custom 01].

Repository context:
- GitHub account / owner: rib4ever
- Repository: trading-dashboard
- Main project path: pine-script/master-smc-sats/
- Default branch currently used: main

Project purpose:
Build a high-performance TradingView Pine Script v6 scalping indicator by combining:
1. Flux Charts style Market Structure / OB / FVG / Sweep logic.
2. WillyAlgoTrader SATS adaptive trend-quality logic.
3. Ravi's custom sniper-entry confluence rules.
4. A controlled LuxAlgo-style smart key-level / liquidity engine, adapted safely into the existing v6 master code.

Core trading rule:
No random entries. Setup, opportunity, sniper, and ultra-sniper signals must require proper confluence:
- Existing key-level touch or reaction.
- HTF OB/FVG context.
- Liquidity sweep / reclaim confirmation.
- Execution OB/FVG or structure confirmation.
- SATS trend-quality confirmation with TQI / ER filters.
- Volume, volatility, and killzone checks when enabled.

Current confirmed working base:
- Protected base: pine-script/master-smc-sats/01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine
- Do not overwrite the base directly.
- New logic must be designed as patches or modular blocks first, then assembled into a candidate only after validation.

Current active candidate:
- Generated candidate path: pine-script/master-smc-sats/03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine
- Built by: pine-script/master-smc-sats/03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py
- Source base: v1.4 protected base.
- Added block: pine-script/master-smc-sats/03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine

Current GitHub project structure:
- pine-script/master-smc-sats/00_MASTER_COMPILED/ — final full compiled Pine Script versions after patches are validated.
- pine-script/master-smc-sats/01_BASE_WORKING_VERSION/ — protected backups of the last working Pine Script.
- pine-script/master-smc-sats/02_SMC_CORE/ — market structure, swing, BOS/CHoCH, OB, FVG logic.
- pine-script/master-smc-sats/03_SCRIPT_BLOCKS/ — modular Pine block workspace and assembler automation.
- pine-script/master-smc-sats/03_MASTER_CANDIDATES/ — candidate merged master versions before final confirmation.
- pine-script/master-smc-sats/03_KEY_LEVEL_ENGINE/ — HTF key levels, fallback historical key levels, liquidity levels.
- pine-script/master-smc-sats/04_SATS_ENGINE/ — SATS adaptive trend-quality engine.
- pine-script/master-smc-sats/05_ENTRY_RULES/ — setup, opportunity, sniper, ultra-sniper entry rules.
- pine-script/master-smc-sats/06_RISK_TP_SL/ — SL, TP, liquidity target, and risk-line logic.
- pine-script/master-smc-sats/07_VISUALS_ALERTS/ — labels, lines, boxes, mini status panel, and alert logic.
- pine-script/master-smc-sats/08_PATCHES/ — patch plans, failed attempts, fixes, and implementation notes.
- pine-script/master-smc-sats/09_PROJECT_MEMORY/ — project memory prompts and session update templates.
- pine-script/master-smc-sats/PROJECT_NETWORK_MAP.md — human-readable map of the folder/script network.
- pine-script/master-smc-sats/README.md — main project summary and workflow rules.

Workflow now:
requirements → isolated patch → script block → master candidate → TradingView test → compiled final

Reason:
TradingView Pine Script must ultimately be one complete `.pine` file, but GitHub stores separate logical blocks to make development and troubleshooting easier.

Modular workspace:
- 03_SCRIPT_BLOCKS/README.md
- 03_SCRIPT_BLOCKS/99_final_assembly_notes.md
- 03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine
- 03_SCRIPT_BLOCKS/07_entry_confluence_engine_connection_notes.md
- 03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py

Smart key-level behavior required by Ravi:
- When price is in open space and there is no obvious historical level on the left, scan historical candles to identify meaningful support/resistance below or above price.
- Prefer the strongest level, not simply the nearest level.
- Include liquidity in the key-level list.
- Visual display must be optional in settings.
- Noise must be filtered so the chart does not become messy.
- Fallback key-level engine should support entry validation and future TP/liquidity targeting only when enabled.

Block 06 status:
- File: pine-script/master-smc-sats/03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine
- Not standalone. Do not paste by itself into TradingView.
- It has no `//@version` and no `indicator()` declaration.
- It uses unique `smart` and `sk` prefixes.

Block 06 output hooks:
- `smartAnyKeyTouched`
- `smartBullKeyReaction`
- `smartBearKeyReaction`
- `smartBullLiquidityTouched`
- `smartBearLiquidityTouched`
- `smartBuyLiquidityTarget`
- `smartSellLiquidityTarget`

Safe entry connection rules:
1. Do not replace v1.4 key logic. Extend it only.
2. Add `smartAnyKeyTouched` to `anyExistingKeyLevelTouched`.
3. Add `smartBullKeyReaction` as an OR condition inside `bullKeyReaction`.
4. Add `smartBearKeyReaction` as an OR condition inside `bearKeyReaction`.
5. Keep smart TP integration OFF until entry validation compiles and works visually.

Recent TradingView validation:
- Ravi tested the v1.5 candidate on Gold / XAUUSD.
- 3M and 15M were showing smart levels correctly.
- 5M initially had runtime error: `array.get()` index 0 out of bounds, array size is 0.
- The assembler was patched with guards around current-TF OB/FVG visual loops.
- After rebuild, Ravi confirmed the 5M runtime issue is gone.
- Ravi also confirmed smart levels and master visuals appear correctly on 15M.

Latest issue and fix:
- Ravi reported the mini status panel was still alive and sitting on the price area.
- He could disable it, but there was no option in settings to move it to top right, top left, bottom right, or bottom left.
- Important distinction: an earlier placeholder script had a movable warning table, but the real v1.5 master candidate still had the old floating price-level `statusLabel`.
- Fixed by updating `03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py` to inject the real mini status position setting into the generated candidate.

Mini status v1.5 patch details:
- Input changed from `Show Mini Status Label` to `Show Mini Status Panel`.
- New input: `Mini Status Position`.
- Options:
  - `Right of Price` — original floating label behavior.
  - `Top Right` — fixed table panel.
  - `Top Left` — fixed table panel.
  - `Bottom Right` — fixed table panel.
  - `Bottom Left` — fixed table panel.
- Corner modes use Pine `table` objects, not price-level labels, so they do not sit on live price.
- The generated candidate must be rebuilt through GitHub Actions after this assembler change.

GitHub Action workflow:
- File: .github/workflows/build-pine-v15-candidate.yml
- Purpose: builds the generated v1.5 candidate from protected v1.4 base and Block 06.
- Recommended path: GitHub → Actions → Build Pine v1.5 Candidate → Run workflow → main.
- After a green run: open the generated candidate file, click Raw, copy raw Pine text into TradingView, test 3M / 5M / 15M.

Important Pine Script lessons from failed attempts:
- Do not mutate global variables inside functions in Pine v6.
- Avoid duplicate input names.
- Declare all new variables before using them.
- Avoid blindly merging LuxAlgo v5 into the master v6 script.
- If ta.crossover/ta.crossunder causes warnings, assign to a variable first.
- Keep all new patch variables uniquely prefixed, preferably smart or sk.
- Do not paste GitHub webpage HTML into TradingView. Always open Raw and copy raw Pine text.
- Isolated patch files can have `//@version` and `indicator()`. Modular blocks must not.
- Guard arrays before using `array.get()` when the array can be empty.

Next recommended action:
1. Let GitHub Actions rebuild the candidate after the latest assembler change, or manually run `Build Pine v1.5 Candidate` on main.
2. Open: pine-script/master-smc-sats/03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine
3. Tap Raw and copy the raw Pine text into TradingView.
4. Check Settings → Visuals and confirm `Mini Status Position` exists.
5. Test `Top Right`, `Top Left`, `Bottom Right`, and `Bottom Left`.
6. Retest 3M / 5M / 15M on XAUUSD.

Self-updating memory-loop instruction:
At the end of every important project update, generate a new updated version of this memory prompt.

The updated prompt must include:
- What changed in the session.
- Which files/folders were created or modified.
- Which Pine Script version is currently considered the latest working version.
- Which patch or block is currently being tested.
- Any TradingView errors found.
- Any decisions made by Ravi.
- The next recommended action.

Also update PROJECT_NETWORK_MAP.md after each important structural or path change.

Clearly title each new version:
Updated Project Memory Prompt — Master SMC + SATS [date/version]
```
