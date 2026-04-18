# AGENTS.md

Scope: this file applies to work inside `/Users/ukc/projects/dissertation/mindmap`.

## Purpose

This directory contains the browser-based dissertation argument map viewer.

## Working files

- `index.html`: page structure and script/style includes
- `styles.css`: viewer styles
- `app.js`: client-side interaction logic
- `argument_graph.json`: generated data consumed by the UI
- `README.md`: local usage notes

## Run locally

From the repository root:

```bash
python3 scripts/build_argument_graph.py
scripts/run_mindmap.sh
```

Default URL:

```text
http://localhost:8000/mindmap/
```

## Editing rules

- Treat `argument_graph.json` as generated output; prefer updating its source generator instead of manual edits.
- Keep changes in `index.html`, `styles.css`, and `app.js` minimal and consistent with the existing plain static setup.
- If UI changes depend on graph shape or metadata, rebuild the graph before validating.

## Validation

- Reload the viewer in a browser after changes.
- For data-related changes, rerun `python3 scripts/build_argument_graph.py`.
