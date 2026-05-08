# Patch 10 Theme Engine

v1.6 visual theme engine plan.

Status: files created.

Created files:
- 03_SCRIPT_BLOCKS/09a_theme_engine.pine
- 03_SCRIPT_BLOCKS/98_assemble_v1_6_theme_candidate.py

Candidate output path:
- 03_MASTER_CANDIDATES/master-smc-sats-ravi-custom-01-v1.6-theme-engine-candidate.pine

Safe rule:
- v1.5 stays focused on logic stability.
- v1.6 adds theme control only.
- Theme engine must not change entry logic.

Theme presets:
- Minimal Pro
- Glass
- Crystal
- Diamond
- Earthy
- Nature
- Midnight Pro
- Gold Trader
- Cyber Neon
- Manual Custom

Implementation note:
The theme block keeps the existing color variable names used by the base script:
- bullColor
- bearColor
- neutColor
- slColor
- tpColor

This allows existing visuals to inherit the selected theme without replacing every label, box, and line in one risky patch.
