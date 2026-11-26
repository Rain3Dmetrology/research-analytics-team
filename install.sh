#!/usr/bin/env bash
# ResearchTeam annex installer and read-only startup preflight.
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
CHECK=0
for a in "$@"; do case "$a" in -c|--check|-Check) CHECK=1;; *) echo "Unknown option: $a"; exit 2;; esac; done
if command -v python >/dev/null 2>&1; then PY=python
elif command -v python3 >/dev/null 2>&1; then PY=python3
else echo "FAIL: Python is required for compatibility verification."; exit 1; fi
gate="$SRC/scripts/compatibility_check.py"
blocked=0
installed=0
for name in .claude .codex .trae .trae-cn .qoder .workbuddy; do
    base="$HOME/$name/skills"
    [ -d "$base" ] || continue
    dmr="$base/deep-market-research"
    dest="$base/research-orchestrator"
    annex="$dest/SKILL.md"
    if [ "$CHECK" = 1 ]; then
        if [ ! -f "$annex" ]; then echo "WARN: $name annex not installed"; continue; fi
        "$PY" -B "$gate" --dmr "$dmr" --annex "$annex" || blocked=1
    else
        if ! "$PY" -B "$gate" --dmr "$dmr"; then blocked=1; continue; fi
        mkdir -p "$dest"
        cp "$SRC/portable/SKILL.md" "$annex"
        if ! "$PY" -B "$gate" --dmr "$dmr" --annex "$annex"; then blocked=1; continue; fi
        installed=$((installed+1))
    fi
done
if [ "$CHECK" = 1 ]; then
    "$PY" -B "$gate" --dmr "$HOME/.workbuddy/skills/deep-market-research" --package "$HOME/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team" || blocked=1
elif [ "$installed" = 0 ]; then blocked=1; fi
if [ "$blocked" = 1 ]; then echo "RESULT: FAIL - fix incompatible or drifted artifacts before launch."; exit 1; fi
echo "RESULT: PASS - verified artifacts; start a fresh session."
