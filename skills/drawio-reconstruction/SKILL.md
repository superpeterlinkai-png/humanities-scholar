---
name: drawio-reconstruction
description: "Reconstruct a diagram image or image folder into editable Draw.io files with rendered previews. Preserve wording, visual relationships, and uncertainty; verify both technical validity and fidelity to the reference."
---

# Draw.io Reconstruction

Use this skill for high-quality reconstruction of diagram images into `.drawio` files.

## Working agreement

The user's current request and established authorization take precedence over
this skill's workflow defaults. Use the available context, resolve routine choices,
and complete the requested work. Ask only about missing information that materially
changes meaning, evidence, scope, or authorization; continue independent work.
Treat later corrections as steering unless the user replaces the task.

Keep supporting guides subordinate to that scope. Their examples and suggested
structures are optional. If a skill requirement actually blocks delivery, identify
the file and exact clause and explain the affected part; do not infer a new approval
requirement from a recommendation.

## Humanities Research Use

Reconstruction preserves the source image's claims; it does not validate them.
Before reproducing a humanities research figure, distinguish visual fidelity from
scholarly endorsement.

- Preserve original wording, dates, names, scripts, transliterations,
  periodisation, quotation marks, uncertainty markers, legends, citations, and
  directional or contested relations.
- Do not modernise historical terminology, resolve ambiguous labels, translate
  original-language text, change emic categories into analytical categories, or
  convert a dotted or uncertain relation into a solid one without permission.
- Treat arrows, hierarchy, proximity, colour, boundaries, and node size as
  meaning-bearing. A visually convenient substitution may change the historical or
  conceptual claim.
- Keep source notes, archival identifiers, image credits, and copyright notices
  legible when they appear in the reference.
- For sacred, culturally sensitive, community-owned, colonial, restricted, or
  personally identifying material, flag reproduction or editing risks rather than
  assuming technical access grants ethical permission.
- If the user asks to improve the argument represented by the diagram, separate
  that analytical revision from faithful reconstruction and implement the requested
  content changes. Ask only if the intended new claim is materially ambiguous.

When a new figure is being designed rather than reconstructed, route first to
`figure-designer`. This skill reproduces or edits an established visual; it does
not decide whether the visual's categories and relations are scholarly defensible.

## Helper Script Location

Resolve `SKILL_DIR` to the absolute directory containing this `SKILL.md` before running any bundled helper. Use the resolved skill location provided by the runtime; never assume the skill is installed under `~/.codex`, `~/.agents`, or any other fixed directory.

All commands below use `$SKILL_DIR` to mean that resolved absolute directory.

## Fidelity Contract

The primary goal is visual fidelity to the reference image. Editability is secondary.

Do not treat semantic equivalence as success. A generic icon, generic curve, generic font size, approximate panel, or approximate background is a defect when the reference has a specific visual style.

Script checks only prove technical validity. A diagram is not complete merely because `.drawio` opens, exports, or passes `check_drawio.py` / `batch_verify.py`. Completion requires visual comparison against the reference at full size.

Work only in the target directory or target files named by the user. Do not repair, overwrite, or improve neighboring diagrams because they look related. If the requested target is ambiguous, inspect and report the ambiguity before editing.

Never silently rewrite the user's content. If the user asks for larger fonts or a more professional PPT style, first distinguish:

- **Layout-only refinement**: increase font size, resize boxes, improve spacing, align elements, adjust line breaks without changing words.
- **Content compression**: shorten sentences, remove details, rewrite labels. Do this
  when requested; otherwise keep wording and ask only if compression is necessary
  to meet a conflicting layout constraint.

## Batch reconstruction

For a directory or multiple images, read
[batch-workflow.md](references/batch-workflow.md). It defines the manifest,
exclusive output files, scheduling, and per-image verification. Skip that workflow
for a single-image task. Resolve `SKILL_DIR` to this skill's root in every helper command.

## Match the work to the request

For a new reconstruction, inventory the whole reference and complete the fidelity
workflow below. For a local edit, preserve unaffected elements and inspect the
changed region, containing panels, neighboring layout, and resulting full preview.
Do not reconstruct an accepted diagram from scratch to change one label or font.

## Reference inventory

Before a new reconstruction, create a visible-element inventory. For complex or batch work, write it to `<stem>.audit.md`; for a very small single image, maintain it in working notes and still perform the same checks.

For a new reconstruction, the inventory covers every visible region and element:

- canvas size, background, grid, texture, gradients, shadows, page boundary
- title, subtitle, section headers, footer, page number
- panels, cards, containers, dividers, badges, numbered markers
- every text block and label
- every icon, artwork, screenshot, logo, chart, thumbnail, or decorative visual
- every arrow, curve, connector, loop, bracket, dashed path, and arrowhead
- all spacing relationships that define the layout

Record the details needed to track each item:

- `id`
- approximate region or bbox
- content / visual description
- selected medium: native / SVG / crop / generated-cleanup
- style notes: color, stroke, font, size, shadow, curve geometry, padding
- status: pending / done / needs-fix / accepted

Do not begin final delivery until all visible inventory items are accepted or explicitly reported as unresolved.

## Media and layout details

Prefer native editable labels and structure. Complex artwork may need source
crops; use SVG or native icons only when they preserve the reference's actual
shape and style. Do not substitute a generic symbol for a distinctive image.

For a new reconstruction, or edits to crops, icons, arrows, text size, or layout,
read the relevant sections of
[reconstruction-details.md](references/reconstruction-details.md). This preserves
the specific crop, image-encoding, geometry, and containment checks without loading
them for an unrelated small edit. Helper paths are relative to the skill root.

## Default Workflow

1. Identify the reference image and target output directory.
2. Create or update the batch manifest when processing folders or multiple images.
3. For each image, create the reference inventory and style token notes.
4. Rebuild the diagram with native Draw.io elements wherever feasible for text and structure.
5. Classify every non-text visual with the medium decision rules.
6. Use source-image crops or transparent PNGs for complex/style-specific visuals; use SVG/native only for simple clean icons that pass shape/style matching.
7. Export a PNG preview with Draw.io CLI.
8. Run the checker and investigate failures against the actual render. Fix real
   defects; document any demonstrated false positive from heuristic checks.
9. Perform a full visual audit against the reference at full size, item by item.
10. Correct material defects in the affected output and recheck it. Finish when
    the requested fidelity and usability are met; if a tool or source limitation
    prevents a reliable fix, deliver the inspectable work with that limit explicit.
11. Report changed files and remaining quality risks.

Default outputs:

- `<name>.drawio`
- `<name>.png`
- `<name>.audit.md` for batch or complex reconstructions

## Mandatory Visual Audit

Before final response, compare the actual exported preview against the reference
 at the intended size. A new reconstruction needs the full inventory checked; a
 local edit needs the affected elements and their layout consequences checked.

Blocking defects:

- missing visible element
- generic substitute icon
- wrong icon/artwork style, stroke, scale, or internal detail
- wrong curve, loop, dashed path, arrow route, arrowhead, or connector layering
- wrong title/body font size, weight, line break, color, or alignment
- text overlap, clipping, border touching, or awkward wrapping not in the reference
- wrong panel/card size, corner radius, shadow, border, or spacing
- background mismatch, missing gradient/grid/texture, or wrong page boundary
- crop seam, blur, halo, bad transparency, wrong crop boundary, or neighboring content inside crop
- script-only pass without reference comparison
- any inventory item still marked `needs-fix`

Fix unresolved material defects when a reliable correction is available. Do not
claim full fidelity while defects remain. A persistent capability or source limit
calls for an accurate account of the incomplete part, not an indefinite retry loop.

For batch jobs, the parent agent must open every exported preview and every worker audit file before final response. Worker completion is not delivery acceptance.

## Using A User-Approved Reference Diagram

If the user provides a manually adjusted screenshot or `.drawio` file as a quality reference, use it as the style source before changing another diagram.

Prefer the `.drawio` file when available because it exposes real geometry:

- Extract font sizes by semantic role.
- Extract geometry ratios: card width/height, title/body text box heights, icon size, role-label height, evidence panel height, outcome row height, and padding.
- Apply those role-based values to the target diagram before subjective visual adjustments.
- Preserve the target diagram's wording. Use the reference for typography, spacing, icon sizing, and layout density only.
- If the reference `.drawio` has stale page metadata but exports correctly, use the content bounding box and exported PNG for validation.

## Redline Feedback

If the user provides a screenshot with red boxes or annotations:

- Treat each marked region as a blocking defect.
- Do not reinterpret the request as a new reconstruction unless asked.
- First fix containment, clipping, overflow, wrong crop, wrong icon style, wrong arrow path, and wrong typography in the marked regions.
- Preserve the user's current text and manual edits.
- If a red box marks a cartoon/illustration/visual metaphor, consider replacing SVG recreation with a crop from the reference.

## Verification

Always verify the `.drawio` after edits:

```bash
python "$SKILL_DIR/scripts/check_drawio.py" path/to/file.drawio
python "$SKILL_DIR/scripts/export_drawio.py" path/to/file.drawio path/to/preview.png
```

For batch jobs:

```bash
python "$SKILL_DIR/scripts/batch_manifest.py" path/to/images --output-dir path/to/output --write
python "$SKILL_DIR/scripts/batch_verify.py" path/to/output/drawio_batch_manifest.json
```

The checker catches XML validity and common containment failures; it is not a substitute for visual inspection. After export, inspect the rendered PNG against the reference before final response.

## Final Response

Keep the final response short:

- Link to the `.drawio` file.
- Link to the rendered `.png` preview.
- Mention whether crops or SVG/native elements were used for major visual elements.
- Mention any remaining manual review point, especially if visual audit items remain unresolved.
