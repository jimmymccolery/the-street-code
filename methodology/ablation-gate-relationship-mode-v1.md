# Ablation Gate Execution Guide: Relationship-Mode V1.x Operationalization Decision

**Established:** 2026-06-30 (post-Council-#1-close session; companion to posts 0129 + 0130)
**Maintained by:** operator; CC updates on empirical contact
**Purpose:** Clean-room execution guide for the four-condition ablation gate that unlocks (or retires) the V1.x operationalization of the reserved `relationship_mode` schema slot. Standalone-executable: a fresh CC session, fresh substrate, or future-operator can open this file with zero prior context and run the gate end-to-end.
**Provenance:** Council #1 (Fiske RMT relationship-mode primitive vs existing decomposition sufficiency) closed 2026-06-30 evening at Pattern B ADOPT-FOLD via Option B per-item deliberation. ADOPT half executed as posts 0129 + 0130 (commit 3ab3d68). BANK half is this guide.

---

## What this guide is and is NOT

**This guide is** the standalone-executable operational procedure for the ablation gate. It enumerates: the four ablation conditions with pass/fail criteria; the task decomposition across Claude Code (BUILDER surface) and Comet Computer (RESEARCH-AGENT surface); the calibrated prompts for each surface; the per-phase cost estimates; the failure modes + fallbacks; the handoff artifacts each phase produces.

**This guide is NOT** the architectural spec for the reserved slot (Post 0130 is the spec) or the narrative of how Council #1 arrived at the ablation gate (Post 0129 is the narrative) or the substrate outputs themselves (archived at `~/Projects/the-street-code/_archive/2026-06-30-council-1-relationship-mode/`). The guide points to those artifacts; it does not duplicate their content.

---

## The four ablation conditions (recap for standalone use)

All four are conjunctive. If any one fails, the reserved slot is retired at near-zero sunk cost and Post 0130's canonical status is amended with the empirical finding. If all four pass, the V1.x operationalization proceeds (~36-72h BUILD-side work per Post 0130's cost arithmetic).

### Condition 1 — Mode-blind ablation

**Question:** does the mode do anything at all?

**Procedure:** run consolidation-pass cached-policy regeneration twice under identical prototype-population conditions:
- Run A: mode assigned per prototype mode-assignment heuristic
- Run B: mode forced to `UNDEFINED_OR_MIXED` for all ordered pairs

Diff the resulting cached policies + downstream NPC decisions.

**Pass criterion:** measurable delta between Run A and Run B in cached-policy content and/or NPC decision distributions.

**Fail criterion:** cached policies + NPC decisions indistinguishable across Run A and Run B. Interpretation: existing decomposition (HEXACO H + attachment + sentiment override) already carries the variance; mode is inert; retire the slot.

### Condition 2 — Mode-permutation ablation

**Question:** does the mode-gate actually gate, and in the theoretically-predicted direction?

**Procedure:** select a sample of ordered pairs; hold sentiment scalar + event history fixed; swap mode label (e.g., `MARKET_PRICING` → `COMMUNAL_SHARING`); re-run decision-scoring for the pair's next N candidate actions.

**Pass criterion:** decision-scoring output changes in the theoretically-predicted direction (e.g., MP-swapped-to-CS pairs shift toward need-based cooperation rather than proportional-exchange scoring).

**Fail criterion:** decision-scoring output unchanged across mode swap. Interpretation: the mode-gate exists in the code but does not gate; design flaw (fix and re-run) rather than data flaw. If gate is fixed and Condition 2 still fails after re-run, the mode's interpretive-grammar-selection function is not operationalizable at the framework's decision-scoring layer; retire the slot.

### Condition 3 — Sharpened sentiment-collinearity ablation (LOAD-BEARING)

**Question:** does the mode do UNIQUE work beyond what the sentiment scalar already carries?

**Procedure:** across the full prototype population, extract per-pair mode assignment + sentiment scalar + closeness-linked general-factor proxy. Run partialling regression: quantify how much mode-driven variance in decision-scoring survives after subtracting off variance predictable from the closeness general factor. The general factor is characterized by Zakharin & Bates 2023 Study 4 as "typically higher for closer relationships" and requires operationalization here as a specific proxy variable derived from the framework's existing sentiment scalar + pair-relational history features.

**Pass criterion:** substantial residual variance after partialling. Threshold requires methodology calibration (see Phase 2 Comet Computer brief below); as a directional anchor, residual should be at minimum non-trivial in effect-size terms (a psychometrics-literate collaborator should specify the effect-size threshold empirically per the prototype population's characteristics).

**Fail criterion:** residual variance is negligible after partialling; mode is largely re-encoding closeness in fancier language. Interpretation: this is the specific failure mode Zakharin & Bates 2023's own general-factor finding foreshadows (documented in Post 0129); retire the slot; the framework's existing sentiment scalar already carries the differential-variance work the mode would nominally provide.

**Why this is the load-bearing condition:** Conditions 1 and 2 check whether the mode does anything and does the right thing; Condition 3 checks whether the mode does anything the framework's existing decomposition does not already do. Passing 1 and 2 while failing 3 is possible and corresponds to "the mode changes outcomes, but only in the same ways sentiment would already change them." That is the exact failure mode that would waste 36-72h of BUILD-side work.

### Condition 4 — WEIRD-defaults disclosure check

**Question:** does the mode-assignment heuristic honor the framework's cross-cultural discipline, or does it silently default all pairs to WEIRD-derived mode distributions?

**Procedure:** two-part audit.

Part 4a (code audit): read the prototype mode-assignment heuristic. Verify it consults `cultural_context_tag` (the schema placeholder from Post 0128). Verify it produces different mode distributions for pairs flagged as non-WEIRD context versus WEIRD context (or leaves non-WEIRD pairs `UNDEFINED_OR_MIXED` pending scholarship).

Part 4b (literature grounding audit): for any assignment rules that DO produce non-WEIRD-specific distributions, verify the rules are grounded in primary-source cross-cultural RMT literature (per the framework's Rule 19 Marcus Reed Protocol external-attribution discipline). If the heuristic produces "for cultural_context_tag = X, mode distribution is Y," where does Y come from?

**Pass criterion:** heuristic consults `cultural_context_tag`; produces context-differentiated distributions OR conservatively leaves non-WEIRD pairs `UNDEFINED_OR_MIXED`; any context-specific distributions grounded in primary-source cross-cultural literature (URL/DOI verified).

**Fail criterion:** heuristic silently defaults WEIRD (all pairs get British-general-population-derived mode distributions regardless of cultural context tag). Interpretation: fix-before-shipping failure mode (not a "retire the slot" outcome; the slot may still earn its place, but the operationalization commitment cannot proceed until the assignment heuristic honors the framework's discipline).

---

## Task decomposition across surfaces

The gate composes work across two substrates. Neither can execute the whole gate alone; the composition is what makes the gate schedulable at reduced total cost.

**Claude Code (BUILDER surface):** filesystem access, terminal execution, git operations, simulation runs against local prototype code, data export as CSV, code audit. Owns Conditions 1 + 2 in full, Condition 3 sub-step 3a (data extraction), Condition 4 sub-step 4a (code audit), and the final canonical mutations after operator ratification.

**Comet Computer (RESEARCH-AGENT surface):** browser-driven statistical tooling (Colab / Kaggle / JASP web / Perplexity code execution), Perplexity Deep Research literature search, cross-substrate methodology calibration, browser-based document synthesis. Owns Condition 3 sub-steps 3b (statistical analysis) + 3c (methodology calibration + interpretation), Condition 4 sub-step 4b (literature grounding audit), and the aggregate report drafting.

---

## Phase 1 — Claude Code (BUILDER surface)

**Estimated cost: 15-26 hours BUILD-side work**

**Objective:** produce the prototype simulation state that generates the data Comet Computer will analyze; execute Conditions 1, 2, and Condition 4 sub-step 4a directly; export Condition 3 sub-step 3a data as a handoff CSV.

### Phase 1 task list

1. **Prototype mode-assignment heuristic (4-8h).** Throwaway code. Reads pair-relational history features + `cultural_context_tag` + pair-summary features; produces a mode assignment per ordered pair at consolidation-pass time. Design constraint: heuristic must be principled enough that Condition 2's swap test produces theoretically-predicted direction changes; heuristic must consult `cultural_context_tag` per Condition 4a.
2. **Prototype mode-gate on decision-scoring (6-10h).** Throwaway code. Modifies the expected-free-energy scoring pipeline to make specific scoring terms conditional on the pair's assigned mode. Design constraint: the mode-gate must be structurally distinct from the sentiment-scalar-weighted terms already in the scoring pipeline (else Condition 3 will trivially fail).
3. **Run prototype simulation across three tycoon-population scenarios (1-3h execution + wait time).** Populations: staff-loyalty relationships (multi-decade employment arc); customer-patronage relationships (recurring customer visits); league/competitor dynamics (rival bowlers, league members, team dynamics). Each population runs 5-15 game-years to accumulate sufficient pair-relational history for meaningful statistical power.
4. **Condition 1 execution (1-2h).** Re-run cached-policy regeneration with mode forced `UNDEFINED_OR_MIXED`; diff against the mode-assigned regeneration. Record delta as PASS or FAIL.
5. **Condition 2 execution (1-2h).** Sample pairs across the three populations; execute mode swaps; re-run decision-scoring; verify directional predictions per RMT primitive semantics. Record per-pair outcome; aggregate to PASS or FAIL.
6. **Condition 3 sub-step 3a: data export (1-2h).** Export a CSV with per-pair rows: `pair_id`, `population_type`, `mode_assignment`, `sentiment_scalar`, `closeness_general_factor_proxy` (see Comet Computer brief for proxy operationalization guidance), plus decision-scoring output distributions across a sample of candidate actions. This is the handoff artifact Phase 2 consumes.
7. **Condition 4 sub-step 4a: code audit (1-2h).** Read the prototype mode-assignment heuristic. Verify it consults `cultural_context_tag`. Verify it produces different distributions for tagged-non-WEIRD pairs. Document any distributions found + their derivation logic. This audit produces a second handoff artifact for Phase 2 sub-step 4b (literature grounding).

### Phase 1 handoff artifacts to Phase 2

Produce a `~/Desktop/ablation-gate-phase-1-handoff-YYYY-MM-DD/` folder containing:

- `phase-1-report.md` — Condition 1 result (PASS/FAIL + delta); Condition 2 result (PASS/FAIL + directional-check details); Condition 4a code-audit summary
- `phase-1-data.csv` — the exported per-pair data for Condition 3 statistical analysis
- `phase-1-mode-assignment-heuristic.md` — extracted prose description of the heuristic's assignment rules, for Phase 2 sub-step 4b's literature grounding audit
- `phase-1-limitations.md` — honest weakness flags (see below)

### Phase 1 honest weakness flags to surface

- The prototype mode-assignment heuristic is BUILDER-judgment; production heuristic should be operator-scholarship-informed. Phase 1 heuristic is designed to enable the gate to test the ARCHITECTURE (does the enum earn its variance) not the specific rulebook.
- The closeness general-factor proxy operationalization is the wildcard variable for Condition 3. Phase 1 produces a candidate proxy (documented in the handoff) but Phase 2's methodology calibration may specify a different proxy the analysis re-derives.
- Population scenarios' sim-run duration affects statistical power. 5-15 game-years is an initial anchor; if Phase 2 finds statistical power insufficient, Phase 1 re-runs at longer duration.

---

## Phase 2 — Comet Computer (RESEARCH-AGENT surface)

**Estimated cost: 7-16 hours (Comet-driven; operator supervises)**

**Objective:** execute Condition 3 sub-steps 3b (statistical analysis) + 3c (methodology calibration + interpretation); execute Condition 4 sub-step 4b (literature grounding audit); produce aggregate PASS/FAIL report for the four-condition gate.

### Phase 2 task list

1. **Load Phase 1 handoff into Comet-accessible environment (0.5-1h).** Upload `phase-1-data.csv` to Colab / Kaggle / Perplexity code execution. Load `phase-1-report.md` + `phase-1-mode-assignment-heuristic.md` + `phase-1-limitations.md` as Comet context.
2. **Condition 3 sub-step 3b: statistical analysis (4-8h).** Run partialling regression per calibrated Comet prompt below. Iterate on model specification (covariate selection, general-factor proxy operationalization, effect-size threshold). Verify assumptions (linearity, residual distribution, multicollinearity beyond the sentiment-mode axis). Produce residual-variance estimate with confidence interval.
3. **Condition 3 sub-step 3c: methodology calibration + interpretation (2-4h).** Perplexity Deep Research query set on partialling methodology for psychometric general-factor models. Cross-substrate calibration on effect-size threshold: what residual size counts as "substantial enough to justify the enum" vs. "negligible enough to retire the slot." Draft interpretation with explicit acknowledgment of methodology-choice uncertainty.
4. **Condition 4 sub-step 4b: literature grounding audit (1-4h).** For each non-WEIRD-specific mode distribution rule documented in Phase 1's heuristic, verify the rule's grounding via Perplexity Deep Research. Apply Rule 19 Marcus Reed Protocol three-condition gate: source exists / says what cited / semantically applicable to the framework's use. Flag any rules that fail the gate.
5. **Aggregate report writeup (1-2h).** Assemble the four-condition PASS/FAIL matrix. Document the residual-variance measurement + confidence interval + methodology choices. Document the literature-grounding audit outcomes. Produce two-part recommendation: (a) PASS/FAIL verdict for each condition; (b) aggregate verdict (OPERATIONALIZE if all four pass; RETIRE if Condition 1, 2, or 3 fail; FIX-HEURISTIC-BEFORE-PROCEEDING if Condition 4 fails).

### Phase 2 calibrated Comet Computer prompt (paste into Comet)

The prompt below is calibrated per the framework's paired-n=4 substrate-discipline lesson (`~/.claude/projects/-Users-jimmy/memory/feedback_substrate_opaque_citation_format_as_risk_signal.md`). Do not paraphrase; paste as-is.

```
You are executing Phase 2 of an ablation gate for a procedural-character architecture decision. The Phase 1 handoff folder contains: phase-1-data.csv (per-pair prototype simulation data); phase-1-report.md (Conditions 1 + 2 + 4a results); phase-1-mode-assignment-heuristic.md (prose description of the assignment rules); phase-1-limitations.md (honest weakness flags).

Your objective: execute Conditions 3 and 4b of the four-condition ablation gate specified in ~/Projects/the-street-code/methodology/ablation-gate-relationship-mode-v1.md. Produce a Phase 2 aggregate report suitable for operator ratification.

MANDATORY VERIFICATION TRAIL (first section of your output):
- List every data column you read from phase-1-data.csv with type + range
- List every methodology source you consulted with full URL / arXiv / DOI
- List every Perplexity Deep Research query you ran with the returned top-3 sources
- Explicitly acknowledge any data or methodology decisions where you defaulted to convention rather than empirical calibration

ECHO/NOVEL DISCIPLINE:
For each substantive claim in your analysis, tag it ECHO (matches existing framework canon / prior methodology precedent) or NOVEL (new claim requiring justification). For every NOVEL claim, provide four fields: (1) claim in one sentence; (2) evidence source with URL/DOI; (3) confidence level H/M/L with justification; (4) what would change your mind.

Condition 3 sub-step 3b (statistical analysis) requirements:
- Partialling regression: mode-driven variance in decision-scoring, partialling out variance predictable from closeness general-factor proxy. Specify the proxy operationalization explicitly (Phase 1 provided a candidate; you may re-derive if psychometrically justified).
- Verify regression assumptions: linearity, residual normality, multicollinearity check on mode-vs-sentiment specifically.
- Report residual variance with confidence interval.
- Report effect size in Cohen's f² or comparable metric.

Condition 3 sub-step 3c (methodology calibration) requirements:
- Perplexity DR query on effect-size thresholds for psychometric general-factor partialling models. Cite the methodology sources verbatim with URLs.
- Specify the effect-size threshold you are applying for PASS/FAIL, with justification from the methodology literature.
- Explicitly acknowledge that the threshold is a methodology-choice judgment; provide sensitivity analysis if the residual value is near the threshold boundary.

Condition 4 sub-step 4b (literature grounding audit) requirements:
- For each non-WEIRD-specific mode distribution rule in phase-1-mode-assignment-heuristic.md, run Perplexity DR to verify grounding in primary-source cross-cultural RMT literature.
- Apply Rule 19 Marcus Reed Protocol three-condition gate: (1) source exists (URL verified); (2) source says what the rule cites it as saying (primary-text quote verification); (3) semantically applicable to the framework's tycoon-simulation use case (not name-collision with unrelated construct).
- Flag any rules that fail the gate.

BANS:
- No persona theater ("As a research agent I will...")
- No generic methodology recap ("Partialling regression is a statistical technique that...")
- No summarization-without-citation ("The literature suggests..." without URLs)
- No claims about what "the operator" wants; execute the specified procedure and report results

OUTPUT SHAPE:
Aggregate report in markdown. Sections in order: (1) Verification trail; (2) Condition 3 sub-step 3b analysis + result; (3) Condition 3 sub-step 3c methodology calibration + interpretation; (4) Condition 4 sub-step 4b literature grounding audit + result; (5) Aggregate four-condition PASS/FAIL matrix (Condition 1 and 2 from Phase 1; Condition 3 from this phase; Condition 4 from Phase 1a + this phase 4b combined); (6) Aggregate verdict (OPERATIONALIZE / RETIRE / FIX-HEURISTIC-BEFORE-PROCEEDING); (7) Honest weakness flags on the analysis itself.
```

### Phase 2 handoff artifacts to Phase 3

- `phase-2-aggregate-report.md` — the seven-section report specified in the Comet prompt output shape
- `phase-2-data-analysis-artifact.ipynb` (or equivalent) — the actual Colab/Kaggle notebook with the regression + assumption checks, for operator + CC re-audit
- `phase-2-limitations.md` — Comet's honest weakness flags on its own analysis

### Phase 2 failure modes + fallbacks

- **Comet stalls on the partialling regression.** Fallback: Claude Code can run the analysis via local Python (scikit-learn / statsmodels / pingouin) in a Bash-executed script. Comet's advantage is speed + multi-source integration + browser-based tooling, not capability exclusivity. If Comet stalls, redirect to Claude Code and lose the Perplexity DR methodology calibration piece (which Claude Code can partially compensate via WebFetch/WebSearch on methodology sources).
- **Comet produces uncalibrated output (persona theater, no citations, opaque format).** Fallback: this is the exact failure mode the paired-n=4 substrate-discipline lesson documented. Re-run with prompt tightened per the memory's Tier 1 discipline (mandatory verification trail; ECHO/NOVEL fields with URLs; explicit bans). If second run still uncalibrated, redirect to Perplexity Deep Research directly (not Comet-driven; operator runs the DR query manually) plus Claude Code for the statistical piece.
- **Residual variance measurement is ambiguous (near-threshold value).** This is design territory, not framework-discipline territory. Phase 2 should surface the ambiguity in the aggregate report; Phase 3 (operator ratification) is where the ambiguity gets resolved via operator judgment on how much upside the operationalization needs to justify the 36-72h investment.

---

## Phase 3 — Operator ratification + write-back (Claude Code executes)

**Estimated cost: 1-2 hours operator + 2-4 hours Claude Code**

**Objective:** operator reviews Phase 2 aggregate report; ratifies the aggregate verdict (or contests it); Claude Code executes the canonical mutations that follow from the ratified verdict.

### Phase 3 task list

1. **Operator reads Phase 2 aggregate report.** Reviews the four-condition PASS/FAIL matrix, the residual-variance measurement, the literature-grounding audit outcomes, and Comet's honest weakness flags on its own analysis.
2. **Operator ratifies aggregate verdict or contests.** Per Rule 10 Conservative-Bias, ambiguous residual-variance measurements should default to RETIRE unless the operator has design-side reason to accept the ambiguity. Rule 19 Marcus Reed Protocol failures on Condition 4b (fabricated cross-cultural attributions) block ratification; the heuristic must be re-derived with primary-source-verified grounding before proceeding.
3. **Claude Code executes the canonical mutation matching the ratified verdict:**
   - **If OPERATIONALIZE ratified:** Claude Code produces a V1.x operationalization spec (new post in the framework corpus; SUMMARY.md update; post-ideas.md status update). The spec covers: mode-assignment production heuristic (informed by Phase 1's prototype heuristic + operator scholarship); mode-gate production implementation; consolidation-pass extension for mode assignment; cached-policy regeneration extension; audit-layer extension for mode-discipline compliance; test-run validation across tycoon-population scenarios. Estimated V1.x BUILD-side cost: 36-72h (bracketing Post 0126's 33-88h Wireduan-generosity-ledger estimate).
   - **If RETIRE ratified:** Claude Code produces a schema migration to remove the `relationship_mode` field from the pair-summary record; amends Post 0130 with the empirical finding as a dated update-note (per framework's immutability convention; post body remains unchanged; the update-note documents the ablation gate outcome + retirement); updates SUMMARY.md; documents the retirement as a memory record.
   - **If FIX-HEURISTIC-BEFORE-PROCEEDING ratified:** Phase 1 sub-step 1 (prototype mode-assignment heuristic) re-runs with the specific fixes Phase 2's Condition 4b audit identified; the full ablation gate re-runs from the fix point. No canonical mutation until re-run produces ratifiable verdict.
4. **Update auto-memory.** Regardless of verdict: memory records for the ablation gate execution + the ratified verdict + any Phase 2 methodology decisions worth preserving for future ablation-gate work.
5. **Run `regen_launcher_hashes.py`** to refresh the Treasure Map / CC-nav payload if posts changed.

---

## Cost aggregation

| Phase | Surface | Estimated cost |
|---|---|---|
| Phase 1 (BUILDER) | Claude Code | 15-26h |
| Phase 2 (RESEARCH-AGENT) | Comet Computer | 7-16h |
| Phase 3 (RATIFICATION + WRITE-BACK) | Operator + Claude Code | 3-6h |
| **Total ablation gate execution** | **Composed** | **25-48h** |
| V1.x operationalization (if PASS) | Claude Code | 36-72h |
| Schema retirement (if FAIL) | Claude Code | 2-4h |

The ablation gate itself (25-48h) is a fraction of the V1.x operationalization it gates (36-72h). The gate's job is to prevent spending the 36-72h if the enum will not earn its variance; the gate's cost is the price of that certainty.

---

## Scheduling considerations

Per Post 0129's analysis + framework Rule 10 Conservative-Bias, three reasonable scheduling options:

1. **Now-ish, before V1 ship (2026-10-31):** answer is known before V1 locks. Cost: 25-48h out of the remaining V1 budget for what is essentially R&D on a V1.x decision. Pro: no post-V1 uncertainty. Con: V1 budget contention.
2. **Immediately after V1 ships, before V1.x planning:** no V1 budget contention. Pro: shipped code is available for the prototype to extend. Con: V1.x scoping conversations happen without the empirical answer.
3. **Whenever V1.x scoping needs the answer:** cost falls at the exact decision moment. Pro: no waste on premature ablation. Con: V1.x planning might commit to operationalization before the ablation runs; finding out after-the-fact that the ablation fails is worse than finding out during planning.

Framework recommendation: Option 2 (defer the cost; don't spend V1 budget on a V1.x decision). But this is operator-judgment territory on how much you value knowing-early vs. protecting the V1 budget.

---

## Cross-references

- **Post 0129** — Council #1 close narrative; documents how the ablation gate was synthesized (Substrate B's mechanism composed with Substrate C's setting) and why Pattern B ADOPT-FOLD was the correct classification
- **Post 0130** — Reserved slot architectural spec; documents the schema commitment + the four-condition ablation gate at the architecture level
- **Post 0128** — Schema-placeholder discipline precedent (`cultural_context_tag` + `intersectional_position_tags[]` + `identity_stage`); parallel pattern to `relationship_mode` slot
- **Post 0126** — Wireduan generosity-ledger mechanic; 33-88h estimate for structurally-comparable relational primitive; Steam V1.0 deferral precedent
- **Post 0119** — Audit-first sequencing discipline under Path A; the discipline this ablation gate operationalizes
- **`~/Projects/the-street-code/_archive/2026-06-30-council-1-relationship-mode/`** — Council #1 substrate outputs (A/B/C) + orchestrator synthesis
- **`~/.claude/projects/-Users-jimmy/memory/project_council_1_close_pattern_b_2026-06-30.md`** — Council #1 arc close memory
- **`~/.claude/projects/-Users-jimmy/memory/feedback_rule_14_pattern_a_vs_b_modal_status_check.md`** — Rule 14 Pattern A vs B modal-status-check discipline
- **`~/.claude/projects/-Users-jimmy/memory/feedback_substrate_opaque_citation_format_as_risk_signal.md`** — paired-n=4 substrate-discipline calibration lesson informing the Phase 2 Comet prompt
- **`~/.claude/projects/-Users-jimmy/memory/feedback_substrate_self_attestation_unenforceable.md`** — Rule 19 substrate-self-attestation-unenforceable discipline informing the verification trail requirement
- **Zakharin & Bates 2023** — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0287391 — the psychometric evidence foreshadowing the Condition 3 collinearity worry

---

## Guide revision protocol

Update this guide when:
- Any phase runs and surfaces a procedure refinement (Phase 1 heuristic design, Phase 2 methodology calibration, Phase 3 ratification pattern)
- The paired-n=4 substrate-discipline lesson evolves (Comet prompt calibration changes)
- A new ablation-gate deployment against a different Council decision surfaces reusable pattern (candidate promotion from guide to general methodology template)
- Framework canonical files that this guide cross-references (Post 0128 schema-placeholder discipline; Rule 14 Pattern B vocabulary; Rule 19 Marcus Reed Protocol) update in ways that affect guide content

Do NOT retroactively edit the guide's core procedure after a phase begins execution; per the framework's immutability convention, mid-execution scope changes are anti-pattern territory. Add dated update-notes at the guide's foot instead.
