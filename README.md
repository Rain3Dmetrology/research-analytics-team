# Research Analytics Team

[English](#english) | [中文](#中文)

<a id="english"></a>
## English

### Why this exists
- Deep research (industry / competitor / company / market / academic / monitoring) that is **source-graded, cross-validated, confidence-labeled, and reproducible** — output quality no longer depends on which machine or which agent platform you happen to be on.
- Kills the pain of ad-hoc research: inconsistent depth, unsourced claims, and non-reproducible results when you switch devices or agents.

### Three layers, one kernel
- **deep-market-research (dmr) = the credibility core and the only research entry.** It owns research-intent routing and the single-session SOP (Step 0–8), report templates A–E (general / industry five-segment / competitor four-dimension / academic / monitoring-increment), T1–T4 source grading, ≥2-source cross-validation, contradiction ledger, adversarial audit, and confidence labels.
- **This repo = the team-orchestration form (WorkBuddy Team expert package).** 5 roles (lead editor + 4 members) with a global budget governor, two-phase source pool, run-manifest archival, timeout degradation, and a bounded revise loop.
- **`portable/SKILL.md` = a platform asset-routing annex, NOT a research entry.** It does not respond to research triggers (`调研 / 竞品 / 尽调 / …` are all owned by dmr). It mounts only when dmr Step 1 — or an explicit user request — needs platform assets: connectors, xlsx/Python modeling, visualization, parallel collection.

### Install
- **One-click (annex form)**: run `install.ps1` (Windows) or `./install.sh` (Unix) — copies `portable/SKILL.md` into every detected platform's skills directory as `research-orchestrator` and warns when the installed dmr copy is below the required pin.
- **WorkBuddy (team form)**: clone this repo, copy the repo root into `~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/`, then enable it in the Expert Center.
- **Other platforms (annex form)**: copy `portable/SKILL.md` into your platform's skills directory. Research intent still routes through dmr; the annex only adds asset routing.

### Usage
- **WorkBuddy**: select the expert, or type a trigger like `调研 [行业/赛道] 的竞争格局与趋势` — the lead runs the full SOP with the 4-member team.
- **Fast mode**: single-threaded by default — the lead runs dmr Step 1/4/8 directly (≤10 min SLA), skipping team assembly (`assemble`/`dispatch`) unless a team is explicitly requested.
- **Portable annex**: never auto-triggers on research words. Ask explicitly for asset routing / connector mapping / parallel collection, or let dmr Step 1 mount it.

### Engineering robustness
- **Acceptance-first**: before `dispatch` the lead produces acceptance criteria (each with a measurable anchor) + three-state termination conditions (criteria met / budget exhausted / max N rounds), confirmed by the user in one round — aligned with dmr Step 0.
- **Budget governor**: wall-clock SLA (std ≤30 min / fast ≤10 min) + search cap ≤60 with an honest counting clause (hard limit vs self-count, disclosed in the run manifest), 80% early warning / 100% freeze → degraded delivery; gateway (AgentEarth etc., if connected) calls tracked on a credit track (calls × 0.5 credit each, soft warning line 30).
- **Two-phase source pool**: Phase-1 domain pre-allocation (academic / Chinese UGC / quantitative — one owner per entity×domain) kills duplicate collection; Phase-2 merge adjudication is the only evidence entry.
- **Domain-independence adjudication gate**: every candidate `Confirmed` conclusion gets its supporting sources tagged by collection domain (D1–D6); a same-domain source pair caps the label at `Corroborated`.
- **run-manifest.json** per run: query, param card, final source pool, adjudication decisions, component versions, budget consumption, degradation events.
- **Adversarial audit floor**: role-swapped critics (external model, or a declared "opposing reviewer" on same-model fallback), each producing a ≥3-item counter-evidence list that must land in the contradiction ledger.
- **Three QC layers, non-interchangeable**: 6-dimension gate (coverage) / adversarial audit (counter-evidence) / lint (format & citations) — missing any layer must be disclosed.
- **Member checkpoint obligations**: at ≤20% remaining turns (per each agent's own frontmatter maxTurns) or budget warning — stop collecting, return a structured digest.
- **Pause-line / pending-takeover**: a timed-out member freezes a snapshot (budget used, source increments, done/pending) and is marked pending-takeover; the lead then adjudicates among clean rerun (global slack only) / manual takeover / accept degradation.

### Files
- `.codebuddy-plugin/plugin.json` — package manifest (incl. `requires: deep-market-research >=2.7.0 <3` version pin)
- `agents/` — 5 role agents (team-lead + 4 members)
- `avatars/` — member icons (256×256, ≤18 KB each)
- `portable/SKILL.md` — cross-platform asset-routing annex
- `orchestration/contract.md` — platform-agnostic orchestration contract (3 verbs × 3 platforms)
- `install.ps1` / `install.sh` — one-click annex installer (per-platform dmr pin preflight)
- `settings.json` — runtime defaults (language, fallbacks)
- `.github/workflows/consistency-gate.yml` — CI single-source-of-truth gate
- `CHANGELOG.md`, `LICENSE`

### CI gate — 13 consistency checks
1. version parity (plugin.json == portable == CHANGELOG)
2. dmr requires-pin present in four places (plugin.json / portable / team-lead / README Files section)
3. no bare-github dead links in README
4. agent manifest parity (dir == plugin.json == teamInfo roster)
5. every agent still references the dmr core
6. robustness regression guards (lead tokens + member checkpoints, no magic numbers)
7. annex demotion + connector-registry guards (portable stays an annex; connector usage routed to dmr `references/data-sources.md`)
8. README drift + primitive-ban guards (three-layer positioning, templates A–E, CI count matches; platform verbs banned outside contract.md)
9. orchestration contract guard (contract.md exists, 3 verbs × 3 platforms, ≤150 lines, referenced by team-lead)
10. pause-line guard (timeout → snapshot → pending-takeover, 3-branch adjudication; rerun spends the global slack, never raises the cap)
11. agent-roster freeze (R1): agents/ stays exactly the 5 fixed role files — six-domain routing is a table, not extra headcount
12. aggregation-gateway qualifier guard (R2): every agentearth/agentkey mention in data-sourcer.md carries a conditional qualifier (若平台已连 / 已连才启用) within 200 chars — gateways stay optional enhancement layers
13. bounded revise-loop guard (R3): team-lead keeps the "最多 2 轮修订 + 强制通过" termination tokens; no unbounded-loop vocabulary

`--self-test` runs the negative matrix in CI: 3 injected violations, each must FAIL the gate.

### Release checklist
1. Before merge: `python scripts/consistency_check.py` (+ `--self-test`) passes locally.
2. Version parity: plugin.json == portable frontmatter == portable body note == CHANGELOG top; README history entries (EN+CN) and the Files-section pin updated in the same commit.
3. Smoke both installers: `install.ps1` on Windows, `install.sh` in a Linux container.
4. Push main → CI green.
5. Tag `vX.Y.Z` and push the tag.
6. Publish the GitHub Release from the tag; release notes quote the CHANGELOG entry (errata merge as `Amended` into the existing entry, no new tag).
7. Re-run the installer; verify platform annex copies match the new version and satisfy the dmr pin.

### History & roadmap
- **0.7.4** — FrontierAgent/Apodex governance audit absorption (5 DAT migrations into contract.md): task-lifecycle five-state board (pending/active/completed/blocked/cancelled, orchestrator-maintained) · orchestrator idle-loop exemption (waiting for sub-agent reports ≠ idle; idle = re-dispatching same task card with zero new evidence) · duplicate-action stop-loss (same query/URL 3× → rollback resample, does not consume round budget) · load-bearing conclusion instant verification (E1 evidence attached at point of production, Phase 2 adjudication only upgrades) · in-flight mid-course correction (user instruction queued to `collect` boundary + partial-validity assessment — unaffected results preserved, no batch rerun; touches the research goal → back to Step 0, source pool retained). Version quadruple-source aligned to 0.7.4.
- **0.7.3** — install tooling batch: `install.ps1` / `install.sh` one-click annex install with per-platform dmr pin preflight (`.gitattributes` LF pin) — closes the platform-copy drift class (a stale 0.6.1 annex copy was found in the wild, 3 versions behind); README release checklist (7 steps); README Files-section pin sync (`>=2.6.0` → `>=2.7.0`, missed in 0.7.2) + gate check 2 now also enforces the README pin.
- **0.7.2** — P2 batch (version precision + honest labeling): dmr `requires` tightened to `>=2.7.0 <3` (3-source sync: plugin.json + team-lead frontmatter + portable metadata); Coze column in the contract.md adapter table annotated "design-time, not live-tested".
- **0.7.1** — README facade sync + check-8 mechanism-token guard (SOP kernel unchanged): README robustness section purged of stale version label; mechanism checklist completed to match 0.6.0/0.7.0 actual delivery (acceptance-first / credit dual-track / domain-independence adjudication / pause-line · pending-takeover); Files section now lists settings.json; check 8 extended 4 mechanism tokens (待接管 / credit / 验收标准 / 域独立性).
- **0.7.0** — P1 batch (global-optimal spec v1.2): acceptance-first (verify criteria + termination conditions before `dispatch`, 1 round of user confirmation, aligned with dmr v2.6.0 Step 0); six-domain routing table D1–D6 (platform-split preferred sources + fallback paths + same-source warnings — routing is a table, not extra headcount); aggregation-gateway four-path probe SOP (negative findings must be `probe-scoped`, never extrapolated); domain-independence adjudication gate (same-domain source pairs cap at `Corroborated`); credit dual-track budget (gateway calls × 0.5 credit, soft warning at 30); CI checks 11–13 (roster freeze / gateway qualifiers / bounded revise loop) + negative-matrix self-test; dmr `requires` tightened to `>=2.6.0 <3`.
- **0.6.1** — consistency fix: research parameter-card source-pool entry format unified to `实体 | 域 | 源URL | 层级 | 日期 | 置信` (fixed internal `层级Tier` English pollution + `URL`/`源URL` drift); field-definition pointer now targets dmr v2.5.0 structured schema; dmr `requires` tightened to `>=2.5.0 <3`.
- **0.6.0** — pause-line / pending-takeover semantics: member timeout no longer jumps straight to degradation — snapshot first (piggybacked on checkpoints), mark pending-takeover, then a 3-branch adjudication (clean rerun / human takeover via the intervention window / accept degradation); batch rerun forbidden; rerun budget = global slack only.
- **0.5.0** — primitive downshift: all platform-specific orchestration verbs removed from agent bodies, portable, and README; agents now speak contract verbs only; WorkBuddy parameter details live in contract.md; CI primitive-ban guard.
- **0.4.0** — orchestration contract layer: 3 platform-agnostic verbs (`assemble` / `dispatch` / `collect`) with a 3-platform adapter table (WorkBuddy / Coze / single-thread), incl. Coze no-skill-inheritance (inline param cards) and schedule-trigger monitoring; CI check 9.
- **0.3.0** — coze-audit batch: three-layer README alignment + drift guard, fast-mode single-thread rule, honest budget counting, adversarial-audit floor, connector-registry routing, avatar slimming.
- **0.2.1** — portable demoted to asset-routing annex (A1); all 25 audit findings closed.
- **0.2.0** — budget governor, two-phase source pool, member checkpoints, run-manifest, externalized adversarial audit.
- Roadmap: platform adapters as needed (new column = new platform); contract layer stays thin.

### Acknowledgments
- Credibility core inherited from [deep-market-research](https://github.com/Rain3Dmetrology/deep-market-research) (dmr); engineering-robustness mechanisms inspired by `gpt-researcher-team` (timeout / fallback / notification / source-pool / multi-dimensional review).

---

<a id="中文"></a>
## 中文

### 解决什么
- 一句话触发深度调研（行业 / 竞品 / 公司 / 市场 / 学术 / 持续监测），产出**带源分级、交叉验证、置信标签、可复现**的报告——质量不再依赖你用哪台电脑、哪个智能体平台。
- 治痛点：换设备、换平台后调研深度忽高忽低、结论无源、不可复现。

### 三层架构，一个内核
- **deep-market-research（dmr）= 可信度内核，也是唯一调研入口。** 它拥有调研意图路由与单会话 SOP（Step 0–8）、报告模板 A–E（通用 / 行业五大板块 / 竞品四维 / 学术 / 监测增量）、T1–T4 源分级、≥2 源交叉验证、矛盾台账、对抗审计、置信标签。
- **本仓库 = 团队编排形态（WorkBuddy Team 专家包）。** 5 个角色（研究主编 + 4 成员），配全局预算器、两段式来源池、run-manifest 归档、超时降级、有界修订循环。
- **`portable/SKILL.md` = 平台资产路由 annex，不是调研入口。** 它不响应调研类触发词（`调研 / 竞品 / 尽调 / …` 均归 dmr 接管）；仅当 dmr Step 1——或用户明确点名——需要平台资产（连接器、xlsx/Python 建模、可视化、并行采集）时才挂载。

### 安装
- **一键（annex 形态）**：运行 `install.ps1`（Windows）或 `./install.sh`（Unix）——把 `portable/SKILL.md` 以 `research-orchestrator` 名落位各已检测平台的技能目录，并核对已装 dmr 副本是否满足 pin（不足则告警）。
- **WorkBuddy（团队形态）**：克隆本仓库，把仓库根目录拷入 `~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/`，在专家中心启用。
- **其他平台（annex 形态）**：把 `portable/SKILL.md` 拷入你平台的技能目录。调研意图仍走 dmr；annex 只补充资产路由。

### 用法
- **WorkBuddy**：选择该专家，或输入触发词如 `调研 [行业/赛道] 的竞争格局与趋势`——主编带 4 成员跑完整 SOP。
- **快版**：默认单线程——主编直跑 dmr Step 1/4/8（SLA ≤10 分钟），免 `assemble`/`dispatch`；仅用户显式要求时才启用团队形态。
- **Portable annex**：绝不因调研词自动触发。需明确点名资产路由 / 连接器映射 / 并行采集，或由 dmr Step 1 挂载。

### 工程健壮性
- **验收先行**：`dispatch` 前主编产出验收标准（每条含度量锚点）＋ 终止条件三态（达标即停 / 预算耗尽即停 / 最多 N 轮），交用户 1 轮确认——与 dmr Step 0 产出行对齐。
- **全局预算器**：墙钟 SLA（标准版 ≤30 分钟 / 快版 ≤10 分钟）+ 搜索封顶 ≤60 次，附计数口径诚实条款（硬限 / 自计数，记入 run-manifest），80% 预警 / 100% 冻结 → 降级交付；聚合网关（AgentEarth 等，若平台已连）调用另记 credit 口径（调用数 × 0.5 credit/次，软预警线 30）。
- **两段式来源池**：Phase1 分域预分配（学术 / 中文 UGC / 测算——每实体×域唯一属主）杜绝重复采集；Phase2 合并裁决是唯一证据入口。
- **域独立性裁决门**：候选 `Confirmed` 结论的支撑源逐一标注采集域（D1–D6）；存在同域源对时该结论最高标 `Corroborated`。
- **run-manifest.json** 逐次归档：查询原文、参数卡、来源池终态、裁决决策、组件版本、预算消耗、降级事件。
- **对抗审计最低标准**：换角色视角 critic（外部模型，或同模回退时声明「反方审稿人」），每类产出 ≥3 条反证清单，必须落入矛盾台账。
- **三层质检不可互相替代**：6 维闸门（覆盖）/ 对抗审计（反向证据）/ lint（格式引用）——缺任一层必须披露。
- **成员 checkpoint 义务**：剩余轮次 ≤20%（以各自 frontmatter maxTurns 为基数）或预算预警时——停止采集、回传结构化摘要。
- **暂停线 / 待接管**：成员超时先落执行快照（已用预算、来源增量、完成/待办）并标「待接管」；主理人三分支裁决——清理重跑（只花全局余量）/ 人工接手 / 接受降级。

### 文件结构
- `.codebuddy-plugin/plugin.json` — 包清单（含 `requires: deep-market-research >=2.7.0 <3` 版本 pin）
- `agents/` — 5 个角色 agent（主理人 + 4 成员）
- `avatars/` — 成员图标（256×256，单张 ≤18KB）
- `portable/SKILL.md` — 跨平台资产路由 annex
- `orchestration/contract.md` — 平台无关编排契约（3 动词 × 3 平台）
- `settings.json` — 运行时默认值（语言、回退策略）
- `.github/workflows/consistency-gate.yml` — CI 单一事实源一致性门禁
- `CHANGELOG.md`、`LICENSE`

### CI 门禁 — 13 项一致性检查
1. 版本对齐（plugin.json == portable == CHANGELOG）
2. dmr requires-pin 四处在位（plugin.json / portable / team-lead / README Files 节）
3. README 无裸 github 死链
4. agent 清单对齐（目录 == plugin.json == teamInfo 花名册）
5. 每个 agent 仍引用 dmr 内核
6. 健壮性机制回归守卫（主理人 token + 成员 checkpoint，无魔法数字）
7. annex 降维 + 连接器注册表守卫（portable 保持 annex 定位；连接器用法路由到 dmr `references/data-sources.md`）
8. README 漂移 + 原语清零守卫（三层定位、模板 A–E、CI 项数一致；平台动词仅允许出现在 contract.md）
9. 编排契约守卫（contract.md 存在、3 动词 × 3 平台、≤150 行、被 team-lead 引用）
10. 暂停线守卫（超时 → 快照 → 待接管 → 三分支裁决；重跑只花全局余量、永不追加封顶）
11. 编制冻结守卫（R1）：agents/ 恒为 5 个既定角色文件——六域路由是表不是编制，禁建数据源绑定型 subagent
12. 聚合网关限定词守卫（R2）：data-sourcer.md 中 agentearth/agentkey 每次出现处邻近 200 字符内必含限定词（若平台已连 / 已连才启用）——网关只作可选增强层，不作硬配置数据源
13. 有界修订循环守卫（R3）：team-lead 保有「最多 2 轮修订＋强制通过」终止 token；验收循环无无界语汇

`--self-test` 在 CI 中运行负向矩阵：3 例注入违例，每例必须使门禁 FAIL。

### 发布清单
1. 合并前：本地跑 `python scripts/consistency_check.py`（含 `--self-test`）通过。
2. 版本对齐：plugin.json == portable frontmatter == portable 正文注 == CHANGELOG 顶行；README 版本历史（中英）与 Files 节 pin 同批更新。
3. 双安装脚本冒烟：Windows 跑 `install.ps1`，Linux 容器跑 `install.sh`。
4. push main → CI 绿。
5. 打 `vX.Y.Z` tag 并推送。
6. 从 tag 发布 GitHub Release，notes 引用 CHANGELOG 对应条目（勘误以 Amended 并入既有条目，不打新 tag）。
7. 重跑安装脚本，核对平台 annex 副本版本 = 新版本且满足 dmr pin。

### 版本历史与路线图
- **0.7.4** — FrontierAgent/Apodex 治理审计吸收（contract.md 5 项 DAT 迁移）：任务生命周期五态任务板（pending/active/completed/blocked/cancelled，主理人唯一维护）· 主理人空转豁免（挂起等待子任务回报 ≠ 空转；空转 = 重复派相同任务卡且零新增证据）· 重复动作止损（相同查询/URL 连续 3 次 → 回滚重采样，不消耗迭代预算）· 承重结论即时验证（产生处附 E1 证据，Phase 2 裁决只升不降）· 运行中中途纠偏（用户指令排队至 collect 边界 + 部分有效性评估——未受影响成果保留、禁止整批重跑；触及调研主目标回 Step 0，来源池保留）。版本四源对齐 0.7.4。
- **0.7.3** — 安装工具批次：`install.ps1` / `install.sh` annex 一键安装＋逐平台 dmr pin 预检（`.gitattributes` 固定 LF）——关闭「平台副本漂移」问题类（实测发现野外 0.6.1 副本落后 3 版）；README 发布清单（7 步）；Files 节 pin 同步（`>=2.6.0` → `>=2.7.0`，0.7.2 漏改）＋门禁检查 2 扩展覆盖 README pin。
- **0.7.2** — P2 批（版本精确化 + 诚实标注）：dmr `requires` 精确化为 `>=2.7.0 <3`（plugin.json + team-lead frontmatter + portable metadata 三源同步）；contract.md 适配表 Coze 列标注「设计态，未实测」。
- **0.7.1** — README 门面同步 + 检查 8 机制 token 守卫（SOP 内核零变化）：README 工程健壮性小节去除 stale 版本标签、机制清单补齐至 0.6.0/0.7.0 实际交付（验收先行 / credit 双口径 / 域独立性裁决门 / 暂停线·待接管）；Files 节补列 settings.json；检查 8 扩展 4 枚机制 token（待接管 / credit / 验收标准 / 域独立性）。
- **0.7.0** — P1 批（全局最优 spec v1.2）：验收先行（`dispatch` 前产出验收标准＋终止条件，用户 1 轮确认，与 dmr v2.6.0 Step 0 对齐）；六域取数路由表 D1–D6（平台分域首选源＋降级路径＋同源警告——路由是表不是编制）；聚合网关四路探测 SOP（负向结论必标 `probe-scoped`、禁止外推）；域独立性裁决门（同域源对最高标 `Corroborated`）；credit 双口径预算（网关调用 × 0.5 credit，软预警线 30）；CI 检查 11–13（编制冻结 / 网关限定词 / 有界修订循环）＋负向矩阵自测；dmr `requires` 收紧为 `>=2.6.0 <3`。
- **0.6.1** — 一致性修复：研究参数卡「已收集来源池」池条目格式统一为 `实体 | 域 | 源URL | 层级 | 日期 | 置信`（修正内部 `层级Tier` 英文污染与 `URL`/`源URL` 术语漂移）；字段定义指针改指 dmr v2.5.0 结构化 schema；dmr `requires` 收紧为 `>=2.5.0 <3`。
- **0.6.0** — 暂停线 / 待接管语义：成员超时不再直跳降级——先落执行快照（挂 checkpoint 回传）、标「待接管」，再由主理人三分支裁决（清理重跑 / 人工接手走介入窗口 / 接受降级）；禁止整批重跑；重跑预算只取全局余量。
- **0.5.0** — 原语下沉：agents 正文、portable、README 中的平台专属编排动词全部清零，agents 只说契约动词；WorkBuddy 参数细则收编入 contract.md；CI 原语清零守卫。
- **0.4.0** — 编排契约层：3 个平台无关动词（`assemble` 组队 / `dispatch` 派单 / `collect` 收编）+ 3 平台适配表（WorkBuddy / Coze / 单线程），含 Coze 子会话不继承 Skills（参数卡内联）与日程周期触发监测；CI check 9。
- **0.3.0** — coze 审计批次：三层定位 README 对齐 + 漂移守卫、快版单线程铁律、预算器计数口径、对抗审计最低标准、连接器注册表路由、avatar 瘦身。
- **0.2.1** — portable 降维为资产路由 annex（A1）；25 项审计发现全部关闭。
- **0.2.0** — 预算器、两段式来源池、成员 checkpoint、run-manifest、对抗审计外部化。
- 路线图：按需增加平台适配列（新平台=加一列）；契约层保持薄。

### 致谢
- 可信度内核继承自 [deep-market-research](https://github.com/Rain3Dmetrology/deep-market-research)（dmr）；工程健壮性机制借鉴 `gpt-researcher-team` 的超时/兜底/通报/来源池与多维审稿思路。
