#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SMC = ROOT / "pine-script" / "master-smc-sats"
PROJECT = ROOT / "pine-script" / "master-smc-sats-nci-story"

BASE = SMC / "00_MASTER_COMPILED" / "master-smc-sats-ravi-custom-01-v1.7-CONFIRMED-WORKING.pine"
FALLBACK = SMC / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.9-premium-visual-candidate.pine"
NCI_BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "10_nci_story_layer_v0_1_1_compile_safe.pine"
OUT = PROJECT / "03_CANDIDATES" / "master-smc-sats-nci-story-v0.1.1.pine"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// MASTER SMC + SATS + NCI STORY CANDIDATE v0.1.1
// Base: existing SMC/SATS engine.
// Added: compile-safe NCI story layer as optional panel only.
// Safety rule: no entry, alert, risk, SATS, OB/FVG, or liquidity logic changes.
// ══════════════════════════════════════════════════════════════════════════════
"""


def count_active(text: str, token: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def main():
    source = BASE if BASE.exists() else FALLBACK
    if not source.exists():
        raise RuntimeError("No SMC/SATS base candidate found")
    c = source.read_text(encoding="utf-8")
    block = NCI_BLOCK.read_text(encoding="utf-8")

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
        "showNciStoryLayer",
        "nciFinalStory",
        "COMPILE-SAFE",
    ]:
        if required not in c:
            raise RuntimeError(f"Candidate missing required content: {required}")

    # These are intentionally forbidden in v0.1.1 because they caused compile errors in v0.1.
    for forbidden in [
        " = bias",
        "htfPoiBullOk",
        "htfPoiBearOk",
        "bullZoneOk",
        "bearZoneOk",
        "str.tostring(tqi",
        "str.tostring(er",
    ]:
        if forbidden in c:
            raise RuntimeError(f"Candidate still contains unsafe assumed variable: {forbidden}")

    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(c, encoding="utf-8")
    print(f"Created candidate: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
