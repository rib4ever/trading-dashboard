# NCI Market Structure and Key Level Standards

## Source of truth

This document is based only on Ravi's NCI documents and Ravi's confirmed project rules.

No generic SMC / ICT / random support-resistance logic should be used as NCI Market Structure logic unless Ravi approves it.

## Purpose of Market Structure

NCI Market Structure is used to answer:

- What is the current trend?
- Where are the key zones for entry?
- Where should stop loss and take profit be planned?
- When did the trend start?
- When is the trend finished?
- What market cycle phase is price currently in?

## Core NCI components

The Market Structure module must be built from these parts:

```text
Pulse Wave
Pullback Wave
Internal Structure
Main Structure
Key Level
Recent High / Recent Low
Valid Breakout
Trend Started / Trend Finished
Range / No Trade Condition
Market Cycle Context
HTF Bias
Internal Trend
Confluence / Unconfluence
POI Strategy Context
```

## Ravi confirmed decisions for v0.2

### 1. Key Level replacement rule

```text
Latest valid pullback replaces the previous key level.
```

The script must not keep an old key level active after a newer valid pullback creates a newer valid NCI key level.

### 2. Internal structure visibility rule

```text
Internal structure should be visible on the chart.
```

But noise must be controlled. The visual system must not overload the chart with too many internal labels.

### 3. Top-down analysis rule

NCI Market Structure should be handled through top-down analysis and market cycle context.

The dashboard and chart should clearly separate:

```text
HTF Bias / HTF Trend
Current TF Trend
Internal Trend
Key Level
Market Cycle Context
Confluence / Unconfluence
POI Strategy Context
```

### 4. Optional instrument-specific display filtering

Instrument-specific filtering is allowed only as an optional display / sensitivity setting.

Important:

```text
Core NCI logic must remain NCI-based.
Instrument-specific settings may reduce visual noise, but must not replace NCI rules.
```

Allowed optional display presets:

```text
Universal
BTCUSD display filter
XAUUSD display filter
Scalping display filter
Day trading display filter
Swing trading display filter
Manual custom
```

## Pulse Wave

A pulse wave is the strong movement in the main trend direction.

Implementation note:

- The first automated version should not guess too much.
- It should detect possible pulse waves using NCI candle-pressure logic and then show them as `PW?` or `Pulse Candidate`.
- Final pulse-wave confirmation must be checked with the later pullback and key-level logic.

## Pullback Wave

A pullback wave is the corrective movement against the main trend.

NCI notes:

- Pulse wave should be longer.
- Pullback should be shorter.
- In a stable trend, price has many pullbacks.
- Pullback is connected to the key level.
- A valid pullback shows reversal power during the main trend.

## Pullback standards

The pullback rules must support:

### 1. Two-Marubozu pullback

Bullish pressure version:

```text
1. Two Maru candles.
2. Close 2 is above Close 1.
3. Total length of both candles is almost similar, from 70%.
4. Judge total candle length, not only body.
```

Bearish pressure version:

```text
1. Two Maru candles.
2. Close 2 is below Close 1.
3. Total length of both candles is almost similar, from 70%.
4. Judge total candle length, not only body.
```

### 2. Big Maru + small candle pullback

Bullish pressure version:

```text
1. First candle must be BIG.
2. First candle is compared with 5 recent Maru candles.
3. Second candle must be small.
4. Second candle total length <= 30% of previous candle total length.
5. Lowest low of second candle is above 50% level of first candle.
6. Meaning: no significant selling pressure.
```

Bearish pressure version:

```text
1. First candle must be BIG.
2. First candle is compared with 5 recent Maru candles.
3. Second candle must be small.
4. Second candle total length <= 30% of previous candle total length.
5. Highest high of second candle is below 50% level of first candle.
6. Meaning: no significant buying pressure.
```

### 3. Price action confirmation if one condition fails

```text
If one pullback condition fails:
- Wait for confirmation.
- At least one normal or Maru candle must close beyond the original pullback pattern.
- Confirmation should happen within the next 4 candles.
```

## Key Level

Key Level is not a random horizontal line.

A valid NCI Key Level must be connected to:

```text
Market Structure
Pulse Wave
Pullback Wave
Trend start / trend finish logic
Valid breakout logic
```

## Valid breakout of Key Level

A trend changes only when there is a valid breakout of the relevant NCI key level.

First coding version should mark:

```text
KL candidate
Breakout candidate
Valid breakout pending
Valid breakout confirmed
```

Do not label the market as fully changed only from a normal wick break or weak close.

## Breakout standard

Breakout Line can be applied to:

```text
Recent High / Recent Low
Key Level
POI Zone
Range
```

### 1. Two-Marubozu breakout

```text
1. Two Maru candles.
2. Close 2 is above Close 1 for bullish breakout.
3. Both candles close above Breakout Line.
4. Total length of two candles is almost similar, from 70%.
```

Bearish version is mirrored below the Breakout Line.

### 2. Big Maru + small candle breakout

Bullish breakout:

```text
1. First candle must be big compared with five previous Maru candles.
2. Second candle must be small.
3. Second candle total length <= 30% of previous candle total length.
4. Lowest low of second candle is above 50% level of first candle.
5. More than 30% of the body of the first candle must be above Breakout Line.
```

Bearish breakout is mirrored below the Breakout Line.

## Range rule

If price is moving horizontally without valid breakout, the system should identify a range and avoid giving trend-continuation confidence.

Range can be formed by:

```text
Maru candle range
Pinbar / Doji range
Invalid Pullback
Fake Breakout
No liquidity range
```

## v0.2 coding rule

The first Market Structure script block should be conservative.

It should not immediately create full trading signals.

It should show:

```text
Pulse candidate
Pullback candidate
Internal structure candidate
Latest key level candidate
Valid breakout candidate
Range warning
HTF bias placeholder / dashboard field
Internal trend field
Confluence / unconfluence placeholder
Debug reason
```

## Noise-control rule for internal structure

Internal structure must be visible, but noise must be controlled using settings such as:

```text
Show internal structure: ON/OFF
Minimum internal move size
Maximum labels per lookback
Show only latest internal swing
Show only internal trend line
Display filter: Universal / BTCUSD / XAUUSD / Manual
```

## Candidate merge rule

Before merging v0.2 into candidate:

```text
1. Confirm NCI logic source.
2. Test on BTCUSD 5M.
3. Test on XAUUSD 3M.
4. Test on EURUSD 15M.
5. Confirm key level replacement works.
6. Confirm internal structure is visible but not noisy.
7. Confirm dashboard separates HTF bias and internal trend.
```
