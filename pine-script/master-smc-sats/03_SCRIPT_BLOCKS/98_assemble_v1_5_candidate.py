#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
BASE = PROJECT / "01_BASE_WORKING_VERSION" / "master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine"
BLOCK = PROJECT / "03_SCRIPT_BLOCKS" / "06_smart_key_level_engine.pine"
OUT = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine"

ZONE_MARK = "// ══════════════════════════════════════════════════════════════════════════════\n// ZONE + KEY LEVEL CONFLUENCE\n// ══════════════════════════════════════════════════════════════════════════════"
ALERT_MARK = "// ══════════════════════════════════════════════════════════════════════════════\n// ALERTS\n// ══════════════════════════════════════════════════════════════════════════════"
STATUS_MARK = "// Mini status label"

NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// v1.5 CANDIDATE NOTE
// Built from protected v1.4 base plus isolated smart key-level block.
// Smart levels are current-chart-timeframe pivot clusters.
// Mini status panel has selectable placement.
// Test in TradingView before promotion to compiled master.
// ══════════════════════════════════════════════════════════════════════════════
"""

STATUS_PANEL = '''// Mini status panel
var label statusLabel = na
var table statusTopRight = table.new(position.top_right, 1, 1)
var table statusTopLeft = table.new(position.top_left, 1, 1)
var table statusBottomRight = table.new(position.bottom_right, 1, 1)
var table statusBottomLeft = table.new(position.bottom_left, 1, 1)

clearStatusTable(table t) =>
    table.cell(t, 0, 0, "", text_color = color.new(color.white, 100), bgcolor = color.new(color.black, 100), text_size = size.small)

drawStatusTable(table t, string s) =>
    table.cell(t, 0, 0, s, text_color = color.white, bgcolor = color.new(color.black, 20), text_size = size.small, text_halign = text.align_left)

if barstate.islast
    label.delete(statusLabel)
    clearStatusTable(statusTopRight)
    clearStatusTable(statusTopLeft)
    clearStatusTable(statusBottomRight)
    clearStatusTable(statusBottomLeft)
    if showMiniStatus
        biasTxt = htfBullishBias ? "Bull" : htfBearishBias ? "Bear" : "Neutral"
        statusTxt = "Preset: " + masterPreset +
          "\\nBias: " + biasTxt + " (" + str.tostring(biasPct, "#.0") + "%)" +
          "\\nKZ: " + killzoneName + " | " + (killzoneAllowed ? "OK" : "BLOCK") + (effectiveKillzoneOnly and killzoneName == "NO KILLZONE" and not allowNoKz ? " - enable Allow NO KILLZONE" : "") +
          "\\nTQI: " + str.tostring(tqi, "#.00") + " / " + str.tostring(effectiveMinTqi, "#.00") +
          "\\nER: " + str.tostring(erValue, "#.00") + " / " + str.tostring(effectiveMinEr, "#.00") +
          "\\nVol: " + volumeState + " | ATR: " + volatilityState +
          "\\nHTF POI B/S: " + (htfBullPoiContext ? "B ok" : "B x") + " / " + (htfBearPoiContext ? "S ok" : "S x") +
          "\\nExec Zone B/S: " + (executionBullZoneOk ? "B ok" : "B x") + " / " + (executionBearZoneOk ? "S ok" : "S x") +
          "\\nKey Touch: " + (anyExistingKeyLevelTouched ? "YES" : "NO") + " | B/S " + (bullKeyReaction ? "B ok" : "B x") + "/" + (bearKeyReaction ? "S ok" : "S x")
        if miniStatusPosition == "Top Right"
            drawStatusTable(statusTopRight, statusTxt)
        else if miniStatusPosition == "Top Left"
            drawStatusTable(statusTopLeft, statusTxt)
        else if miniStatusPosition == "Bottom Right"
            drawStatusTable(statusBottomRight, statusTxt)
        else if miniStatusPosition == "Bottom Left"
            drawStatusTable(statusBottomLeft, statusTxt)
        else
            statusLabel := label.new(bar_index + 2, close, statusTxt, style = label.style_label_left, color = color.new(color.black, 20), textcolor = color.white, size = size.small)'''

OB_OLD = '''    obCount = currTfOBs.size()
    for i = 0 to obCount - 1
        ob = currTfOBs.get(i)
        obColor = ob.dir > 0 ? color.new(bullColor, 82) : color.new(bearColor, 82)
        obBorder = ob.dir > 0 ? bullColor : bearColor
        newBox = box.new(left = ob.barIdx, top = ob.top, right = bar_index + obExtend, bottom = ob.bottom, border_color = obBorder, border_width = 1, bgcolor = obColor, text = ob.dir > 0 ? "OB ↑" : "OB ↓", text_color = obBorder, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
        obBoxes.unshift(newBox)'''

OB_NEW = '''    obCount = currTfOBs.size()
    if obCount > 0
        for i = 0 to obCount - 1
            ob = currTfOBs.get(i)
            obColor = ob.dir > 0 ? color.new(bullColor, 82) : color.new(bearColor, 82)
            obBorder = ob.dir > 0 ? bullColor : bearColor
            newBox = box.new(left = ob.barIdx, top = ob.top, right = bar_index + obExtend, bottom = ob.bottom, border_color = obBorder, border_width = 1, bgcolor = obColor, text = ob.dir > 0 ? "OB ↑" : "OB ↓", text_color = obBorder, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
            obBoxes.unshift(newBox)'''

FVG_OLD = '''    fvgCount = currTfFvgs.size()
    for i = 0 to fvgCount - 1
        fvg = currTfFvgs.get(i)
        fvgBg = fvg.dir > 0 ? color.new(bullColor, 87) : color.new(bearColor, 87)
        fvgBorder = fvg.dir > 0 ? color.new(bullColor, 60) : color.new(bearColor, 60)
        fvgTxt = fvg.dir > 0 ? bullColor : bearColor
        newBox = box.new(left = fvg.barIdx, top = fvg.top, right = bar_index + fvgExtend, bottom = fvg.bottom, bgcolor = fvgBg, border_width = 1, border_style = line.style_dashed, border_color = fvgBorder, text = fvg.dir > 0 ? "FVG ↑" : "FVG ↓", text_color = fvgTxt, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
        fvgBoxes.unshift(newBox)'''

FVG_NEW = '''    fvgCount = currTfFvgs.size()
    if fvgCount > 0
        for i = 0 to fvgCount - 1
            fvg = currTfFvgs.get(i)
            fvgBg = fvg.dir > 0 ? color.new(bullColor, 87) : color.new(bearColor, 87)
            fvgBorder = fvg.dir > 0 ? color.new(bullColor, 60) : color.new(bearColor, 60)
            fvgTxt = fvg.dir > 0 ? bullColor : bearColor
            newBox = box.new(left = fvg.barIdx, top = fvg.top, right = bar_index + fvgExtend, bottom = fvg.bottom, bgcolor = fvgBg, border_width = 1, border_style = line.style_dashed, border_color = fvgBorder, text = fvg.dir > 0 ? "FVG ↑" : "FVG ↓", text_color = fvgTxt, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
            fvgBoxes.unshift(newBox)'''


def must(text, old, new, name):
    if old not in text:
        raise RuntimeError(f"Missing marker: {name}")
    return text.replace(old, new, 1)


def replace_between(text, start, end, new):
    a = text.find(start)
    b = text.find(end, a)
    if a < 0 or b < 0:
        raise RuntimeError("Missing status section markers")
    return text[:a] + new.rstrip() + "\n\n" + text[b:]


def counts(text):
    v = i = 0
    for line in (x.strip() for x in text.splitlines()):
        if line.startswith("//@version"):
            v += 1
        elif line and not line.startswith("//") and line.startswith("indicator("):
            i += 1
    return v, i


def main():
    base = BASE.read_text(encoding="utf-8")
    block = BLOCK.read_text(encoding="utf-8")
    if not base.startswith("//@version=6"):
        raise RuntimeError("Base must start with //@version=6")
    if counts(block) != (0, 0):
        raise RuntimeError("Smart block must stay isolated: no active version or indicator")

    c = base
    c = must(c, "// ══════════════════════════════════════════════════════════════════════════════\n// GROUPS", NOTE + "\n// ══════════════════════════════════════════════════════════════════════════════\n// GROUPS", "groups")
    c = must(c, 'showMiniStatus     = input.bool(true, "Show Mini Status Label", group = GRP_VIS)', 'showMiniStatus     = input.bool(true, "Show Mini Status Panel", group = GRP_VIS)\nminiStatusPosition = input.string("Right of Price", "Mini Status Position", options = ["Right of Price", "Top Right", "Top Left", "Bottom Right", "Bottom Left"], group = GRP_VIS)', "mini input")
    c = must(c, ZONE_MARK, block.rstrip() + "\n\n" + ZONE_MARK, "insert smart block")

    c = c.replace('smartKeyPreferStrongest = input.bool(true,  "Prefer Strongest Level", group = GRP_SK)', 'smartKeySourceInfo      = input.string("Chart timeframe", "Smart Level Source TF", options = ["Chart timeframe"], group = GRP_SK)\nsmartKeySelectionMode   = input.string("Nearest", "Smart Level Selection", options = ["Nearest", "Strongest"], group = GRP_SK)')
    c = c.replace('float score = smartKeyPreferStrongest ? hits * 10.0 + recency - distAtr * 0.05 : -distAtr + hits * 0.25', 'float score = smartKeySelectionMode == "Strongest" ? hits * 10.0 + recency - distAtr * 0.05 : -distAtr + hits * 0.10 + recency * 0.05')
    c = must(c, 'anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched', 'anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched or smartAnyKeyTouched', "smart key hook")
    c = must(c, '     (k2_obNearDir == 1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == 1 and nearLevel(k2FvgLevel)))', '     (k2_obNearDir == 1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == 1 and nearLevel(k2FvgLevel)) or\n     smartBullKeyReaction)', "bull hook")
    c = must(c, '     (k2_obNearDir == -1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == -1 and nearLevel(k2FvgLevel)))', '     (k2_obNearDir == -1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == -1 and nearLevel(k2FvgLevel)) or\n     smartBearKeyReaction)', "bear hook")
    c = must(c, OB_OLD, OB_NEW, "OB guarded visual block")
    c = must(c, FVG_OLD, FVG_NEW, "FVG guarded visual block")
    c = replace_between(c, STATUS_MARK, ALERT_MARK, STATUS_PANEL)
    c = c.replace("// End of Master SMC + SATS Sniper System v1.4", "// End of Master SMC + SATS Sniper System v1.5 SMART KEY LIQUIDITY CANDIDATE", 1)

    v, ind = counts(c)
    if (v, ind) != (1, 1):
        raise RuntimeError(f"Candidate must contain one active version and indicator. Found version={v}, indicator={ind}")
    for s in ["miniStatusPosition", "smartAnyKeyTouched", "if obCount > 0", "if fvgCount > 0"]:
        if s not in c:
            raise RuntimeError(f"Candidate missing required content: {s}")
    if "<!DOCTYPE html>" in c or "<html" in c:
        raise RuntimeError("Candidate contains HTML, not raw Pine")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(c, encoding="utf-8")
    print(f"Created candidate: {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
