Here you go; this is a **drop-in `README.md`** that exactly matches what you set up. You can copy-paste it as-is.

````markdown
# Dissertation

Markdown-first PhD thesis materials with a Pandoc-based build.

---

## Build

Canonical build configuration lives in `defaults.yaml`.

### HTML preview
```bash
scripts/build_html.sh
````

### PDF build

```bash
scripts/build_pdf.sh
```

Rendered outputs are written to `build/` and are not tracked by default.

---

## Repository conventions

* **Source of truth**: Markdown chapters, bibliography files, assets.
* **Abstract**: `abstract.md` (repo root) is the canonical abstract. Its text is also in the `abstract` field of `defaults.yaml` for Pandoc rendering — keep them in sync.
* **Build artefacts**: PDFs, HTML, and LaTeX auxiliary files are ignored.
* **Milestone PDFs** (submitted drafts) may be tracked separately if needed.
* Chapters live in `chapters/`.
* Exploratory or abandoned text lives in `drafts/`.

---

## History and scope

**2026-02-10**

This repository supersedes earlier GitHub versions from 2024 and a Dropbox-based draft from 2025.

* Earlier material is preserved on an archive branch.
* The `main` branch represents a clean restart from February 2026 onward.

```

If you want a matching `CHANGELOG.md` or a one-page “how to add a new chapter” note for future-you, say the word and I will generate it.
```
