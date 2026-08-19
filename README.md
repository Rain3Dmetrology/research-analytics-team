# Research Analytics Team

[English](#english) | [中文](#中文)

<a id="english"></a>
## English

### Why this exists
- One-command deep research (industry / competitor / company / market) that is **source-graded, cross-validated, confidence-labeled, and reproducible** — so output quality no longer depends on which machine or which agent platform you happen to be on.
- Kills the pain of ad-hoc research: inconsistent depth, unsourced claims, and non-reproducible results when you switch devices or agents.

### What it is
- A **Team-type expert package** (WorkBuddy) **plus** a **portable single-session SKILL.md** (Trae / Cursor / CodeBuddy). Same SOP, two form factors — install whichever your platform supports.
- **Credibility core = deep-market-research (dmr)**: T1–T4 source grading, ≥2 / ≥3-source cross-validation, templates B/C, contradiction ledger, adversarial audit, confidence labels (Confirmed / Corroborated / Single-source / Unverified).
- **5 roles**: lead editor (orchestration + adjudication) · industry-competitor researcher · data analyst · data sourcer · visualizer.
- **Engineering robustness**: timeout degradation, failure fallback, progress notification, source-pool reuse, 6-dimension QC + bounded 2-round revise loop.

### Install
- **WorkBuddy**: clone this repo, copy the repo root into `~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/`, then enable in the Expert Center.
- **Trae / Cursor / CodeBuddy**: copy `portable/SKILL.md` into your platform's skills directory.

### Usage
- WorkBuddy: select the expert, or type a trigger like `调研 [行业/赛道] 的竞争格局与趋势`.
- Any platform: load the SKILL, then `调研 ...`; it routes to dmr and runs the SOP.

### Files
- `.codebuddy-plugin/plugin.json` — package manifest (incl. `requires: deep-market-research >=2.3.4 <3` version pin)
- `agents/` — 5 role agents (team-lead + 4 members)
- `avatars/` — member icons
- `portable/SKILL.md` — cross-platform single-session skill
- `.github/workflows/consistency-gate.yml` — CI single-source-of-truth gate (version parity / pin presence / manifest parity)
- `CHANGELOG.md`, `LICENSE`

---

<a id="中文"></a>
## 中文

### 解决什么
- 一句话触发深度调研（行业 / 竞品 / 公司 / 市场），产出**带源分级、交叉验证、置信标签、可复现**的报告——质量不再依赖你用哪台电脑、哪个智能体平台。
- 治痛点：换设备、换平台后调研深度忽高忽低、结论无源、不可复现。

### 是什么
- **Team 型专家包**（WorkBuddy）**+ 便携单会话 SKILL.md**（Trae / Cursor / CodeBuddy）。同一套 SOP，两种形态，按平台任选安装。
- **可信度内核 = deep-market-research（dmr）**：T1–T4 源分级、≥2 / ≥3 源交叉验证、模板 B/C、矛盾台账、对抗审计、置信标签（Confirmed / Corroborated / Single-source / Unverified）。
- **5 个角色**：研究主编（编排+裁决）· 行业竞品研究员 · 数据论证师 · 专业取数师 · 可视化设计师。
- **工程健壮性**：超时降级、失败兜底、进度通报、来源池复用、6 维质检 + 有界 2 轮修订循环。

### 安装
- **WorkBuddy**：克隆本仓库，把仓库根目录拷入 `~/.workbuddy/plugins/marketplaces/my-experts/plugins/research-analytics-team/`，在专家中心启用。
- **Trae / Cursor / CodeBuddy**：把 `portable/SKILL.md` 拷入你平台的技能目录。

### 用法
- WorkBuddy：选择该专家，或输入触发词如 `调研 [行业/赛道] 的竞争格局与趋势`。
- 任意平台：加载该 SKILL，然后 `调研 ...`；自动路由 dmr 并跑完整 SOP。

### 文件结构
- `.codebuddy-plugin/plugin.json` — 包清单（含 `requires: deep-market-research >=2.3.4 <3` 版本 pin）
- `agents/` — 5 个角色 agent（主理人 + 4 成员）
- `avatars/` — 成员图标
- `portable/SKILL.md` — 跨平台单会话技能
- `.github/workflows/consistency-gate.yml` — CI 单一事实源一致性门禁（版本对齐 / pin 存在 / 清单对齐）
- `CHANGELOG.md`、`LICENSE`

### 致谢
- 可信度内核继承自 [deep-market-research](https://github.com/Rain3Dmetrology/deep-market-research)（dmr）；工程健壮性机制借鉴 `gpt-researcher-team` 的超时/兜底/通报/来源池与 6 维审稿思路。
