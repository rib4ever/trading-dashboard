# ChatGPT Project Memory Prompt

Use this prompt as the persistent working memory for all future development on **NCI x SMC Market Story Visualizer [Ravi Custom]**.

## Identity

You are helping Ravi build a TradingView Pine Script v6 indicator called:

```text
NCI x SMC Market Story Visualizer [Ravi Custom]
```

This project is separate from the existing `master-smc-sats` project and must live in:

```text
pine-script/nci-smc-market-story-visualizer/
```

## Highest-priority project law

This is not a buy/sell indicator yet.

It is a **visual market story narrator**.

It must reproduce Ravi's manual drawing logic.

## Default timeframe hierarchy

The project is not only HTF/LTF.

It must use a configurable 4-timeframe hierarchy, defaulting to:

```text
4H → 1H → 15M → 5M
```

Role mapping:

```text
4H  = master story
1H  = -1 explanation of 4H
15M = -1 explanation of 1H
5M  = -1 explanation of 15M
```

The same hierarchy repeats fractally on every lower level.

If a 1M layer is added later:

```text
1M explains 5M
```

## Current chart timeframe rule

The current chart timeframe must be respected as an active working layer.

Example:

```text
Selected stack = 4H / 1H / 15M / 5M
Current chart = 30M

Show:
4H master story
1H active story
30M key levels / working chart structure
15M internal movement
5M reaction summary
```

The current chart TF does not replace the selected hierarchy.

## Event anchor rule

Never start lower timeframe analysis randomly.

Start from the higher timeframe event anchor.

Valid event anchors:

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

## Connected structure rule

The indicator must not randomly mark uptrend/downtrend or random zones.

It must connect structure according to NCI logic:

```text
valid breakout
valid pullback
range formation
continuation
failure
transition
```

4H is the master anchor.

The script must adapt to the last relevant 4H market-structure sequence.

## Adaptive zones rule

Do not use a fixed arbitrary number like 20 zones as the design principle.

Correct principle:

```text
Show all story-relevant zones and levels from the active 4H structure.
```

Hide unrelated old zones and obsolete zones in normal mode.

Show them only in debug mode.

## Range rule

Range is a core market story.

Range may begin after:

```text
valid breakout
valid pullback
failed continuation
liquidity sweep
compression after impulse
```

Range story must include:

```text
range high
range low
range midline
premium/discount
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

Range edges = decision areas.

## Bullish connected story

```text
LL / HL area
→ valid bullish breakout
→ HH
→ pullback to HL / KL UP
→ continuation or range
→ next HH or failure
```

If range begins:

```text
Bullish leg
→ HH
→ range
→ range low becomes decision area
→ range high becomes continuation/break area
```

## Bearish connected story

```text
HH / LH area
→ valid bearish breakout
→ LL
→ pullback to LH / KL DOWN
→ continuation or range
→ next LL or failure
```

If range begins:

```text
Bearish leg
→ LL
→ range
→ range high becomes decision area
→ range low becomes continuation/break area
```

## HTF LL / HH reaction continuation rule

This rule is mandatory.

If the 4H is bearish and creates a new LL, then a 1H bullish reaction from that new LL is treated first as a **pullback explanation**, not as a bullish reversal.

```text
4H bearish continuation candidate
→ 4H creates new LL
→ 1H reacts upward from the 4H LL
→ 1H mission = explain the pullback from that 4H LL
→ watch whether 1H forms LH / KL DOWN rejection
→ 4H bearish continuation remains active until valid 4H invalidation or reversal
```

Opposite bullish case:

```text
4H bullish continuation candidate
→ 4H creates new HH
→ 1H reacts downward from the 4H HH
→ 1H mission = explain the pullback from that 4H HH
→ watch whether 1H forms HL / KL UP rejection
→ 4H bullish continuation remains active until valid 4H invalidation or reversal
```

Decision rule:

```text
LTF reaction from HTF LL/HH = pullback explanation first.
HTF continuation story remains active until HTF structure is invalidated by valid NCI structure rules.
LTF movement can warn, clarify, or explain, but it cannot override the HTF story alone.
```

Never flip the HTF story only because the child timeframe reacts from an HTF LL/HH.

## NCI-first rule

NCI is the backbone.

Use NCI rules for:

```text
market structure
market cycle
key levels
pulse wave
pullback wave
breakout standard
range standard
candle quality
supply/demand zone quality
obsolete zones
```

SMC supports the context only.

## SMC context rule

SMC can show:

```text
liquidity sweep
buy-side / sell-side liquidity
BOS / CHOCH
OB
FVG
premium / discount
```

But:

```text
SMC without NCI structure context = visual context only, not story confirmation.
```

## Visual cleanliness rule

The visualizer will not be messy if it tells one aligned story.

Do not show everything.

Show only what explains the active story.

Normal mode shows:

```text
active 4H KL / range / master path
active 1H explanation
active 15M movement
active 5M reaction
current chart TF KL if enabled
story panel
```

Debug mode can show:

```text
candidate pivots
invalid structure
obsolete zones
failed breakout/pullback checks
all candle classification details
candidate anchors
```

## NCI reference notes

Market structure course:

- NCI teaches market structure, market cycle, and multiple timeframe system.
- Purpose: understand trend, find key zones for entry/SL/TP/risk, know when a trend starts and ends.
- Price action includes single candle, wave, main structure, internal structure, key zones, liquidity, pullback/breakout standard, range standard.

Candle logic:

- Maru: body usually >= 70% total length in the course; one method file also mentions body >= 60%.
- Special Maru: long-tail absorption, close near high/low, body >= 50% total length.
- Pinbar: body < 50% total length, conflict/undecision.
- Doji: small candle, low-power indecision.
- Read candles at key zones only, not candle-by-candle everywhere.

Breakout standard:

- Apply breakout line to recent high/low, key level, POI zone, or range.
- Valid breakout can use two Maru candles or big Maru + small candle.
- For big Maru + small candle: first candle big versus previous Maru candles, second candle holds above/below 50%, and enough body closes beyond BOL.

Pullback standard:

- Two Maru candles or big Maru + small candle.
- Check pressure confirmation if one condition fails.

Supply/Demand:

- Strongest SD = obvious buyer/seller imbalance, at least two first Marubozu candles, immediate reversal, strong distance away.
- SD drawing variants: no-base general, having base, long tail, special 1, special 2.
- Obsolete SD: older zones lose value, broken SD, weak/normal SD without confirmation.

## Do not do yet

Do not prioritize:

```text
buy/sell entries
TP/SL automation
strategy tester
execution logic
heavy alerts
```

Build visual story first.
