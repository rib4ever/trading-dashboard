# Master SMC + SATS + NCI Story Integration

## Purpose
This workspace is for the new architecture where the existing SMC/SATS script remains the structural engine and the NCI story layer is added on top.

## Core decision

```text
SMC/SATS = source of truth for structure, OB, FVG, HTF POI, liquidity, SATS quality and execution context.
NCI Story = interpretation layer that explains the market story using 4H → 1H → 15M → 5M hierarchy.
```

## Why this path
The standalone NCI prototype successfully developed the story concept, but the key-level engine became unstable and sometimes selected weaker zones. The SMC/SATS system already identifies practical OB/FVG/POI zones better, so the NCI layer should read and explain those zones instead of rebuilding them.

## Build safety rule
Do not directly modify the stable SMC/SATS production file. Every test must be created as a candidate in this workspace first.

## First candidate goal

```text
master-smc-sats-nci-story-v0.1
```

The first candidate should only add:

```text
1. NCI story panel
2. 4H / 1H / 15M / 5M role explanation
3. NCI wording mapped from SMC/SATS zones
4. Optional toggle to show/hide NCI story layer
```

It must not change:

```text
1. Entries
2. Alerts
3. Risk logic
4. SATS filters
5. OB/FVG detection
6. Liquidity sweep logic
7. Existing SMC/SATS dashboard behaviour
```

## Required hierarchy

```text
4H master story
→ 1H explains 4H
→ 15M explains 1H
→ 5M execution/reaction monitor
```

The same verification model must repeat at each child layer.

## Issue tracker
See GitHub issue #46 for integration requirements.
