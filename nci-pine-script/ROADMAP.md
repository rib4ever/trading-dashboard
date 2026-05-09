# NCI Pine Script Roadmap

## Project direction

Build the NCI Master Indicator progressively, module by module, using Pine Script v6 and a GitHub-based workflow.

## Release plan

### v0.1 — Preset Engine + Candle Engine + Debug Dashboard

Status: **Initial foundation**

Includes:

- Pine Script v6 setup
- Universal, Scalping, Day Trading, Swing Trading, BTCUSD, XAUUSD, Manual Custom presets
- Strict NCI mode
- Debug mode
- Marubozu detection
- Special Maru detection
- Pinbar detection
- Doji detection
- Normal candle classification
- Dashboard
- Foundation alerts

### v0.2 — Market Structure Engine

Planned modules:

- Swing high / swing low detection
- HH / HL / LH / LL labels
- Main structure state
- Internal structure state
- Up key level
- Down key level
- Basic trend-change warning

### v0.3 — Supply and Demand Zone Engine

Planned modules:

- No-base general supply/demand
- Having-base supply/demand
- Long-tail zones
- Special case 1: first candle too big
- Special case 2: second candle too big
- Safety-zone option
- Active zone box management

### v0.4 — Strongest SD + Obsolete SD Engine

Planned modules:

- Strongest SD score
- Fresh / tested / weak / broken / obsolete status
- Zone age penalty
- Zone touch penalty
- Broken-zone filter

### v0.5 — Breakout + Pullback Standards

Planned modules:

- Two-Maru breakout
- Big-Maru + small candle breakout
- Breakout confirmation
- False breakout warning
- Two-Maru pullback
- Big-Maru + small candle pullback
- Pullback confirmation

### v0.6 — Entry Model Engine

Planned models:

- Strongest SD setup
- Normal SD + confirmation setup
- Break & retest setup
- Pullback continuation setup
- Trend-change setup

### v0.7 — MTF + Alerts

Planned modules:

- HTF trend bias
- HTF key level
- HTF SD context
- Entry-timeframe confirmation
- Alert expansion

### v1.0 — Stable NCI Indicator

Stable release requirements:

- Clean visuals
- Strict NCI logic
- Debug dashboard
- Alert system
- Object count control
- Testing screenshots/logs
- Clear user guide

## Golden rule

No random buy/sell signals. Every signal must be explainable through the NCI chain:

```text
Trend → Key Level → Zone → Candle Pressure → Breakout/Pullback Confirmation → RR Check → Signal
```
