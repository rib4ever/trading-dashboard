# NCI x SMC Market Story Visualizer [Ravi Custom]

Dedicated project folder for the **NCI x SMC Market Story Visualizer**.

This project is **not** a buy/sell signal indicator at this stage. Its first mission is to visually narrate price action like Ravi's manual drawings: connected structure, multi-timeframe alignment, range/trend story, key levels, and liquidity context.

## Core mission

```text
Visualize the story of price action from 4H → 1H → 15M → 5M,
using NCI market-structure rules as the backbone
and SMC liquidity context as support.
```

## Default timeframe stack

```text
TF Slot 1 = 4H   → Master story / dominant market structure
TF Slot 2 = 1H   → -1 explanation of 4H
TF Slot 3 = 15M  → -1 explanation of 1H
TF Slot 4 = 5M   → -1 explanation of 15M
```

The hierarchy is fractal. Each lower timeframe starts from the higher timeframe event anchor and explains that higher timeframe story.

## Current chart timeframe rule

The current chart timeframe is respected as an active working layer. Example: on a 30M chart, 30M key levels and working structure are shown while still aligning with the 4H → 1H → 15M → 5M stack.

## Core laws

1. 4H is the master story.
2. 1H explains 4H.
3. 15M explains 1H.
4. 5M explains 15M.
5. Current chart TF is an additional working layer, not a replacement.
6. LTF analysis starts from the HTF event anchor, never randomly.
7. Structure must remain connected through valid NCI breakout, pullback, range, and key-level rules.
8. Zone count is adaptive to the active 4H structure, not fixed to an arbitrary number such as 20.
9. Range is a core market chapter, not noise.
10. After a valid breakout or valid pullback, a range can begin and must stay connected to the story.
11. NCI is the structural backbone; SMC is supporting liquidity context.
12. Normal mode shows only story-relevant visuals; debug mode shows deeper checks.

## Folder map

```text
pine-script/nci-smc-market-story-visualizer/
├── README.md
├── PROJECT_NETWORK_MAP.md
├── 01_BLUEPRINT/
│   └── NCI_SMC_MARKET_STORY_VISUALIZER_BLUEPRINT.md
├── 02_CORE_RULES/
│   └── core_network_mind.md
├── 03_REQUIREMENTS/
│   └── requirements_and_scope.md
├── 04_RESOURCES/
│   └── NCI_REFERENCE_INDEX.md
├── 05_PINE/
│   └── 00_SKELETON/
│       └── nci_smc_market_story_visualizer_v0_0.pine
└── 09_PROJECT_MEMORY/
    └── chatgpt_project_memory_prompt.md
```

## Development status

Current stage: **project structure and master blueprint initialized**.

Do not prioritize execution logic, alerts, TP/SL automation, or strategy backtesting until the visual story engine is stable.
