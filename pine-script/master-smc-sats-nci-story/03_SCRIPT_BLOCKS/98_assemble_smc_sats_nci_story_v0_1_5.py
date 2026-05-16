#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats-nci-story"
BASE = PROJECT / "03_CANDIDATES" / "master-smc-sats-nci-story-v0.1.4.pine"
SMART_BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "12_smart_validation_v0_1_5_min.pine"
OUT = PROJECT / "03_CANDIDATES" / "master-smc-sats-nci-story-v0.1.5.pine"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// MASTER SMC + SATS + NCI STORY CANDIDATE v0.1.5
// Base: v0.1.4.
// Added: Smart Validation Enhancer inspired by ICT Validated SMC.
// Purpose: validate 3-OK dashboard alignment with HTF bias, candle close, sweep,
// impulse/FVG, SATS quality, cooldown, score, labels and smart panel.
// Safety: existing SMC/SATS/NCI story logic is preserved; this is an additive layer.
// ══════════════════════════════════════════════════════════════════════════════
"""


def count_active(text: str, token: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def main():
    if not BASE.exists():
        raise RuntimeError(f"Missing base: {BASE}")
    if not SMART_BLOCK.exists():
        raise RuntimeError(f"Missing smart block: {SMART_BLOCK}")

    c = BASE.read_text(encoding="utf-8")
    block = SMART_BLOCK.read_text(encoding="utf-8")

    if count_active(block, "//@version") != 0 or count_active(block, "indicator(") != 0:
        raise RuntimeError("Smart block must not contain active version or indicator")

    c = c.replace("MASTER SMC + SATS + NCI STORY CANDIDATE v0.1.4", "MASTER SMC + SATS + NCI STORY CANDIDATE v0.1.5", 1)
    c = c.replace("// Base: existing SMC/SATS engine.", "// Base: existing SMC/SATS engine. v0.1.5 adds smart validation.", 1)
    c = c.replace("// Safety rule: no entry, risk, SATS, OB/FVG drawing, or liquidity logic changes.", "// Safety rule: smart validation is additive; core entry/risk/SATS/SMC logic preserved.", 1)
    if "// Rebuild Version:" in c:
        c = c.replace("// Rebuild Version:", NOTE + "\n// Rebuild Version:", 1)
    else:
        c = NOTE + "\n" + c

    c = c.rstrip() + "\n\n" + block.rstrip() + "\n"

    if count_active(c, "//@version") != 1:
        raise RuntimeError("Candidate must contain exactly one //@version")
    if count_active(c, "indicator(") != 1:
        raise RuntimeError("Candidate must contain exactly one indicator declaration")
    for required in [
        "v0.1.5",
        "nciV15BuySignal",
        "nciV15SellSignal",
        "NCI v0.1.5 Validated BUY",
        "NCI v0.1.5 Validated SELL",
        "nciV15BuyScore",
        "nciV15SellScore",
        "nciBuyThreeOkAlert",
        "nciSellThreeOkAlert",
    ]:
        if required not in c:
            raise RuntimeError(f"Missing required content: {required}")
    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(c, encoding="utf-8")
    print(f"Created candidate: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
