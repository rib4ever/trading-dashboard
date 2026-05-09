# NCI Top-Down Market Cycle Algorithm

## Source

This document is based on Ravi's direct clarification of NCI top-down market cycle analysis.

## Core correction

The NCI script must not scan all timeframes independently and display all random key levels together.

The correct NCI method is sequential top-down analysis.

```text
H4 → H1 → M15 → M5
```

Each lower timeframe is checked only after the higher timeframe market structure and key level context are known.

## Main objective

The script must show the whole market picture through market cycles, not local swing noise.

## Correct analysis sequence

### Step 1 — Start with H4

The script must first analyze H4.

On H4, identify:

```text
H4 trend
H4 pulse wave
H4 pullback wave
H4 market structure
H4 key level
H4 broken key level if applicable
```

Only after H4 is understood should the script move to H1.

### Step 2 — Move to H1 from H4 context

H1 analysis must be done from the H4 key-level / market-cycle context.

The script should not create unrelated H1 key levels across the whole chart.

On H1, identify:

```text
H1 trend inside H4 context
H1 pulse wave
H1 pullback wave
H1 market structure
H1 key level
H1 broken key level if applicable
```

### Step 3 — Move to M15 from H1 context

M15 analysis must be done from the H1 key-level / market-cycle context.

On M15, identify:

```text
M15 trend inside H1 context
M15 pulse wave
M15 pullback wave
M15 market structure
M15 key level
M15 broken key level if applicable
```

### Step 4 — Move to M5 from M15 context

M5 is the opportunity / execution structure layer.

M5 should be checked only after H4, H1, and M15 context is known.

On M5, identify:

```text
M5 internal structure
M5 opportunity wave
M5 pullback / breakout confirmation
M5 reaction near POI / key level
```

## Trend broken rule

If a buy trend key level is broken, the same timeframe must be re-analyzed from the latest higher high.

Example:

```text
H1 is in an uptrend.
H1 buy trend key level is broken.
This means H1 may be starting a downtrend.
Now check from the latest H1 higher high that caused/belonged to the broken structure.
From that latest high, look for H1 downtrend market structure and H1 downtrend key levels.
```

If no valid same-timeframe key level appears, then continue down to the next lower timeframe.

Example:

```text
H1 buy KL broken.
Check H1 downtrend from latest H1 higher high.
If no valid H1 downtrend key level exists:
    move to M15 and check M15 key level from that same market-cycle context.
```

## Opposite trend start logic

When the trend key level is broken, the script should not instantly mark the opposite trend randomly.

It should:

```text
1. Mark previous trend KL as broken.
2. Identify the latest high/low that becomes the start reference for opposite trend analysis.
3. Check same timeframe for valid opposite-trend structure.
4. If same timeframe lacks valid key level, go one timeframe lower.
5. Continue the top-down sequence.
```

## Key level ownership rule

Each timeframe owns its own key level.

```text
H4 KL belongs to H4.
H1 KL belongs to H1.
M15 KL belongs to M15.
M5 internal KL belongs to M5 execution context.
```

Lower timeframe key levels do not replace higher timeframe key levels.

Higher timeframe key levels create the context for lower timeframe analysis.

## Display rule

The script must not show every detected level from every timeframe randomly.

It should show:

```text
The active HTF context.
The active key level for the timeframe being analyzed.
The broken key level if relevant.
The next lower timeframe context only after the previous timeframe is resolved.
```

## Range rule in top-down context

If the current timeframe is in range:

```text
Do not force PW or PBW.
Wait for valid NCI breakout.
After breakout, continue market-cycle analysis from that breakout direction.
```

## Practical coding implication

The current wave detector block is only a local detector and is too noisy when used directly on the visible timeframe.

The next redesign must create a state-machine style top-down engine:

```text
Analyze H4 state
↓
If H4 state valid, analyze H1 from H4 context
↓
If H1 state valid, analyze M15 from H1 context
↓
If M15 state valid, analyze M5 from M15 context
```

## Required dashboard fields

The dashboard should eventually show:

```text
H4 State: Up / Down / Range / Broken / Waiting BO
H4 Active KL
H4 Broken KL
H1 State from H4 context
H1 Active KL
H1 Broken KL
M15 State from H1 context
M15 Active KL
M5 Opportunity State
Current active analysis step
```

## Do not proceed rule

Do not merge the Market Structure / Key Level Map to candidate until this top-down sequential logic is implemented and Ravi confirms that it matches NCI market cycle behaviour.
