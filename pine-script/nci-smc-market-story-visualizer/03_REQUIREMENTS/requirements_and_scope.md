# Requirements and Scope

Project: **NCI x SMC Market Story Visualizer [Ravi Custom]**

## 1. Primary requirement

Build a TradingView Pine Script v6 indicator that visualizes market structure as a coherent story.

It must align with Ravi's manual drawings and must not behave like a random zone drawer.

## 2. Core requirements

### R1 — Multi-timeframe stack

Default:

```text
4H → 1H → 15M → 5M
```

These four timeframes must be configurable in settings.

### R2 — Current chart TF layer

The current chart timeframe must be respected.

If current chart = 30M, the indicator must show 30M key levels/working structure while still keeping the 4H/1H/15M/5M hierarchy.

### R3 — Fractal hierarchy

The same structure logic repeats on each -1 layer:

```text
4H explained by 1H
1H explained by 15M
15M explained by 5M
5M optionally explained by 1M later
```

### R4 — Event anchor start

Lower timeframe analysis starts from the higher timeframe event anchor.

No random LTF structure start.

### R5 — Connected structure

Market structure must stay connected through valid NCI logic.

It must not randomly mark up/down trends.

### R6 — Adaptive zones

Zone/level count must be adaptive to the active 4H market structure.

No arbitrary max like 20 as a design law.

### R7 — Range integration

Range is part of market structure.

A range may start after:

- valid breakout,
- valid pullback,
- failed continuation,
- compression,
- liquidity sweep.

### R8 — NCI-first structure

NCI rules control:

- market structure,
- market cycle,
- key levels,
- candle classification,
- breakout/pullback validation,
- range logic,
- SD zone quality.

### R9 — SMC-support context

SMC adds:

- liquidity sweeps,
- BOS/CHOCH,
- OB/FVG,
- buy-side/sell-side liquidity,
- premium/discount.

SMC does not override NCI.

### R10 — Visual clarity

Normal mode must show only story-relevant visuals.

Debug mode can show deeper data.

### R11 — HTF LL / HH reaction handling

The indicator must treat lower-timeframe reactions from a higher-timeframe LL/HH as pullback explanations first, not immediate reversals.

Bearish example:

```text
4H bearish continuation candidate
→ 4H creates new LL
→ 1H reacts upward from 4H LL
→ 1H explains pullback from 4H LL
→ 4H bearish story remains active until valid 4H invalidation or reversal
```

Bullish example:

```text
4H bullish continuation candidate
→ 4H creates new HH
→ 1H reacts downward from 4H HH
→ 1H explains pullback from 4H HH
→ 4H bullish story remains active until valid 4H invalidation or reversal
```

Decision rule:

```text
LTF reaction from HTF LL/HH = pullback explanation first.
LTF can warn or clarify, but it cannot override the HTF story alone.
```

## 3. Non-requirements for initial stage

Do not prioritize:

- auto buy/sell arrows,
- entries,
- TP/SL boxes,
- strategy tester logic,
- trading execution,
- heavy alerts.

## 4. Presets

Future presets:

```text
Custom 4H/1H/15M/5M default
XAUUSD visual day-trading
BTCUSD visual intraday
Scalping stack
Swing stack
Manual custom
```

## 5. Success definition

The indicator is successful when it can answer visually:

```text
What is the 4H story?
Where is price in the 4H story?
What 4H event is being explained?
Is the child timeframe reaction only a pullback explanation or a valid transition warning?
How does 1H explain 4H?
How does 15M explain 1H?
How does 5M explain 15M?
Does the current chart timeframe fit the story?
Is the market trend, pullback, range, breakout, fakeout, or transition?
```
