#!/usr/bin/env bash
set -euo pipefail
mkdir -p build

FILES=(
  chapters/00_frontmatter.md
  chapters/ch_00_intro.md
  chapters/references.md
)

XREFS=build/xrefs.tex

# Chapter numbers come from position in the full chapters/*.md sequence, so
# \ref{ch:...} to an excluded chapter still prints its real number instead of ??.
# Excluded chapters get a stub \newlabel plus an anchor so the link is not dangling.
awk '
  /^# / {
    if ($0 ~ /\{-\}/ || $0 ~ /\{\.unnumbered\}/) next
    n++
    if (match($0, /\{#[^}]+\}/)) {
      label = substr($0, RSTART + 2, RLENGTH - 3)
      title = $0
      sub(/^# /, "", title)
      sub(/[ \t]*\{#[^}]*\}.*$/, "", title)
      print FILENAME "\t" n "\t" label "\t" title
    }
  }
' chapters/*.md > build/all_chapter_labels.tsv

: > "$XREFS"
: > build/xrefs_report.txt
while IFS=$'\t' read -r file num label title; do
  for included in "${FILES[@]}"; do
    [ "$file" = "$included" ] && continue 2
  done
  printf '\\newlabel{%s}{{%s}{1}{%s}{chapter.%s}{}}\n' "$label" "$num" "$title" "$num" >> "$XREFS"
  printf '\\AtBeginDocument{\\hypertarget{chapter.%s}{}}\n' "$num" >> "$XREFS"
  printf '  %s -> Chapter %s (%s)\n' "$label" "$num" "$title" >> build/xrefs_report.txt
done < build/all_chapter_labels.tsv

if [ -s "$XREFS" ]; then
  echo "Resolving cross-chapter references to excluded chapters:"
  cat build/xrefs_report.txt
fi

pandoc --defaults=defaults.yaml -H "$XREFS" "${FILES[@]}" -o build/thesis.pdf
echo "Wrote build/thesis.pdf"
