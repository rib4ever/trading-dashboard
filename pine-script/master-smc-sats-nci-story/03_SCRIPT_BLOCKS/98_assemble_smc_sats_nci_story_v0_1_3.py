#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SMC = ROOT / "pine-script" / "master-smc-sats"
PROJECT = ROOT / "pine-script" / "master-smc-sats-nci-story"

BASE = SMC / "00_MASTER_COMPILED" / "master-smc-sats-ravi-custom-01-v1.7-CONFIRMED-WORKING.pine"
FALLBACK = SMC / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.9-premium-visual-candidate.pine"
# v0.1.3 is a text-only wording patch generated from the stable v0.1.2 story block.
NCI_BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "10_nci_story_layer_v0_1_2_strong_ob_story.pine"
OUT = PROJECT / "03_CANDIDATES" / "master-smc-sats-nci-story-v0.1.3.pine"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// MASTER SMC + SATS + NCI STORY CANDIDATE v0.1.3
// Base: existing SMC/SATS engine.
// Added: easy-wording NCI story layer using strong supply/demand OB as main key levels.
// Safety rule: no entry, alert, risk, SATS, OB/FVG drawing, or liquidity logic changes.
// ══════════════════════════════════════════════════════════════════════════════
"""


def count_active(text: str, token: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def make_easy_wording(block: str) -> str:
    replacements = {
        "v0.1.2 STRONG OB STORY": "v0.1.3 EASY STORY",
        "v0.1.2": "v0.1.3",
        "NCI x SMC/SATS": "NCI Story",
        "Final": "Big Picture",
        "Key Source": "Main Levels",
        "4H Location": "Where Price Is",
        "Confidence": "Level Quality",
        "4H OB B/S": "4H Levels",
        "1H Role": "1H",
        "15M Role": "15M",
        "5M Role": "5M",
        "Execution": "Entry Watch",
        "Strong S/D OB": "Strong Buy/Sell OB",
        "SUPPLY DECISION STORY": "SELL AREA - wait reaction",
        "DEMAND DECISION STORY": "BUY AREA - wait reaction",
        "DEMAND STORY ACTIVE": "BUYERS IN CONTROL",
        "SUPPLY STORY ACTIVE": "SELLERS IN CONTROL",
        "RANGE / DECISION STORY": "WAIT - MARKET IN MIDDLE",
        "Inside strong supply OB": "Price is inside strong supply",
        "Inside strong demand OB": "Price is inside strong demand",
        "Between strong OBs": "Price is between supply and demand",
        "Working from strong demand OB": "Demand is controlling",
        "Working below strong supply OB": "Supply is controlling",
        "Building strong OB memory": "Waiting for strong level",
        "Strong OB story": "Strong level",
        "Valid OB story": "Good level",
        "Building / weak OB story": "Weak / building",
        " decision inside demand": ": inside buy area",
        " decision inside supply": ": inside sell area",
        " continues parent": ": same direction",
        " decision / range": ": waiting",
        " pullback against parent": ": pullback",
        " building": ": building",
        "EXEC WAIT: hierarchy not aligned": "WAIT: story not aligned",
        "EXEC WATCH: 5M demand OB reaction": "WATCH BUY: 5M demand",
        "EXEC WATCH: 5M supply OB reaction": "WATCH SELL: 5M supply",
        "EXEC WAIT: no 5M OB reaction": "WAIT: no clear 5M reaction",
    }
    for old, new in replacements.items():
        block = block.replace(old, new)
    return block


def main():
    source = BASE if BASE.exists() else FALLBACK
    if not source.exists():
        raise RuntimeError("No SMC/SATS base candidate found")

    c = source.read_text(encoding="utf-8")
    block = make_easy_wording(NCI_BLOCK.read_text(encoding="utf-8"))

    if count_active(block, "//@version") != 0 or count_active(block, "indicator(") != 0:
        raise RuntimeError("NCI story block must not contain active version or indicator declaration")

    if "// MASTER SMC + SATS SNIPER SYSTEM [Ravi Custom 01]" in c:
        c = c.replace("// MASTER SMC + SATS SNIPER SYSTEM [Ravi Custom 01]", "// MASTER SMC + SATS SNIPER SYSTEM [Ravi Custom 01]\n" + NOTE, 1)
    else:
        c = NOTE + "\n" + c

    c = c.rstrip() + "\n\n" + block.rstrip() + "\n"

    if count_active(c, "//@version") != 1:
        raise RuntimeError("Candidate must contain exactly one active //@version")
    if count_active(c, "indicator(") != 1:
        raise RuntimeError("Candidate must contain exactly one active indicator()")

    for required in [
        "MASTER SMC + SATS SNIPER SYSTEM",
        "requireHtfPoiContext",
        "SATS",
        "TQI",
        "NCI STORY LAYER",
        "NCI Story",
        "Big Picture",
        "Entry Watch",
        "v0.1.3",
    ]:
        if required not in c:
            raise RuntimeError(f"Candidate missing required content: {required}")

    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(c, encoding="utf-8")
    print(f"Created candidate: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
