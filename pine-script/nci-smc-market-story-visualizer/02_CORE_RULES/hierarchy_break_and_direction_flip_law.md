# Hierarchy Break and Direction Flip Law

This rule is mandatory for the NCI x SMC Market Story Visualizer.

## Core idea

When a higher-timeframe hierarchy is broken, the lower-timeframe structure must be recalculated from the new directional context.

A lower timeframe cannot continue using the old parent key level direction after the parent timeframe has invalidated that structure.

## Bearish-to-bullish example

```text
4H bearish structure
→ price breaks the 4H KL DOWN / LH decision area with valid NCI breakout pressure
→ old bearish hierarchy is invalidated
→ 4H story changes to transition / bullish reversal candidate
→ 1H must stop explaining bearish continuation
→ 1H must start recalculating from the opposite side
→ new KL logic begins from bullish direction: broken KL DOWN becomes retest/HL decision area
```

## Bullish-to-bearish example

```text
4H bullish structure
→ price breaks the 4H KL UP / HL decision area with valid NCI breakdown pressure
→ old bullish hierarchy is invalidated
→ 4H story changes to transition / bearish reversal candidate
→ 1H must stop explaining bullish continuation
→ 1H must start recalculating from the opposite side
→ new KL logic begins from bearish direction: broken KL UP becomes retest/LH decision area
```

## Decision rule

```text
Parent structure controls child interpretation.
If parent key level breaks with valid NCI pressure, child structure must flip from explanation mode into transition/rebuild mode.
After confirmed parent break, child key levels must be recalculated from the new opposite-direction story.
```

## Important distinction

A simple lower-timeframe reaction does not flip the higher-timeframe story.

But a valid higher-timeframe key-level break does.

```text
LTF reaction from HTF LL/HH = pullback explanation first.
Valid HTF KL break = hierarchy invalidation / recalculation trigger.
```

## Required future engine behavior

The future NCI Market Structure Engine must track:

```text
active parent direction
active parent KL UP
active parent KL DOWN
parent invalidation level
valid breakout / breakdown pressure
break confirmation state
retest state
new opposite-direction KL calculation
child mode: continuation / pullback explanation / transition / rebuild
```

## Child timeframe behavior after parent break

Before parent break:

```text
Child explains parent continuation or pullback.
```

After valid parent break:

```text
Child stops defending old story.
Child switches to transition/rebuild mode.
Child waits for new parent anchor.
Child recalculates KLs in the new direction.
```

## Visual story output should say

Examples:

```text
4H bearish hierarchy broken; 1H recalculating bullish transition from broken KL retest.
```

```text
4H bullish hierarchy broken; 1H recalculating bearish transition from broken KL retest.
```

```text
Parent break not validated; child reaction remains pullback explanation.
```
