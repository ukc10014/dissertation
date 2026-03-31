#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-8000}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

cd "$ROOT_DIR"

echo "[mindmap] Serving repository at: $ROOT_DIR"
echo "[mindmap] Open: http://localhost:${PORT}/mindmap/"
echo "[mindmap] Press Ctrl+C to stop."

python3 -m http.server "$PORT"
