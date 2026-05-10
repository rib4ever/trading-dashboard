# NCI x SMC KL Identification Upgrade — v1.4.3.2 Mapping

## User observation

Some key levels are visually close but not always at the correct NCI candle/zone origin. Candidate/not-KL labels create noise and reduce trust.

## New priority

Use SMC structure logic to identify the valid NCI key level origin.

## Correct KL identification sequence

1. Detect confirmed swing structure.
   - Swing high = confirmed pivot high.
   - Swing low = confirmed pivot low.
   - These are structure points, not automatic key levels.

2. Confirm BOS / structure break.
   - Bullish KL is valid only when price breaks the previous meaningful swing high.
   - Bearish KL is valid only when price breaks the previous meaningful swing low.
   - BOS can use wick or close depending on settings, but close is stricter.

3. Locate the origin of the displacement leg.
   - Bullish demand KL = the last bearish candle or last pullback low zone before the bullish displacement that created BOS.
   - Bearish supply KL = the last bullish candle or last pullback high zone before the bearish displacement that created BOS.
   - Do not use the latest candidate if it did not create the BOS.

4. Validate reaction / displacement.
   - After the origin candle/zone, the next 3 to 5 candles should show directional pressure.
   - Bullish demand requires bullish pressure after the origin.
   - Bearish supply requires bearish pressure after the origin.
   - This helps avoid random pivots becoming KL.

5. Validate active / obsolete status.
   - Demand becomes broken/obsolete when price closes or strongly trades below the demand bottom using mitigation buffer.
   - Supply becomes broken/obsolete when price closes or strongly trades above the supply top using mitigation buffer.
   - Broken or fully mitigated child KL should not remain visible as active KL.

6. Candidate labels behavior.
   - Default Story mode should not show “not KL” candidate labels.
   - Candidates can remain available only in Debug mode.
   - Active visual should show confirmed/active KLs and relevant child context only.

## Visual rule

- 4H confirmed supply/demand must always be available as the parent story anchor.
- 1H/15M/5M zones should be shown only when they explain the parent story.
- Labels should be compact on-chart and detailed through hover tooltip.
- If multiple labels are close, stagger them to the right using offsets.

## Next build instruction

Create v1.4.3.2 from v1.4.3.1 stable patch.

Primary changes:

1. Replace pivot-as-KL behavior with BOS-origin KL behavior.
2. Hide candidate/not-KL labels from Story mode.
3. Add reaction pressure validation after the origin candle.
4. Add stricter active/obsolete filtering.
5. Keep the v1.4.3 clean visual style.
