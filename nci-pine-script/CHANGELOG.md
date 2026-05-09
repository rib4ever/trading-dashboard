# Changelog — NCI Pine Script Indicator

## v0.1.3 — Label readability patch

### Changed

- Updated candle marker text colors for better visibility on solid/light TradingView chart backgrounds.
- Project visual rule confirmed:
  - White text should only be used when the label has a strong colored background.
  - Labels without a strong background should use black text.
- Active Pine file updated:
  - `pine/NCI_Master_Indicator_latest.pine`

### Reason

The previous label text was difficult to read on solid/non-colored chart backgrounds.

## v0.1.2 — Candle priority correction

### Changed

- Corrected candle priority order:
  1. Maru
  2. Doji
  3. Special Maru
  4. Pinbar
  5. Normal
- Prevented Maru candles from being captured as Special Maru.
- Prevented Doji candles from being captured as Pinbar.
- Made Pinbar and Special Maru classification stricter.

## v0.1 — Initial foundation

### Added

- Created NCI Pine Script project structure.
- Confirmed Pine Script v6 as the project standard.
- Confirmed indicator-only development for now.
- Added preset system:
  - Universal
  - Scalping
  - Day Trading
  - Swing Trading
  - BTCUSD
  - XAUUSD
  - Manual Custom
- Added strict NCI mode.
- Added debug mode.
- Added Candle Engine foundation:
  - Marubozu
  - Special Maru
  - Pinbar
  - Doji
  - Normal candle
- Added dashboard showing candle classification and calculation values.
- Added foundation alert conditions for candle types.

### Notes

This version is not an entry model yet. It only validates candle pressure classification before building market structure and supply/demand logic.
