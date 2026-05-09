# NCI Pulse Wave and Pullback Wave Logic

## Source of truth

This document extracts the NCI wave rules from Ravi's NCI Google Drive material and Ravi's confirmations.

This document must be used before coding the new v0.2 MTF Market Structure + Key Level Map.

## Critical objective rule

```text
Wrong pulse / pullback wave
→ wrong market structure
→ wrong key level
→ wrong HTF bias
→ wrong confluence / unconfluence
→ wrong POI strategy
→ wrong signal
```

Therefore, the script must not create NCI key levels from random swing highs/lows.

A key level must come from valid NCI wave logic.

## NCI Market Structure purpose

The Market Structure and Market Cycle course defines the purpose of Market Structure as:

```text
Understand trend.
Find zones for entry, stop loss, take profit.
Control risk.
Know when a trend starts and finishes.
Combine market structure, market cycle, and multiple timeframe system.
```

## NCI candle pressure base

NCI reads price through important/significant candles and waves, not every small candle.

Main candle types:

```text
Marubozu / Maru
Special Maru
Pinbar
Doji
Normal candle
```

Important note:

```text
NCI does not read candle by candle everywhere.
NCI reads candle/wave behaviour at key zones to understand the market picture.
```

## Marubozu / Maru rule

NCI standard:

```text
Marubozu candle = body >= 70% of total candle length.
It shows consistent buying or selling pressure.
Always judge body divided by total length.
```

Implementation:

```text
bodyRatio = abs(close - open) / (high - low)
Maru = bodyRatio >= 0.70
```

## Special Maru rule

NCI standard:

Bullish Special Maru:

```text
Long tail below.
Close price very near high.
Body >= 50% of total candle length.
Shows shock move and buyers absorbing selling pressure.
```

Bearish Special Maru:

```text
Long tail above.
Close price very near low.
Body >= 50% of total candle length.
Shows shock move and sellers absorbing buying pressure.
```

Implementation note:

Special Maru is candle-pressure information, but for v0.2 key level calculation we should be careful. The main pullback/breakout standards are built around Maru, normal confirmation candles, and valid breakout/pullback rules.

## Pinbar rule

NCI standard:

```text
Pinbar body < 50% of total length.
It is a significant big candle.
Color is skipped / not important.
Shows buyers and sellers are joined, power not clearly decided.
```

## Doji rule

NCI standard:

```text
Doji is a small candle.
Buyers and sellers are joined.
Low power indecision.
```

## Pulse Wave concept

NCI shows Pulse Wave as the stronger directional wave in the main trend.

From the Market Structure course:

```text
Pulse wave is longer.
Pullback is shorter.
A stable trend has many pullbacks.
Pullback is the key level.
```

Practical interpretation for coding:

```text
Pulse Wave should be the dominant directional movement.
It should not be defined by one random candle alone.
It should be connected to valid pullback and key level formation.
```

## Pullback Wave concept

NCI shows Pullback Wave as the corrective wave against the main movement.

Important rule:

```text
A valid pullback expresses reversal power during the main trend.
Pullback is the key level.
```

This is why key levels must be created from valid pullback waves, not random swings.

## Pullback Standard 1 — Two Marubozu candles

Bullish pressure version:

```text
1. Two Maru candles.
2. Close 2 is above close 1.
3. Total length of the two candles is almost similar, from 70%.
4. Judge total candle length, not only body.
```

Bearish pressure version:

```text
1. Two Maru candles.
2. Close 2 is below close 1.
3. Total length of the two candles is almost similar, from 70%.
4. Judge total candle length, not only body.
```

Implementation:

```text
rangeSimilarity = min(range1, range2) / max(range1, range2)
validSimilarity = rangeSimilarity >= 0.70
```

## Pullback Standard 2 — Big Maru + one small candle

Bullish pressure version:

```text
1. First candle must be BIG.
2. First candle is compared with 5 recent Maru candles.
3. Second candle must be SMALL.
4. Second candle total length <= 30% of previous candle total length.
5. Lowest low of second candle is above 50% level of first candle.
6. Meaning: no significant selling pressure.
```

Bearish pressure version:

```text
1. First candle must be BIG.
2. First candle is compared with 5 recent Maru candles.
3. Second candle must be SMALL.
4. Second candle total length <= 30% of previous candle total length.
5. Highest high of second candle is below 50% level of first candle.
6. Meaning: no significant buying pressure.
```

## Pullback confirmation when one condition fails

NCI says when one pullback condition fails, check price action confirmation.

Bullish confirmation:

```text
At least one normal candle or Maru candle closes above the original highest high of the pullback pattern.
Confirmation must happen within next 4 candles.
Then the whole pullback is valid.
```

Bearish confirmation:

```text
At least one normal candle or Maru candle closes below the original lowest low of the pullback pattern.
Confirmation must happen within next 4 candles.
Then the whole pullback is valid.
```

## Breakout Line / BOI application

NCI Breakout Standard can be applied to:

```text
Recent high / recent low
Key level
POI zone
Range
```

The breakout line represents the zone/line that needs a valid breakout.

## Breakout Standard 1 — Two Marubozu candles

Bullish version:

```text
1. Two Maru candles.
2. Close 2 is above close 1.
3. Both candles close above the Breakout Line.
4. Total length of two candles is almost similar, from 70%.
5. For this standard, no need to check how much percent of the first candle body closed above the breakout line.
```

Bearish version:

```text
1. Two Maru candles.
2. Close 2 is below close 1.
3. Both candles close below the Breakout Line.
4. Total length of two candles is almost similar, from 70%.
```

## Breakout Standard 2 — Big Maru + one small candle

Bullish version:

```text
1. First candle must be BIG.
2. First candle is compared with 5 recent Maru candles.
3. Second candle must be SMALL.
4. Second candle total length <= 30% of previous candle total length.
5. Lowest low of second candle is above 50% level of first candle.
6. More than 30% of the body of first candle is above the Breakout Line.
```

Bearish version:

```text
1. First candle must be BIG.
2. First candle is compared with 5 recent Maru candles.
3. Second candle must be SMALL.
4. Second candle total length <= 30% of previous candle total length.
5. Highest high of second candle is below 50% level of first candle.
6. More than 30% of the body of first candle is below the Breakout Line.
```

## Range rule

NCI Range definition:

```text
Market is running up and down in a horizontal area without a valid breakout.
```

Condition described in the course:

```text
Close price is still running within a single candle after 2–5 candles.
```

Types of range to focus on:

```text
Range by Marubozu candle.
Range by Pinbar or Doji candles.
Range by invalid pullback.
Range by fake breakout.
No liquidity range.
```

Trading rule:

```text
Skip trading range and wait for valid breakout.
```

## Key Level rule from wave logic

Key level must be created after valid wave logic.

Core rule:

```text
Pullback is the key level.
```

Meaning for coding:

```text
1. Detect the dominant pulse wave.
2. Detect the valid pullback wave using NCI pullback standards.
3. The key level is derived from that valid pullback wave.
4. Latest valid pullback replaces the previous key level only within the same timeframe layer.
```

## Multi-timeframe rule

Each timeframe owns its own market structure and key levels.

```text
H4 key level remains H4 key level.
H1 key level remains H1 key level.
M15 key level remains M15 key level.
M5 key level / internal structure remains execution context.
```

Lower timeframe key levels must not replace higher timeframe key levels.

## Coding implication for v0.2 rebuild

Do not code the final MTF key level map until the following detectors exist:

```text
1. Maru / Special Maru / Pinbar / Doji base candle logic.
2. Two-Maru pullback detector.
3. Big-Maru + small-candle pullback detector.
4. Pullback price-action confirmation detector.
5. Two-Maru breakout detector.
6. Big-Maru + small-candle breakout detector.
7. Range detector.
8. Per-timeframe key level state.
9. Broken key level state using valid breakout, not wick break.
```

## Next implementation step

Build one clean script block first:

```text
script_blocks/02_wave_logic_detector_v0_2_block.pine
```

This block must only test:

```text
Two-Maru pullback
Big-Maru + small-candle pullback
Pullback confirmation
Two-Maru breakout
Big-Maru + small-candle breakout
Range warning
```

Only after this block is validated should we build:

```text
script_blocks/03_mtf_key_level_map_v0_2_block.pine
```
