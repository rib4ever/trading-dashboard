# NCI Pine Script Indicator Project

This folder contains the GitHub-based development workspace for the **NCI Master Indicator** for TradingView.

## Confirmed project standards

- **Pine Script version:** v6 only
- **Script type:** Indicator only for now
- **Default market mode:** Universal / neutral for all markets
- **Special presets:** Universal, Scalping, Day Trading, Swing Trading, BTCUSD, XAUUSD, Manual Custom
- **Signal style:** Strict NCI rules + Debug mode
- **Development model:** Same modular GitHub workflow used for the SMC + SATS project

## Core NCI logic order

Every future signal must follow this decision flow:

```text
Trend → Key Level → Zone → Candle Pressure → Breakout/Pullback Confirmation → RR Check → Signal
```

No random buy/sell arrows. The script must behave as a structured decision assistant based on the NCI documents.

## Current version

```text
v0.1 — Preset Engine + Candle Engine + Debug Dashboard
```

## Folder structure

```text
nci-pine-script/
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── BUGS_AND_FIXES.md
├── TESTING_LOG.md
├── pine/
│   ├── NCI_Master_Indicator_latest.pine
│   ├── NCI_Master_Indicator_v0_1.pine
│   └── archive/
├── docs/
│   ├── 01_NCI_Project_Overview.md
│   ├── 02_NCI_Standards.md
│   ├── 03_Candle_Engine.md
│   └── 08_Debug_Guide.md
├── modules/
│   ├── 01_candle_engine.md
│   └── 02_preset_engine.md
├── tests/
│   ├── XAUUSD_3M_tests.md
│   ├── BTCUSD_5M_tests.md
│   └── Universal_market_tests.md
└── prompts/
    ├── debug_prompt.md
    └── upgrade_prompt.md
```

## Development rule

Each stable checkpoint will be saved as a separate version file. The active clean version is always:

```text
pine/NCI_Master_Indicator_latest.pine
```

