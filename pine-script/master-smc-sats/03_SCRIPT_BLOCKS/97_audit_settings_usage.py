#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
CANDIDATE = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine"
OUT = PROJECT / "08_PATCHES" / "patch-11-settings-usage-report.md"

START_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*input\.(\w+)\(")
GROUP_RE = re.compile(r"group\s*=\s*([A-Za-z_][A-Za-z0-9_]*)")
TITLE_RE = re.compile(r"input\.\w+\(\s*\n?\s*\"([^\"]+)\"")

GROUP_LABELS = {
    "GRP_THEME": "02 Theme Engine",
    "GRP_MASTER": "01 Master / Entry Filters",
    "GRP_SMC": "05 SMC Engine",
    "GRP_VIS": "08 Visual Display",
    "GRP_HTFLVL": "07 HTF Key Levels",
    "GRP_SATS": "06 SATS Engine",
    "GRP_SK": "07 Smart Key Levels",
    "GRP_ENTRY": "04 Entry Workflow",
    "GRP_RISK": "09 Risk / TP / SL",
    "GRP_ALERT": "10 Alerts",
}


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if "//" in line:
            line = line.split("//", 1)[0]
        lines.append(line)
    return "\n".join(lines)


def collect_input_blocks(text: str):
    lines = text.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = START_RE.match(line)
        if not m:
            i += 1
            continue
        name, input_type = m.groups()
        start_line = i + 1
        block_lines = [line]
        balance = line.count("(") - line.count(")")
        i += 1
        while i < len(lines) and balance > 0:
            block_lines.append(lines[i])
            balance += lines[i].count("(") - lines[i].count(")")
            i += 1
        block = "\n".join(block_lines)
        blocks.append((name, input_type, block, start_line))
    return blocks


def classify(group: str, name: str) -> str:
    if group == "GRP_THEME":
        return "Theme-only"
    if group == "GRP_VIS":
        return "Visual-only"
    if group == "GRP_ALERT":
        return "Alert-only"
    if group == "GRP_RISK":
        return "Risk-only"
    if group in {"GRP_MASTER", "GRP_ENTRY", "GRP_HTFLVL", "GRP_SK", "GRP_SMC", "GRP_SATS"}:
        return "Logic / engine"
    if name.startswith("manual"):
        return "Manual-only"
    return "Review"


def main():
    text = CANDIDATE.read_text(encoding="utf-8")
    code = strip_comments(text)
    inputs = []

    for name, input_type, block, start_line in collect_input_blocks(text):
        gm = GROUP_RE.search(block)
        group = gm.group(1) if gm else "UNKNOWN"
        tm = TITLE_RE.search(block)
        title = tm.group(1) if tm else ""
        refs = len(re.findall(rf"\b{re.escape(name)}\b", code))
        downstream_refs = max(0, refs - 1)
        inputs.append({
            "group": group,
            "group_label": GROUP_LABELS.get(group, group),
            "name": name,
            "title": title,
            "type": input_type,
            "refs": downstream_refs,
            "line": start_line,
            "class": classify(group, name),
        })

    group_order = []
    grouped = {}
    for row in inputs:
        group = row["group"]
        if group not in grouped:
            grouped[group] = []
            group_order.append(group)
        grouped[group].append(row)

    lines = []
    lines.append("# Patch 11 — Settings Usage Report")
    lines.append("")
    lines.append("Generated from:")
    lines.append(f"```text\n{CANDIDATE.relative_to(ROOT)}\n```")
    lines.append("")
    lines.append(f"Total input variables found: **{len(inputs)}**")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("- Downstream refs = how many times the input variable appears after its declaration.")
    lines.append("- A value of 0 means the setting may be disconnected or only used indirectly. Review manually before deleting.")
    lines.append("- This report understands multiline Pine inputs and attempts basic classification.")
    lines.append("")

    disconnected = [r for r in inputs if r["refs"] == 0]
    lines.append("## Summary")
    lines.append(f"- Inputs requiring manual connectivity review: **{len(disconnected)}**")
    lines.append(f"- Groups found: **{len(grouped)}**")
    lines.append("")

    if disconnected:
        lines.append("## Inputs requiring manual review")
        lines.append("| Group | Variable | Title | Type | Line |")
        lines.append("|---|---|---|---:|---:|")
        for row in disconnected:
            lines.append(f"| `{row['group']}` | `{row['name']}` | {row['title']} | `{row['type']}` | {row['line']} |")
        lines.append("")

    lines.append("## Inputs by group")
    lines.append("")
    for group in group_order:
        label = GROUP_LABELS.get(group, group)
        lines.append(f"### {group} — {label}")
        lines.append("| Variable | Title | Type | Downstream refs | Class | Line |")
        lines.append("|---|---|---:|---:|---|---:|")
        for row in grouped[group]:
            lines.append(f"| `{row['name']}` | {row['title']} | `{row['type']}` | {row['refs']} | {row['class']} | {row['line']} |")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Created settings usage report: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
