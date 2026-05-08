#!/usr/bin/env python3
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
ASSEMBLER_V15 = PROJECT / "03_SCRIPT_BLOCKS" / "98_assemble_v1_5_candidate.py"
THEME_BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "09a_theme_engine.pine"
V15_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine"
V16_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine"

COLOR_START = "// ══════════════════════════════════════════════════════════════════════════════\n// COLORS\n// ══════════════════════════════════════════════════════════════════════════════"
COLOR_END = "// ══════════════════════════════════════════════════════════════════════════════\n// MASTER PRESETS\n// ══════════════════════════════════════════════════════════════════════════════"

STATUS_OLD = "text_color = color.white, bgcolor = color.new(color.black, 20)"
STATUS_NEW = "text_color = themePanelText, bgcolor = themePanelBg"
FLOATING_OLD = "color = color.new(color.black, 20), textcolor = color.white"
FLOATING_NEW = "color = themePanelBg, textcolor = themePanelText"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// v1.6 THEME ENGINE CANDIDATE NOTE
// Built from v1.5 candidate plus 09a_theme_engine.pine.
// Theme engine changes visual colors only and should not affect entry logic.
// Test in TradingView before promotion to compiled master.
// ══════════════════════════════════════════════════════════════════════════════
"""


def replace_between(text, start, end, new):
    a = text.find(start)
    b = text.find(end, a)
    if a < 0 or b < 0:
        raise RuntimeError("Missing color section markers")
    return text[:a] + new.rstrip() + "\n\n" + text[b:]


def count_active(text, token):
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def main():
    runpy.run_path(str(ASSEMBLER_V15), run_name="__main__")

    candidate = V15_OUT.read_text(encoding="utf-8")
    theme = THEME_BLOCK.read_text(encoding="utf-8")

    if count_active(theme, "//@version") != 0 or count_active(theme, "indicator(") != 0:
        raise RuntimeError("Theme block must remain isolated: no active version or indicator")

    themed_color_section = COLOR_START + "\n" + theme.rstrip()
    c = replace_between(candidate, COLOR_START, COLOR_END, themed_color_section)

    c = c.replace("// v1.5 CANDIDATE NOTE", NOTE + "\n// v1.5 CANDIDATE NOTE", 1)
    c = c.replace(STATUS_OLD, STATUS_NEW)
    c = c.replace(FLOATING_OLD, FLOATING_NEW)
    c = c.replace("// End of Master SMC + SATS Sniper System v1.5 SMART KEY LIQUIDITY + ENTRY WORKFLOW CANDIDATE", "// End of Master SMC + SATS Sniper System v1.6 THEME ENGINE CANDIDATE")

    if count_active(c, "//@version") != 1 or count_active(c, "indicator(") != 1:
        raise RuntimeError("v1.6 candidate must contain one active version and one indicator")
    for required in ["themePreset", "themeBaseBull", "bullColor = themeBaseBull", "themePanelBg", "entryWorkflowMode", "smartAnyKeyTouched"]:
        if required not in c:
            raise RuntimeError(f"v1.6 candidate missing required content: {required}")
    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    V16_OUT.parent.mkdir(parents=True, exist_ok=True)
    V16_OUT.write_text(c, encoding="utf-8")
    print(f"Created v1.6 theme candidate: {V16_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
