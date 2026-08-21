## [0.7.1] - 2026-08-22

README 门面同步 + 检查 8 机制 token 守卫（SOP 内核零变化）。

### Fixed
- 中英 README 工程健壮性小节去除 stale 版本标签（v0.3.0），机制清单补齐：验收先行 / credit 双口径 / 域独立性裁决门 / 暂停线·待接管——与 0.6.0/0.7.0 实际交付对齐。
- 中英 README Files 节补列 settings.json。

### Added
- 检查 8 README_REQUIRED 扩展 4 枚机制 token（待接管 / credit / 验收标准 / 域独立性）——README 缺任一机制描述即 CI FAIL，堵住「机制已交付、README 未记载」的漂移通道。

## [0.7.0] - 2026-08-22

P1 批（全局最优 spec v1.2 · S1c + S2 + S3 + S4 + S7）：验收先行 + 六域路由 + 域独立性裁决 + credit 双口径 + 红线 CI 门禁。

### Added
- **S2 · 六域取数路由表（data-sourcer.md）**：D1–D6 平台分域首选源 / 降级路径 / 同源警告 / 启用条件——TRAE 侧 tdx（通达信）／wind-aifin／天眼一下／pkulaw 原生资产映射，WorkBuddy 侧 westock-mcp／yingmi／tyc-mcp／patsnap-search；编制铁律：**域是路由维度不是 subagent 编制**（4+1 角色不变，工具进武器库）。
- **S7 · 聚合网关多路探测 SOP（data-sourcer.md）**：AgentEarth 等聚合网关域能力判定四路探测缺一不可（① 关键词直查 ② 语义路由 ③ 厂商名探测 ④ 执行冒烟）；负向结论必标 `probe-scoped` 禁止外推（实证：同网关 keyword 直查与厂商名探测工具数 6 vs 122）；探测消耗计入 credit 口径。
- **S1c · 验收先行（team-lead.md Step 0）**：`dispatch` 前产出「验收标准（每条含度量锚点）＋ 终止条件三态（复用『最多 2 轮修订＋第 3 次强制通过』语义，不新增循环）」，交用户 1 轮确认；确认后记入《研究参数卡》推荐字段「验收标准」——与 dmr v2.6.0 Step 0 产出行对齐。
- **S3 · 域独立性检查（team-lead.md Phase 2 裁决前置）**：候选 `Confirmed` 结论的支撑源标采集域（D1–D6）；同域对（共享底层数据，典型如 tdx ＋ AgentEarth-Tushare 同引交易所公告）最高标 `Corroborated`，不得标 `Confirmed`；不修改 dmr 置信阈值定义，仅作裁决前置门。
- **S4 · credit 双口径（team-lead.md 全局预算器）**：聚合网关调用按 credit 计（调用数 × 0.5 credit/次），软预警线默认 30 credit/次调研，只预警不硬断；与次数口径（80% 预警）双轨并行，任一触发即广播「停止扩源、整理回传」。
- **CI 检查 11–13（红线 R1–R3 门禁）**：11 编制冻结（agents/ 恒为 5 个既定角色文件）；12 聚合网关限定词守卫（data-sourcer.md 中 agentearth/agentkey 每次出现处邻近 200 字符内必含「若平台已连 / 已连才启用」）；13 有界修订循环守卫（「最多 2 轮修订」＋「强制通过」token 在位，无无界语汇）。
- **`--self-test` 负向矩阵**：consistency_check.py 新增自测模式——3 例注入违例（第 6 个 agent 文件 / 无限定词网关提及 / 删强制通过 token），每例必须使门禁 FAIL；CI workflow 增自测步骤随门禁执行。（注：检查 12 负向例采用「注入无限定词提及」而非「删除单处限定词」——现行文本限定词密集，删除单处后邻近 200 字符内仍有其他限定词覆盖，不构成对规则本身的违例。）

### Changed
- dmr `requires` 由 `>=2.5.0 <3` 收紧为 `>=2.6.0 <3`（plugin.json ＋ team-lead frontmatter ＋ portable metadata 三处同步；团队现依赖 dmr v2.6.0 Step 0 验收先行与参数卡 schema）。
- README：CI 门禁 10 → 13 项（EN＋CN）；dmr pin 文本 2.3.4 → 2.6.0；新增 0.7.0 版本历史。
- data-sourcer.md 核心能力新增「六域路由取数」条目；工作流第 2 步接入六域路由表。

## [0.6.1] - 2026-08-20

一致性修复：消除与 dmr v2.5.0 的参数卡字段漂移 + 内部命名不一致。

### Fixed
- 研究参数卡「已收集来源池」池条目格式统一为 `实体 | 域 | 源URL | 层级 | 日期 | 置信`：修正内部 `层级Tier` 英文污染与 `URL`/`源URL` 术语不一致；明确 `域` 为团队采集分域（D1/D2/D3）编排扩展，dmr schema 基础 5 字段（实体/源URL/层级/日期/置信）以 `references/parameter-card-schema.md` 为唯一权威。
- 团队《研究参数卡》字段定义指针由 dmr 旧版「8 字段表」改为指向 dmr v2.5.0 结构化 schema（消除跨组件字段定义漂移）。

### Changed
- dmr `requires` 约束由 `>=2.3.4 <3` 收紧为 `>=2.5.0 <3`（团队现依赖 dmr v2.5.0 参数卡 schema 单一权威）。

## [0.6.0] - 2026-08-20

Pause-line / pending-takeover semantics (R3, multi-agent stop-resume engineering): member timeout no longer jumps straight to degradation — the run now has an explicit recovery plane (snapshot → pending-takeover → 3-branch adjudication) to pair with the existing stop plane (budget freeze / checkpoints / degradation disclosure).

### Added
- **contract.md pause-line section**: on member timeout / no-response — freeze the task (no immediate retry, batch rerun forbidden), snapshot first (budget spent + source-pool increments + items produced + unfinished list, piggybacked on the member checkpoint return), mark **pending-takeover (待接管)**, then the lead adjudicates exactly one of 3 branches: ① clean rerun (re-dispatch the same task card; pool evidence kept — the rerunner consumes from the pool, no re-fetching; rerun spends the **global slack only**, never raising the search cap, never re-allocating shares; ≤1 rerun per member) ② human takeover (via the intervention window, snapshot + gap disclosed) ③ accept degradation (per the existing failure/degradation table, gap into open questions). The `collect` iron rule now routes timeout through pending-takeover instead of straight degradation.
- **CI check 10 — pause-line guard**: contract.md must keep 待接管 + the 3 adjudication branches (清理重跑 / 人工接手 / 接受降级) + the rerun-budget rule (全局余量); team-lead and portable must stay in sync (待接管 + 全局余量 tokens in all three).

### Changed
- **team-lead SOP**: the "no full-retry on timeout" clause upgraded to the pause-line clause — checkpoint returns now double as execution snapshots; timeout goes through the 3-branch adjudication instead of jumping to the degraded product; fast-mode / no-confirm paths go straight to branch ③.
- **portable/SKILL.md**: the timeout-degradation bullet extended with the same pending-takeover adjudication, semantics deferred to contract.md.
- **README**: CI gate 9 → 10 checks (EN + CN), version history entry added; plugin.json description now lists the pause-line takeover mechanism.

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
