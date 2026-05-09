# Patch 16 — Fibonacci POI Lifecycle / Market Cycle Engine

## Purpose

Improve the Fibonacci POI visual engine so it respects the market cycle instead of leaving old Fibonacci / POI zones visible after they are mitigated, completed, or invalidated.

## Problem observed

A bullish Fibonacci POI zone can remain visible after price has already traded into it and made it no longer useful. This creates confusion because the chart keeps showing an old buy POI instead of waiting for a new valid cycle or switching to an available sell structure.

## Core market-cycle model

```text
Impulse → Pullback → POI touch / mitigation → Reaction or invalidation → New cycle
```

## Visual-only rule

This patch must not change:

```text
entries
alerts
risk logic
SL / TP logic
SMC calculations
SATS calculations
```

It only controls whether the Fibonacci / POI visual layer is allowed to remain visible.

## Bullish cycle

1. Identify bullish impulse leg: swing low → swing high.
2. Draw Fibonacci retracement from low to high.
3. Highlight 61.8%–80% discount zone.
4. Search for bullish OB/FVG confluence in the zone.
5. If price touches the zone/POI, mark the cycle as mitigated.
6. If price reacts upward after mitigation, mark the POI as served/completed.
7. If price closes below the protected invalidation level, mark the cycle invalid.
8. Hide the active bullish Fibonacci when completed or invalid.

## Bearish cycle

1. Identify bearish impulse leg: swing high → swing low.
2. Draw Fibonacci retracement from high to low.
3. Highlight 61.8%–80% premium zone.
4. Search for bearish OB/FVG confluence in the zone.
5. If price touches the zone/POI, mark the cycle as mitigated.
6. If price reacts downward after mitigation, mark the POI as served/completed.
7. If price closes above the protected invalidation level, mark the cycle invalid.
8. Hide the active bearish Fibonacci when completed or invalid.

## New settings

```text
Fib Lifecycle Mode
Hide Completed / Invalid Fib
Mitigation Source
Invalidation Mode
Reaction Confirm Bars
Reaction Confirm ATR
Allow Opposite Cycle Switch
Show Ghost After Completion
```

## Recommended defaults

```text
Fib Lifecycle Mode = Auto Cycle
Hide Completed / Invalid Fib = true
Mitigation Source = POI or Fib Zone
Invalidation Mode = Close Beyond 80%
Reaction Confirm Bars = 3
Reaction Confirm ATR = 0.35
Allow Opposite Cycle Switch = true
Show Ghost After Completion = false
```

## Valid / mitigated / completed / invalid rules

### Mitigated
A cycle becomes mitigated when price touches either:

```text
Fib 61.8%-80% band
or strongest POI box
```

### Completed / served
A mitigated bullish cycle is completed if price reacts upward by at least the configured ATR amount within the confirmation window.

A mitigated bearish cycle is completed if price reacts downward by at least the configured ATR amount within the confirmation window.

### Invalidated
Bullish cycle invalidated if price closes below the configured protected level.

Bearish cycle invalidated if price closes above the configured protected level.

## Desired chart behavior

```text
If valid active cycle exists → show fib / POI.
If touched but not yet completed/invalidated → keep showing.
If completed/served → hide or ghost depending on settings.
If invalidated → hide or ghost depending on settings.
If opposite valid cycle appears → show opposite cycle.
If no valid cycle exists → show no active fib / POI.
```

## Implementation file

```text
03_SCRIPT_BLOCKS/11_fibonacci_poi_engine.pine
```

## Build path

```text
Build Pine v1.9 Premium Visual Candidate
```

because v1.9 already includes the premium visual hierarchy layer.

## Status

Planned for immediate implementation.
