# SMC/SATS → NCI Story Integration Map

## Architecture

```text
Existing SMC/SATS engine
    ↓
Existing OB/FVG/HTF POI/liquidity/SATS variables
    ↓
NCI Story Mapper
    ↓
NCI Story Panel + optional compact labels
```

## Core rule
NCI must not create a competing key-level engine in this path. It must read the zones and context already detected by SMC/SATS and translate them into NCI storytelling.

## Required timeframe story

```text
4H = master market story
1H = explains / refines 4H
15M = explains / reacts inside 1H
5M = execution reaction monitor
```

## Mapping table

| SMC/SATS concept | NCI Story concept | Notes |
|---|---|---|
| HTF1 / HTF2 bias | 4H / 1H directional pressure | Use existing bias, do not recalculate unless missing. |
| HTF OB | Parent key-level candidate | OB is a structural zone. NCI decides story wording. |
| HTF FVG | Imbalance / reaction candidate | FVG can be used as reaction area or confirmation. |
| Nearest HTF POI | Active parent decision zone | Used to define whether price is inside supply/demand/range. |
| Current TF OB/FVG | Execution zone | Used for 5M monitoring, not automatic entry. |
| Sweep / reclaim | Liquidity confirmation | Supports NCI reaction/reversal story. |
| SATS TQI / ER | Trend quality / energy | Used to describe confidence, not to force NCI zones. |
| Mitigated zone | Weakened KL | Should not be treated as fresh. |
| Broken zone | Obsolete KL | Hidden from active story unless debug is enabled. |

## NCI Story states

```text
4H SUPPLY STORY ACTIVE
4H DEMAND STORY ACTIVE
4H SUPPLY DECISION ACTIVE
4H DEMAND DECISION ACTIVE
4H RANGE / DECISION STORY
4H BREAKOUT / BREAKDOWN WATCH
```

## Role wording

```text
1H aligns with 4H
1H pullback against 4H
1H decision inside 4H
15M explains 1H
15M counter-move / pullback
5M execution aligns
5M reaction monitor
```

## Execution wording

```text
EXEC WAIT: HTF story not clear
EXEC WAIT: 1H not aligned
EXEC WAIT: 15M not aligned
EXEC WATCH: 5M supply reaction
EXEC WATCH: 5M demand reaction
EXEC ALIGNED: monitor reaction, not a signal
```

## Safety checks before code merge

1. SMC/SATS entries must remain unchanged.
2. Alerts must remain unchanged.
3. Risk/SL/TP must remain unchanged.
4. Existing OB/FVG detection must remain unchanged.
5. NCI story must be optional.
6. No extra heavy boxes by default.
7. Mobile panel must be readable.
8. Story must not contradict SMC/SATS dashboard.

## Recommended first build

Create one candidate copied from the latest stable/confirmed SMC/SATS script. Then add only a small NCI story section:

```text
1. Inputs: Show NCI Story, Panel Position, Panel Detail
2. Mapper functions: NCI final story, role text, execution text
3. Table panel only
4. No new zones yet
```

## Future build after v0.1

```text
v0.2: Add compact labels from NCI story.
v0.3: Add NCI scoring using existing SMC/SATS zones.
v0.4: Add NCI mode presets.
v1.0: Promote if stable on BTC, XAUUSD, NAS100, 4H/1H/15M/5M/3M/1M.
```
