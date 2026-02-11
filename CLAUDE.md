# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **writing-first project** — a PhD dissertation by Kanad Chakrabarti, "Reasons for Persons, or The Good Successor Problem." The work covers AI ethics, cosmic-scale moral philosophy, and constitutional alignment for superintelligent AI. Research includes embedded LLM experiment transcripts and analyses.

Work here is primarily prose editing, structural reorganization, and citation management — not software development. Code may appear occasionally but is not the focus. Edits may come from Claude Code, Codex, or manual editing in Sublime Text / VS Code. The **rendered PDF is the source of truth** for how the document should look.

## Build Commands

Requires Pandoc 3.6.3+ and a LaTeX distribution (for PDF). The PDF output is the primary deliverable; HTML/Docx are secondary future concerns.

```bash
scripts/build_pdf.sh    # PDF output → build/thesis.pdf (primary)
scripts/build_html.sh   # HTML preview → build/thesis.html
```

Both scripts use `defaults.yaml` for Pandoc configuration and glob `chapters/*.md` (alphabetical order matters for chapter sequencing).

## Repository Layout

- `chapters/` — Source markdown chapters (the canonical content)
- `chapters/gdocs/` — Google Docs export backups of earlier drafts
- `defaults.yaml` — Pandoc config: metadata, geometry, bibliography, LaTeX preamble
- `bib/` — Bibliography files (referenced as `bib/bibliography_ukc.bib`)
- `templates/` — LaTeX preamble (referenced in defaults.yaml but may not yet exist)
- `assets/` — Images and diagrams
- `drafts/` — Exploratory or abandoned text
- `milestones/` — Submitted/checkpoint PDFs
- `build/` — Generated outputs (gitignored)

## Conventions

- **Before modifying any source file** (`.md`, `.bib`, `.sh`, or similar data/code files), make a backup copy with a `~` suffix (e.g., `ch_03.md` → `ch_03.md~`). This follows the Unix convention for backup files.
- All thesis content is authored in Markdown with Pandoc-flavored extensions (citations, LaTeX math, cross-references).
- Build artifacts (PDF, HTML, LaTeX aux files) are gitignored.
- Chapter files are named with `ch_` prefix and ordered alphabetically for correct Pandoc concatenation.
- Commits tend to be checkpoint-style rather than continuous.
