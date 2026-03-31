#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_PATH="${1:-$ROOT_DIR/mindmap_bundle.tar.gz}"

FILES=(
  "scripts/build_argument_graph.py"
  "scripts/run_mindmap.sh"
  "scripts/export_mindmap_bundle.sh"
  "mindmap/index.html"
  "mindmap/app.js"
  "mindmap/styles.css"
  "mindmap/README.md"
  "mindmap/argument_graph.json"
  "docs/mindmap_implementation_plan.md"
  "docs/safe_desktop_sync.md"
)

cd "$ROOT_DIR"

for f in "${FILES[@]}"; do
  if [[ ! -f "$f" ]]; then
    echo "[export] Missing expected file: $f" >&2
    exit 1
  fi
done

mkdir -p "$(dirname "$OUT_PATH")"

tar -czf "$OUT_PATH" "${FILES[@]}"

echo "[export] Wrote bundle: $OUT_PATH"
echo "[export] Contains:"
for f in "${FILES[@]}"; do
  echo "  - $f"
done
