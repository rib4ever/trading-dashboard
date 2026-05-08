#!/usr/bin/env python3
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
ASSEMBLER_V18 = PROJECT / "03_SCRIPT_BLOCKS" / "98_assemble_v1_8_fibonacci_poi_candidate.py"
V18_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.8-fibonacci-poi-candidate.pine"
PV_BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "12_premium_visual_hierarchy_engine.pine"
V19_OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.9-premium-visual-candidate.pine"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// v1.9 PREMIUM VISUAL HIERARCHY CANDIDATE NOTE
// Built from v1.8 Fibonacci POI candidate.
// Adds visual hierarchy controls and premium Fibonacci/POI presentation.
// This candidate must not affect entries, alerts, risk, SMC, or SATS logic.
// Test in TradingView before promotion.
// ══════════════════════════════════════════════════════════════════════════════
"""

PV_INSERT_MARKER = "// ══════════════════════════════════════════════════════════════════════════════\n// 11 FIBONACCI POI VISUAL ENGINE — BLOCK VERSION"

OLD_FIB_LINES = """        if fibShowFibLines
            fibLine0 := line.new(x1, fib0, x2, fib0, color = color.new(fibLineColor, 20), style = line.style_solid, width = 1)
            fibLine618 := line.new(x1, fib618, x2, fib618, color = fibLineColor, style = line.style_dashed, width = 1)
            fibLine705 := line.new(x1, fib705, x2, fib705, color = color.new(themeWarning, 0), style = line.style_solid, width = 2)
            fibLine786 := line.new(x1, fib786, x2, fib786, color = fibLineColor, style = line.style_dashed, width = 1)
            fibLine800 := line.new(x1, fib800, x2, fib800, color = fibLineColor, style = line.style_dashed, width = 1)
            fibLine100 := line.new(x1, fib100, x2, fib100, color = color.new(fibLineColor, 20), style = line.style_solid, width = 1)
"""

NEW_FIB_LINES = """        if fibShowFibLines
            if pvShowFibFullLines
                fibLine0 := line.new(x1, fib0, x2, fib0, color = pvMutedLine, style = line.style_solid, width = 1)
                fibLine100 := line.new(x1, fib100, x2, fib100, color = pvMutedLine, style = line.style_solid, width = 1)
            if pvShowFibKeyLines
                fibLine618 := line.new(x1, fib618, x2, fib618, color = color.new(fibLineColor, pvIsClean ? 55 : 35), style = line.style_dashed, width = 1)
                fibLine786 := line.new(x1, fib786, x2, fib786, color = color.new(fibLineColor, pvIsClean ? 55 : 35), style = line.style_dashed, width = 1)
                fibLine800 := line.new(x1, fib800, x2, fib800, color = color.new(fibLineColor, pvIsClean ? 65 : 45), style = line.style_dotted, width = 1)
            fibLine705 := line.new(x1, fib705, x2, fib705, color = pvPoiBorder, style = line.style_solid, width = pvFibLineWidthMain)
"""

REPLACEMENTS = [
    (
        'color fibBoxColor = color.new(fibBaseColor, 84)\n        color fibBoxBorder = color.new(fibBaseColor, 30)',
        'color fibBoxColor = pvFibBandBg\n        color fibBoxBorder = pvFibBandBorder'
    ),
    (
        'fibRetracementBox := box.new(x1, fibZoneTop, x2, fibZoneBottom, bgcolor = fibBoxColor, border_color = fibBoxBorder, text = "Fib POI 61.8%-80%", text_color = fibLineColor, text_size = size.tiny)',
        'fibRetracementBox := box.new(x1, fibZoneTop, x2, fibZoneBottom, bgcolor = fibBoxColor, border_color = fibBoxBorder, text = pvLabelsMinimal ? "" : "FIB POI 61.8-80", text_color = fibLineColor, text_size = size.tiny, text_halign = text.align_left)'
    ),
    (
        'color poiBg = color.new(themeWarning, 78)\n            color poiBorder = color.new(themeWarning, 0)',
        'color poiBg = pvPoiBg\n            color poiBorder = pvPoiBorder'
    ),
    (
        'fibPoiBox := box.new(bar_index - fibEffectiveLookback, math.max(fibBestPoiTop, fibBestPoiBottom), x2, math.min(fibBestPoiTop, fibBestPoiBottom), bgcolor = poiBg, border_color = poiBorder, text = "STRONG POI", text_color = poiBorder, text_size = size.small)',
        'fibPoiBox := box.new(bar_index - math.min(fibEffectiveLookback, 80), math.max(fibBestPoiTop, fibBestPoiBottom), x2, math.min(fibBestPoiTop, fibBestPoiBottom), bgcolor = poiBg, border_color = poiBorder, border_width = pvPoiBorderWidth, text = pvIsClean ? "POI" : "STRONG POI", text_color = poiBorder, text_size = pvLabelSizeTiny, text_halign = text.align_left)'
    ),
    (
        'fibPoiLabel := label.new(x2, (fibBestPoiTop + fibBestPoiBottom) / 2.0, "Fib POI\\n" + dirTxt + "\\n" + fibBestPoiType + "\\nScore " + str.tostring(fibBestPoiScore, "#.0"), style = label.style_label_left, color = poiBorder, textcolor = themePanelText, size = size.small)',
        'fibPoiLabel := label.new(x2, (fibBestPoiTop + fibBestPoiBottom) / 2.0, pvCompactPoiLabel ? "Fib POI • " + (fibBullMode ? "BUY" : "SELL") + "\\n" + fibBestPoiType + " • " + str.tostring(fibBestPoiScore, "#.0") : "Fib POI\\n" + dirTxt + "\\n" + fibBestPoiType + "\\nScore " + str.tostring(fibBestPoiScore, "#.0"), style = label.style_label_left, color = poiBorder, textcolor = themePanelText, size = pvLabelSizeTiny)'
    ),
    (
        'fibDirLabel := label.new(x2, fib705, fibBullMode ? "Bull Fib 70.5%" : "Bear Fib 70.5%", style = label.style_label_left, color = color.new(fibLineColor, 15), textcolor = themePanelText, size = size.tiny)',
        'fibDirLabel := pvLabelsMinimal ? na : label.new(x2, fib705, fibBullMode ? "70.5% Bull Fib" : "70.5% Bear Fib", style = label.style_label_left, color = color.new(pvPoiBorder, 15), textcolor = themePanelText, size = size.tiny)'
    ),
]


def count_active(text, token):
    return sum(1 for line in text.splitlines() if line.strip().startswith(token))


def main():
    runpy.run_path(str(ASSEMBLER_V18), run_name="__main__")
    c = V18_OUT.read_text(encoding="utf-8")
    pv = PV_BLOCK.read_text(encoding="utf-8")

    if count_active(pv, "//@version") != 0 or count_active(pv, "indicator(") != 0:
        raise RuntimeError("Premium visual block must remain isolated: no active version or indicator")

    c = c.replace("// v1.8 FIBONACCI POI VISUAL ENGINE CANDIDATE NOTE", NOTE + "\n// v1.8 FIBONACCI POI VISUAL ENGINE CANDIDATE NOTE", 1)

    if PV_INSERT_MARKER not in c:
        raise RuntimeError("Could not find Fibonacci block marker for premium visual insertion")
    c = c.replace(PV_INSERT_MARKER, pv.rstrip() + "\n\n" + PV_INSERT_MARKER, 1)

    if OLD_FIB_LINES not in c:
        raise RuntimeError("Could not find original Fibonacci line drawing block")
    c = c.replace(OLD_FIB_LINES, NEW_FIB_LINES, 1)

    for old, new in REPLACEMENTS:
        if old not in c:
            raise RuntimeError(f"Could not find visual replacement target: {old[:80]}")
        c = c.replace(old, new, 1)

    c = c.replace("// End of Master SMC + SATS Sniper System v1.8 FIBONACCI POI CANDIDATE", "// End of Master SMC + SATS Sniper System v1.9 PREMIUM VISUAL HIERARCHY CANDIDATE")

    if count_active(c, "//@version") != 1 or count_active(c, "indicator(") != 1:
        raise RuntimeError("v1.9 candidate must contain one active version and one indicator")
    for required in ["13 Premium Visual Hierarchy", "pvMode", "pvPoiAccent", "pvFibBandBg", "12 Fibonacci POI Visual Engine", "showFibPoiEngine", "entryWorkflowMode"]:
        if required not in c:
            raise RuntimeError(f"v1.9 candidate missing required content: {required}")
    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    V19_OUT.parent.mkdir(parents=True, exist_ok=True)
    V19_OUT.write_text(c, encoding="utf-8")
    print(f"Created v1.9 premium visual candidate: {V19_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
