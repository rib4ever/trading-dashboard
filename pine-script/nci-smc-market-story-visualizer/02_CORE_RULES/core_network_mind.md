# Core Network Mind

This document is the highest-priority memory and design law for the **NCI x SMC Market Story Visualizer [Ravi Custom]**.

## 1. Project identity

This is not a classic indicator.

It is a **market story visualizer** designed to reproduce Ravi's manual chart-drawing logic.

The first goal is visual analysis, not execution.

## 2. Final core operating law

```text
The NCI x SMC Market Story Visualizer must narrate price action across a selected 4-timeframe hierarchy, defaulting to 4H → 1H → 15M → 5M.

4H is the master story.
1H explains 4H.
15M explains 1H.
5M explains 15M.

Each lower timeframe must begin from the higher timeframe event anchor and explain that higher timeframe story, not create random independent structure.

The current chart timeframe must also be respected as a working layer without breaking the selected hierarchy.

Structure must be connected through valid NCI breakout, pullback, key level, range, and market-cycle logic.

Range is a core market chapter, not noise.
After valid breakout or valid pullback, a range may begin and must remain part of the connected story.

Zone count must be adaptive to the active 4H structure, not fixed arbitrarily.

Only story-relevant visuals should be shown, so the indicator remains clean and reads like Ravi’s manual drawings.

NCI provides the structural backbone.
SMC provides supporting liquidity context.
The final output is one clear aligned story of price action.
```

## 3. Priority hierarchy

```text
Priority 1: 4H master story
Priority 2: 4H event anchor
Priority 3: 1H explanation of 4H
Priority 4: 15M explanation of 1H
Priority 5: 5M explanation of 15M
Priority 6: Current chart timeframe working layer
Priority 7: NCI validation
Priority 8: SMC support context
Priority 9: Story panel / final narrative
```

## 4. Timeframe hierarchy

Default stack:

```text
TF1 = 4H
TF2 = 1H
TF3 = 15M
TF4 = 5M
```

Role meaning:

```text
4H  = master chapter / dominant structure / main market cycle
1H  = -1 child structure explaining 4H
15M = -1 child structure explaining 1H
5M  = -1 child structure explaining 15M
```

Future extension:

```text
1M explains 5M
```

## 5. Current chart timeframe layer

If the current chart timeframe is not one of the selected stack timeframes, it must be added as a working layer.

Example:

```text
Selected stack: 4H / 1H / 15M / 5M
Current chart: 30M

Show:
4H master story
1H active structure
30M current chart KL / working structure
15M internal structure
5M reaction summary
```

The chart timeframe must not replace the selected stack.

## 6. Event anchor law

Lower timeframe analysis must not start randomly.

It starts from the higher timeframe event anchor.

Valid anchors:

```text
HTF pullback start
HTF key level touch
HTF range high reaction
HTF range low reaction
HTF sweep above/below
HTF breakout candle
HTF failed breakout candle
HTF retest of broken level
```

## 7. Connected market-structure law

The indicator must not randomly mark uptrend/downtrend.

Structure must remain connected from the last valid 4H structural origin to current price.

### Bullish connected path

```text
LL / HL area
→ valid bullish breakout
→ HH
→ pullback to HL / KL UP
→ continuation or range
→ next HH or failed continuation
```

If range forms:

```text
Bullish leg
→ HH
→ range begins
→ range low becomes decision area
→ range high becomes continuation/break area
```

### Bearish connected path

```text
HH / LH area
→ valid bearish breakout
→ LL
→ pullback to LH / KL DOWN
→ continuation or range
→ next LL or failed continuation
```

If range forms:

```text
Bearish leg
→ LL
→ range begins
→ range high becomes decision area
→ range low becomes continuation/break area
```

## 8. Adaptive zone law

No arbitrary fixed count such as 20 zones.

Correct rule:

```text
Show all story-relevant zones and structure from the last valid 4H market-structure sequence.
```

Hide irrelevant zones in normal mode.

Keep rejected/obsolete zones available only in debug mode.

## 9. Range law

Range is a core market chapter.

Range may begin after:

```text
valid breakout
valid pullback
failed continuation
liquidity sweep
compression after impulse
```

Range output should include:

```text
range high
range low
midline
premium area
discount area
buy-side liquidity
sell-side liquidity
sweep above
sweep below
failed breakout
valid breakout
range rotation
range-to-trend transition
```

Middle of range = noise / low conviction.

Range edges = decision zones.

## 10. NCI-first law

NCI controls the structure:

- market structure,
- market cycle,
- key levels,
- pulse wave,
- pullback wave,
- breakout standard,
- range standard,
- candle quality,
- supply/demand quality.

SMC only supports the story with liquidity and POI context.

## 11. SMC-support law

SMC context includes:

```text
liquidity sweep
buy-side liquidity
sell-side liquidity
BOS / CHOCH
OB
FVG
premium / discount
```

But:

```text
SMC without NCI structure context = visual context only, not story confirmation.
```

## 12. Visual anti-mess law

The chart remains clean by story filtering.

Normal mode shows:

```text
active 4H KL / range / structure path
active 1H explanation
active 15M movement
active 5M reaction
current chart TF KL if enabled
story panel
```

Normal mode hides:

```text
old broken zones
obsolete zones
unrelated pivots
random micro swings
disconnected trend labels
invalid noise
```

Debug mode can reveal them.

## 13. No execution priority

Do not prioritize:

```text
buy/sell arrows
entry signals
TP/SL automation
strategy tester logic
trade execution
heavy alerts
```

until the visual story engine is stable.
