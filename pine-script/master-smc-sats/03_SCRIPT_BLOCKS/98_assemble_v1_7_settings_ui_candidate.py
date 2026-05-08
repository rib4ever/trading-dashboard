#!/usr/bin/env python3
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
ASSEMBLER_V16 = PROJECT / "03_SCRIPT_BLOCKS" / "98_assemble_v1_6_theme_candidate.py"
V16_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine"
V17_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.7-settings-ui-cleanup-candidate.pine"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// v1.7 SETTINGS UI CLEANUP CANDIDATE NOTE
// Built from v1.6 candidate.
// This pass reorganizes TradingView settings groups and labels only.
// It should not change entry logic, SMC logic, SATS logic, risk logic, or alerts.
// Test in TradingView before promotion.
// ══════════════════════════════════════════════════════════════════════════════
"""

REPLACEMENTS = [
    ('GRP_MASTER = "🎯 Master Sniper Presets"', 'GRP_MASTER = "01 Quick Start / Master Preset"'),
    ('GRP_SMC    = "🏦 SMC Engine"', 'GRP_SMC    = "05 SMC Engine / Bias Timeframes"'),
    ('GRP_SATS   = "🧠 SATS Trend Quality Engine"', 'GRP_SATS   = "06 SATS Trend Quality Engine"'),
    ('GRP_RISK   = "🎯 Risk / TP / SL"', 'GRP_RISK   = "10 Risk / TP / SL"'),
    ('GRP_VIS    = "🎨 Visuals"', 'GRP_VIS    = "09 Visual Display"'),
    ('GRP_HTFLVL = "🧭 HTF Key Levels"', 'GRP_HTFLVL = "07 HTF Key Levels"'),
    ('GRP_ALERT  = "🔔 Alerts"', 'GRP_ALERT  = "11 Alerts"'),
    ('GRP_THEME = "Theme Engine"', 'GRP_THEME = "02 Theme Engine / Chart Colors"'),
    ('GRP_SK = "🧭 Smart Key Levels / Liquidity"', 'GRP_SK = "08 Smart Key Levels / Liquidity"'),
    ('GRP_ENTRY = "🚦 Entry Workflow"', 'GRP_ENTRY = "04 Entry Workflow"'),

    ('"Manual Bull"', '"Manual Theme Bull"'),
    ('"Manual Bear"', '"Manual Theme Bear"'),
    ('"Manual Neutral"', '"Manual Theme Neutral"'),
    ('"Manual SL"', '"Manual Theme SL"'),
    ('"Manual TP"', '"Manual Theme TP"'),

    ('"Manual Min TQI"', '"Advanced Manual Min TQI"'),
    ('"Manual Ultra TQI"', '"Advanced Manual Ultra TQI"'),
    ('"Manual Min ER"', '"Advanced Manual Min ER"'),
    ('"Manual: Killzone Only"', '"Advanced Manual: Killzone Only"'),
    ('"Manual: Sweep Mandatory"', '"Advanced Manual: Sweep Mandatory"'),
    ('"Manual: Block LOW / VERY LOW Volume"', '"Advanced Manual: Block Low Volume"'),
    ('"Manual: Block LOW Volatility"', '"Advanced Manual: Block Low Volatility"'),
    ('"Manual: SATS Confirmation Lookback"', '"Advanced Manual: SATS Confirmation Lookback"'),

    ('"Show Mini Status Panel"', '"Show Status Panel"'),
    ('"Mini Status Position"', '"Status Panel Position"'),
    ('"Show Entry / SL / TP Lines"', '"Show Entry, SL and TP Lines"'),
    ('"OB: Show Last"', '"Order Blocks: Show Last"'),
    ('"FVG: Show Last"', '"FVGs: Show Last"'),
    ('"HTF Key Level 1"', '"HTF Key Timeframe 1"'),
    ('"HTF Key Level 2"', '"HTF Key Timeframe 2"'),
    ('"HTF 1 Color"', '"HTF Level 1 Color"'),
    ('"HTF 2 Color"', '"HTF Level 2 Color"'),
    ('"Require Existing Key Level Touch Before Entry"', '"Require Key-Level Touch Before Entry"'),
    ('"Smart Cluster / Touch Tolerance xATR"', '"Smart Cluster Tolerance xATR"'),
    ('"Smart Current Candle Touch Buffer xATR"', '"Smart Touch Buffer xATR"'),
    ('"Use Smart Levels For TP Liquidity"', '"Use Smart Levels For TP Liquidity Later"'),
]


def count_active(text, token):
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def main():
    runpy.run_path(str(ASSEMBLER_V16), run_name="__main__")
    c = V16_OUT.read_text(encoding="utf-8")
    c = c.replace("// v1.6 THEME ENGINE CANDIDATE NOTE", NOTE + "\n// v1.6 THEME ENGINE CANDIDATE NOTE", 1)
    for old, new in REPLACEMENTS:
        c = c.replace(old, new)
    c = c.replace("// End of Master SMC + SATS Sniper System v1.6 THEME ENGINE CANDIDATE", "// End of Master SMC + SATS Sniper System v1.7 SETTINGS UI CLEANUP CANDIDATE")

    if count_active(c, "//@version") != 1 or count_active(c, "indicator(") != 1:
        raise RuntimeError("v1.7 candidate must contain one active version and one indicator")
    for required in ["01 Quick Start / Master Preset", "02 Theme Engine / Chart Colors", "04 Entry Workflow", "09 Visual Display", "entryWorkflowMode", "themePreset", "smartAnyKeyTouched"]:
        if required not in c:
            raise RuntimeError(f"v1.7 candidate missing required content: {required}")
    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    V17_OUT.parent.mkdir(parents=True, exist_ok=True)
    V17_OUT.write_text(c, encoding="utf-8")
    print(f"Created v1.7 settings UI candidate: {V17_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
