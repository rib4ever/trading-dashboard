# NCI x SMC Market Story Visualizer Blueprint

Project: **NCI x SMC Market Story Visualizer [Ravi Custom]**

Pine version target: **Pine Script v6**

## 1. Product definition

The visualizer is a TradingView Pine Script indicator that narrates price action across multiple timeframes.

It must match Ravi's manual drawing logic:

```text
4H master story
→ 1H explanation
→ 15M working movement
→ 5M internal reaction
→ current chart TF working layer when applicable
→ one aligned price-action story
```

The first stable version should focus on visual structure only.

## 2. Scope for v1.0

### In scope

- Configurable four-timeframe stack.
- Default stack: 4H / 1H / 15M / 5M.
- Current chart timeframe layer.
- Connected 4H master structure path.
- Fractal -1 hierarchy logic.
- Higher-timeframe LL/HH reaction continuation logic.
- NCI key levels.
- NCI candle classification.
- NCI breakout/pullback states.
- NCI range story.
- NCI supply/demand classification.
- SMC liquidity context.
- Story panel.
- Debug mode.

### Out of scope for initial build

- Buy/sell execution signals.
- Automated TP/SL.
- Strategy tester mode.
- Trade automation.
- Direct TradingView push automation.

## 3. User settings design

### Timeframe settings

```pine
TF Slot 1: 4H
TF Slot 2: 1H
TF Slot 3: 15M
TF Slot 4: 5M
Show current chart timeframe layer: true
Auto-align chart timeframe: true
```

### Mode settings

```text
Visualization Mode:
- Clean
- Story
- Debug

Story Mode:
- NCI Only
- SMC Context Only
- Hybrid NCI + SMC

Range Handling:
- Enabled by default
```

### Display settings

```text
Show 4H master path
Show 1H child path
Show 15M child path
Show 5M reaction markers
Show chart TF key levels
Show NCI SD zones
Show SMC context
Show story panel
Show debug labels
```

## 4. Data model concept

Each timeframe should produce a common structure object conceptually:

```text
TFState
- timeframe
- trendState: bullish / bearish / range / transition / unknown
- phase: pulse / pullback / breakout / range / retest / fakeout
- activeKLUp
- activeKLDown
- recentHigh
- recentLow
- structureOrigin
- eventAnchor
- eventAnchorType: pullback-start / KL-touch / LL-reaction / HH-reaction / range-edge / breakout / breakdown / retest / fakeout
- childMission: continuation explanation / pullback explanation / range rotation explanation / reversal warning / wait
- rangeHigh
- rangeLow
- rangeMid
- activeDemand
- activeSupply
- breakoutState
- pullbackState
- candlePressureState
- storyText
```

Pine does not support full custom object workflows like normal languages, so implementation should use parallel variables/functions and arrays where needed.

## 5. Engine implementation order

### Phase 0.0 — Skeleton

Create indicator shell with:

- Pine v6 header.
- TF slot inputs.
- Display mode inputs.
- Story table placeholder.
- Function placeholders.

### Phase 0.1 — Timeframe Role Engine

Implement:

- selected TF slot inputs,
- chart timeframe detection,
- simple chart TF layer toggle,
- story panel showing TF roles.

### Phase 0.2 — Candle Engine

Implement NCI candle classification:

- Maru,
- Special Maru,
- Pinbar,
- Doji,
- Normal.

Initial simple thresholds:

```text
Maru: body / range >= 0.70
Special Maru: body / range >= 0.50 + long wick absorption + close near high/low
Pinbar: body / range < 0.50 + large wick
Doji: small body
```

### Phase 0.3 — Basic KL Engine

Implement pivot-based preliminary KL detection per timeframe.

Important: this is only an early approximation. Final KL must follow connected NCI structure logic.

### Phase 0.4 — 4H Master Structure Engine

Build connected master structure:

- detect structural origin,
- connect pulse/pullback,
- identify active KL,
- prevent random trend labels.

### Phase 0.5 — Event Anchor Engine

Detect anchors:

- pullback origin,
- KL touch,
- LL reaction after bearish impulse,
- HH reaction after bullish impulse,
- range edge reaction,
- breakout candle,
- failed breakout candle,
- retest.

Mandatory rule:

```text
LTF reaction from HTF LL/HH = pullback explanation first.
HTF continuation story remains active until HTF structure is invalidated by valid NCI structure rules.
```

### Phase 0.6 — Fractal Child Engine

Apply same logic downward:

```text
4H anchor → 1H explanation
1H anchor → 15M explanation
15M anchor → 5M explanation
```

The child timeframe must not override the parent story by reaction alone. It must classify whether it is explaining continuation, pullback, range rotation, fakeout, or transition warning.

### Phase 0.7 — Range Story Engine

Implement:

- range high/low/mid,
- range active state,
- rotation up/down,
- sweep/fakeout,
- valid range breakout,
- transition from range to trend.

### Phase 0.8 — NCI Breakout/Pullback Validation

Implement NCI standards:

- two Maru candles,
- big Maru + small candle,
- close beyond breakout line,
- candle body position relative to breakout line,
- confirmation candle when one condition fails.

### Phase 0.9 — NCI Supply/Demand Engine

Implement SD drawing types:

- no-base general,
- having base,
- long tail,
- special 1,
- special 2,
- strongest SD,
- obsolete SD.

### Phase 1.0 — Story Panel + Clean Visuals

Implement final visual output:

- multi-timeframe story panel,
- active structure paths,
- KL labels,
- range labels,
- relevant zones,
- alignment status.

## 6. Story panel structure

Suggested table:

```text
NCI x SMC Story
TF Stack: 4H → 1H → 15M → 5M
Chart TF: 30M
4H: Bearish continuation / New LL reaction / KL DOWN still active
1H: Explaining pullback from 4H LL, not reversal yet
15M: Internal bullish pullback movement / watch for weakening near 1H KL
5M: Reaction / micro rejection or continuation detail
Chart TF: 30M KL visible
Story: Lower TF is explaining the 4H bearish pullback until valid 4H invalidation
```

## 7. Story states

The Story Decision Engine should output one of:

```text
4H bullish continuation
4H bearish continuation
4H pullback active
4H bearish LL reaction / child pullback explanation
4H bullish HH reaction / child pullback explanation
4H range active
1H opposes 4H as pullback explanation
15M supports 1H
5M reaction only
range rotation up
range rotation down
fakeout above range
fakeout below range
valid breakout forming
new trend forming
no clean story
```

## 8. Visual rules

### Normal mode

Show only:

- active 4H structure path,
- active 4H KL/range,
- active 4H event anchor,
- active 1H explanation / mission,
- active 15M movement,
- active 5M reaction,
- current chart TF KL,
- story panel.

### Debug mode

Show:

- all candidate pivots,
- rejected structure points,
- invalid pullbacks/breakouts,
- candle classifications,
- obsolete SD zones,
- failed anchor attempts.

## 9. Design rule for visual cleanliness

The visual stack is not messy if it tells one aligned story.

Do not draw four independent analyses.

Draw one story across four roles.

```text
4H = chapter
1H = explanation
15M = working movement
5M = reaction
```

## 10. HTF LL / HH reaction scenario

This scenario is mandatory.

```text
4H bearish trend
→ price creates a new 4H LL
→ 1H reacts upward from that 4H LL
```

Correct handling:

```text
Do not call bullish reversal by default.
Treat 1H upward movement as pullback explanation from the 4H LL.
Wait to see whether 1H forms LH / KL DOWN rejection for bearish continuation.
Only valid 4H invalidation or valid 4H reversal changes the master story.
```

Opposite bullish case:

```text
4H bullish trend
→ price creates a new 4H HH
→ 1H reacts downward from that 4H HH
```

Correct handling:

```text
Do not call bearish reversal by default.
Treat 1H downward movement as pullback explanation from the 4H HH.
Wait to see whether 1H forms HL / KL UP rejection for bullish continuation.
Only valid 4H invalidation or valid 4H reversal changes the master story.
```

## 11. Final build goal

A user should open any chart and instantly understand:

```text
What is the 4H story?
Where is price inside that story?
What 4H event is being explained?
Is the child timeframe reaction only a pullback explanation, or a valid transition warning?
How does 1H explain 4H?
How does 15M explain 1H?
How does 5M explain 15M?
Where are the current chart timeframe key levels?
Is the market trending, pulling back, ranging, sweeping, breaking out, or transitioning?
```
