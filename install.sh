#!/usr/bin/env bash
# Research Analytics Team - Unix one-click installer (annex form)
# Copies portable/SKILL.md into every detected agent platform's skills/
# directory as `research-orchestrator`, then checks each platform's installed
# dmr copy against the required pin. The WorkBuddy team form is a plugin
# package install (see README) and stays manual.
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
ANNEX_DIR="research-orchestrator"

VERSION="$(sed -n 's/.*"version": *"\([0-9.]*\)".*/\1/p' "$SRC/.codebuddy-plugin/plugin.json" | head -n1)"
PIN="$(sed -n 's/.*"deep-market-research": *"\([^"]*\)".*/\1/p' "$SRC/.codebuddy-plugin/plugin.json" | head -n1)"
PIN_MIN="${PIN#>=}"
PIN_MIN="${PIN_MIN%%[ <]*}"
echo "Installing research-analytics-team annex v$VERSION (dmr pin $PIN)"

TARGETS=(
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.trae/skills"
  "$HOME/.trae-cn/skills"
  "$HOME/.qoder/skills"
  "$HOME/.workbuddy/skills"
)

installed=0
for base in "${TARGETS[@]}"; do
  if [ -d "$base" ]; then
    dest="$base/$ANNEX_DIR"
    mkdir -p "$dest"
    cp "$SRC/portable/SKILL.md" "$dest/SKILL.md"
    dmr_skill="$base/deep-market-research/SKILL.md"
    if [ -f "$dmr_skill" ]; then
      dmr_v="$(sed -n 's/^version: *"\([0-9.]*\)".*/\1/p' "$dmr_skill" | head -n1)"
      if [ "$(printf '%s\n' "$dmr_v" "$PIN_MIN" | sort -V | head -n1)" = "$PIN_MIN" ]; then
        echo "[$base] annex v$VERSION installed (dmr v$dmr_v satisfies $PIN)"
      else
        echo "WARNING: [$base] dmr v$dmr_v < pin minimum $PIN_MIN — run deep-market-research install.sh first" >&2
      fi
    else
      echo "WARNING: [$base] dmr not installed — annex stays dormant until dmr (pin $PIN) is present" >&2
    fi
    installed=$((installed + 1))
  fi
done

if [ "$installed" -eq 0 ]; then
  echo "No supported agent skills directory found. Copy portable/SKILL.md into your platform's skills/research-orchestrator/ manually."
  exit 1
fi
echo "Done. WorkBuddy team form: copy the repo root into ~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/ (see README)."
