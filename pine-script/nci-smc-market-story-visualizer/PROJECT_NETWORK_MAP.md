# Project Network Map

Project: **NCI x SMC Market Story Visualizer [Ravi Custom]**

Location:

```text
pine-script/nci-smc-market-story-visualizer/
```

## 1. Master purpose

The indicator must behave as a **visual market narrator**, not as a signal machine.

It must show one connected price-action story across the selected timeframe stack:

```text
4H → 1H → 15M → 5M
```

and also respect the current chart timeframe as an additional active layer when it is not one of the four selected slots.

## 2. Core network flow

```text
Selected TF Stack
    ↓
4H Master Story Engine
    ↓
4H Event Anchor Engine
    ↓
1H Internal Explanation Engine
    ↓
1H Event Anchor Engine
    ↓
15M Internal Explanation Engine
    ↓
15M Event Anchor Engine
    ↓
5M Internal Reaction Engine
    ↓
Current Chart TF Working Layer
    ↓
NCI Validation Layer
    ↓
SMC Liquidity Context Layer
    ↓
Story Decision Engine
    ↓
Visual Engine
```

## 3. Engine list

### A. Timeframe Role Engine

Responsibilities:

- Read selected TF Slot 1/2/3/4.
- Default stack: 4H / 1H / 15M / 5M.
- Detect current chart timeframe.
- Add current chart TF layer when required.
- Keep all layers aligned into the hierarchy.

### B. 4H Master Story Engine

Responsibilities:

- Detect last relevant 4H market-structure sequence.
- Avoid random trend labels.
- Track connected bullish/bearish/range story.
- Define 4H KL UP/DOWN, recent HH/HL/LH/LL, pulse, pullback, breakout, and range.

### C. Event Anchor Engine

Responsibilities:

- Identify where the next lower timeframe must start reading.
- Anchor types:
  - pullback start,
  - KL touch,
  - range high/low touch,
  - sweep,
  - breakout candle,
  - failed breakout candle,
  - retest of broken level.

### D. Fractal Child Structure Engine

Responsibilities:

- Repeat the same structure logic on each -1 layer.
- 1H explains 4H.
- 15M explains 1H.
- 5M explains 15M.
- Optional future 1M explains 5M.

### E. NCI Candle Engine

Responsibilities:

- Classify Maru, Special Maru, Pinbar, Doji, Normal candle.
- Read candles only at key zones or important structure events, not candle by candle everywhere.

### F. NCI Breakout / Pullback Engine

Responsibilities:

- Validate breakouts and pullbacks using NCI standards.
- Distinguish valid breakout, weak breakout, fakeout, failed breakout, valid pullback, invalid pullback.

### G. Range Story Engine

Responsibilities:

- Treat range as a full market chapter.
- Draw range high, range low, midline, premium/discount.
- Classify rotation, sweep, fakeout, valid breakout, and range-to-trend transition.
- Remember that range can start after a valid breakout or valid pullback.

### H. Supply & Demand Engine

Responsibilities:

- Detect NCI SD zones.
- Classify strongest, normal, weak, obsolete, safety, broken.
- Draw only story-relevant active zones in normal mode.

### I. SMC Context Engine

Responsibilities:

- Add liquidity sweep, BOS/CHOCH, OB, FVG, buy-side/sell-side liquidity.
- SMC supports the NCI story but never replaces it.

### J. Story Decision Engine

Responsibilities:

- Convert structure and context into narrative state:
  - bullish continuation,
  - bearish continuation,
  - pullback active,
  - range active,
  - range rotation up/down,
  - fakeout,
  - valid breakout forming,
  - new trend forming,
  - no clean story.

### K. Visual Engine

Responsibilities:

- Show only story-relevant visuals.
- Display hierarchy cleanly.
- Keep debug details optional.

## 4. Visual hierarchy

```text
4H  = strongest visual priority / master zones / master story
1H  = structure bridge / active HTF explanation
15M = working movement / pullback-breakout detail
5M  = internal reaction / micro confirmation
Chart TF = highlighted working layer if different from selected stack
```

## 5. Adaptive structure rule

The project must not use an arbitrary fixed zone count like 20.

Correct rule:

```text
Show the complete active structure path from the last valid 4H structural origin to current price.
```

The number of levels/zones/paths is adaptive and story-based.

## 6. Normal mode vs Debug mode

Normal mode:

- active 4H story,
- active 1H/15M/5M explanation,
- current chart TF KL if enabled,
- relevant ranges/zones,
- current story panel.

Debug mode:

- rejected pivots,
- invalid breakout/pullback checks,
- obsolete SD zones,
- all candidate anchors,
- candle classifications,
- internal reason labels.
