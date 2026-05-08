#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
V17_CONFIRMED = PROJECT / "00_MASTER_COMPILED" / "master-smc-sats-ravi-custom-01-v1.7-CONFIRMED-WORKING.pine"
V17_CANDIDATE = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.7-settings-ui-cleanup-candidate.pine"
FIB_BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "11_fibonacci_poi_engine.pine"
V18_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.8-fibonacci-poi-candidate.pine"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// v1.8 FIBONACCI POI VISUAL ENGINE CANDIDATE NOTE
// Built from v1.7 confirmed working.
// Adds visual-only Fibonacci POI support.
// This candidate must not affect entries, alerts, risk, SMC, or SATS logic.
// Test in TradingView before promotion.
// ══════════════════════════════════════════════════════════════════════════════
"""

END_MARKERS = [
    "// End of Master SMC + SATS Sniper System v1.7 SETTINGS UI CLEANUP CANDIDATE",
    "// End of Master SMC + SATS Sniper System v1.6 THEME ENGINE CANDIDATE",
    "// End of Master SMC + SATS Sniper System v1.5 SMART KEY LIQUIDITY + ENTRY WORKFLOW CANDIDATE",
]


def count_active(text, token):
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def main():
    source = V17_CONFIRMED if V17_CONFIRMED.exists() else V17_CANDIDATE
    c = source.read_text(encoding="utf-8")
    fib = FIB_BLOCK.read_text(encoding="utf-8")

    if count_active(fib, "//@version") != 0 or count_active(fib, "indicator(") != 0:
        raise RuntimeError("Fib block must remain isolated: no active version or indicator")

    c = c.replace("// v1.7 SETTINGS UI CLEANUP CANDIDATE NOTE", NOTE + "\n// v1.7 SETTINGS UI CLEANUP CANDIDATE NOTE", 1)

    inserted = False
    for marker in END_MARKERS:
        if marker in c:
            c = c.replace(marker, fib.rstrip() + "\n\n// End of Master SMC + SATS Sniper System v1.8 FIBONACCI POI CANDIDATE", 1)
            inserted = True
            break
    if not inserted:
        c = c.rstrip() + "\n\n" + fib.rstrip() + "\n\n// End of Master SMC + SATS Sniper System v1.8 FIBONACCI POI CANDIDATE\n"

    if count_active(c, "//@version") != 1 or count_active(c, "indicator(") != 1:
        raise RuntimeError("v1.8 candidate must contain one active version and one indicator")
    for required in ["12 Fibonacci POI Visual Engine", "showFibPoiEngine", "fibPreset", "fibBestPoiScore", "Fib POI 61.8%-80%", "themeOBBull", "entryWorkflowMode"]:
        if required not in c:
            raise RuntimeError(f"v1.8 candidate missing required content: {required}")
    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    V18_OUT.parent.mkdir(parents=True, exist_ok=True)
    V18_OUT.write_text(c, encoding="utf-8")
    print(f"Created v1.8 Fibonacci POI candidate: {V18_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
