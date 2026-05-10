# SMC Market Structure Reference Notes

## Source

User provided file: `SMC.txt`

The script header identifies it as:

```text
Market Structure Dashboard | Flux Charts
Pine Script v6
License: Mozilla Public License 2.0
Author note: © fluxchart
```

## Project usage rule

This file is stored as a **reference resource only**.

Do not randomly copy/paste the full external script into Ravi's NCI project. Use it to understand good engineering patterns and then rebuild the NCI logic in our own structure.

Because the referenced script is under MPL 2.0, if we directly reuse any meaningful code section, the reused file/section must retain proper MPL notice and attribution. For now, use only the concepts and architecture as reference.

## Useful concepts from the reference script

The reference indicator is useful because it separates market structure into clear modules:

```text
1. Timeframe inputs and weights
2. Swing high/low detection
3. Market structure state: HH / HL / LH / LL
4. Real-time structure override when price breaks previous swing
5. Order block and FVG context
6. MTF dashboard organization
7. Visual overlay controls
8. Alerts for swing breaks, sweeps, structure changes, OB/FVG changes
```

## Concepts to adapt into Ravi's NCI logic

### 1. SwingData style

Use a structured object/state model similar to:

```text
prevH
currH
prevL
currL
```

But adapt it to NCI:

```text
last pulse high
last pulse low
last pullback high
last pullback low
active KL UP
active KL DOWN
active range high
active range low
```

### 2. Structure labels

The reference tracks HH / HL / LH / LL.

For NCI, HH/HL/LH/LL are not enough. We need to translate them into:

```text
Pulse wave
Pullback wave
Internal structure
Valid breakout
Invalid breakout / false break
Range start
Range active
Trend changed
```

### 3. Real-time override

The reference script updates structure if price breaks previous swing high/low.

For NCI this must become:

```text
When price breaks active KL with valid breakout rules, trend/cycle recalculates from the opposite direction.
```

Important: simple wick or one weak close is not enough. NCI breakout standards must be applied.

### 4. Dashboard pattern

The Flux dashboard structure is useful. For our project, the dashboard should show story, not just raw metrics:

```text
4H Master Story
1H Role
15M Role
5M Role
Active KL UP / DOWN
Market Cycle
Breakout / Pullback / Range status
SD/OB/FVG context
Warning / no-trade reason
```

## NCI rules that override the reference script

The Flux script is an SMC market structure dashboard. It is not NCI by itself.

Our rules have priority:

```text
1. 4H -> 1H -> 15M -> 5M hierarchy.
2. Lower timeframe must explain parent, not create an independent story.
3. Key levels must come from NCI pulse/pullback/range logic, not random pivots.
4. Valid breakout and pullback require NCI candle standards.
5. Supply/Demand zones are ranges, not exact lines.
6. Obsolete zones/levels must be filtered.
7. No validation = no KL label.
8. Story must make sense visually and logically.
```

## NCI standards to connect

Use these NCI references together with the SMC script:

```text
Market structure course
Market Structure and Market Cycle
Break Out
Pull Back
Define strongest SD zone
Define obsolete SD zone
How to draw supply and demand zones
```

Key NCI points already documented:

```text
Marubozu body >= 70% total candle
Special Maru: body >= 50%, long tail, close near high/low
Breakout can be recent high/low, KL, POI, or range
Valid breakout examples: two Maru candles, big Maru + small candle, confirmation candle
Pullback examples: two Maru candles, big Maru + small candle, confirmation if condition fails
Support/resistance is price level; supply/demand is price range
Obsolete SD: old zones lose value, broken zones are obsolete, weak/normal SD without confirmation is obsolete
```

## Implementation direction from this point

Stop patching random full scripts.

Next build should be a clean engine refactor:

```text
v1.4.0 NCI x SMC Engine Refactor
```

Modules:

```text
01 constants and inputs
02 candle classification
03 swing engine
04 NCI wave engine
05 KL engine
06 market cycle engine
07 MTF hierarchy engine
08 SD/OB/FVG context engine
09 story engine
10 visuals and dashboard
```

## What not to do

```text
Do not label latest pivot as KL.
Do not show all detected levels randomly.
Do not let 5M override 4H.
Do not create a bullish/bearish story without valid NCI breakout/pullback/range confirmation.
Do not hide uncertainty. If uncertain, say candidate / wait / no confirmed KL.
```
