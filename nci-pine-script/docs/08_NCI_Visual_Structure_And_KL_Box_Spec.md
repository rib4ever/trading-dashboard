# NCI Visual Structure and Key Level Box Specification

## Purpose

This document defines how the NCI indicator should visually display market structure and key levels.

The goal is to match Ravi's manual TradingView drawings:

- Clean structure line.
- Timeframe-specific rectangle key-level boxes.
- Broken key-level boxes.
- Minimal noise.
- Debug labels hidden by default.

## Core correction

The script must not display many PBW/PW labels in normal mode.

Normal mode should show:

```text
1. Valid NCI structure line.
2. Active timeframe key-level box.
3. Broken key-level box if relevant.
4. Small dashboard/context only if enabled.
```

Debug mode can show:

```text
PW labels
PBW labels
Two-Maru labels
Big-Small labels
Confirmation labels
Range gate labels
Breakout candidate labels
```

## Visual target from Ravi's manual examples

The chart should look similar to Ravi's manual drawings:

```text
Aqua / teal market structure line.
Pink/red KL Down rectangle box.
Cyan/teal KL Up rectangle box.
Orange/brown broken KL rectangle box.
Text label inside the box.
```

## Text label standards

Use these labels exactly where possible:

```text
H4 KL ⬆️
H4 KL ⬇️
H1 KL ⬆️
H1 KL ⬇️
M15 KL ⬆️
M15 KL ⬇️
M5 KL ⬆️
M5 KL ⬇️
KL H4 Broken
KL H1 Broken
KL M15 Broken
KL M5 Broken
```

If TradingView has display issues with emoji, fallback text is allowed:

```text
H4 KL UP
H4 KL DOWN
H1 KL UP
H1 KL DOWN
M15 KL UP
M15 KL DOWN
```

## Structure line rule

Market structure line must connect validated structure turning points only.

It must not connect every small candle event.

It should represent:

```text
Pulse wave
Pullback wave
Next pulse wave
```

and should skip chart noise.

## Key-level box rule

A key level must be drawn as a rectangle zone, not only a thin line.

A valid KL box should include:

```text
Timeframe name
Direction
Zone top
Zone bottom
Box extension to the right
```

## KL Up visual style

Suggested style:

```text
Box color: teal / cyan transparent
Border: teal / cyan
Text: black
Label: H1 KL ⬆️ / H1 KL UP
```

## KL Down visual style

Suggested style:

```text
Box color: pink / red transparent
Border: pink / red
Text: black
Label: H4 KL ⬇️ / H4 KL DOWN
```

## Broken KL visual style

Suggested style:

```text
Box color: orange / brown transparent
Border: orange / brown
Text: black
Label: KL H1 Broken
```

## Timeframe visibility rule

The script should not throw all key levels from all timeframes randomly.

Display should follow the top-down sequence:

```text
H4 first
H1 from H4 context
M15 from H1 context
M5 from M15 context
```

## Normal mode vs Debug mode

### Normal mode

Show:

```text
Structure line
KL boxes
Broken KL boxes
Minimal dashboard
```

Hide:

```text
PBW labels
PW labels
Candle classification labels
Internal raw event labels
```

### Debug mode

Show:

```text
PBW labels
PW labels
2M / BS / Confirmation labels
Range labels
Breakout labels
Reason labels
```

## Next implementation target

Create a new visual clean block:

```text
script_blocks/04_structure_line_kl_box_visual_v0_2_1_block.pine
```

This block will focus first on drawing:

```text
1. Clean structure line.
2. KL Up box.
3. KL Down box.
4. Broken KL box.
5. Debug labels OFF by default.
```

## Do not proceed rule

Do not merge this into candidate/master until Ravi confirms the visual output is close to his manual drawings.
