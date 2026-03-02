#!/bin/bash

# Build a single chapter to DOCX with bibliography
# Usage: ./scripts/build_docx.sh ch_01_upg
# Or:    ./scripts/build_docx.sh chapters/ch_01_upg.md

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <chapter_name>"
  echo "Example: $0 ch_01_upg"
  echo "     or: $0 chapters/ch_01_upg.md"
  exit 1
fi

# Extract chapter name
INPUT="$1"
if [[ "$INPUT" == chapters/* ]]; then
  # Strip "chapters/" prefix if provided
  CHAPTER=$(basename "$INPUT" .md)
  INPUT_FILE="$INPUT"
else
  # Assume just the chapter name was provided
  CHAPTER="$1"
  CHAPTER=$(basename "$CHAPTER" .md)
  INPUT_FILE="chapters/${CHAPTER}.md"
fi

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
  echo "Error: File $INPUT_FILE not found"
  exit 1
fi

OUTPUT_FILE="build/${CHAPTER}.docx"

echo "Building $INPUT_FILE -> $OUTPUT_FILE"

pandoc "$INPUT_FILE" \
  -o "$OUTPUT_FILE" \
  --bibliography=bib/bibliography_ukc.bib \
  --bibliography=bib/ch03_additions.bib \
  --citeproc \
  --csl=https://www.zotero.org/styles/chicago-author-date \
  --metadata link-citations=true \
  --metadata title="${CHAPTER}"

echo "Success: $OUTPUT_FILE"
