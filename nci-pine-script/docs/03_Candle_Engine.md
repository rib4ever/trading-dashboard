# NCI Candle Engine

## Purpose

The Candle Engine identifies the basic NCI candle types before we build market structure, pullback, breakout, and supply/demand modules.

## Candle types in v0.1

### Bull Maru / Bear Maru

A Marubozu-style candle shows strong buying or selling pressure.

Default rule:

- Body ratio must be at least 70% of the full candle range.
- Candle must be significant compared with ATR.

### Bull Special Maru / Bear Special Maru

A Special Maru represents a shock move or strong rejection.

Default bullish rule:

- Body ratio must be at least 50%.
- Close must be near the high.
- Lower wick should be stronger than upper wick.

Default bearish rule:

- Body ratio must be at least 50%.
- Close must be near the low.
- Upper wick should be stronger than lower wick.

### Pinbar

A Pinbar shows rejection.

Default rule:

- Body ratio must be below the pinbar threshold.
- One wick must dominate the body.
- Doji candles are excluded from pinbar classification.

### Doji

A Doji shows indecision.

Default rule:

- Body ratio must be very small.
- Candle range should not be excessively large.

### Normal candle

A candle that is not Maru, Special Maru, Pinbar, or Doji.

## Label meanings

| Label | Meaning |
|---|---|
| M+ | Bull Maru |
| M- | Bear Maru |
| SM+ | Bull Special Maru |
| SM- | Bear Special Maru |
| PB+ | Bull Pinbar |
| PB- | Bear Pinbar |
| DJ | Doji |
| N | Normal candle |
