# Patch v0.2 - Clean Structure / Noise Control Plan

This patch improves the first working prototype by reducing visual noise and making the entry models easier to read.

## Main problems from Ravi's chart review

- Too many labels on all timeframes.
- Asian range levels repeat too much on higher timeframes.
- Entry signals appear too early.
- Dashboard does not explain the market story.
- HTF key levels are not visible enough.
- FVG/entry zones need cleaner display and entry outline boxes.

## v0.2 patch goals

1. Add display modes:
   - Clean
   - Normal
   - Full Debug

2. Add timeframe-role behavior:
   - Narrative mode for 4H+
   - Bias mode for 1H
   - Setup mode for 15M/30M
   - Execution mode for 1M/3M/5M

3. Add signal states:
   - Setup
   - Armed
   - Confirmed

4. Add signal cooldown:
   - Prevent repeated entries too close together.

5. Clean Asian range:
   - Show current/latest range only by default.
   - Hide repetitive labels on HTF charts.

6. Add HTF key levels:
   - Previous day high/low.
   - Previous week high/low.
   - HTF bias line.

7. Upgrade dashboard:
   - Current chart role.
   - Active model state.
   - Missing condition / why waiting.
   - Nearest liquidity levels.

8. Preserve entry outline box layer:
   - Transparent rectangle around entry zone.
   - Strategy name at the top.

## Output file

```text
00_MASTER_COMPILED/smc-visual-entry-model-master-v0.2-clean-structure.pine
```

## Note

v0.2 is still not the final master logic. It is a readability and state-control upgrade. The next major patch should be v0.3 with a true OB engine and FVG quality scoring.
