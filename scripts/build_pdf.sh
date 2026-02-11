#!/usr/bin/env bash
set -euo pipefail
mkdir -p build
pandoc --defaults=defaults.yaml chapters/*.md -o build/thesis.pdf
echo "Wrote build/thesis.pdf"
