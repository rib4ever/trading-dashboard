# NCI Project Overview

## Objective

Create an advanced TradingView indicator based on the NCI trading standards.

The indicator will be built progressively and must stay easy to debug, improve, and roll back.

## Confirmed rules

- Pine Script v6 only
- Indicator only for now
- Strict NCI rules by default
- Debug mode by default
- Universal market mode by default
- Dedicated BTCUSD and XAUUSD presets
- GitHub-based version control model

## Signal philosophy

The indicator must not generate random buy/sell arrows. It must follow a structured NCI decision chain:

Trend → Key Level → Zone → Candle Pressure → Breakout/Pullback Confirmation → RR Check → Signal

## Current focus

v0.1 is focused only on the candle engine and preset engine.

This is intentional because every future NCI module depends on clean candle pressure classification.
