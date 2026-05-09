# NCI Reference Index

This document indexes the NCI reference resources used for the NCI x SMC Market Story Visualizer.

## 1. Market structure and market cycle

### Market structure course

Resource: `Market+structure+course.pdf`

Key ideas:

- Market structure and market cycle are used to understand trend, key zones, risk, and when a trend starts/ends.
- NCI separates price action of a single candle from price action of a wave.
- Core components include main structure, internal structure, key zones, pulse wave, pullback wave, breakout, range standard, market liquidity, and multiple timeframe system.
- The course teaches reading chart structure, not candle-by-candle noise.

Implementation impact:

- This is the backbone of the visualizer.
- 4H master story must be connected through pulse/pullback/breakout/range logic.
- Lower timeframes must explain higher timeframe events.

## 2. Define market structure method

Resource: `3.1.+Define+market+structure+method`

Key ideas:

- Pullback requires at least 2 reversal candles continuously.
- First candle should not be range/pinbar/doji.
- Valid breakout requires at least 2 candles closed out of range and not pinbar/doji.
- Marubozu definition appears as body >= 60% total candle in this material.
- Valid case logic uses candle high/low relationships and closing outside the prior candle range.

Implementation impact:

- Initial structure validation must not be random pivot marking.
- Trend change requires valid key-level breakout.
- Pullback and breakout must be validated.

## 3. Pullback standard

Resource: `Pull Back.pdf`

Key ideas:

- Bullish trend pullback standard includes two Maru candles where close 2 is above close 1.
- Total length of the 2 candles should be similar from around 70%.
- Big Maru + one small candle standard: first candle must be big compared to five recent Maru candles, and lowest low of second candle must be above 50% level of first candle.
- If one condition fails, check price-action confirmation for pullback pressure.

Implementation impact:

- Pullback Engine must support two-Maru and big-Maru/small-candle validation.
- Confirmation fallback must be included later.

## 4. Breakout standard

Resource: `Break Out.pdf`

Key ideas:

- Breakout line can be applied to recent high/low, key level, POI zone, or range.
- Two Maru breakout standard: close 2 above close 1, both candles closed beyond breakout line, candle lengths similar from 70%.
- Big Maru + one small candle: first candle big compared to five previous Maru candles, second candle low above 50% of first candle, and more than 30% of first candle body beyond breakout line.
- Price-action confirmation can be used for breakout pressure.

Implementation impact:

- Breakout Engine must apply to KL, recent high/low, POI, and range.
- Range breakout must not be accepted simply because price poked outside.

## 5. Candlestick logic

Resources:

- `5.3+CandlesStick+Parten+every+traders+need+to+know.pdf`
- `6.2.+The+Secret+of+candlestick+parterns.pdf`

Key ideas:

- Marubozu = strong buying/selling pressure.
- In the larger market structure course, Maru candle is body >= 70% total length.
- Special Maru: long tail absorption candle, close very near high/low, body >= 50% total length.
- Pinbar: body < 50% total length, buyers and sellers in conflict.
- Doji: small candle, low-power indecision.
- Candles should be read at key zones, not one-by-one everywhere.

Implementation impact:

- Candle Engine must classify Maru, Special Maru, Pinbar, Doji, Normal.
- Debug mode can show candle labels; normal mode should only use them at key events.

## 6. Supply and Demand — strongest SD

Resource: `8.10.+Define+strongest+SD+zone.pdf`

Key ideas:

- Supply/Demand = imbalance between buyers and sellers.
- Obvious imbalance = strongest SD.
- Strongest SD requires at least two first Marubozu candles, immediate price reversal, and strong distance from first candle.
- SD drawing categories include no-base general, no-base special 1, no-base special 2, no-base long tail, and having base.

Implementation impact:

- SD Engine must classify strongest SD separately.
- Strongest SD should have visual priority when part of active story.

## 7. Supply and Demand vs Support and Resistance

Resource: `8.8+Compare+Supply+and+Demand+with+Support+and+resistance.pdf`

Key ideas:

- Support/resistance = price levels where buyers/sellers are strong.
- Supply/demand = price ranges where buyers/sellers are strong.
- S/R can flip after being broken.
- SD can better show entry/limit/stop/TP/SL areas.

Implementation impact:

- KL may behave like level/zone depending on context.
- Range high/low may be S/R-like borders; SD boxes explain reaction zones.

## 8. Obsolete SD

Resource: `8.11.+Define+obsolete+SD+zone.pdf`

Key ideas:

- Longer time = less value.
- Broken SD becomes obsolete.
- Weak/normal SD without confirmation can become obsolete.

Implementation impact:

- Normal mode should hide or fade obsolete SD.
- Debug mode can show obsolete SD and reason.

## 9. SD drawing rules

### Having base

Resource: `8.7+How+to+draw+supply+and+demand_+Having+base.pdf`

Rules:

- Supply: from highest of base to farthest close price of base.
- Demand: from lowest of base to farthest close price of base.
- If base has doji, cover all doji.

### No base general

Resource: `8.3+How+to+draw+supply+and+demand_+No+base+_+Genneral.pdf`

Rules:

- Supply: from open price of last up candle to highest price of waves.
- Demand: from open price of last down candle to lowest price of waves.

### No base long tail

Resource: `8.6+How+to+draw+supply+and+demand_+No+Base_+Long+tail.pdf`

Rules:

- Supply: from highest of tail to nearest close/open price.
- Demand: from lowest of tail to nearest close/open price.

### Special case 1

Resource: `8.4+How+to+draw+supply+and+demand_+No+base+_+1st+candle+too+big.pdf`

Rules:

- Demand special case when down candle is too big or up candle much smaller.
- Demand: from close/open of recent up candle depending on material variant to lowest price of waves.

### Special case 2

Resource: `8.5+How+to+draw+supply+and+demand_+No+base+_+2nd+candle+too+big.pdf`

Rules:

- Demand special case when second candle is too big.
- Refer to near demand.
- Demand: from middle of up candle to lowest price of waves.

Implementation impact:

- SD Engine should support all these drawing variants.
- Safety zone support is required later.

## 10. Price patterns / reference patterns

Resources:

- `7.1.+Why+you+need+to+understand+Price+pattern.pdf`
- `7.2.+Double+patterns.pdf`
- `7.2.+Break+and+re-test+partterns.pdf`
- `7.3.+Some+of+Reference+patterns.pdf`
- `7.4.+Some+of+Reference+patterns+_+part+2.pdf`

Key ideas:

- Patterns are reference context, not the main engine.
- Always check trend and support/resistance for patterns.
- Break and retest: recent high breaks and closes above, then retest.
- Triangles may be used more to skip trades than to force entries.

Implementation impact:

- Pattern recognition should not be prioritized before core structure.
- Later pattern context can help Story Engine, but not override NCI structure.

## 11. Order types

Resource: `5.2+Orders+types.pdf`

Key ideas:

- Market execution, pending orders, stop loss, take profit.

Implementation impact:

- Not relevant to current visual-only stage.
- Keep for future execution phase only.
