# NCI MTF Key Level Map Design

## Objective

The NCI Market Structure engine must be built around the correct identification of:

```text
Pulse Wave
Pullback Wave
Market Cycle
Market Structure
Key Level
Broken Key Level
HTF Bias
Internal Structure
Confluence / Unconfluence
POI Strategy Context
```

## Critical rule from Ravi

If Pulse Wave and Pullback Wave are calculated incorrectly, the Market Structure will also be wrong.

If Market Structure is wrong, Key Levels will also be wrong.

Therefore:

```text
Do not draw NCI Market Structure before Pulse Wave and Pullback Wave logic is aligned with NCI standards.
Do not draw NCI Key Levels before Market Structure is confirmed from NCI wave logic.
```

## Main objective

The script must show the whole market picture, not local swing noise.

Expected picture:

```text
H4 key level / market cycle
H1 key level / market cycle
M15 key level / market cycle
M5 internal opportunity structure
Broken HTF key levels
Current price context relative to all active KLs
External structure aligned with internal structure
```

## Timeframe layers

### H4 Layer

Purpose:

```text
Major external market structure
Major market cycle context
Main HTF key level zones
```

Expected visual output:

```text
H4 KL UP
H4 KL DOWN
H4 KL Broken
H4 cycle direction
```

### H1 Layer

Purpose:

```text
Main trading bias layer
External structure for intraday trades
Important broken key levels
```

Expected visual output:

```text
H1 KL UP
H1 KL DOWN
H1 KL Broken
H1 cycle direction
```

### M15 Layer

Purpose:

```text
Confirmation and refined structure layer
Current structure context
Intermediate key levels
```

Expected visual output:

```text
M15 KL UP
M15 KL DOWN
M15 KL Broken
M15 internal/external alignment
```

### M5 Layer

Purpose:

```text
Opportunity / execution structure layer
Internal structure for entry planning
Confluence with HTF key levels and POI
```

Expected visual output:

```text
M5 internal trend
M5 opportunity structure
M5 reaction around KL / POI
```

## Key Level creation rule

A key level must not be created from a random swing high or swing low.

A valid NCI Key Level must come from:

```text
1. Correct NCI Pulse Wave identification.
2. Correct NCI Pullback Wave identification.
3. NCI Market Cycle context.
4. NCI structure logic.
5. Valid NCI pullback / breakout confirmation.
```

## Key Level replacement rule

Ravi confirmed:

```text
Latest valid pullback replaces the previous key level.
```

Important:

```text
Replacement happens inside the same timeframe layer only.
```

Example:

```text
Latest valid H1 pullback replaces previous H1 key level.
Latest valid M15 pullback replaces previous M15 key level.
M15 key level must not replace H1 key level.
H1 key level must not replace H4 key level.
```

## Broken Key Level rule

A key level becomes broken only when NCI valid-breakout rules are satisfied.

It should not be marked broken only because of a wick or weak touch.

Broken KL output should show:

```text
H4 KL Broken
H1 KL Broken
M15 KL Broken
```

## Internal vs External structure rule

External structure:

```text
H4 / H1 / M15 main market cycle and key levels.
```

Internal structure:

```text
Lower timeframe opportunity structure, mainly M15 / M5.
```

Internal structure must not dominate the chart.

It should only help after HTF context is known.

## Confluence / Unconfluence rule

The script must eventually show whether current internal structure agrees or disagrees with HTF context.

Example:

```text
HTF Bullish + Internal Bullish = Confluence
HTF Bearish + Internal Bearish = Confluence
HTF Bullish + Internal Bearish = Pullback / Unconfluence
HTF Bearish + Internal Bullish = Pullback / Unconfluence
```

But this must be tied to NCI market cycle logic, not generic EMA-only logic.

## Display rule

The chart should display timeframe-specific key levels clearly:

```text
H4 KL UP / H4 KL DOWN
H1 KL UP / H1 KL DOWN
M15 KL UP / M15 KL DOWN
M5 Opportunity KL / Internal KL
```

Each timeframe should have a distinct label.

Suggested visual style:

```text
H4 = thick zone / strong color
H1 = medium zone
M15 = thinner zone
M5 = light/internal label only
Broken KL = orange/brown or faded broken-zone style
```

## v0.2 rebuild plan

The previous v0.2 script block is now considered a helper-only prototype.

New v0.2 should be rebuilt as:

```text
script_blocks/03_mtf_key_level_map_v0_2_block.pine
```

Development steps:

```text
1. Define NCI pulse/pullback wave logic from documents.
2. Build one timeframe key level detector first.
3. Validate H1 manually against Ravi's drawings.
4. Expand to H4 / H1 / M15 / M5 layers.
5. Add broken KL state.
6. Add dashboard showing all timeframe layers.
7. Add optional display filters only after logic is correct.
```

## Do not proceed rule

Do not merge Market Structure or Key Level logic into candidate/master until:

```text
Pulse Wave logic is validated.
Pullback Wave logic is validated.
Key Level placement is validated.
Broken KL detection is validated.
MTF alignment is visually understandable.
Ravi confirms it matches NCI standards.
```
