# Patch 14 — Fibonacci POI Visual Engine

## Purpose

Add a visual-only Fibonacci POI engine on top of v1.7 confirmed working.

## Rule

This patch must not change entries, alerts, risk logic, SMC logic, or SATS logic.

## Concept

The engine should:

1. Detect the active market-structure leg.
2. Draw directional Fibonacci based on buy/sell structure.
3. Highlight the retracement zone between 61.8% and 80%.
4. Check whether an OB or FVG is inside/touching that retracement area.
5. Select the strongest available POI.
6. Draw a special POI box and label.

## Direction logic

Bullish structure:
- Draw fib from swing low to swing high.
- POI zone is the pullback area between 61.8% and 80% below the high.

Bearish structure:
- Draw fib from swing high to swing low.
- POI zone is the pullback area between 61.8% and 80% above the low.

## Presets

The fib engine should support preset behavior for:

- Auto
- XAUUSD Scalping
- BTCUSD Scalping
- Index Scalping
- Scalping
- Day Trade
- Swing
- Manual Custom

## Display rules

- Fib should be visible on the current chart by default.
- Optional selected timeframe should be available.
- The engine should not draw random fibs.
- It should use confirmed pivots / market structure swings.
- It should update only when a valid swing leg exists.

## Candidate

Target candidate:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.8-fibonacci-poi-candidate.pine
```

## Status

Planned for v1.8, built from v1.7 confirmed working.
