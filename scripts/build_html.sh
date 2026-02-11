#!/usr/bin/env bash
set -euo pipefail
mkdir -p build
pandoc --defaults=defaults.yaml chapters/*.md -s -t html -o build/thesis.html
echo "Wrote build/thesis.html"
