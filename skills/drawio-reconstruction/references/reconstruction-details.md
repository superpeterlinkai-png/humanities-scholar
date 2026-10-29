# Reconstruction details

Read for a new reconstruction or an edit involving media, crops, arrows, typography,
or containment. Resolve `SKILL_DIR` to the parent skill directory, not this
references directory. Apply the sections relevant to the actual change.

## Reconstruction Strategy

Use the best medium for visual fidelity. Do not globally default all non-text visuals to screenshots, and do not globally redraw all visuals as SVG. The deciding question is: which method best matches the reference after export?

Prefer **Draw.io native elements** for:

- editable text, headings, labels, chips, callouts
- boxes, panels, dividers, simple tables, simple charts, badges
- structural arrows/connectors when native geometry can match the reference
- repeated layout structure that should remain easy to edit

Use **PNG crop / screenshot by default** for:

- complex icons, detailed symbols, decorative illustrations, and mixed-object visuals
- style-specific icon families where a generic SVG would not match the reference
- visual metaphors and scene-like artwork: icebergs, people, environments, dashboards, monitors, lab scenes, rooms, landscapes, workflow scenes
- real UI screenshots, phone/dashboard strips, app thumbnails, evidence screenshots, dense mini-diagrams
- people, cartoon characters, expressive faces, hands, body poses, or human-computer scenes
- anything where exact visual fidelity matters more than editability
- any non-text visual that would take many paths, gradients, masks, or manual approximations to redraw
- any visual element where an SVG/native attempt would simplify, omit, or visibly distort important details

Use **SVG/native only** for:

- simple clean icons whose reference shape and style can be matched, not merely named semantically
- icons with simple outline/fill geometry, 1-2 main colors, no essential texture, no dense internal detail, and a clear reference style that can be reproduced
- repeated simple icon families where SVG can preserve the same stroke width, proportions, colors, and scale as the reference
- small source icons where the crop would be blurry or background-contaminated and a shape-level SVG match is feasible
- elements where the user explicitly needs vector editability

Do not use a generic standard icon just because the semantic label matches. Database, chart, document, target, brain, robot, phone, clipboard, cursor, lightbulb, molecule, beaker, monitor, and similar icons still require a shape/style check against the reference.

## Medium Decision Rules

Classify each visual element before reconstructing it.

1. If it is text or structure, use Draw.io native elements.
2. If it is a visual element with distinctive reference style, dense detail, gradients, shadows, multi-object composition, or scene/metaphor content, crop it unless the user explicitly requests vector editability.
3. If it is a simple clean icon, use SVG/native only when the SVG can match the reference's shape, stroke, proportions, fill, and visual family.
4. If an SVG would be semantically correct but visually generic, do not use it. Crop the reference or create a closer shape-level SVG.
5. If a crop is blurry, contaminated, or has a visible rectangle, first fix the crop/background. Switch to SVG only if the visual is simple and the SVG match is closer to the reference than the crop.
6. If crop background seams are visible, try transparent PNG cleanup or match the crop background to the containing panel.
7. If ordinary cleanup leaves halos, ragged edges, watermarks, JPEG blocks, or mismatched panels, place the crop on a same-color background block, crop tighter, or use an available image editing/generation tool to repair only the background.
8. If neither crop nor SVG/native is acceptable, mark the item `needs-fix` in the audit instead of silently substituting a poor drawing.

Blocking medium defects:

- generic substitute icon where the reference has a style-specific icon
- complex visual redrawn as simplified SVG without a user-requested vector-editability reason
- blurry crop of a simple icon when a clean shape-level SVG would match better
- cropped complex artwork with visible background seams, halos, missing strokes, clipped shadows, or unrelated neighboring text/borders
- missing prominent icon, decorative mark, or detailed visual

## Icon Reconstruction Discipline

Before writing icon SVGs or embedding crops, make a role-to-symbol map from the reference. For example:

- Planning: brain, checklist, planning symbol
- Tool Use: wrench, crossed tools, terminal, tool symbol
- Memory: database cylinder, storage, memory symbol
- Verification: shield, checkmark, audit, validation symbol
- Evidence cards: schema/table, logs/document, execution tree/plan, metrics/gauge

For each map entry:

- Use a source-image crop for complex, style-specific, or detailed symbols.
- Use a distinct SVG or native Draw.io symbol only for simple clean icons that can match the reference style.
- Keep stroke width, color, proportions, and size consistent with the reference, not with a generic icon set.
- Do not copy one icon and only change its position or label.
- Do not use a generic placeholder icon unless the reference itself uses that same repeated placeholder.
- If a symbol is not simple and clean, crop that specific symbol from the reference instead of substituting an unrelated SVG.

After creating or editing icons, run `check_drawio.py`. Duplicate image payloads in evidence icons, core-strip icons, workflow-step icons, or outcome-row icons are blocking failures unless the reference intentionally repeats the same symbol.

## Screenshot Crop Rules

Use screenshots/PNG crops when:

- the illustration is too complex to redraw efficiently
- exact visual style matters more than editability
- SVG attempts still look poor or generic
- the user supplied or approved a good crop
- the visual is a complex icon whose details would be lost in a hand-drawn SVG
- the visual is a real UI screenshot, phone strip, dashboard thumbnail, dense evidence artifact, person, scene, or visual metaphor

When using screenshots:

- Avoid screenshots for editable text or structural layout.
- Crop around the target foreground artwork, not around the whole surrounding region.
- Start from a rough ROI, identify the foreground bbox, then add modest safe padding.
- Use the crop helper when possible:

  ```bash
  python "$SKILL_DIR/scripts/crop_assist.py" reference.png --roi x,y,w,h --anchor x,y --exclude x,y,w,h --output-dir crops --name icon_name
  ```

- Inspect the generated preview and candidates visually before embedding a crop. The script proposes bounds; the model still decides which candidate best matches the reference.
- `crop_assist.py` requires Pillow. Use an available runtime containing it or an
  equivalent supported inspection method. If installation is necessary, use an
  isolated task environment and follow the host permissions. Do not invent a new
  approval gate when the task already authorizes the required setup; do not claim
  that crop inspection happened if it could not be performed.
- Use `--exclude` boxes for nearby elements that are inside the rough ROI but not part of the target artwork, especially bullets, body text, title rules, numbered badges, panel borders, and divider lines.
- Safe padding should preserve full strokes, arrowheads, shadows, antialiasing, and immediate intentional whitespace. It should not expand into general empty space.
- Do not crop tightly to visible strokes unless tight cropping is required to avoid neighboring content. A clipped stroke, cut-off arrowhead, missing shadow, or artwork touching the crop edge is a blocking defect.
- Do not include neighboring bullets, labels, title rules, card borders, divider lines, or unrelated same-color marks. If more padding would pull in a neighbor, use the tighter valid candidate and handle the background with transparency or color matching.
- Prefer transparent PNG when the surrounding panel/background is not uniform.
- If transparency is not possible or cleanup creates halos, place the crop on a same-color background block.
- If the crop background color does not match the Draw.io panel, crop tighter, remove the background, recolor/match the crop background, or set the containing panel/background to match.
- If the crop is complex and still has background mismatch after ordinary cleanup, use an available image editing/generation tool to repair or neutralize only the background; do not alter the semantic foreground.
- Check exported PNG for visible seams, antialiasing halos, jagged transparency, blur, or mismatched background. Do not leave visible rectangular crop seams.

## Curves And Arrows

For every arrow or curve, match the reference before choosing implementation.

Create an arrow inventory:

- source element and target element
- start/end anchors
- direction
- line type: solid, dashed, dotted, curved, vertical, horizontal, loop
- stroke width, color, arrowhead type and size
- bend points, corner radius, and whether the path passes in front of or behind panels
- semantic role: workflow transition, feedback loop, evidence support, callout, decorative cue

Implementation order:

1. Native Draw.io connectors for structural connectors when they can match the reference.
2. SVG path for special braces, curved arrows, loop arrows, rounded return paths, or decorative arrows that native Draw.io cannot match.
3. PNG crop only for highly specific non-editable decorative marks.

Large loop arrows, dashed feedback curves, and rounded return paths must match the reference path geometry. Do not replace them with approximate generic connectors.

## Typography And Layout

Extract typography from the reference image before assigning sizes:

- main title
- subtitle
- section titles
- card titles
- card bodies
- labels/chips
- footer/page number
- icon-label pairs

For every text role, capture approximate font size, weight, color, line height, alignment, and available box size. Do not apply SIGMOD running-example font baselines unless the reference is explicitly a SIGMOD-style running example.

Treat every text change as a box-model change:

`text -> text box -> card/row -> containing panel -> neighboring layout`.

Hard failures:

- text visually larger but the background card/panel was not resized
- text box height smaller than rendered text height
- text touches borders, overlaps icons, or extends outside rows/cards
- awkward line breaks not present in the reference when space is available
- parent cards fit text but no longer fit inside the panel
- footer or slide boundary is pushed into content

