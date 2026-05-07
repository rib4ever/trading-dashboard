# Updated Project Memory Prompt — Master SMC + SATS [2026-05-07 / v1.4 base]

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
- New logic must be designed as patches first, then merged into a compiled master only after error-free validation.

Current GitHub project structure:
- pine-script/master-smc-sats/00_MASTER_COMPILED/ — final full compiled Pine Script versions after patches are validated.
- pine-script/master-smc-sats/01_BASE_WORKING_VERSION/ — protected backups of the last working Pine Script.
- pine-script/master-smc-sats/02_SMC_CORE/ — market structure, swing, BOS/CHoCH, OB, FVG logic.
- pine-script/master-smc-sats/03_KEY_LEVEL_ENGINE/ — HTF key levels, fallback historical key levels, liquidity levels.
- pine-script/master-smc-sats/04_SATS_ENGINE/ — SATS adaptive trend-quality engine.
- pine-script/master-smc-sats/05_ENTRY_RULES/ — setup, opportunity, sniper, ultra-sniper entry rules.
- pine-script/master-smc-sats/06_RISK_TP_SL/ — SL, TP, liquidity target, and risk-line logic.
- pine-script/master-smc-sats/07_VISUALS_ALERTS/ — labels, lines, boxes, mini status panel, and alert logic.
- pine-script/master-smc-sats/08_PATCHES/ — patch plans, failed attempts, fixes, and implementation notes.
- pine-script/master-smc-sats/09_PROJECT_MEMORY/ — project memory prompts and session update templates.
- pine-script/master-smc-sats/PROJECT_NETWORK_MAP.md — human-readable map of the folder/script network.
- pine-script/master-smc-sats/README.md — main project summary and workflow rules.

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

Important Pine Script lessons from failed attempts:
- Do not mutate global variables inside functions in Pine v6. This caused errors like: Cannot modify global variable in function.
- Avoid duplicate input names. This caused errors like: variable is already defined.
- Declare all new variables before using them. This caused errors like: Undeclared identifier.
- Avoid blindly merging the LuxAlgo v5 script into the master v6 script.
- If a function call like ta.crossover/ta.crossunder is used inside conditional expressions and TradingView warns about inconsistent calculations, assign the result to a variable first.
- Keep all new patch variables uniquely prefixed, preferably with smart or sk, to avoid collisions.

Recommended safe development method:
1. Keep v1.4 base untouched.
2. Create a small patch in 08_PATCHES first.
3. Add only one engine section at a time.
4. Confirm it compiles in TradingView.
5. Only then merge into 00_MASTER_COMPILED as the next version.
6. Update PROJECT_NETWORK_MAP.md and this memory prompt after each important change.

Next recommended technical action:
Create Patch 02 as a clean, isolated Smart Key Level Engine that only adds:
- input settings with unique names,
- local calculations without global mutation inside functions,
- strongest support/resistance selection,
- equal-high/equal-low liquidity detection,
- optional clean visuals,
- booleans that can be safely plugged into anyExistingKeyLevelTouched, bullKeyReaction, bearKeyReaction, and future TP logic.

Self-updating memory-loop instruction:
At the end of every important project update, generate a new updated version of this memory prompt.

The updated prompt must include:
- What changed in the session.
- Which files/folders were created or modified.
- Which Pine Script version is currently considered the latest working version.
- Which patch is currently being tested.
- Any TradingView errors found.
- Any decisions made by Ravi.
- The next recommended action.

Clearly title each new version:
Updated Project Memory Prompt — Master SMC + SATS [date/version]

Do not remove important historical decisions unless they are clearly obsolete. Keep the prompt compact but complete enough to restart the project safely.
```
