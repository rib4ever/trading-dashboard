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
HTF LL / HH reaction after impulse
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

## 13. HTF LL / HH reaction continuation law

This law is mandatory for correct higher-timeframe storytelling.

When the higher timeframe is in a bearish sequence and creates a new LL, any lower-timeframe bullish reaction from that LL is treated first as a **pullback explanation**, not as a bullish trend reversal.

```text
4H bearish continuation candidate
→ 4H creates new LL
→ 1H reacts upward from the 4H LL
→ 1H mission = explain the pullback from the 4H LL
→ watch whether 1H forms LH / KL DOWN rejection
→ 4H bearish continuation remains active until valid 4H invalidation or reversal
```

The opposite applies in bullish structure:

```text
4H bullish continuation candidate
→ 4H creates new HH
→ 1H reacts downward from the 4H HH
→ 1H mission = explain the pullback from the 4H HH
→ watch whether 1H forms HL / KL UP rejection
→ 4H bullish continuation remains active until valid 4H invalidation or reversal
```

Core decision rule:

```text
LTF reaction from HTF LL/HH = pullback explanation first.
HTF continuation story remains active until HTF structure is invalidated by valid NCI structure rules.
LTF movement can warn, clarify, or explain, but it cannot override the HTF story alone.
```

This prevents false story flips such as:

```text
4H bearish creates LL → 1H moves up → incorrectly call bullish reversal
```

Correct interpretation:

```text
4H bearish creates LL → 1H moves up → likely 4H bearish pullback explanation until proven otherwise
```

Official HTF story change requires valid higher-timeframe structure change, not only lower-timeframe reaction.

## 14. Always-HTF-KL law

The higher timeframe must always have an active key-level story.

```text
There is always a latest relevant 4H supply/demand/key-level zone somewhere in the active structure history.
If the newest candidate is invalid, broken, mitigated, obsolete, or not BOS-created, the engine must search backward until it finds the latest valid NCI key level/zone.
```

The indicator must not casually return:

```text
No confirmed 4H parent KL yet
```

unless there is genuinely not enough chart history loaded.

The 4H KL is the master anchor. Lower timeframes cannot create the main story; they can only explain, refine, react to, or warn against the 4H story.

## 15. BOS-created KL law

A key level is not valid just because a candle, base, swing high, or swing low exists.

A new KL must be created by a wave that breaks structure.

```text
Demand KL = the pullback low / demand zone that led to a valid break above the previous swing high.
Supply KL = the pullback high / supply zone that led to a valid break below the previous swing low.
```

If the latest candidate has not broken the last HH/LL, it is not promoted to active KL.

```text
No BOS = not active KL.
No BOS = search previous BOS-created KL.
```

This must be available as an optional setting, default ON:

```text
Require BOS to Create KL = ON
BOS Requires Close Beyond Structure = optional
```

## 16. KL reaction-candle validation law

A KL candidate must prove that institutions reacted from the zone.

After the KL candle/base is identified, the following 3–4 candles should be checked for reaction pressure.

For demand / KL UP:

```text
After KL candle/base:
- buying pressure should appear
- more bullish pressure than bearish pressure
- strong body / displacement candles preferred
- closes should move away from demand
- price should not immediately deeply re-enter the zone
- the reaction wave should ideally create BOS above previous high
```

For supply / KL DOWN:

```text
After KL candle/base:
- selling pressure should appear
- more bearish pressure than bullish pressure
- strong body / displacement candles preferred
- closes should move away from supply
- price should not immediately deeply re-enter the zone
- the reaction wave should ideally create BOS below previous low
```

Recommended settings:

```text
Require Reaction Candles After KL = ON
Reaction Candle Count = 3
Minimum Reaction Score = 3
```

Reaction scoring should be simple and explainable:

```text
+1 correct candle direction
+1 strong body / displacement
+1 close moves away from zone
+1 closes progress in expected direction
+1 no deep immediate re-entry
```

Scores:

```text
0–2 = weak / ignore
3 = candidate reaction
4–5 = confirmed reaction
```

## 17. Inside-zone decision law

If price is already inside the candidate zone when the engine identifies or displays it, it must not be treated as a clean fresh execution KL.

```text
Price inside supply zone = decision area; wait for rejection or breakout.
Price inside demand zone = decision area; wait for reaction or breakdown.
```

A clean KL story requires:

```text
1. KL candle/base exists
2. correct NCI zone is built
3. reaction candles move away from the zone
4. BOS/structure break validates the wave
5. price later retests/reacts from the zone
```

If price is inside the zone:

```text
Do not say execution aligned.
Say decision zone / reaction pending / wait for trigger.
```

## 18. Label and mobile visual law

Child timeframe labels must remain readable and low-noise.

Use compact labels by default:

```text
1H SUP / 1H DEM
15M SUP / 15M DEM
5M SUP / 5M DEM
```

Full explanations should go into tooltip text where TradingView supports hover, and into the story panel for mobile users.

4H labels remain priority and may show fuller text.

## 19. No execution priority

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
