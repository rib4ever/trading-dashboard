#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PROJECT = ROOT / "pine-script" / "master-smc-sats"
CANDIDATE = PROJECT / "03_MASTER_CANDIDATES" / "master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine"
OUT = PROJECT / "08_PATCHES" / "patch-11-settings-usage-report.md"

INPUT_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*input\.(\w+)\((.*)")
GROUP_RE = re.compile(r"group\s*=\s*([A-Za-z_][A-Za-z0-9_]*)")
TITLE_RE = re.compile(r"input\.\w+\(\s*([^,]+)")


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if "//" in line:
            line = line.split("//", 1)[0]
        lines.append(line)
    return "\n".join(lines)


def main():
    text = CANDIDATE.read_text(encoding="utf-8")
    code = strip_comments(text)
    inputs = []
    for idx, line in enumerate(text.splitlines(), start=1):
        m = INPUT_RE.match(line)
        if not m:
            continue
        name, input_type, rest = m.groups()
        gm = GROUP_RE.search(line)
        group = gm.group(1) if gm else "UNKNOWN"
        refs = len(re.findall(rf"\b{re.escape(name)}\b", code))
        downstream_refs = max(0, refs - 1)
        inputs.append((group, name, input_type, downstream_refs, idx))

    group_order = []
    grouped = {}
    for row in inputs:
        group = row[0]
        if group not in grouped:
            grouped[group] = []
            group_order.append(group)
        grouped[group].append(row)

    lines = []
    lines.append("# Patch 11 — Settings Usage Report")
    lines.append("")
    lines.append("Generated from:")
    lines.append("")
    lines.append(f"```text\n{CANDIDATE.relative_to(ROOT)}\n```")
    lines.append("")
    lines.append(f"Total input variables found: **{len(inputs)}**")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Downstream refs = how many times the input variable appears after its declaration.")
    lines.append("- A value of 0 means the setting may be disconnected or only used indirectly through generated replacement logic. Review manually before deleting.")
    lines.append("- This audit does not change trading logic.")
    lines.append("")

    disconnected = [r for r in inputs if r[3] == 0]
    if disconnected:
        lines.append("## Inputs requiring manual review")
        lines.append("")
        lines.append("| Group | Variable | Type | Line |")
        lines.append("|---|---|---:|---:|")
        for group, name, input_type, refs, idx in disconnected:
            lines.append(f"| `{group}` | `{name}` | `{input_type}` | {idx} |")
        lines.append("")

    lines.append("## Inputs by group")
    lines.append("")
    for group in group_order:
        lines.append(f"### {group}")
        lines.append("")
        lines.append("| Variable | Type | Downstream refs | Line |")
        lines.append("|---|---:|---:|---:|")
        for _, name, input_type, refs, idx in grouped[group]:
            lines.append(f"| `{name}` | `{input_type}` | {refs} | {idx} |")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Created settings usage report: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
