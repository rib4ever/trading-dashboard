# NCI Candidate Master Script

This folder contains the merged candidate version of the NCI Master Indicator.

## Purpose

The candidate script is the testing stage before updating the active latest script.

## Workflow

```text
script_blocks/*
    ↓ tested individually
candidate/NCI_Master_Indicator_candidate.pine
    ↓ tested on TradingView
pine/NCI_Master_Indicator_latest.pine
    ↓ accepted stable working version
releases/vX.X/
```

## Candidate rule

The candidate script can include newly merged modules, but it is not considered stable until tested on:

```text
BTCUSD 5M
XAUUSD 3M
EURUSD 15M
At least one day-trading timeframe
At least one swing-trading timeframe
```
