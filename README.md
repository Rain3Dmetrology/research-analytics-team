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
- **Fast mode**: single-threaded by default — the lead runs dmr Step 1/4/8 directly (≤10 min SLA), skipping TeamCreate/spawn unless a team is explicitly requested.
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
- `orchestration/` — (planned v0.4.0) platform-agnostic orchestration contract
- `.github/workflows/consistency-gate.yml` — CI single-source-of-truth gate
- `CHANGELOG.md`, `LICENSE`

### CI gate — 8 consistency checks
1. version parity (plugin.json == portable == CHANGELOG)
2. dmr requires-pin present in three places
3. no bare-github dead links in README
4. agent manifest parity (dir == plugin.json == teamInfo roster)
5. every agent still references the dmr core
6. robustness regression guards (lead tokens + member checkpoints, no magic numbers)
7. annex demotion + connector-registry guards (portable stays an annex; connector usage routed to dmr `references/data-sources.md`)
8. README drift guard (three-layer positioning, templates A–E, CI count matches)

### History & roadmap
- **0.3.0** — coze-audit batch: three-layer README alignment + drift guard, fast-mode single-thread rule, honest budget counting, adversarial-audit floor, connector-registry routing, avatar slimming.
- **0.2.1** — portable demoted to asset-routing annex (A1); all 25 audit findings closed.
- **0.2.0** — budget governor, two-phase source pool, member checkpoints, run-manifest, externalized adversarial audit.
- Roadmap: v0.4.0 orchestration contract layer (platform-agnostic verbs); v0.5.0 primitive downshift into the contract.

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
- **快版**：默认单线程——主编直跑 dmr Step 1/4/8（SLA ≤10 分钟），免 TeamCreate/spawn；仅用户显式要求时才启用团队形态。
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
- `orchestration/` —（规划中 v0.4.0）平台无关编排契约
- `.github/workflows/consistency-gate.yml` — CI 单一事实源一致性门禁
- `CHANGELOG.md`、`LICENSE`

### CI 门禁 — 8 项一致性检查
1. 版本对齐（plugin.json == portable == CHANGELOG）
2. dmr requires-pin 三处在位
3. README 无裸 github 死链
4. agent 清单对齐（目录 == plugin.json == teamInfo 花名册）
5. 每个 agent 仍引用 dmr 内核
6. 健壮性机制回归守卫（主理人 token + 成员 checkpoint，无魔法数字）
7. annex 降维 + 连接器注册表守卫（portable 保持 annex 定位；连接器用法路由到 dmr `references/data-sources.md`）
8. README 漂移守卫（三层定位、模板 A–E、CI 项数一致）

### 版本历史与路线图
- **0.3.0** — coze 审计批次：三层定位 README 对齐 + 漂移守卫、快版单线程铁律、预算器计数口径、对抗审计最低标准、连接器注册表路由、avatar 瘦身。
- **0.2.1** — portable 降维为资产路由 annex（A1）；25 项审计发现全部关闭。
- **0.2.0** — 预算器、两段式来源池、成员 checkpoint、run-manifest、对抗审计外部化。
- 路线图：v0.4.0 编排契约层（平台无关动词）；v0.5.0 原语下沉至契约。

### 致谢
- 可信度内核继承自 [deep-market-research](https://github.com/Rain3Dmetrology/deep-market-research)（dmr）；工程健壮性机制借鉴 `gpt-researcher-team` 的超时/兜底/通报/来源池与多维审稿思路。
