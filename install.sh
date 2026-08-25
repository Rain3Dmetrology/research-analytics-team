#!/usr/bin/env bash
# Research Analytics Team - Unix one-click installer (annex form)
# Copies portable/SKILL.md into every detected agent platform's skills/
# directory as `research-orchestrator`, then checks each platform's installed
# dmr copy against the required pin. The WorkBuddy team form is a plugin
# package install (see README) and stays manual.
set -euo pipefail

CHECK=0
for a in "$@"; do case "$a" in -c|--check|-Check) CHECK=1;; esac; done

SRC="$(cd "$(dirname "$0")" && pwd)"
ANNEX_DIR="research-orchestrator"

VERSION="$(sed -n 's/.*"version": *"\([0-9.]*\)".*/\1/p' "$SRC/.codebuddy-plugin/plugin.json" | head -n1)"
PIN="$(sed -n 's/.*"deep-market-research": *"\([^"]*\)".*/\1/p' "$SRC/.codebuddy-plugin/plugin.json" | head -n1)"
PIN_MIN="${PIN#>=}"
PIN_MIN="${PIN_MIN%%[ <]*}"
if [ "$CHECK" != "1" ]; then
  echo "Installing research-analytics-team annex v$VERSION (dmr pin $PIN)"
fi

TARGETS=(
  "$HOME/.claude/skills"
  "$HOME/.codex/skills"
  "$HOME/.trae/skills"
  "$HOME/.trae-cn/skills"
  "$HOME/.qoder/skills"
  "$HOME/.workbuddy/skills"
)

if [ "$CHECK" = "1" ]; then
  team_pkg="$HOME/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team"
  blocked=0
  echo "== RAT startup preflight v$VERSION (dmr pin $PIN) =="
  for base in "${TARGETS[@]}"; do
    [ -d "$base" ] || continue
    annex="$base/$ANNEX_DIR/SKILL.md"; dmr="$base/deep-market-research/SKILL.md"
    if [ ! -f "$annex" ]; then echo "  WARN [$base] annex not installed (routing annex, non-blocking)"; continue; fi
    if [ ! -f "$dmr" ]; then
      echo "  [$base] annex ok, dmr MISSING (annex dormant until dmr $PIN)"   # warn, non-blocking
    else
      dmr_v="$(sed -n 's/^version: *"\([0-9.]*\)".*/\1/p' "$dmr" | head -n1)"
      if [ "$(printf '%s\n' "$dmr_v" "$PIN_MIN" | sort -V | head -n1)" = "$PIN_MIN" ]; then
        echo "  [$base] annex ok, dmr v$dmr_v ok (satisfies $PIN)"
      else
        echo "  WARN [$base] dmr v$dmr_v < pin $PIN_MIN (run deep-market-research install.sh)"
      fi
    fi
  done
  if [ -d "$team_pkg" ]; then
    tp_ver="$(sed -n 's/.*"version": *"\([0-9.]*\)".*/\1/p' "$team_pkg/.codebuddy-plugin/plugin.json" | head -n1)"
    if [ "$tp_ver" != "$VERSION" ]; then echo "  FAIL WorkBuddy team pkg v$tp_ver != source v$VERSION (re-sync)"; blocked=1
    else echo "  OK   WorkBuddy team pkg v$tp_ver (matches source)"; fi
    declare -A m=(
      ["SOP five-state board"]="agents/research-analytics-team-team-lead.md:五态"
      ["contract TRAE column"]="orchestration/contract.md:TRAE（TraeWork"
      ["contract same-model degradation"]="orchestration/contract.md:降级"
      ["portable stop-loss"]="portable/SKILL.md:重复动作止损"
    )
    for k in "${!m[@]}"; do
      IFS=: read -r rel pat <<< "${m[$k]}"
      if grep -qF -- "$pat" "$team_pkg/$rel"; then echo "  OK   $k"
      else echo "  FAIL $k missing (stale snapshot)"; blocked=1; fi
    done
    echo "  ACTION: on next RAT session, TeamCreate a NEW team (not reusing old sessions) to pick up v$VERSION"
  else
    echo "  FAIL WorkBuddy team pkg not at $team_pkg (see README)"; blocked=1
  fi
  if [ "$blocked" = "1" ]; then echo "RESULT: FAIL - fix FAIL items above before launching."; exit 1
  else echo "RESULT: PASS - safe to launch (remember TeamCreate new, not old session)."; fi
  exit 0
fi

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
