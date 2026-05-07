# Updated Project Memory Prompt — Master SMC + SATS [2026-05-08 / Modular Block Workflow]

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
- The protected base is the last working Master SMC + SATS Pine Script v1.4 shared by Ravi in chat.
- It is preserved under: pine-script/master-smc-sats/01_BASE_WORKING_VERSION/
- Do not overwrite the base directly.
- New logic must be designed as patches or modular blocks first, then merged into a compiled master only after error-free validation.

Current GitHub project structure:
- pine-script/master-smc-sats/00_MASTER_COMPILED/ — final full compiled Pine Script versions after patches are validated.
- pine-script/master-smc-sats/01_BASE_WORKING_VERSION/ — protected backups of the last working Pine Script.
- pine-script/master-smc-sats/02_SMC_CORE/ — market structure, swing, BOS/CHoCH, OB, FVG logic.
- pine-script/master-smc-sats/03_SCRIPT_BLOCKS/ — modular Pine block workspace for splitting and troubleshooting the master by logic section.
- pine-script/master-smc-sats/03_KEY_LEVEL_ENGINE/ — HTF key levels, fallback historical key levels, liquidity levels.
- pine-script/master-smc-sats/03_MASTER_CANDIDATES/ — candidate merged master versions before final confirmation.
- pine-script/master-smc-sats/04_SATS_ENGINE/ — SATS adaptive trend-quality engine.
- pine-script/master-smc-sats/05_ENTRY_RULES/ — setup, opportunity, sniper, ultra-sniper entry rules.
- pine-script/master-smc-sats/06_RISK_TP_SL/ — SL, TP, liquidity target, and risk-line logic.
- pine-script/master-smc-sats/07_VISUALS_ALERTS/ — labels, lines, boxes, mini status panel, and alert logic.
- pine-script/master-smc-sats/08_PATCHES/ — patch plans, failed attempts, fixes, and implementation notes.
- pine-script/master-smc-sats/09_PROJECT_MEMORY/ — project memory prompts and session update templates.
- pine-script/master-smc-sats/PROJECT_NETWORK_MAP.md — human-readable map of the folder/script network.
- pine-script/master-smc-sats/README.md — main project summary and workflow rules.

Latest structural decision:
Ravi approved a safer modular workflow instead of directly merging large patches into v1.4.

Workflow now:
requirements → isolated patch → script block → master candidate → TradingView test → compiled final

Reason:
TradingView Pine Script must ultimately be one complete `.pine` file, but GitHub can store separate logical blocks to make development and troubleshooting easier.

New modular workspace:
- Created: pine-script/master-smc-sats/03_SCRIPT_BLOCKS/README.md
- Created: pine-script/master-smc-sats/03_SCRIPT_BLOCKS/99_final_assembly_notes.md
- Updated: pine-script/master-smc-sats/PROJECT_NETWORK_MAP.md
- Updated: pine-script/master-smc-sats/09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md

Planned script block order:
1. 00_header_and_groups.pine — header, version, indicator declaration, groups, constants.
2. 01_inputs_and_presets.pine — all inputs and preset logic.
3. 02_types_and_utilities.pine — types and helper functions.
4. 03_core_smc_engine.pine — swings, structure, OB/FVG, sweep/reclaim.
5. 04_mtf_bias_engine.pine — MTF request.security data and HTF bias scoring.
6. 05_sats_engine.pine — SATS ER/TQI/ATR adaptive trend engine.
7. 06_smart_key_level_engine.pine — strongest historical support/resistance, EQH/EQL, PD/PW/PM levels.
8. 07_entry_confluence_engine.pine — setup, opportunity, sniper, ultra-sniper logic.
9. 08_risk_tp_sl_engine.pine — SL, TP, dynamic R, liquidity targets.
10. 09_visual_engine.pine — lines, boxes, labels, status panel.
11. 10_alert_engine.pine — alerts and webhook JSON.
12. 99_final_assembly_notes.md — dependency order and candidate checklist.

Latest feature direction:
Ravi wants a smart historical / fallback key-level engine that behaves like the useful part of LuxAlgo SMC, but must be safely adapted into the master script instead of blindly pasted.

Required smart key-level behavior:
- When price is in open space and there is no obvious historical level on the left, the script should scan historical candles to identify meaningful support/resistance below or above price.
- Ravi prefers the strongest level, not simply the nearest level.
- Liquidity must be included in the key-level list.
- Visual display must be optional in settings.
- Noise must be filtered so the chart does not become messy.
- The fallback key-level engine should support entry validation and future TP/liquidity targeting only when enabled.

LuxAlgo-inspired parts worth adapting:
1. Strong / weak swing high and low tracking.
2. Internal structure high / low tracking.
3. Equal high / equal low liquidity detection.
4. Previous D/W/M highs and lows as liquidity/key levels.
5. Historical level selection using touch count / strength scoring.
6. Clean optional lines and labels.

Patch 02 status:
- File: pine-script/master-smc-sats/08_PATCHES/patch-02-smart-key-level-engine-isolated-v0.1.pine
- Ravi tested it visually in TradingView.
- Observed: Smart Support / EQL and Smart Resistance / EQH lines displayed correctly.
- It should now be converted into a clean modular block: 03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine

Candidate status:
- A v1.5 candidate placeholder / warning version was tested by Ravi and displayed the orange warning label.
- It is not final.
- Do not promote it to compiled/final until the modular block merge compiles and respects all v1.4 entry conditions.

Important Pine Script lessons from failed attempts:
- Do not mutate global variables inside functions in Pine v6. This caused errors like: Cannot modify global variable in function.
- Avoid duplicate input names. This caused errors like: variable is already defined.
- Declare all new variables before using them. This caused errors like: Undeclared identifier.
- Avoid blindly merging the LuxAlgo v5 script into the master v6 script.
- If a function call like ta.crossover/ta.crossunder is used inside conditional expressions and TradingView warns about inconsistent calculations, assign the result to a variable first.
- Keep all new patch variables uniquely prefixed, preferably with smart or sk, to avoid collisions.
- Do not paste GitHub webpage HTML into TradingView. Always open the raw file and copy raw Pine text.

Recommended next technical action:
Create the first real modular block files under 03_SCRIPT_BLOCKS, starting with:
- 06_smart_key_level_engine.pine
- 07_entry_confluence_engine.pine connection notes

Then assemble a new v1.5 candidate only after the smart key-level block is logically checked.

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

Do not remove important historical decisions unless they are clearly obsolete. Keep the prompt compact but complete enough to restart the project safely.
```
