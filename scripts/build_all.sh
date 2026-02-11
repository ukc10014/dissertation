#!/usr/bin/env bash
set -euo pipefail

mkdir -p build

pandoc --defaults=defaults.yaml chapters/*.md -t latex -o build/thesis.tex

pandoc --defaults=defaults.yaml chapters/*.md \
  --pdf-engine=xelatex \
  --pdf-engine-opt=-interaction=nonstopmode \
  --pdf-engine-opt=-file-line-error \
  --pdf-engine-opt=-halt-on-error \
  -o build/thesis.pdf

# Second pass to resolve cross-references/bookmarks
pandoc --defaults=defaults.yaml chapters/*.md \
  --pdf-engine=xelatex \
  --pdf-engine-opt=-interaction=nonstopmode \
  --pdf-engine-opt=-file-line-error \
  --pdf-engine-opt=-halt-on-error \
  -o build/thesis.pdf

echo "Wrote build/thesis.tex and build/thesis.pdf"
