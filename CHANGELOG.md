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
