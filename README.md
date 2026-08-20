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
- **WorkBuddy (team form)**: clone this repo, copy the repo root into `~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/`, then enable it in the Expert Center.
- **Other platforms (annex form)**: copy `portable/SKILL.md` into your platform's skills directory. Research intent still routes through dmr; the annex only adds asset routing.

### Usage
- **WorkBuddy**: select the expert, or type a trigger like `调研 [行业/赛道] 的竞争格局与趋势` — the lead runs the full SOP with the 4-member team.
- **Fast mode**: single-threaded by default — the lead runs dmr Step 1/4/8 directly (≤10 min SLA), skipping team assembly (`assemble`/`dispatch`) unless a team is explicitly requested.
- **Portable annex**: never auto-triggers on research words. Ask explicitly for asset routing / connector mapping / parallel collection, or let dmr Step 1 mount it.

### Engineering robustness (v0.3.0)
- **Budget governor**: wall-clock SLA (std ≤30 min / fast ≤10 min) + search cap ≤60 with an honest counting clause (hard limit vs self-count, disclosed in the run manifest), 80% early warning / 100% freeze → degraded delivery.
- **Two-phase source pool**: Phase-1 domain pre-allocation (academic / Chinese UGC / quantitative — one owner per entity×domain) kills duplicate collection; Phase-2 merge adjudication is the only evidence entry.
- **run-manifest.json** per run: query, param card, final source pool, adjudication decisions, component versions, budget consumption, degradation events.
- **Adversarial audit floor**: role-swapped critics (external model, or a declared "opposing reviewer" on same-model fallback), each producing a ≥3-item counter-evidence list that must land in the contradiction ledger.
- **Three QC layers, non-interchangeable**: 6-dimension gate (coverage) / adversarial audit (counter-evidence) / lint (format & citations) — missing any layer must be disclosed.
- **Member checkpoint obligations**: at ≤20% remaining turns (per each agent's own frontmatter maxTurns) or budget warning — stop collecting, return a structured digest.

### Files
- `.codebuddy-plugin/plugin.json` — package manifest (incl. `requires: deep-market-research >=2.3.4 <3` version pin)
- `agents/` — 5 role agents (team-lead + 4 members)
- `avatars/` — member icons (256×256, ≤18 KB each)
- `portable/SKILL.md` — cross-platform asset-routing annex
- `orchestration/contract.md` — platform-agnostic orchestration contract (3 verbs × 3 platforms)
- `.github/workflows/consistency-gate.yml` — CI single-source-of-truth gate
- `CHANGELOG.md`, `LICENSE`

### CI gate — 10 consistency checks
1. version parity (plugin.json == portable == CHANGELOG)
2. dmr requires-pin present in three places
3. no bare-github dead links in README
4. agent manifest parity (dir == plugin.json == teamInfo roster)
5. every agent still references the dmr core
6. robustness regression guards (lead tokens + member checkpoints, no magic numbers)
7. annex demotion + connector-registry guards (portable stays an annex; connector usage routed to dmr `references/data-sources.md`)
8. README drift + primitive-ban guards (three-layer positioning, templates A–E, CI count matches; platform verbs banned outside contract.md)
9. orchestration contract guard (contract.md exists, 3 verbs × 3 platforms, ≤150 lines, referenced by team-lead)
10. pause-line guard (timeout → snapshot → pending-takeover, 3-branch adjudication; rerun spends the global slack, never raises the cap)

### History & roadmap
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
- **WorkBuddy（团队形态）**：克隆本仓库，把仓库根目录拷入 `~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/`，在专家中心启用。
- **其他平台（annex 形态）**：把 `portable/SKILL.md` 拷入你平台的技能目录。调研意图仍走 dmr；annex 只补充资产路由。

### 用法
- **WorkBuddy**：选择该专家，或输入触发词如 `调研 [行业/赛道] 的竞争格局与趋势`——主编带 4 成员跑完整 SOP。
- **快版**：默认单线程——主编直跑 dmr Step 1/4/8（SLA ≤10 分钟），免 `assemble`/`dispatch`；仅用户显式要求时才启用团队形态。
- **Portable annex**：绝不因调研词自动触发。需明确点名资产路由 / 连接器映射 / 并行采集，或由 dmr Step 1 挂载。

### 工程健壮性（v0.3.0）
- **全局预算器**：墙钟 SLA（标准版 ≤30 分钟 / 快版 ≤10 分钟）+ 搜索封顶 ≤60 次，附计数口径诚实条款（硬限 / 自计数，记入 run-manifest），80% 预警 / 100% 冻结 → 降级交付。
- **两段式来源池**：Phase1 分域预分配（学术 / 中文 UGC / 测算——每实体×域唯一属主）杜绝重复采集；Phase2 合并裁决是唯一证据入口。
- **run-manifest.json** 逐次归档：查询原文、参数卡、来源池终态、裁决决策、组件版本、预算消耗、降级事件。
- **对抗审计最低标准**：换角色视角 critic（外部模型，或同模回退时声明「反方审稿人」），每类产出 ≥3 条反证清单，必须落入矛盾台账。
- **三层质检不可互相替代**：6 维闸门（覆盖）/ 对抗审计（反向证据）/ lint（格式引用）——缺任一层必须披露。
- **成员 checkpoint 义务**：剩余轮次 ≤20%（以各自 frontmatter maxTurns 为基数）或预算预警时——停止采集、回传结构化摘要。

### 文件结构
- `.codebuddy-plugin/plugin.json` — 包清单（含 `requires: deep-market-research >=2.3.4 <3` 版本 pin）
- `agents/` — 5 个角色 agent（主理人 + 4 成员）
- `avatars/` — 成员图标（256×256，单张 ≤18KB）
- `portable/SKILL.md` — 跨平台资产路由 annex
- `orchestration/contract.md` — 平台无关编排契约（3 动词 × 3 平台）
- `.github/workflows/consistency-gate.yml` — CI 单一事实源一致性门禁
- `CHANGELOG.md`、`LICENSE`

### CI 门禁 — 10 项一致性检查
1. 版本对齐（plugin.json == portable == CHANGELOG）
2. dmr requires-pin 三处在位
3. README 无裸 github 死链
4. agent 清单对齐（目录 == plugin.json == teamInfo 花名册）
5. 每个 agent 仍引用 dmr 内核
6. 健壮性机制回归守卫（主理人 token + 成员 checkpoint，无魔法数字）
7. annex 降维 + 连接器注册表守卫（portable 保持 annex 定位；连接器用法路由到 dmr `references/data-sources.md`）
8. README 漂移 + 原语清零守卫（三层定位、模板 A–E、CI 项数一致；平台动词仅允许出现在 contract.md）
9. 编排契约守卫（contract.md 存在、3 动词 × 3 平台、≤150 行、被 team-lead 引用）
10. 暂停线守卫（超时 → 快照 → 待接管 → 三分支裁决；重跑只花全局余量、永不追加封顶）

### 版本历史与路线图
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
