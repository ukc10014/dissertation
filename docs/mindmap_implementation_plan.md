# Dissertation Argument Mind-Map Plan

This plan turns your existing dissertation markdown into a web-based, drill-down argument map.

## Goal

A 3-level interactive map:

1. **Argument flow** (chapter-level and major claim-level).
2. **Specific points** (sub-claims/sections within each chapter).
3. **Relevant sources** (bibliography items cited inside each section).

## What is already in the repo

The core source files are already well-structured for this workflow:

- Introduction: `chapters/ch_01_upg.md`
- Main chapter drafts: `chapters/ch_03_combined.md`, `chapters/ch_04.md`
- Structural skeleton of whole thesis: `chapters/outline/upgrade_outline_v9.md`
- Bibliography source: `bib/bibliography_ukc.bib`

## Proposed architecture

### 1) Build a canonical graph JSON

Use `scripts/build_argument_graph.py` to parse:

- Markdown headings -> argument nodes
- Heading hierarchy -> parent/child edges
- Inline citation keys (`@Key`) -> source nodes
- Section -> source links via citation edges

Output:

- `mindmap/argument_graph.json`

### 2) Render in a browser UI

Build a small frontend (next step) using one of:

- **React Flow** (best for node editing + expansion UX)
- **Cytoscape.js** (best for larger, denser networks)
- **D3** (best control, most engineering effort)

Recommended first pass: **React Flow**.

### 3) Drill-down behavior

- Click a chapter node: expand major sections.
- Click a section node: expand sub-sections.
- Click a subsection node: show linked citations.
- Click a citation node: open metadata card (title/author/year from `.bib`).

### 4) Visual style (Lombardi-inspired)

- Curved edges, handwritten-like labels optional.
- Color channels:
  - chapter families
  - normative vs empirical vs methodological claims
  - source types (book/article/preprint)
- Multiple layout modes:
  - left-to-right "argument flow"
  - radial "constellation"

## Suggested implementation phases

### Phase A (now)

- Generate and inspect `mindmap/argument_graph.json`.
- Validate hierarchy and citation coverage.

### Phase B

- Scaffold minimal web app (`mindmap-app/`) with React + React Flow.
- Add search by keyword and citation key.

### Phase C

- Enrich nodes with manual tags:
  - `claim_type` (`definitional`, `normative`, `empirical`, `method`)
  - `status` (`draft`, `stable`, `to-write`)
  - `importance` (1–5)

### Phase D

- Add filters and export:
  - show only one chapter or one claim type
  - export PNG/SVG for supervision meetings

## Practical next actions

1. Run:

   ```bash
   python3 scripts/build_argument_graph.py
   ```

2. Open `mindmap/argument_graph.json` and spot-check nodes for chapter 1/3/4 + outline.
3. Confirm whether you want the UI to be:
   - a static HTML/JS page in this repo, or
   - a small React app.
4. Add one curation pass where we rename machine-parsed headings to polished node labels.

## Notes on fidelity

Automated parsing gives a strong first graph, but your key argument turns (especially in Chapter 1 and the outline) will benefit from a light manual curation layer. The best pattern is:

- **auto-extract structure**
- **manually curate high-level claim labels**
- **auto-link citations**

That yields a map that is both faithful to your text and presentation-ready.
