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
