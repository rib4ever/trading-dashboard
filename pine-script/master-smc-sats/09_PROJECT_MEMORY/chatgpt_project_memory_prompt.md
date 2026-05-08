# Updated Project Memory Prompt — Master SMC + SATS [2026-05-08 / v1.7 Confirmed Working]

Copy and paste this prompt into a new ChatGPT conversation whenever the project needs to continue from the correct state.

```text
You are continuing Ravi's TradingView Pine Script project: Master SMC + SATS Sniper System [Ravi Custom 01].

Repository context:
- GitHub owner: rib4ever
- Repository: trading-dashboard
- Main project path: pine-script/master-smc-sats/
- Default branch: main

Project purpose:
Build a high-performance TradingView Pine Script v6 scalping indicator by combining:
1. Flux Charts style Market Structure / OB / FVG / Sweep logic.
2. WillyAlgoTrader SATS adaptive trend-quality logic.
3. Ravi's custom sniper-entry confluence rules.
4. Smart key-level / liquidity validation.
5. Premium theme engine and clean mobile-friendly settings UX.

Core trading rule:
No random entries. Setup, opportunity, sniper, and ultra-sniper signals must require proper confluence:
- Existing key-level touch or reaction.
- HTF OB/FVG context.
- Liquidity sweep / reclaim confirmation.
- Execution OB/FVG or structure confirmation.
- SATS trend-quality confirmation with TQI / ER filters.
- Volume, volatility, and killzone checks when enabled.

Current confirmed working version:
- Confirmed by Ravi: v1.7 works as expected.
- Current confirmed working candidate:
  pine-script/master-smc-sats/03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.7-settings-ui-cleanup-candidate.pine

Protected base:
- pine-script/master-smc-sats/01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine
- Do not overwrite this base directly.

Version lineage:
- v1.4 = protected working base.
- v1.5 = smart key levels + entry workflow.
- v1.6 = theme engine + chart color collections.
- v1.7 = settings UI cleanup + premium theme pack + OB/FVG visibility fix. CONFIRMED WORKING.

Current active build path:
- v1.5 assembler:
  pine-script/master-smc-sats/03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py
- v1.6 assembler:
  pine-script/master-smc-sats/03_SCRIPT_BLOCKS/98_assemble_v1_6_theme_candidate.py
- v1.7 assembler:
  pine-script/master-smc-sats/03_SCRIPT_BLOCKS/98_assemble_v1_7_settings_ui_candidate.py

Important active blocks:
- pine-script/master-smc-sats/03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine
- pine-script/master-smc-sats/03_SCRIPT_BLOCKS/07_entry_workflow_engine.pine
- pine-script/master-smc-sats/03_SCRIPT_BLOCKS/09a_theme_engine.pine

Confirmed v1.7 features:
- Smart key levels / liquidity engine.
- Entry workflow modes: Market Structure Only, Setups Only, Opportunity Mode, Confirmed Entries, Full Mode, Manual Custom.
- Mini/status panel placement.
- Cleaner settings page with numbered groups.
- Theme engine with chart color collections.
- Creative premium themes.
- OB/FVG dedicated visibility colors so light themes do not make zones disappear.
- Hardened GitHub build workflows against non-fast-forward push errors.

Theme pack includes:
- Claude
- Onyx
- Bone
- Lavender
- Arctic
- Night
- ICT V2
- Glass
- Bone Luxe
- Lavender Mist
- Arctic Frost
- Night Phantom
- Onyx Gold
- Diamond Ice
- Forest Temple
- Ember Smoke
- Ocean Glass
- Royal Burgundy
- Crystal
- Diamond
- Earthy
- Nature
- Midnight Pro
- Gold Trader
- Cyber Neon
- Manual Custom

Recommended themes:
- Default: Night Phantom
- XAUUSD premium: Onyx Gold
- Modern luxury: Diamond Ice
- Clean light mode: Bone Luxe

Workflow rule:
requirements → isolated patch → script block → master candidate → TradingView test → confirmed working / compiled final

Future development rule:
- Future patches must start from v1.7 confirmed working candidate.
- Do not edit v1.4 protected base directly.
- Do not add new logic without keeping v1.7 as a safe checkpoint.
- If adding visuals/themes, keep trading logic unchanged.
- If adding logic, create a patch plan first.

Known Pine Script safety rules:
- Do not modify global variables inside functions.
- Avoid duplicate input variable names.
- Declare all new variables before using them.
- Keep modular blocks without //@version and without indicator().
- Guard arrays before array.get() when arrays can be empty.
- Always copy TradingView code from GitHub Raw, never from the GitHub webpage.
- Avoid combining logic changes and visual changes in the same patch unless unavoidable.

Current important project memory files:
- pine-script/master-smc-sats/PROJECT_NETWORK_MAP.md
- pine-script/master-smc-sats/09_PROJECT_MEMORY/chatgpt_project_memory_prompt.md
- pine-script/master-smc-sats/09_PROJECT_MEMORY/session-update-2026-05-08-v1.7-confirmed-working.md

Next recommended action:
Promote v1.7 to 00_MASTER_COMPILED as the confirmed working master version, then build future patches on top of v1.7.

Self-updating memory-loop instruction:
At the end of every important project update, update this memory prompt and PROJECT_NETWORK_MAP.md.
```
