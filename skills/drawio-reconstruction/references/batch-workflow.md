## Batch Folder Workflow

Use this workflow when the user provides a directory of images or asks for batch reconstruction.

### Batch Intent And Scheduling

Before opening images for detailed visual analysis, decide whether the request is a batch reconstruction task:

- Treat the request as batch reconstruction when it names a folder, multiple image files, a glob/pattern, or any target that resolves to **2 or more image entries**.
- Create and review the manifest before detailed per-image work begins.
- When sub-agent tooling is available and useful, use a bounded worker pool no larger than the available concurrency and the number of pending images. Give each active worker exactly one image and an exclusive write set for that image's `.drawio`, exported `.png`, audit file, and private asset/crop directory. Reuse a free slot for the next image instead of trying to start every worker at once.
- When sub-agent tooling is unavailable, disabled, capacity-limited, or unnecessary for a small batch, process entries serially in manifest order. Preserve the same inventory, reconstruction, export, check, and visual-audit requirements.
- Tell the user about scheduling limitations only when they materially affect timing or delivery. Do not block a valid batch solely because parallel execution is unavailable.
- The coordinating agent may inspect thumbnails or file metadata to confirm scope, naming, orientation, and shared style constraints before choosing the schedule.

1. Identify the input directory, output directory, naming convention, and overwrite policy.
2. Create a batch manifest:

   ```bash
   python "$SKILL_DIR/scripts/batch_manifest.py" path/to/images --output-dir path/to/output --write
   ```

3. Review the manifest before editing. Process only entries in the manifest unless the user expands scope.
4. For each image, define the expected `<stem>.drawio`, `<stem>.png`, and lightweight `<stem>.audit.md` outputs in the target output directory.
5. Choose a bounded parallel schedule or a serial schedule:
   - Assign exclusive output files for each active entry.
   - Tell workers they are not alone in the codebase and must not revert or edit other workers' outputs.
   - Require every entry to follow the same full workflow as a standalone single-image task. Batch mode is only a scheduling strategy; it does not reduce fidelity, inventory, reconstruction, export, check, or visual-audit requirements.
   - Apply this quality gate to every entry: produce `.drawio`, `.png`, and `<stem>.audit.md`; create the complete visible-element inventory; classify non-text visuals; use crops/SVG/native elements according to the normal medium rules; run required checks/exports; visually compare the exported preview against the reference; mark unresolved visual defects instead of claiming completion.
   - Keep final batch verification, visual inspection, audit review, and the user-facing completion report with the coordinating agent.
6. After reconstruction, run batch verification:

   ```bash
   python "$SKILL_DIR/scripts/batch_verify.py" path/to/output/drawio_batch_manifest.json
   ```

7. Open every exported preview and compare it with the reference. Do not trust worker completion or script success alone.
8. Report completed entries, skipped entries, failures, and any images that need review.

Default batch outputs:

- `drawio_batch_manifest.json`
- `<image-stem>.drawio`
- `<image-stem>.png`
- `<image-stem>.audit.md`

Update an existing output when the user asks to edit or replace it. For a new batch
that encounters unrelated existing outputs, skip those files or use distinct names
according to the task context; do not overwrite them by accident.
