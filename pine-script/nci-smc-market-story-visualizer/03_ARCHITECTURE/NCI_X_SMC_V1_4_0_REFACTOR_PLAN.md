# NCI x SMC v1.4.0 Refactor Plan

## Reason for refactor

Ravi correctly rejected the previous direction because the script was starting to randomly populate levels.

The project must not be a pivot indicator.

The new direction is:

```text
Use the uploaded SMC Market Structure Dashboard as an engineering reference.
Use NCI rules as the trading logic authority.
Build a clean modular NCI x SMC story engine.
```

## Reference architecture inspiration

The uploaded SMC reference has useful engineering ideas:

```text
SwingData type
PivotData type
HH/HL/LH/LL structure labels
Real-time structure override
MTF dashboard
OB/FVG context
Alert states
```

We should adapt the structure, not blindly copy the script.

## Core NCI x SMC engine modules

### 01 Constants and inputs

Configurable timeframe stack:

```text
4H / 1H / 15M / 5M default
Optional 30M / chart TF working layer
Presets for XAUUSD, BTCUSD, NAS100, Scalping, Day Trade, Swing
```

### 02 Candle classification

Detect:

```text
Marubozu
Special Maru
Pinbar
Doji
Normal candle
```

NCI defaults:

```text
Maru body >= 70% total candle
Special Maru body >= 50% with long tail and close near high/low
Pinbar body < 50% and significant tail
Doji small body / indecision
```

### 03 Swing engine

Use SMC-style swing memory:

```text
prevH
currH
prevL
currL
HH / HL / LH / LL
```

But do not finalize NCI KL from swing alone.

### 04 NCI wave engine

Classify major movement into:

```text
Pulse wave
Pullback wave
Internal structure
Noise to skip
```

### 05 KL engine

Key level must come from active NCI story:

```text
Bullish KL UP = protected pullback low / valid HL after pulse
Bearish KL DOWN = protected pullback high / valid LH after pulse
Range KLs = range high / range low after valid range standard
```

No validation = candidate only.

### 06 Breakout engine

Apply NCI breakout standard:

```text
Break line can be recent high/low, KL, POI, or range.
Valid breakout uses two Maru candles, or big Maru + small candle, or confirmation candle.
At least 2 candles closed outside range for some market structure cases.
Weak wick break = sweep/fakeout, not trend change.
```

### 07 Pullback engine

Apply NCI pullback standard:

```text
Two Maru candles in continuation direction
Close 2 above/below close 1 depending on direction
Two candle total length similarity from 70%
Or Big Maru + small candle with no significant opposite pressure
If one condition fails, require confirmation candle
```

### 08 Market cycle engine

States:

```text
Bullish pulse active
Bullish pullback active
Bearish pulse active
Bearish pullback active
Range beginning
Range active
Breakout validation pending
Trend changed
Transition / wait
```

### 09 MTF hierarchy engine

Default hierarchy:

```text
4H = master story
1H = explains 4H
15M = explains 1H
5M = explains 15M
```

Important:

```text
Lower timeframe cannot create random independent story.
If higher timeframe KL breaks validly, lower timeframe recalculates from opposite direction.
```

### 10 SD / OB / FVG context engine

Use NCI SD zone rules and SMC OB/FVG as confluence:

```text
Strongest SD = obvious imbalance, at least first two Maru candles, immediate reversal, strong move away
Having base supply: highest of base to farthest close of base
Having base demand: lowest of base to farthest close of base
No-base supply/demand general and special cases
Obsolete SD: old, broken, weak/normal without confirmation
```

### 11 Story engine

Output should read like Ravi's manual chart story:

```text
4H KL DOWN touched; 4H pullback cycle active.
1H bullish structure explains the 4H pullback, not reversal yet.
15M internal bullish confirms pullback continuation.
5M waits for reaction / execution confirmation.
```

### 12 Visual engine

Show only story-relevant elements:

```text
Active parent KL
Working child KL
Relevant SD/OB/FVG zone
Range high/low if range active
Recalculation marker if parent KL validly breaks
```

Avoid random lines.

## Deliverable path

The next true implementation should be:

```text
05_PINE/01_VERSIONS/nci_smc_market_story_visualizer_v1_4_0_refactor_alpha.pine
```

## Testing standard

First test should not ask Ravi to manually calibrate.

Ravi should only check:

```text
Does it compile?
Does the panel say v1.4.0?
Does it show 4H/1H/15M/5M story?
Does it avoid random KLs?
Does the master story make sense compared with visible structure?
```
