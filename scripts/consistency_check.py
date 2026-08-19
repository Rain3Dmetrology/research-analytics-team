#!/usr/bin/env python3
"""RAT consistency gate: single-source-of-truth checks (zero dependencies).

Fails the build when any of these drift:
  1. version parity: plugin.json == portable frontmatter == portable body note == latest CHANGELOG
  2. dmr requires-pin present in plugin.json, portable metadata, team-lead frontmatter
  3. README contains no bare-github attribution dead link
  4. agent manifest parity: agents/ dir == plugin.json agents == teamInfo roster
  5. every agent file still references the dmr core
  6. robustness-mechanism regression guards: every member file keeps its maxTurns
     checkpoint obligation; team-lead keeps budget governor / domain pre-allocation /
     two-phase pool / run-manifest / adjudication-path; portable stays in sync
  7. annex demotion guard (audit A1): portable must not claim single-session
     equivalence or own research-intent routing; dmr owns intent routing
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIN_NAME = "deep-market-research"
PIN_RANGE = re.compile(r">=\s*2\.\d+\.\d+\s*<\s*3")
errors = []


def fail(msg):
    errors.append(msg)


# --- load artifacts ---------------------------------------------------------
pj = json.loads((ROOT / ".codebuddy-plugin" / "plugin.json").read_text(encoding="utf-8"))
pj_version = pj.get("version", "")

portable_path = ROOT / "portable" / "SKILL.md"
portable = portable_path.read_text(encoding="utf-8")

changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")

lead_path = ROOT / "agents" / "research-analytics-team-team-lead.md"
lead = lead_path.read_text(encoding="utf-8")

# --- 1. version parity ------------------------------------------------------
m = re.search(r'^\s*version:\s*"?(\d+\.\d+\.\d+)"?\s*$', portable, re.M)
portable_fm_version = m.group(1) if m else None

m = re.search(r"版本\s*(\d+\.\d+\.\d+)", portable)
portable_body_version = m.group(1) if m else None

m = re.search(r"^##\s*\[(\d+\.\d+\.\d+)\]", changelog, re.M)
cl_version = m.group(1) if m else None

versions = {
    "plugin.json": pj_version,
    "portable frontmatter": portable_fm_version,
    "portable body note": portable_body_version,
    "latest CHANGELOG": cl_version,
}
if len(set(versions.values())) != 1 or None in versions.values():
    fail(f"version parity broken: {versions}")

# --- 2. dmr requires pin ----------------------------------------------------
pj_req = pj.get("requires", {}).get(PIN_NAME, "")
if not pj_req or not PIN_RANGE.search(pj_req):
    fail(f"plugin.json requires['{PIN_NAME}'] missing or malformed (expected '>=2.x.y <3'), got: {pj_req!r}")

m = re.search(r'^\s*requires:\s*"?' + re.escape(PIN_NAME) + r'[^"\n]*"?$', portable, re.M)
if not m or not PIN_RANGE.search(m.group(0)):
    fail("portable/SKILL.md metadata missing requires pin for deep-market-research (>=2.x <3)")

m = re.search(r'^requires:\s*"?' + re.escape(PIN_NAME) + r'[^"\n]*"?$', lead, re.M)
if not m or not PIN_RANGE.search(m.group(0)):
    fail("team-lead frontmatter missing requires pin for deep-market-research (>=2.x <3)")

# --- 3. README dead-link check ---------------------------------------------
if re.search(r"\]\(\s*https://github\.com/?\s*\)", readme):
    fail("README contains a bare github.com attribution link (dead link)")

# --- 4. agent manifest parity ----------------------------------------------
agent_files = sorted(p.name for p in (ROOT / "agents").glob("*.md"))
pj_agents = sorted(a.replace("./agents/", "") for a in pj.get("agents", []))
if agent_files != pj_agents:
    fail(f"agents/ dir mismatch: on-disk={agent_files} vs plugin.json={pj_agents}")

team = pj.get("teamInfo", {})
roster = sorted(team.get("memberAgents", []) + [team.get("leadAgent", "")])
member_ids = sorted(m.get("id", "") for m in pj.get("members", []))
if roster != member_ids:
    fail(f"teamInfo roster mismatch: roster={roster} vs members={member_ids}")

# --- 5. dmr reference integrity --------------------------------------------
for f in agent_files:
    txt = (ROOT / "agents" / f).read_text(encoding="utf-8")
    if PIN_NAME not in txt:
        fail(f"agents/{f} no longer references the dmr core")

# --- 6. robustness-mechanism regression guards ------------------------------
member_files = [f for f in agent_files if f != lead_path.name]
for f in member_files:
    txt = (ROOT / "agents" / f).read_text(encoding="utf-8")
    if "maxTurns checkpoint" not in txt:
        fail(f"agents/{f} lost its 'maxTurns checkpoint 义务' section (timeout-degradation contract)")
    if "结构化摘要" not in txt:
        fail(f"agents/{f} lost the structured-digest return contract (lead context overload guard)")

LEAD_GUARDS = [
    "全局预算器",
    "分域预分配",
    "两段式",
    "run-manifest",
    "裁决路径",
    "渲染收敛",
    "介入窗口",
]
for token in LEAD_GUARDS:
    if token not in lead:
        fail(f"team-lead SOP lost robustness mechanism token: {token!r}")

PORTABLE_GUARDS = ["资产路由", "全局预算器", "分域预分配", "run-manifest", "裁决路径"]
for token in PORTABLE_GUARDS:
    if token not in portable:
        fail(f"portable/SKILL.md out of sync with team-lead SOP (missing token: {token!r})")

# --- 7. annex demotion guard (audit A1) --------------------------------------
ANNEX_PORTABLE_GUARDS = [
    "不再自称单会话等价实现",  # demotion declaration must stay
    "不响应调研类触发词",      # must not own research-intent routing
    "挂载方式与资产路由表",    # annex positioning section must stay
]
for token in ANNEX_PORTABLE_GUARDS:
    if token not in portable:
        fail(f"portable/SKILL.md annex demotion (audit A1) regressed: missing token {token!r}")
if "降维为平台资产路由 annex" not in lead:
    fail("team-lead SOP lost the portable annex-demotion statement (audit A1)")

# --- report -----------------------------------------------------------------
if errors:
    print("CONSISTENCY GATE FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"CONSISTENCY GATE PASSED (v{pj_version}, pin {pj_req})")
