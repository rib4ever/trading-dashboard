# NCI Source of Truth Rules

## Core rule

All NCI Pine Script logic must be based on:

1. Ravi's Google Drive NCI documents.
2. Ravi's direct clarification or approval.

No important trading logic should be invented from general trading knowledge.

## Strictly prohibited

Do not add generic trading assumptions unless Ravi confirms them.

Do not mix external SMC, ICT, support/resistance, order block, or liquidity logic into the NCI indicator unless the NCI documents support it or Ravi approves it.

Do not copy logic from the SMC + SATS project into the NCI project unless it is only project-structure workflow, debugging structure, or GitHub organization method.

## Most important NCI modules

The following modules must be built strictly from NCI standards:

```text
Market Structure
Market Cycle
Key Levels
Internal Structure
Pullback Wave
Pulse Wave
Breakout Standard
Pullback Standard
Supply and Demand Zones
Strongest SD Zones
Obsolete SD Zones
```

## Market Structure rule

Market Structure must follow the NCI method, not generic HH/HL/LH/LL logic alone.

Generic swing labels may be used as technical helpers only, but the final structure state must respect NCI rules such as:

- Pulse wave
- Pullback wave
- Internal structure
- Key level
- Valid breakout
- Trend started / trend finished logic
- Market cycle context

## Key Level rule

Key levels must be drawn according to NCI standards.

The script must not randomly draw support/resistance lines and call them NCI key levels.

A valid NCI key level must be connected to NCI market structure and market cycle logic.

## Development rule

When a rule is unclear:

```text
STOP → Ask Ravi → Save clarification → Then implement
```

## Candidate merge rule

Before merging any Market Structure, Market Cycle, or Key Level module into the candidate master script, the rules must be checked against the NCI documents and/or confirmed by Ravi.
