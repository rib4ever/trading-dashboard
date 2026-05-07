# 03_MASTER_CANDIDATES

This folder is for merged master candidate versions before they replace the last confirmed working base.

## Current target

`master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine`

Purpose:
- Start from v1.4 last working master script.
- Merge Patch 02 Smart Historical Key Level + Liquidity Engine.
- Keep the original v1.4 base untouched until TradingView confirms the candidate compiles.

## Candidate validation rule

A file in this folder is not considered the new base until:
1. It is pasted into TradingView Pine Editor as pure `.pine` text.
2. It compiles with zero red errors.
3. It displays Smart Support / Smart Resistance correctly.
4. It does not create random sniper/opportunity entries away from key levels.
5. It is manually confirmed by Ravi.
