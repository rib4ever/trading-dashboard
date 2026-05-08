# Session Update — 2026-05-08 — v1.5 Runtime + Placeholder Fix

## What Ravi reported

1. The generated v1.5 smart key liquidity candidate works visually on 3M and 15M, but throws a TradingView runtime error on 5M:

```text
Runtime error: RE10045
Error on bar 10615: In 'array.get()' function.
Index 0 is out of bounds, array size is 0.
at #main():1527
```

2. The old v1.5 placeholder warning label was plotted at the live price level, disturbing the chart.

## Fix applied in GitHub

### Runtime safety fix

Updated:

```text
03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py
```

Change:
- Added runtime guards around current timeframe OB/FVG visual loops.
- This prevents Pine from running `array.get(0)` when `currTfOBs` or `currTfFvgs` is empty.
- The fix is applied by the assembler when it rebuilds the generated v1.5 candidate.

### Workflow improvement

Updated:

```text
.github/workflows/build-pine-v15-candidate.yml
```

Change:
- Added push path triggers for the assembler, Block 06, and v1.4 base.
- Manual workflow run is still valid and recommended when GitHub does not auto-run after bot/API commits.

### Placeholder UI fix

Updated:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-candidate-smart-key-levels.pine
```

Change:
- Replaced price-level `label.new()` placeholder with a selectable `table` warning.
- New settings:
  - Show Placeholder Warning
  - Placeholder Position: Top Right, Top Left, Bottom Right, Bottom Left, Middle Right, Middle Left

## Next required action

Run this GitHub Action manually once:

```text
Actions → Build Pine v1.5 Candidate → Run workflow → main
```

Then open the generated file:

```text
03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine
```

Open Raw, copy all Pine code, paste into TradingView, and retest 3M / 5M / 15M.

## Current status

- v1.4 remains the protected last working base.
- v1.5 smart key liquidity candidate is still under test.
- Do not promote v1.5 to `00_MASTER_COMPILED` until the 5M runtime error is confirmed fixed in TradingView.
