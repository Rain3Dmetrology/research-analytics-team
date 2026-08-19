## [0.5.0] - 2026-08-20

Primitive downshift (audit M2, R2-B): platform verbs leave the agent bodies — orchestration now speaks contract verbs only; platform syntax lives exclusively in `orchestration/contract.md`.

### Changed
- **agent bodies de-coupled from WorkBuddy syntax**: team-lead's 10 platform-verb occurrences (TeamCreate / spawn / SendMessage / subagent_type) replaced with contract verbs — `assemble`（组队）/ `dispatch`（派单）/ `collect`（收编）— each pointing to the contract adapter table; forbidden-behavior and budget-governor sections re-phrased on contract verbs with identical semantics.
- **member agents return via `collect`**: the "SendMessage 回传" sections in all 4 member files renamed to "回传（`collect` 契约）"; return semantics unchanged (structured digest to the lead).
- **portable/SKILL.md**: 3 platform-verb occurrences replaced with `dispatch` wording (domain pre-allocation + two-phase pool clauses unchanged).
- **collaboration rule 5 parameter details moved into contract.md**: the Agent-tool `name`/`subagent_type` member-ID resolution rules now live in contract.md's "WorkBuddy 适配参数细则"; team-lead rule 5 references the contract instead of restating.
- **README**: fast-mode line re-phrased on contract verbs; CI check 8 description updated.

### Added
- **contract.md WorkBuddy adapter parameter details**: Agent-tool parameter rules (name/subagent_type = member Agent ID, no Chinese/self-invented names), assemble/collect message-relay iron rule, and the wall-clock SLA accounting basis (`assemble` completion for std / first step for fast).
- **CI check 8 primitive-ban guard**: TeamCreate / spawn / SendMessage / subagent_type are banned outside `orchestration/contract.md` — agents/, portable/SKILL.md, and README are scanned; reintroducing any platform verb fails the build.

## [0.4.0] - 2026-08-20

Contract layer (audit M2, R2-A): orchestration primitives de-coupled from any single platform — pure additive change, agent bodies untouched.

### Added
- **`orchestration/contract.md` — platform-agnostic orchestration contract**: 3 contract verbs (`assemble` 组队 / `dispatch` 派单 / `collect` 收编) with semantics, pre/post-conditions, and iron rules; a 3-platform adapter table (WorkBuddy / Coze / single-thread); failure-and-degradation adapters; Coze-specific constraints.
- **Coze constraints codified**: sub-sessions do not inherit Skills → `dispatch` must inline the full param card (role digest + task card + dmr adjudication essentials) into the sub-session prompt; schedule triggers drive template-E monitoring increments (no full rewrites, aligned with dmr v2.4.0).
- **CI check 9 — orchestration contract guard**: contract.md must exist, define all 3 verbs, carry the 3-platform table with the Coze no-skill-inheritance constraint and schedule-trigger path, stay ≤150 lines (thin contract, not another SOP), and be referenced by team-lead.
- **team-lead step 0**: "启动第一步读适配表" — the lead reads the adapter table before Phase 1 to resolve the current platform's verb mapping; platform syntax in the SOP body is explicitly scoped as the WorkBuddy adaptation.

## [0.3.0] - 2026-08-20

Coze cross-audit batch: resolves 8 coze findings (M1 / M3 / V1 / V2 / V4 / D1 / D2 / D5) + asset slimming (D4). Positioning and mechanism drift is now CI-enforced, not promised.

### Changed
- **M1 — README three-layer re-alignment**: README rewritten around dmr (credibility kernel + the only research entry) / this repo (team-orchestration form) / `portable/SKILL.md` (asset-routing annex, never auto-triggered); templates A–E coverage restored; CI check-count description synced with the script — all four drift spots closed.
- **M3 — fast-mode single-thread rule**: fast mode defaults to single-thread (lead runs dmr Step 1/4/8 directly, ≤10-min SLA), TeamCreate/spawn only on explicit user request; scheduling-failure fallback to single-thread is reclassified as an exception path — the ≤10-min SLA vs. team-overhead contradiction is dissolved.
- **D1 — single threshold definition**: the "≥2 独立 Tier1–3 源确认" threshold now lives once in the team-lead preamble; Phase-2 adjudication and the 6-dim QC gate reference it instead of restating the number; CI guards occurrence count == 1.
- **D5 — checkpoint de-magicked**: all four member agents base the ≤20% checkpoint on their own frontmatter `maxTurns` instead of the hardcoded "约第 40 轮起，maxTurns=50"; CI forbids reintroduction of the magic number.
- **V2 — connector registry routing**: team-lead member-capability list and the portable asset table now route connector status/usage to dmr `references/data-sources.md` as the single registry (quote-don't-copy), with an all-connectors-failed → default-layer fallback disclosed in the report; CI guards both references.
- **plugin.json**: description de-drifted (templates A–E, annex positioning, budget-governor mechanisms) + `patsnap` typo fix.

### Added
- **CI check 8 — README drift guard**: forbids "two form factors" / "两种形态" (annex demotion wording), requires the annex wording / templates A–E / no-trigger pledge, and enforces that the README-stated CI check count matches the script.
- **V1 — honest budget-counting clause**: search-cap enforcement distinguishes platform hard limits from lead self-counting; actual consumption and counting basis (hard-limit / self-count) are recorded in run-manifest.json; self-counting must never be presented as platform-enforced in methodology statements.
- **V4 — adversarial-audit floor (non-degradable)**: critics must be role-swapped (external model in its own identity; same-model fallback must declare an "opposing reviewer" stance and attack after restating), each critic class produces a ≥3-item counter-evidence list (0 items = not executed), and counter-evidence must land in the contradiction ledger or open questions — never silently dropped.
- **D2 — three-QC-layer single responsibility**: 6-dim QC (structural coverage) / adversarial audit (counter-evidence & balance) / lint (format & citations) declared non-interchangeable; any missing layer must be disclosed in the methodology statement.

### Fixed
- **D4 — avatar slimming**: 6 avatars resampled to 256×256 with 256-color quantization; repo blob total 6.81 MB → <1 MB (per-image ≤18 KB), manifest paths unchanged.

## [0.2.1] - 2026-08-19

Audit follow-up batch: resolves remaining findings A1 / A5 + CI modernization. Closes all 25 findings from the dmr-RAT 2026 audit (A1 here; C8/D3/D4 resolved on the dmr side as v2.4.0).

### Changed
- **A1 — portable demoted to platform-asset-routing annex**: `portable/SKILL.md` no longer claims to be the "equivalent single-session implementation" and no longer owns research-intent routing. Trigger words (调研/竞品/尽调/扒一下/挖一下/对标/对位/市场测算) are explicitly ceded to dmr §七; the annex mounts only via (a) explicit dmr Step-1 reference or (b) explicit user request for asset routing / connector mapping / parallel-collection orchestration. Intent-routing rows removed from its routing table (now a dmr-demand-driven asset table); source_of_truth split explicitly (dmr owns research SOP, team-lead owns team orchestration). team-lead intro and robustness preamble updated to match.
- **A5 residual — template de-duplication in agents**: industry-competitor-researcher no longer re-states template B five-section / template C four-dimension internals; both now reference dmr `references/templates.md` B/C as the single authority (quote-don't-copy), plus lens library pointer to `references/optional-modules.md`.
- **Template E alignment**: Step-0 routing gains the monitoring-increment path (周报/月报/持续监测 with prior snapshot → template E, delta-only, no full rewrite), matching dmr v2.4.0.
- CI: actions/checkout@v5 + actions/setup-python@v6 (clears Node-20 deprecation warnings).

### Added
- **CI gate check 7 (annex-demotion guard)**: fails if portable drops its demotion declaration, its no-intent-routing pledge, or its mounting/asset-table section, or if team-lead drops the annex-demotion statement — A1's resolution is now enforced, not promised.

## [0.2.0] - 2026-08-19

Audit P1 batch: engineering-robustness mechanisms promoted from prose promises to enforced SOP + CI guards. Resolves findings B3 / C1 / C2 / A2 / A3 / A4 / B2 / B4 / B5 / B6 / C4 / C5 / C7 / C9 / D1 / D2 from the dmr-RAT 2026 audit.

### Added
- **C1 global budget governor** (team-lead SOP §工程健壮性机制·0): wall-clock SLA (std ≤30 min / fast ≤10 min) + total search cap (≤60, Phase1 members ≤15 each, lead review ≤10), 80% early-warning broadcast, 100% freeze → degraded skeleton delivery with budget-truncation disclosure.
- **C2 two-phase source pool**: Phase1-pre domain pre-allocation (D1 academic/official, D2 Chinese UGC, D3 quantitative — one owner per entity×domain) kills parallel write-blind duplication; Phase2 merge adjudication (higher-Tier/newer-date wins, conflicts → contradiction ledger) is now the sole post-Phase1 evidence entry.
- **B3 member checkpoint obligations**: all four member agents gained a "maxTurns checkpoint 义务" section — at ≤20% remaining turns or lead budget warning: stop new collection, immediately return structured partial output (no hang / no silent exit / no discarded evidence), matching the lead's timeout-degradation table.
- **C7/D2 run-manifest.json**: every run archives query / param-card snapshot / final source pool / adjudication decisions / component versions (dmr pin + team version) / budget consumption / degradation events — reproducibility upgraded from process promise to runtime artifact.
- **B5 knowledge archival**: Phase N closing triple — dmr §七-aligned structured note (entity-level evidence cache, mandatory pre-read on re-runs), run manifest, next-run warmup hint.
- **D1 intervention windows**: stage-boundary progress notifications now open an explicit continue/pivot/supplement window (fast path exempt); mid-run additions → pool write + partial recompute.
- **C4 externalized adversarial audit**: ≥1 of the ≥2 critic classes routes to external models first (ask-opencli Grok/Gemini, or multi-ai-research, if platform-connected); fallback to same-model critic with explicit "同模自评" disclosure.
- **C1 budget line in progress notifications** + **A4 dual-axis quality report** (dmr 100-point scorecard + confidence distribution) + **B2 adjudication-path field** in methodology statements.
- **CI gate check 6 (robustness regression guards)**: member files must keep checkpoint + structured-digest contracts; team-lead must keep budget governor / domain pre-allocation / two-phase pool / run-manifest / adjudication-path / render-convergence / intervention-window tokens; portable must stay in sync.

### Changed
- **B4 render convergence**: Phase1 members now produce item-level structured finding lists only (no prose rendering); full-report rendering happens exactly once at Phase N — eliminates double rendering (est. 30–40% token waste) and inter-render drift.
- **C5 structured return contract**: members return ≤300-char digest + structured tables (not prose); lead assembles per-chapter and rolls off assembled content (context-overload guard).
- **A2/B6 QC wording aligned to dmr**: 6-dimension definitions and round semantics are owned by dmr Phase3 (chapter-level, max 3 rounds, forced pass with residual improvements); the lead's final gate is a re-check, not a re-definition.
- **A3 param card**: research param card references the dmr Step-0 8-field superset (no schema duplication), adds domain-assignment and budget rows.

### Fixed
- **C9 measurement-discipline gaps** (data-analyst): cross-currency normalization (rate + as-of date), TAM/SAM/SOM three-scenario ranges (no single-point precision theater), paid-report secondhand citation chains with circular-reference detection, structural-proxy anchors (customs / patent trends / listed-company segment triangulation).

## [0.1.2] - 2026-08-19

### Added
- Version pin: `requires: "deep-market-research >=2.3.4 <3"` declared in three places (`.codebuddy-plugin/plugin.json`, team-lead frontmatter, `portable/SKILL.md` metadata) — dmr core upgrades now require explicit review, preventing silent template drift.
- CI single-source-of-truth gate (`.github/workflows/consistency-gate.yml` + `scripts/consistency_check.py`): version parity across plugin.json / portable frontmatter / portable body note / latest CHANGELOG entry; requires-pin presence in all three declaration sites; README dead-link check (bare `github.com` attribution); agent-manifest parity (agents/ dir vs plugin.json agents + teamInfo members); dmr reference integrity in every agent file.

### Fixed
- `portable/SKILL.md` body version note (0.1.0) contradicted its own frontmatter (0.1.1) — unified to 0.1.2.
- README attribution linked dmr to bare `https://github.com/` (dead link) — now points to the real repository.

## [0.1.1] - 2026-08-19

### Changed
- 甄势析（industry-competitor-researcher）：补 R6/R7 低优先风险修复（重建版，原审计文本未持久化）。
  - R6 来源池回写：发现的高质量一手源（官方/IR/专利/财报/工商/权威报告）须回写《研究参数卡·已收集来源池》供 data-sourcer/计详实 复用。
  - R7 反向/负面证据检索义务 + 证据缺席声明：主动找反证，检索未见强反证时须显式声明「证据缺席≠无风险」，禁止沉默通过。

## [0.1.0] - 2026-08-19

### Added
- Team-type expert package (5 roles) with dmr credibility core: T1–T4 source grading, ≥2/≥3-source cross-validation, templates B/C, contradiction ledger, adversarial audit, confidence labels.
- Engineering robustness mechanisms: timeout degradation table, failure fallback, progress-notification template, cross-phase source-pool reuse.
- Phase N 6-dimension QC checklist + bounded 2-round revise loop (forced pass at round 3, residual → open issues).
- Candidate-confidence semantics: members label candidate confidence; lead finalizes at Phase2 after fusing data-sourcer structured evidence.
- `wechat-article-search` preload for the industry-competitor researcher (Tier 3–4 supplement).
- Portable single-session `portable/SKILL.md` for Trae / Cursor / CodeBuddy (same SOP, cross-platform).

### Changed
- Compressed Coze-absorption / anti-bloat rationale prose into a concise rule list for a lean published build.
- Generalized personal venv and install paths for portability (no user-specific disk paths in tracked files).
