#!/usr/bin/env python3
"""
Assemble Master SMC + SATS v1.5 Smart Key Liquidity Candidate.

Purpose
-------
This script safely builds a candidate Pine file from:
1. The protected v1.4 base working script.
2. The modular Block 06 Smart Key Level Engine.
3. The documented entry-confluence connection rules.
4. Runtime safety patches for empty visual arrays.

It does NOT edit the protected v1.4 base.
It writes a new candidate under 03_MASTER_CANDIDATES/.

Run from repository root:
    python pine-script/master-smc-sats/03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py

Then open the generated candidate file on GitHub, click Raw, and copy the raw Pine code into TradingView.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"

BASE_PATH = PROJECT / "01_BASE_WORKING_VERSION" / "master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine"
SMART_BLOCK_PATH = PROJECT / "03_SCRIPT_BLOCKS" / "06_smart_key_level_engine.pine"
OUT_PATH = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.5-smart-key-liquidity-candidate.pine"

INSERT_MARKER = "// ══════════════════════════════════════════════════════════════════════════════\n// ZONE + KEY LEVEL CONFLUENCE\n// ══════════════════════════════════════════════════════════════════════════════"

OLD_ANY_TOUCH = "anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched"
NEW_ANY_TOUCH = "anyExistingKeyLevelTouched = currentSwingKeyTouched or currentPdPwPmTouched or currentPoiTouched or htfKey1Touched or htfKey2Touched or smartAnyKeyTouched"

OLD_BULL_END = "     (k2_obNearDir == 1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == 1 and nearLevel(k2FvgLevel)))"
NEW_BULL_END = "     (k2_obNearDir == 1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == 1 and nearLevel(k2FvgLevel)) or\n     smartBullKeyReaction)"

OLD_BEAR_END = "     (k2_obNearDir == -1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == -1 and nearLevel(k2FvgLevel)))"
NEW_BEAR_END = "     (k2_obNearDir == -1 and nearLevel(k2ObLevel)) or\n     (k2_fvgNearDir == -1 and nearLevel(k2FvgLevel)) or\n     smartBearKeyReaction)"

OLD_OB_VISUAL_LOOP = """    obCount = currTfOBs.size()
    for i = 0 to obCount - 1
        ob = currTfOBs.get(i)
        obColor = ob.dir > 0 ? color.new(bullColor, 82) : color.new(bearColor, 82)
        obBorder = ob.dir > 0 ? bullColor : bearColor
        newBox = box.new(left = ob.barIdx, top = ob.top, right = bar_index + obExtend, bottom = ob.bottom, border_color = obBorder, border_width = 1, bgcolor = obColor, text = ob.dir > 0 ? "OB ↑" : "OB ↓", text_color = obBorder, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
        obBoxes.unshift(newBox)"""
NEW_OB_VISUAL_LOOP = """    obCount = currTfOBs.size()
    if obCount > 0
        for i = 0 to obCount - 1
            ob = currTfOBs.get(i)
            obColor = ob.dir > 0 ? color.new(bullColor, 82) : color.new(bearColor, 82)
            obBorder = ob.dir > 0 ? bullColor : bearColor
            newBox = box.new(left = ob.barIdx, top = ob.top, right = bar_index + obExtend, bottom = ob.bottom, border_color = obBorder, border_width = 1, bgcolor = obColor, text = ob.dir > 0 ? "OB ↑" : "OB ↓", text_color = obBorder, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
            obBoxes.unshift(newBox)"""

OLD_FVG_VISUAL_LOOP = """    fvgCount = currTfFvgs.size()
    for i = 0 to fvgCount - 1
        fvg = currTfFvgs.get(i)
        fvgBg = fvg.dir > 0 ? color.new(bullColor, 87) : color.new(bearColor, 87)
        fvgBorder = fvg.dir > 0 ? color.new(bullColor, 60) : color.new(bearColor, 60)
        fvgTxt = fvg.dir > 0 ? bullColor : bearColor
        newBox = box.new(left = fvg.barIdx, top = fvg.top, right = bar_index + fvgExtend, bottom = fvg.bottom, bgcolor = fvgBg, border_width = 1, border_style = line.style_dashed, border_color = fvgBorder, text = fvg.dir > 0 ? "FVG ↑" : "FVG ↓", text_color = fvgTxt, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
        fvgBoxes.unshift(newBox)"""
NEW_FVG_VISUAL_LOOP = """    fvgCount = currTfFvgs.size()
    if fvgCount > 0
        for i = 0 to fvgCount - 1
            fvg = currTfFvgs.get(i)
            fvgBg = fvg.dir > 0 ? color.new(bullColor, 87) : color.new(bearColor, 87)
            fvgBorder = fvg.dir > 0 ? color.new(bullColor, 60) : color.new(bearColor, 60)
            fvgTxt = fvg.dir > 0 ? bullColor : bearColor
            newBox = box.new(left = fvg.barIdx, top = fvg.top, right = bar_index + fvgExtend, bottom = fvg.bottom, bgcolor = fvgBg, border_width = 1, border_style = line.style_dashed, border_color = fvgBorder, text = fvg.dir > 0 ? "FVG ↑" : "FVG ↓", text_color = fvgTxt, text_halign = text.align_right, text_valign = text.align_center, text_size = size.small)
            fvgBoxes.unshift(newBox)"""

OLD_END_TAG = "// End of Master SMC + SATS Sniper System v1.4"
NEW_END_TAG = "// End of Master SMC + SATS Sniper System v1.5 SMART KEY LIQUIDITY CANDIDATE"

HEADER_NOTE = """// ══════════════════════════════════════════════════════════════════════════════
// v1.5 CANDIDATE NOTE
// Generated by 03_SCRIPT_BLOCKS/98_assemble_v1_5_candidate.py
// Source base: 01_BASE_WORKING_VERSION/master-smc-sats-ravi-custom-01-v1.4-LAST-WORKING.pine
// Added: 03_SCRIPT_BLOCKS/06_smart_key_level_engine.pine
// Connection: smart key-level hooks extend, not replace, v1.4 key reactions.
// Runtime safety: empty OB/FVG visual arrays are guarded before array.get().
// Test required in TradingView before promotion to 00_MASTER_COMPILED.
// ══════════════════════════════════════════════════════════════════════════════
"""


def must_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"Required replacement marker not found: {label}")
    return text.replace(old, new, 1)


def active_pine_header_counts(text: str) -> tuple[int, int]:
    """
    Count executable Pine headers.

    Important Pine detail:
    - //@version=6 is a Pine directive, even though it starts with //.
    - Normal comments must still be ignored.
    """
    version_count = 0
    indicator_count = 0
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("//@version"):
            version_count += 1
            continue
        if line.startswith("//"):
            continue
        if line.startswith("indicator("):
            indicator_count += 1
    return version_count, indicator_count


def has_active_directive_or_indicator(block: str) -> bool:
    version_count, indicator_count = active_pine_header_counts(block)
    return version_count > 0 or indicator_count > 0


def main() -> None:
    if not BASE_PATH.exists():
        raise FileNotFoundError(f"Base file not found: {BASE_PATH}")
    if not SMART_BLOCK_PATH.exists():
        raise FileNotFoundError(f"Smart block not found: {SMART_BLOCK_PATH}")

    base = BASE_PATH.read_text(encoding="utf-8")
    smart_block = SMART_BLOCK_PATH.read_text(encoding="utf-8")

    if not base.startswith("//@version=6"):
        raise RuntimeError("Base file does not start with //@version=6")
    if "indicator(" not in base[:1000]:
        raise RuntimeError("Base file does not appear to contain a Pine indicator declaration near the top")
    if has_active_directive_or_indicator(smart_block):
        raise RuntimeError("Smart block must not contain an executable //@version or indicator() declaration")

    candidate = base

    first_section = "// ══════════════════════════════════════════════════════════════════════════════\n// GROUPS"
    if first_section not in candidate:
        raise RuntimeError("Could not find GROUPS section marker for candidate note insertion")
    candidate = candidate.replace(first_section, HEADER_NOTE + "\n" + first_section, 1)

    if INSERT_MARKER not in candidate:
        raise RuntimeError("Could not find ZONE + KEY LEVEL CONFLUENCE marker")
    candidate = candidate.replace(
        INSERT_MARKER,
        smart_block.rstrip() + "\n\n" + INSERT_MARKER,
        1,
    )

    candidate = must_replace(candidate, OLD_ANY_TOUCH, NEW_ANY_TOUCH, "anyExistingKeyLevelTouched")
    candidate = must_replace(candidate, OLD_BULL_END, NEW_BULL_END, "bullKeyReaction smart OR")
    candidate = must_replace(candidate, OLD_BEAR_END, NEW_BEAR_END, "bearKeyReaction smart OR")

    # Runtime safety fix found by Ravi on 5M XAUUSD:
    # Pine numeric loops like `for i = 0 to array.size() - 1` can still attempt
    # array.get(0) when the array is empty. Guard current-TF OB/FVG visual loops.
    candidate = must_replace(candidate, OLD_OB_VISUAL_LOOP, NEW_OB_VISUAL_LOOP, "guard current TF OB visual loop")
    candidate = must_replace(candidate, OLD_FVG_VISUAL_LOOP, NEW_FVG_VISUAL_LOOP, "guard current TF FVG visual loop")

    candidate = candidate.replace(OLD_END_TAG, NEW_END_TAG, 1)

    required_hooks = [
        "smartAnyKeyTouched",
        "smartBullKeyReaction",
        "smartBearKeyReaction",
        "smartBullLiquidityTouched",
        "smartBearLiquidityTouched",
    ]
    for hook in required_hooks:
        if hook not in candidate:
            raise RuntimeError(f"Missing expected smart hook after assembly: {hook}")

    version_count, indicator_count = active_pine_header_counts(candidate)
    if version_count != 1:
        raise RuntimeError(f"Candidate must contain exactly one executable //@version line, found {version_count}")
    if indicator_count != 1:
        raise RuntimeError(f"Candidate must contain exactly one executable indicator() declaration, found {indicator_count}")
    if "<!DOCTYPE html>" in candidate or "<html" in candidate:
        raise RuntimeError("Candidate appears to contain HTML, not raw Pine text")
    if "if obCount > 0" not in candidate or "if fvgCount > 0" not in candidate:
        raise RuntimeError("Runtime array guards were not inserted into the candidate")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(candidate, encoding="utf-8")
    print(f"Created candidate: {OUT_PATH.relative_to(ROOT)}")
    print("Next: open this file on GitHub, click Raw, copy into TradingView, and test compile.")


if __name__ == "__main__":
    main()
