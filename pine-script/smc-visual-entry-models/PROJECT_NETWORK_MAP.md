# Project Network Map - SMC Visual Entry Models

Root path:

```text
pine-script/smc-visual-entry-models/
```

Purpose: create a TradingView Pine v6 overlay indicator that visualizes Ravi's SMC entry-model study framework.

## Folder network

```text
pine-script/smc-visual-entry-models/
├── README.md
├── PROJECT_NETWORK_MAP.md
├── 00_MASTER_COMPILED/
├── 01_BASELINE/
├── 02_STRUCTURE_LIQUIDITY/
├── 03_ENTRY_MODELS/
├── 04_VISUALS_ALERTS/
├── 05_DEBUG_NOTES/
└── 09_PROJECT_MEMORY/
```

## Main candidate

```text
00_MASTER_COMPILED/smc-visual-entry-model-master-v0.1.pine
```

## Core layers

| Layer | Purpose |
|---|---|
| Structure | Swing highs/lows, BOS, MSS style shifts |
| Liquidity | Prior swing levels and Asian range levels |
| Zones | Premium/discount, FVG areas, OB-style fallback areas |
| Models | Sweep reversal, continuation pullback, range raid reversal |
| Visuals | Lines, boxes, labels, and dashboard |
| Alerts | TradingView alertconditions for study signals |

## Model mapping

Model 1: liquidity sweep, reclaim, MSS, FVG/OB zone, target opposite liquidity.

Model 2: trend bias, BOS, displacement, pullback into zone, target next liquidity.

Model 3: Asian range raid, return inside range, MSS, zone retest, target opposite range side.

Educational analysis tool only. Backtest before using any model in live market conditions.
