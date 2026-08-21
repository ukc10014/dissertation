#!/usr/bin/env bash
set -euo pipefail
mkdir -p build

FILES=(
  chapters/00_frontmatter.md
  chapters/ch_00_intro.md
  chapters/references.md
)

pandoc --defaults=defaults.yaml "${FILES[@]}" -o build/thesis.pdf
echo "Wrote build/thesis.pdf"
