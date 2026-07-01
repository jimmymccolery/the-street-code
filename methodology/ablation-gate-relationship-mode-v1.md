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

````
You are executing Phase 2 of an ablation gate for a procedural-character architecture decision. The Phase 1 handoff folder (~/Desktop/ablation-gate-phase-1-handoff-YYYY-MM-DD/) contains four files:

- phase-1-data.csv: per-pair prototype simulation data. Expected columns: pair_id (string); population_type (enum: staff_loyalty / customer_patronage / league_competitor); mode_assignment (enum: COMMUNAL_SHARING / AUTHORITY_RANKING / EQUALITY_MATCHING / MARKET_PRICING / UNDEFINED_OR_MIXED); sentiment_scalar (float, range [-1.0, 1.0]); closeness_gf_proxy (float, Phase 1 candidate operationalization); pair_interaction_frequency (integer, count of Layer 1 events between the pair in the recency window); decision_score_sample_{1..N} (floats, sampled candidate-action scores per pair); plus per-pair covariates from the pair-summary schema.
- phase-1-report.md: Conditions 1 + 2 + 4a results with PASS/FAIL classification.
- phase-1-mode-assignment-heuristic.md: prose description of the assignment rules.
- phase-1-limitations.md: honest weakness flags from Phase 1.

If any expected file is missing or any expected column is absent from phase-1-data.csv, STOP and escalate to the operator with an explicit "missing handoff element" report. Do not proceed with defaults.

Your objective: execute Conditions 3 (sub-steps 3b and 3c) and Condition 4 sub-step 4b of the four-condition ablation gate specified in ~/Projects/the-street-code/methodology/ablation-gate-relationship-mode-v1.md. Produce a Phase 2 aggregate report suitable for operator ratification, plus a reproducible analysis notebook.

================================================================
ENVIRONMENT + PACKAGE STACK:
================================================================
- Preferred environment: Perplexity's built-in code execution surface. Use this first.
- Fallback environment: Google Colab (upload phase-1-data.csv; save notebook to /content/ and export .ipynb before session ends).
- Required packages: pandas (data loading + manipulation); numpy (numerics); statsmodels (regression + assumption checks); pingouin (partial correlation + effect-size CIs); matplotlib (residual diagnostics + QQ plots). If the preferred environment lacks a package, install via pip install <pkg> at the top of the notebook.
- Random seed: numpy.random.seed(42) at notebook start for reproducibility across bootstrap operations.

================================================================
MANDATORY VERIFICATION TRAIL (first section of your output):
================================================================
- List every data column you read from phase-1-data.csv with type + observed range + N (rows) + missingness count
- List every methodology source you consulted with full URL / arXiv / DOI
- List every Perplexity Deep Research query you ran with the returned top-3 sources
- Explicitly acknowledge any data or methodology decisions where you defaulted to convention rather than empirical calibration
- Report the environment (Perplexity code execution vs Colab vs other) and the exact package versions used

================================================================
ECHO/NOVEL DISCIPLINE:
================================================================
For each substantive claim in your analysis, tag it ECHO (matches existing framework canon / prior methodology precedent) or NOVEL (new claim requiring justification). For every NOVEL claim, provide four fields: (1) claim in one sentence; (2) evidence source with URL/DOI; (3) confidence level H/M/L with justification; (4) what would change your mind.

================================================================
CONDITION 3 sub-step 3b (STATISTICAL ANALYSIS) — DETAILED PROCEDURE:
================================================================

STEP 1 — Data validation.
Load phase-1-data.csv. Verify: all expected columns present; mode_assignment values are in the specified enum; sentiment_scalar values are in [-1, 1]; closeness_gf_proxy is numeric non-null. Report N (total pairs), N per population_type, N per mode_assignment. If any validation fails, STOP + escalate.

STEP 2 — General-factor proxy operationalization.
Check phase-1-mode-assignment-heuristic.md for a specified closeness general-factor proxy. IF Phase 1 specifies a proxy, USE IT AS-IS (Phase 1 has the runtime context Phase 2 lacks). IF Phase 1 does NOT specify a proxy, use this fallback:

  closeness_gf_proxy_fallback = zscore(sentiment_scalar) + zscore(pair_interaction_frequency)

Document which path you took (specified vs fallback) in the verification trail.

STEP 3 — Regression specification (hierarchical ΔR² approach).
The load-bearing question is: how much variance in decision-scoring survives after partialling out closeness. Use hierarchical multiple regression measuring ΔR² when mode dummies enter block 2 after closeness enters block 1.

Pseudocode (translate to concrete pandas + statsmodels):

```
# Aggregate decision_score across sampled candidate actions per pair
score_cols = [c for c in df.columns if c.startswith('decision_score_sample_')]
df['decision_score_mean'] = df[score_cols].mean(axis=1)

# Block 1: closeness alone
M0 = smf.ols('decision_score_mean ~ closeness_gf_proxy', data=df).fit()

# Block 2: closeness + mode dummies (drop UNDEFINED_OR_MIXED as reference)
df['mode_assignment'] = pd.Categorical(df['mode_assignment'],
    categories=['UNDEFINED_OR_MIXED', 'COMMUNAL_SHARING', 'AUTHORITY_RANKING',
                'EQUALITY_MATCHING', 'MARKET_PRICING'])
M1 = smf.ols('decision_score_mean ~ closeness_gf_proxy + C(mode_assignment)',
             data=df).fit()

# Delta R-squared
delta_r2 = M1.rsquared - M0.rsquared

# Cohen's f-squared effect size
f2 = delta_r2 / (1 - M1.rsquared)

# Bootstrap 95% CI for delta R-squared
np.random.seed(42)
bootstrap_deltas = []
for i in range(5000):
    sample = df.sample(n=len(df), replace=True, random_state=i)
    m0_b = smf.ols('decision_score_mean ~ closeness_gf_proxy', data=sample).fit()
    m1_b = smf.ols('decision_score_mean ~ closeness_gf_proxy + C(mode_assignment)',
                   data=sample).fit()
    bootstrap_deltas.append(m1_b.rsquared - m0_b.rsquared)
ci_lower, ci_upper = np.percentile(bootstrap_deltas, [2.5, 97.5])
```

Also run the analysis per population_type subset (staff_loyalty; customer_patronage; league_competitor). Population-specific ΔR² may differ meaningfully from pooled ΔR² and is diagnostic — the framework's tycoon-population differentiation is exactly the setting where mode effects may vary by relationship shape.

STEP 4 — Assumption checks (all mandatory; report each PASS/FAIL/CONCERN with figure or statistic in the notebook + summary in the report).
- Linearity: residuals-vs-fitted scatterplot for M1; visual inspection for pattern.
- Residual normality: QQ-plot + Shapiro-Wilk (if N < 5000) or Anderson-Darling (if N >= 5000) on M1 residuals.
- Homoscedasticity: Breusch-Pagan test on M1 residuals (statsmodels.stats.diagnostic.het_breuschpagan).
- Multicollinearity: VIF for closeness_gf_proxy in M1. Because M1 contains one continuous covariate plus mode dummies, VIF should be < 5 unless mode dummies are collinear with closeness (which would indicate the ablation's null hypothesis: mode IS closeness relabeled). If VIF > 5, this is diagnostic, not fatal — report the VIF value in the results and flag the collinearity.
- Sample-size sufficiency: report per-mode N; if any mode enum has N < 30, note that stability of that mode's dummy coefficient is questionable.

STEP 5 — Report the results in aggregate-report Section 2.
Pooled analysis: ΔR², Cohen's f², 95% bootstrap CI, all assumption-check outcomes.
Per-population analysis: ΔR² with 95% CI for each of the three tycoon-population subsets; note which populations pass/fail their local threshold.
Assumption-check summary: any FAIL or CONCERN flags with implications for interpretation.

================================================================
CONDITION 3 sub-step 3c (METHODOLOGY CALIBRATION) — DETAILED PROCEDURE:
================================================================

STEP 1 — Threshold anchor.
Initial anchor: ΔR² >= 0.05 AND Cohen's f² >= 0.02 (Cohen 1988 small-effect convention; https://doi.org/10.4324/9780203771587). PASS = both thresholds cleared in pooled analysis AND bootstrap CI lower bound exceeds threshold. AMBIGUOUS = CI crosses threshold. FAIL = CI upper bound below threshold.

STEP 2 — Threshold calibration via literature.
Run the following four seed Perplexity Deep Research queries (or their close equivalents). Report the returned top-3 sources per query with URL/DOI. Update the threshold anchor if the literature specifies field-specific convention differing from Cohen 1988:

Query 1 — Methodology: "Effect-size threshold conventions for hierarchical multiple regression delta R-squared in psychometric general-factor validation studies"
Query 2 — Domain: "Fiske Relational Models Theory cross-cultural validation non-WEIRD samples"
Query 3 — Threshold specificity: "Small vs medium delta R-squared conventions in individual-differences research versus experimental psychology"
Query 4 — Assumption diagnostics: "Regression diagnostic best practices for hierarchical multiple regression with categorical predictors"

Document the returned sources with URL/DOI in the verification trail. If literature specifies a different threshold, note the specification and its source; use the literature-calibrated threshold as the PASS/FAIL cutoff; note the Cohen 1988 baseline for comparison.

STEP 3 — Sensitivity analysis if borderline.
If pooled ΔR² CI crosses the threshold OR pooled and per-population results diverge in verdict, run sensitivity analysis:
(a) Alternative proxy operationalizations: sentiment_scalar alone; pair_interaction_frequency alone; alternative weighting between the two.
(b) Alternative aggregation of decision_score: median instead of mean; per-candidate-action instead of aggregated.
(c) Alternative bootstrap size: 10000 iterations instead of 5000.

Report which sensitivity variations change the verdict. If verdict is robust to all sensitivity variations, mark HIGH-CONFIDENCE-VERDICT. If verdict changes under at least one variation, mark VERDICT-CONTINGENT-ON-METHODOLOGY-CHOICE + escalate.

================================================================
CONDITION 4 sub-step 4b (LITERATURE GROUNDING AUDIT) — DETAILED PROCEDURE:
================================================================

For each non-WEIRD-specific mode distribution rule documented in phase-1-mode-assignment-heuristic.md:

STEP 1 — Extract the rule.
Identify the rule's specific claim (e.g., "for cultural_context_tag = 'East-Asian-collectivist', mode distribution shifts toward COMMUNAL_SHARING by X%"). If Phase 1 did not produce any non-WEIRD-specific rules (heuristic conservatively left all non-WEIRD pairs UNDEFINED_OR_MIXED), report zero rules to audit and Condition 4b PASSES by no-rules-fired.

STEP 2 — Run Perplexity DR to verify grounding.
Query template: "Fiske Relational Models Theory distribution in [specific cultural context named by the rule]"
Retrieve primary sources. Prefer peer-reviewed cross-cultural RMT validation studies over general secondary sources.

STEP 3 — Apply Rule 19 Marcus Reed three-condition gate to each source Phase 1 cited:
- Condition 3a — source exists: URL verified; check that the URL returns HTTP 200 and that the returned page's title matches the cited title.
- Condition 3b — source says what the rule cites it as saying: locate the primary-text passage; quote it verbatim in the report; verify the passage supports the rule's quantitative or categorical claim.
- Condition 3c — source is semantically applicable: not a name-collision with unrelated construct (verify the source is about Fiske Relational Models Theory, not another "relational models" theory); not a different use of the same term (e.g., not a marketing-relational-models paper); applicable to the framework's tycoon-simulation use case.

STEP 4 — Report per-rule verdict.
PASS: all three conditions met.
FAIL: any condition unmet; specify which and why.
AMBIGUOUS: source exists but semantic applicability is contested.

Condition 4b aggregate: PASS if all rules PASS; FAIL if any rule FAILs; MIXED if some AMBIGUOUS + rest PASS.

================================================================
BANS:
================================================================
- No persona theater ("As a research agent I will...")
- No generic methodology recap ("Partialling regression is a statistical technique that...")
- No summarization-without-citation ("The literature suggests..." without URLs)
- No claims about what "the operator" wants; execute the specified procedure and report results
- No silent methodology substitution: if you deviate from the specified regression / proxy / threshold, explicitly flag the deviation + reason in the verification trail

================================================================
SELF-MONITORING + ESCALATION CRITERIA:
================================================================
Escalate to the operator (do not resolve to PASS or FAIL) if any of the following fire:
1. Phase 1 handoff missing expected files or columns.
2. Regression assumption checks show CONCERN or FAIL that materially affects interpretability.
3. ΔR² 95% CI crosses the calibrated threshold in pooled analysis (AMBIGUOUS classification).
4. Pooled and per-population verdicts diverge (e.g., staff_loyalty PASS but customer_patronage FAIL).
5. Sensitivity analysis shows verdict is contingent on methodology choice.
6. Any Condition 4 rule FAILS the Rule 19 three-condition gate.
7. Preferred environment (Perplexity code execution) is unavailable AND fallback environment is unavailable.

Escalation format: aggregate report Section 6 (Aggregate verdict) uses "ESCALATE — OPERATOR JUDGMENT REQUIRED" with a numbered list of the specific escalation triggers that fired + the specific ambiguity each trigger surfaces.

================================================================
OUTPUT ARTIFACTS:
================================================================

Artifact 1 — Aggregate report in markdown. Sections in order:
(1) Verification trail (per Mandatory Verification Trail spec above)
(2) Condition 3 sub-step 3b analysis + result (pooled + per-population; assumption-check summary)
(3) Condition 3 sub-step 3c methodology calibration (4 query results; threshold anchor + any calibration adjustment; sensitivity analysis if borderline)
(4) Condition 4 sub-step 4b literature grounding audit (per-rule verdict with Rule 19 three-condition gate outcomes)
(5) Aggregate four-condition PASS/FAIL matrix (Condition 1 + 2 from Phase 1; Condition 3 pooled + per-population; Condition 4a from Phase 1 + Condition 4b from this phase)
(6) Aggregate verdict: OPERATIONALIZE / RETIRE / FIX-HEURISTIC-BEFORE-PROCEEDING / ESCALATE
(7) Honest weakness flags on the analysis itself (methodology choices you defaulted; assumption-check concerns; sensitivity contingencies)

Artifact 2 — Reproducible analysis notebook. Save as .ipynb (Jupyter/Colab format). Include markdown cells explaining each analysis step; code cells with the actual regression + assumption checks + bootstrap CI; output cells with figures. Package with a top-line requirements list (pandas + numpy + statsmodels + pingouin + matplotlib) and random seed 42. Save to phase-2-analysis-artifact.ipynb.

Both artifacts hand off to Phase 3 (operator ratification + Claude Code canonical mutation).
````

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
