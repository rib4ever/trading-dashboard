# Bugs and Fixes — NCI Pine Script Indicator

Use this file to track every TradingView compile error, visual issue, logic issue, and fix.

## Active issues

### v0.2 Market Structure block is not aligned with NCI full market picture

Date: 2026-05-09
Version: v0.2 script block
Market / Timeframe: Gold H4 / H1 / M15 examples from Ravi
Preset: NCI Market Structure / Key Level
Issue:

The first v0.2 Market Structure block only shows local pulse, pullback, internal swing labels, and latest key levels. This creates noise and does not represent the NCI full market picture.

Ravi's expected NCI Market Structure requires:

- Higher-timeframe key levels from H4, H1, M15, and later M5.
- Market cycle alignment across timeframes.
- External structure and internal structure connected together.
- Key levels drawn as timeframe-specific zones/levels, not random local swing lines.
- Broken HTF key levels shown clearly.
- Current price context shown relative to HTF and lower timeframe key levels.
- Internal opportunity structure should be read only after HTF bias/trend and market cycle are clear.

Cause:

The v0.2 block was built as a technical internal swing helper, not as a true NCI top-down market structure engine.

Fix required:

Redesign v0.2 around a Multi-Timeframe NCI Key Level Map:

1. HTF structure layer: H4 / H1 / M15 / M5.
2. Each timeframe gets its own NCI market cycle and key level state.
3. Latest valid pullback replaces key level only within its own timeframe.
4. Show active and broken key levels by timeframe.
5. Separate external structure and internal structure.
6. Internal structure must not dominate the chart; it must be filtered by HTF context.
7. Dashboard must show HTF bias, current TF trend, internal trend, active KLs, broken KLs, confluence/unconfluence state.

Status: Active redesign required before continuing v0.2 coding.

## Fixed issues

None yet.
