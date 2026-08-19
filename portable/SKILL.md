---
name: research-orchestrator
description: >
  调研编排组合技能（零自研内核）：把 deep-market-research(dmr) 的可信度内核与平台调研资产
  （xlsx/Python、可连 MCP 取数、plotly/canva 可视化、并行采集、周期任务）编排成统一入口。
  覆盖 Coze「调研分析技能包」同等能力，并在可信度/中文/零成本出域上超越。
  适用：行业/竞品/公司尽调/数据论证/周期监测类调研。原则：集成已有，不造轮子，内核永远是 dmr。
license: MIT
compatibility: >
  跨平台 Markdown 技能（WorkBuddy / Trae / Cursor / CodeBuddy 等）。本文件是
  research-analytics-team 专家包在「无 Team 编排」时的等价单会话实现；
  平台专属能力（Connector/MCP/automation/Skill 调用）按平台可用性尽力启用，缺失则回退默认层（内置搜索 + 免费 API）。
metadata:
  version: "0.1.2"
  author: "Rain / WorkBuddy"
  source_of_truth: "research-analytics-team-team-lead.md（团队 SOP 为权威）"
  requires: "deep-market-research >=2.3.4 <3"
---

# Research Orchestrator — 调研编排组合技能（便携版 / 跨平台）

> 版本 0.1.2 ｜ 定位：**编排层**，不是新调研内核。
> 本文件是 `research-analytics-team` 专家包在「无 Team 编排」时的**等价单会话实现**；团队 SOP（`research-analytics-team-team-lead.md`）为唯一事实源，二者描述必须一致、不得漂移。
> 跨平台：WorkBuddy 直接可用；Trae / Cursor / CodeBuddy 等 Markdown 技能平台可加载本文件，平台专属能力（Connector/MCP/automation/Skill）按可用性尽力启用，缺失回退默认层（内置搜索 + 免费 API）。

---

## 一、入口与意图路由

用户触发词：`调研 / 行业 / 竞品 / 尽调 / 对标 / 市场测算 / 数据论证 / 周期监测 / 扒一下 / 挖一下`。

**Step R0 — 意图识别（薄路由，不替代 dmr Step 0）**

| 用户意图信号 | 路由目标 | 复用资产 |
|--------------|----------|----------|
| 行业/赛道/产业链/趋势/市场规模 | dmr 模板 B（行业赛道） | deep-market-research |
| 公司/竞品/尽调/对位 | dmr 模板 C（公司竞品） | deep-market-research |
| 上传 CSV/Excel / 建模 / 统计 | L3 数据子流 | xlsx + 受管 Python |
| 专利/财报/工商/行情 等结构化取数 | L4 取数子流 | 已连 MCP（若可用） |
| 需要图表/交互展示 | L5 可视化子流 | plotly + canva |
| 每周/每月/持续盯 | 自治层 | 平台周期任务能力（若可用） |

> 路由后**立即调用 deep-market-research 进入其 Step 0–8 主管线**；L3/L4/L5 是 dmr Step 1 采集阶段的**素材增强**，不是替代。

---

## 二、可信度内核（强制，不可绕过）

**任何时候都必须先走 dmr 的 Step 0–8 + 对应模板。** 本技能禁止：
- ❌ 跳过 dmr 的源分级/交叉验证直接出结论；
- ❌ 把 L3/L4 取到的数据当 Tier 1 硬事实而不经 dmr 裁决；
- ❌ 用可视化美化替代证据论证。

dmr 的置信标签（Confirmed/Corroborated/Single-source/Unverified）、矛盾台账、lint 自检是**最终交付的硬要求**。

> **快版边界**（唯一定义在团队 SOP 的「防冗余铁律」）：快版至少保留 dmr Step1(采集)+Step4(交叉验证)+Step8(模板)，报告注"快版，未全覆盖质量环"。

---

## 三、分层能力编排（L3 / L4 / L5）

### 3.1 L3 数据子流（算账）
- **表格读写**：xlsx / minimax-xlsx 处理 Excel/CSV。
- **建模/EDA**：受管 Python venv（`python`/`python3` 指向隔离环境，预装 pandas/scikit-learn/matplotlib/plotly）做测算。
- **回灌**：结果以证据 ID 写入 dmr 证据池（带源层级 T3 + 日期），参与交叉验证。
- **禁止**：模型输出当确定性结论；预测类标 `Single-source` 列入开放问题。

### 3.2 L4 取数子流（取数）
按平台可用连接器取结构化一手数据，**状态一律条件式（"若平台已连"），绝不硬编码已连**：

| 维度 | 连接器（若平台已连） | 团队对应角色 |
|------|----------------------|--------------|
| 专利 | patsnap-search（智慧芽） | data-sourcer |
| 行情/财报 | westock-mcp（腾讯自选股） | data-sourcer |
| 基金/资产 | yingmi-mcp（盈米，可选） | data-sourcer |
| 代码/技术 | github MCP + gh CLI | data-sourcer |
| 工商/司法/知产 | tyc-mcp（天眼查，需启用） | data-sourcer |
| App 商店 | agent-browser 抓公开页（降级源） | 降级 T4 |

> 连接器未连：回退内置搜索 + dmr 源分级兜底，标注"该维度因环境受限未覆盖"，不阻断。

### 3.3 L5 可视化子流（展示）
- 交互图表：plotly 生成可交互 HTML（对比/趋势/排名）。
- 可编辑汇报图：canva / ui-ux-pro-max。
- 原则：图表服务论证，每张图绑定 dmr 证据 ID。

---

## 四、并行加速

在 dmr Step 1（采集）阶段，对可独立子任务并行采集（平台支持子代理/Agent 时）：
- A：学术/免费 API 源（OpenAlex/Semantic Scholar/arXiv…）
- B：中文 UGC/公众号/知乎（agent-browser + wechat-article-search）
- C：专业 MCP 取数（智慧芽/自选股/tyc）
- D：L3 数据预处理（若用户上传数据集）

各子代理只负责**采集+结构化**，不负责结论；结果统一回灌 dmr 证据池，由 dmr Step 4 交叉验证裁决。

---

## 五、工程健壮性（与团队 SOP 一致）

- **超时降级**：任一并行采集任务超时，返回「部分但结构化」产物（标 `Unverified` / 未完成维度 / 未覆盖 / 降级图），不得悬停；编排者立即采用降级产物进入下一阶段。
- **失败兜底**：调度失败重试 1 次否则降级 dmr 单线程（至少 Step1+Step4+Step8）；来源不足如实标 `Unverified`/`未覆盖` 不编造；连接器未连条件式跳过。
- **进度通报**：每阶段结束通报（已完成/进行中/已确认结论/风险降级/下一步）；终稿含质量分（Confirmed/Corroborated/Single-source/Unverified 占比）+ 最大不确定性 1 条。
- **来源池复用**：已收集来源池为唯一证据入口，优先消耗既有证据、新源回写，跨阶段只从此池取数。
- **6 维质检 + 有界修订循环**：终稿按 来源充分性/事实准确性/观点均衡性/内容深度/结构清晰度/格式规范性 逐条过；命中硬性退回条件退回责任环节局部 patch，最多 2 轮 + 第 3 次强制通过，残留转开放问题。

---

## 六、质量纪律

1. ❌ 绕过 dmr 内核 → 所有结论经 dmr 源分级+交叉验证。
2. ❌ L3/L4 数据当 Tier 1 硬事实 → 必经 dmr 裁决。
3. ❌ 子代理越权下结论 → 只采集+结构化，结论权在 dmr。
4. ❌ 未连源伪装成一手 → 标 `T4 + 降级` / `未覆盖`。
5. ❌ 造新调研方法 → 只编排，方法回 dmr。
6. ✅ 环境受限 → 按 dmr 规则显式标注未覆盖，不编造。

---

## 七、典型调用示例

**用户**：「调研中国工业 AI 3D 视觉测量赛道，重点对标奥普特、凌云光，出一份带数据的周报。」
1. **R0 路由**：行业(模板B) + 竞品(模板C) + 数据论证 + 周报(自治)。
2. **内核**：deep-market-research → Step 0 收敛 → 模板 B+C。
3. **并行采集**：A 学术/免费API；B 中文UGC/公众号；C 智慧芽专利+westock财报+tyc工商(若已连)；D 上传数据预处理。
4. **L5**：plotly 对比/趋势图，canva 汇报看板。
5. **收口**：dmr Step 4–8 交叉验证+矛盾台账+对抗审计 → 带置信标签报告。
6. **自治**：建周期任务（平台支持时），沉淀本地知识库。
