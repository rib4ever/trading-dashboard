# Hierarchy Break Memory Addendum

Use this addendum in all future NCI x SMC Market Story Visualizer development.

## New permanent rule from Ravi

Whenever a higher-timeframe hierarchy is broken, the lower-timeframe structure must change accordingly.

If a higher-timeframe key level breaks with valid NCI pressure, the key-level logic should be recalculated from the opposite direction.

## Core law

```text
LTF reaction from HTF LL/HH = pullback explanation first.
Valid HTF KL break = hierarchy invalidation and recalculation trigger.
```

## Practical implementation rule

Before valid HTF break:

```text
1H explains 4H continuation or pullback.
15M explains 1H.
5M explains 15M.
```

After valid HTF break:

```text
1H stops defending old 4H story.
1H switches to transition/rebuild mode.
1H recalculates structure from the opposite direction.
15M and 5M then follow the new 1H transition/rebuild anchor.
```

## Example bearish structure break

```text
4H bearish continuation
→ 4H KL DOWN / LH area breaks upward with valid NCI pressure
→ old bearish hierarchy is invalidated
→ 4H enters bullish transition/reversal candidate
→ 1H recalculates from bullish side
→ broken KL DOWN becomes retest / HL decision area
```

## Example bullish structure break

```text
4H bullish continuation
→ 4H KL UP / HL area breaks downward with valid NCI pressure
→ old bullish hierarchy is invalidated
→ 4H enters bearish transition/reversal candidate
→ 1H recalculates from bearish side
→ broken KL UP becomes retest / LH decision area
```

## Future engine requirement

The v1.2 Real NCI Market Structure Engine must include:

```text
parent direction state
parent KL break detection
break validation using NCI pressure
hierarchy invalidation flag
opposite-direction recalculation mode
child rebuild state
broken-level retest state
```
