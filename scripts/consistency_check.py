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
     equivalence or own research-intent routing; dmr owns intent routing;
     connector usage in lead + portable must route to the dmr registry
     (references/data-sources.md)
  8. README drift guard (audit M1) + primitive-ban (audit M2, R2-B): README must
     keep the three-layer positioning (no "two form factors" / "两种形态"),
     must mention the annex role, templates A-E, the portable no-trigger
     pledge, and must state the actual CI check count; platform primitives
     (TeamCreate / spawn / SendMessage / subagent_type) are banned outside
     orchestration/contract.md (agents / portable / README scanned)
  9. orchestration contract guard (audit M2, R2-A): orchestration/contract.md
     exists, defines the 3 contract verbs (assemble / dispatch / collect),
     carries the 3-platform adapter table (WorkBuddy / Coze / single-thread)
     with the Coze no-skill-inheritance constraint, stays <= 150 lines, and
     is referenced by the team-lead SOP
 10. pause-line guard (R3): contract.md must keep the pause-line /
     pending-takeover semantics (待接管 + 3 adjudication branches: 清理重跑 /
     人工接手 / 接受降级) and the rerun-budget rule (全局余量, never raising
     the search cap); team-lead SOP and portable must stay in sync (待接管 +
     全局余量 tokens in all three)
 11. agent-roster freeze (red line R1): agents/ stays exactly the 5 fixed
     role files — six-domain routing is a table, not extra headcount;
     data-source-bound subagents are forbidden
 12. aggregation-gateway qualifier guard (red line R2): every
     agentearth/agentkey mention in data-sourcer.md must carry a
     conditional qualifier (若平台已连 / 已连才启用) within 200 chars —
     gateways stay optional enhancement layers, never hardwired sources
 13. bounded revise-loop guard (red line R3): team-lead keeps the
     "最多 2 轮修订" + "强制通过" termination tokens and carries no
     unbounded-loop vocabulary

`--self-test` runs the negative matrix: 3 injected violations, each must
FAIL the gate (red lines ship with their negative tests).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIN_NAME = "deep-market-research"
PIN_RANGE = re.compile(r">=\s*2\.\d+\.\d+\s*<\s*3")
errors = []


def fail(msg):
    errors.append(msg)


# --- negative matrix (red lines R1-R3 ship with their negative tests) --------
def _negative_case(name, mutate, expect):
    """Inject a violation into a throwaway copy of the repo; the gate must FAIL."""
    with tempfile.TemporaryDirectory(prefix="rat-gate-neg-") as tmp:
        tree = Path(tmp) / "repo"
        shutil.copytree(ROOT, tree, ignore=shutil.ignore_patterns(".git"))
        mutate(tree)
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        proc = subprocess.run(
            [sys.executable, str(tree / "scripts" / "consistency_check.py")],
            capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
        )
        out = (proc.stdout or "") + (proc.stderr or "")
        if proc.returncode == 0:
            print(f"SELF-TEST FAILED [{name}]: gate PASSED although a violation was injected")
            sys.exit(1)
        if expect not in out:
            print(f"SELF-TEST FAILED [{name}]: gate failed but without the expected message {expect!r}\n{out}")
            sys.exit(1)
        print(f"  negative case OK [{name}] -> gate failed as required")


def _run_self_test():
    print("SELF-TEST: negative matrix (3 injected violations must each FAIL the gate)")

    def n11_inject_sixth_agent(tree):
        # crafted to pass checks 4-partial/5/6/8 so the failure isolates check 11 (+4 parity)
        (tree / "agents" / "data-sourcer-finance.md").write_text(
            "---\n"
            "name: data-sourcer-finance\n"
            "description: Injected sixth member (negative test for agent-roster freeze).\n"
            "maxTurns: 50\n"
            "skills: [deep-market-research]\n"
            "---\n\n"
            "# 负向注入：第 6 个数据源绑定型成员\n\n"
            "引用 deep-market-research 内核。\n\n"
            "## maxTurns checkpoint 义务\n"
            "- 剩余轮次不足时回传结构化摘要。\n",
            encoding="utf-8",
        )

    def n12_inject_bare_gateway_mention(tree):
        p = tree / "agents" / "data-sourcer.md"
        txt = p.read_text(encoding="utf-8")
        # append a bare gateway mention at EOF, far (>200 chars) from every
        # qualifier — a faithful violation of the rule itself. (Deleting one
        # qualifier is NOT: the file's qualifiers are dense enough that a
        # neighbor still covers the mention within 200 chars.)
        p.write_text(
            txt + "\n\n## injected bare gateway mention (negative test)\n\n"
                  "AgentEarth direct access and agentkey direct access configuration.\n",
            encoding="utf-8",
        )

    def n13_drop_forced_pass_token(tree):
        p = tree / "agents" / "research-analytics-team-team-lead.md"
        txt = p.read_text(encoding="utf-8")
        p.write_text(txt.replace("强制通过", "通过"), encoding="utf-8")

    _negative_case(
        "check 11 / R1: 6th data-source-bound agent file injected",
        n11_inject_sixth_agent,
        "agent-roster freeze",
    )
    _negative_case(
        "check 12 / R2: bare gateway mention injected without a qualifier",
        n12_inject_bare_gateway_mention,
        "aggregation-gateway qualifier guard",
    )
    _negative_case(
        "check 13 / R3: 强制通过 termination token dropped from team-lead",
        n13_drop_forced_pass_token,
        "bounded revise-loop guard",
    )
    print("SELF-TEST PASSED: 3 negative injections all failed the gate as required")


if "--self-test" in sys.argv[1:]:
    _run_self_test()
    sys.exit(0)


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
    if "第 40 轮" in txt:
        fail(f"agents/{f} reintroduced a magic-number checkpoint ('第 40 轮'); base it on frontmatter maxTurns (audit D5)")

LEAD_GUARDS = [
    "全局预算器",
    "分域预分配",
    "两段式",
    "run-manifest",
    "裁决路径",
    "渲染收敛",
    "介入窗口",
    "快版默认单线程",    # audit M3 (R1-2)
    "计数口径诚实条款",  # audit V1 (R1-3)
    "反证清单",          # audit V4 (R1-4)
    "不可互相替代",      # audit D2 (R1-8)
]
for token in LEAD_GUARDS:
    if token not in lead:
        fail(f"team-lead SOP lost robustness mechanism token: {token!r}")

THRESHOLD_TOKEN = "≥2 独立 Tier1–3"
threshold_count = lead.count(THRESHOLD_TOKEN)
if threshold_count != 1:
    fail(f"team-lead must define the cross-validation threshold exactly once (audit D1), found {threshold_count} occurrences of {THRESHOLD_TOKEN!r}")

PORTABLE_GUARDS = ["资产路由", "全局预算器", "分域预分配", "run-manifest", "裁决路径", "待接管"]
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

REGISTRY_REF = "references/data-sources.md"
if REGISTRY_REF not in lead:
    fail(f"team-lead must route connector usage to the dmr registry ({REGISTRY_REF}) as the single source of truth (audit V2)")
if REGISTRY_REF not in portable:
    fail(f"portable/SKILL.md must route connector usage to the dmr registry ({REGISTRY_REF}) as the single source of truth (audit V2)")

# --- 8. README drift guard (audit M1) ----------------------------------------
CHECK_COUNT = 13
README_FORBIDDEN = [
    "two form factors",  # v0.2.1+ is three-layer positioning; portable is an annex, not an equal form
    "两种形态",            # CN mirror of the same drift
]
README_REQUIRED = [
    "annex",        # three-layer positioning must keep the annex wording
    "A–E",          # dmr templates A-E, not B/C only
    "不响应调研",    # portable documented as non-trigger
    "待接管",        # 0.6.0 pause-line/takeover semantics must stay documented
    "credit",       # 0.7.0 gateway-credit budget track must stay documented
    "验收标准",      # 0.7.0 acceptance-first (aligned with dmr Step 0) must stay documented
    "域独立性",      # 0.7.0 same-domain-source cap (Corroborated, not Confirmed) must stay documented
]
for token in README_FORBIDDEN:
    if token in readme:
        fail(f"README drift (audit M1): forbidden token {token!r} — since v0.2.1 portable is an annex, not an equal form factor")
for token in README_REQUIRED:
    if token not in readme:
        fail(f"README drift (audit M1): README missing required token {token!r}")

en_m = re.search(r"(\d+)\s+consistency checks", readme)
cn_m = re.search(r"(\d+)\s*项一致性检查", readme)
if not en_m or int(en_m.group(1)) != CHECK_COUNT:
    fail(f"README EN section must state the actual CI check count ({CHECK_COUNT})")
if not cn_m or int(cn_m.group(1)) != CHECK_COUNT:
    fail(f"README CN section must state the actual CI check count ({CHECK_COUNT})")

# primitive-ban guard (audit M2, R2-B): platform syntax lives ONLY in contract.md
PRIMITIVE_TOKENS = ("TeamCreate", "spawn", "SendMessage", "subagent_type")
for rel in [f"agents/{f}" for f in agent_files] + ["portable/SKILL.md", "README.md"]:
    txt = (ROOT / rel).read_text(encoding="utf-8")
    for tok in PRIMITIVE_TOKENS:
        if tok in txt:
            fail(f"{rel} contains platform primitive {tok!r} — use contract verbs; platform syntax lives only in orchestration/contract.md (audit M2, R2-B)")

# --- 9. orchestration contract guard (audit M2, R2-A) -------------------------
contract_path = ROOT / "orchestration" / "contract.md"
if not contract_path.exists():
    fail("orchestration/contract.md missing — the contract layer is required (audit M2, R2-A)")
else:
    contract = contract_path.read_text(encoding="utf-8")
    for verb in ("assemble", "dispatch", "collect"):
        if verb not in contract:
            fail(f"orchestration/contract.md missing contract verb {verb!r}")
    for platform in ("WorkBuddy", "Coze", "单线程"):
        if platform not in contract:
            fail(f"orchestration/contract.md adapter table missing platform {platform!r}")
    if "子会话不继承 Skills" not in contract:
        fail("orchestration/contract.md missing the Coze no-skill-inheritance constraint (dispatch must inline the param card)")
    if "日程" not in contract:
        fail("orchestration/contract.md missing the Coze schedule-trigger path (template E monitoring)")
    contract_lines = contract.count("\n") + 1
    if contract_lines > 150:
        fail(f"orchestration/contract.md exceeds 150 lines ({contract_lines}) — keep it a thin contract, not another SOP")
    if "orchestration/contract.md" not in lead:
        fail("team-lead SOP must reference orchestration/contract.md as the first startup step (audit M2)")

# --- 10. pause-line / pending-takeover guard (R3) ------------------------------
if contract_path.exists():
    contract_text = contract_path.read_text(encoding="utf-8")
    for token in ("待接管", "清理重跑", "人工接手", "接受降级", "全局余量"):
        if token not in contract_text:
            fail(f"orchestration/contract.md pause-line guard (R3): missing token {token!r}")
else:
    fail("orchestration/contract.md missing — pause-line semantics cannot be verified (R3)")

for token in ("待接管", "清理重跑", "全局余量"):
    if token not in lead:
        fail(f"team-lead SOP pause-line guard (R3): missing token {token!r}")

for token in ("待接管", "全局余量"):
    if token not in portable:
        fail(f"portable/SKILL.md pause-line guard (R3): missing token {token!r}")

# --- 11. agent-roster freeze (red line R1) --------------------------------------
# Six-domain routing is a table carried by data-sourcer, not extra headcount:
# the 4+1 roster is frozen; data-source-bound subagents are forbidden.
AGENT_FREEZE = [
    "data-analyst.md",
    "data-sourcer.md",
    "industry-competitor-researcher.md",
    "research-analytics-team-team-lead.md",
    "visualizer.md",
]
if agent_files != AGENT_FREEZE:
    fail(f"agent-roster freeze (R1): agents/ must stay exactly the 5 fixed role files {AGENT_FREEZE}; data-source-bound subagents are forbidden, got {agent_files}")

# --- 12. aggregation-gateway qualifier guard (red line R2) ----------------------
# AgentEarth/agentkey are optional enhancement layers, never hardwired domain
# sources: every mention in data-sourcer.md must sit next to a conditional
# qualifier (若平台已连 / 已连才启用) within 200 chars.
GATEWAY_RE = re.compile(r"agentearth|agentkey", re.IGNORECASE)
GATEWAY_QUALIFIERS = ("若平台已连", "已连才启用")
GATEWAY_PROXIMITY = 200
sourcer = (ROOT / "agents" / "data-sourcer.md").read_text(encoding="utf-8")
for gm in GATEWAY_RE.finditer(sourcer):
    window = sourcer[max(0, gm.start() - GATEWAY_PROXIMITY): gm.end() + GATEWAY_PROXIMITY]
    if not any(q in window for q in GATEWAY_QUALIFIERS):
        fail(
            f"aggregation-gateway qualifier guard (R2): {gm.group(0)!r} at offset {gm.start()} in "
            f"agents/data-sourcer.md has no conditional qualifier ({' / '.join(GATEWAY_QUALIFIERS)}) "
            f"within {GATEWAY_PROXIMITY} chars — gateways are optional enhancement layers, never hardwired sources"
        )

# --- 13. bounded revise-loop guard (red line R3) --------------------------------
# The acceptance/revise loop must keep its termination tokens and must not
# pick up unbounded-loop vocabulary.
for token in ("最多 2 轮修订", "强制通过"):
    if token not in lead:
        fail(f"bounded revise-loop guard (R3): team-lead lost termination token {token!r}")
for token in ("无限循环", "直到满意", "直到完美", "不限轮次", "无上限修订"):
    if token in lead:
        fail(f"bounded revise-loop guard (R3): team-lead contains unbounded-loop vocabulary {token!r}")

# --- report -----------------------------------------------------------------
if errors:
    print("CONSISTENCY GATE FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"CONSISTENCY GATE PASSED (v{pj_version}, pin {pj_req})")
