# Per-NPC Philosophy Profile Reservation-Plus-Ablation-Gate Execution Guide V1

**Established:** 2026-07-01 (post-Council-#4-close session; companion to posts 0134 + 0135)
**Maintained by:** operator; CC updates on empirical contact
**Purpose:** Clean-room execution guide for the three-condition ablation gate that unlocks (or retires) the V1.x operationalization of the reserved `normative_profile` per-NPC schema slot Substrate D specified during Council #4. Standalone-executable: a fresh CC session, fresh substrate, or future-operator can open this file with zero prior context and run the gate end-to-end.
**Provenance:** Council #4 (cross-cultural discipline audit + per-NPC philosophy architecture) closed 2026-07-01 at Pattern B ADOPT-FOLD via Option B per-item deliberation. Consolidated seven-decision amendment package documented in Post 0135; this guide operationalizes Decision 4 (per-NPC-philosophy-profile BANK).

---

## What this guide is and is NOT

**This guide is** the standalone-executable operational procedure for the ablation gate. It enumerates: the three ablation conditions with pass/fail criteria; the task decomposition across Claude Code (BUILDER surface) and Comet Computer (RESEARCH-AGENT surface); the calibrated prompts for each surface; the per-phase cost estimates; the failure modes plus fallbacks; the handoff artifacts each phase produces.

**This guide is NOT** the architectural spec for the reserved slot (Post 0135 Decision 4 is the spec) or the narrative of how Council #4 arrived at the ablation gate (Post 0134 is the narrative) or the substrate outputs themselves (archived at `~/Projects/the-street-code/_archive/2026-07-01-council-4-cross-cultural-discipline-audit/`). The guide points to those artifacts; it does not duplicate their content.

---

## The three ablation conditions (recap for standalone use)

All three are conjunctive. If any one fails, the reserved slot is retired at near-zero sunk cost and Post 0135 Decision 4's canonical status is amended with the empirical finding. If all three pass for the specific philosophy family under audit, the V1.x operationalization proceeds for that family only (one profile family at a time; broader profile-catalog deployment depends on repeat gate execution per family).

### Condition 1 — Primary-text verification of metadata-only transition sources

**Question:** does the philosophy family's normative rule-set have primary-text grounding at direct-primary-text depth, distinct from Substrate D's access-mode-limited metadata-only surfacing?

**Procedure:** for each rule the profile family encodes (e.g., "Menkitian achievement-graded moral status graduates by demonstrated moral maturity"; "Gyekyean intrinsic dignity plus community enhancement"; "Wireduan sympathetic impartiality grounds normative universality"), verify at primary-text depth. Verification means: PDF or physical copy of the primary source in operator's hands; page-cited passage read verbatim; extracted quotation matches the rule's operational claim.

**Pass criterion:** every load-bearing rule in the profile family's rule-set is grounded in a primary-text passage the operator has verified at direct-primary-text depth.

**Fail criterion:** any load-bearing rule rests on Substrate D's access-mode-limited metadata surfacing without operator-side primary-text confirmation. Interpretation: retire the profile family from V1.x operationalization scope; the rule-set may still be reservable for future operationalization when primary-text access surfaces, but the rule-set cannot ship as production game-logic until primary-text verification closes.

**Why this is a load-bearing condition:** Substrate D honestly disclosed access-mode limitations at Council #4; the calibrated anti-fabrication prompt did not catch every metadata-only entry because "access-limited-but-honestly-disclosed" is exactly the discipline-target the framework's Rule 19 3-condition gate is designed to catch. Condition 1 is the primary-text-verification enforcement of Rule 19 Condition 3b (source says what cited) plus Condition 3c (source is semantically the operator's entity, not name-collision) at the specific-rule scope.

### Condition 2 — Ablation against sentiment-only baselines plus trait-only baselines

**Question:** does the philosophy profile do UNIQUE work beyond what the sentiment scalar plus HEXACO-H trait already carry?

**Procedure:** across the prototype population running the profile family, run three-way comparison:
- Run A: full profile-family decision-scoring
- Run B: sentiment-only decision-scoring (profile field forced to `UNDEFINED_OR_MIXED`; sentiment scalar carries the work)
- Run C: trait-only decision-scoring (profile field forced to `UNDEFINED_OR_MIXED`; HEXACO-H carries the work)

Diff the resulting decision distributions plus downstream NPC behavior. Partialling regression: quantify how much profile-driven variance in decision-scoring survives after subtracting off variance predictable from sentiment scalar (Run B baseline) plus HEXACO-H trait (Run C baseline).

**Pass criterion:** substantial residual variance after partialling against BOTH sentiment scalar AND HEXACO-H trait. Threshold requires methodology calibration (see Phase 2 Comet Computer brief below); as a directional anchor, residual should be at minimum non-trivial in effect-size terms (a psychometrics-literate collaborator should specify the effect-size threshold empirically per the prototype population's characteristics).

**Fail criterion:** residual variance is negligible after partialling; profile is largely re-encoding sentiment plus HEXACO-H in fancier language. Interpretation: this is the specific failure mode the framework's Council #1 relationship-mode ablation gate documented (Zakharin & Bates 2023 general-factor foreshadowing pattern applied at profile-vs-sentiment axis); retire the profile family; the framework's existing sentiment scalar plus HEXACO-H already carry the differential-variance work the profile would nominally provide.

**Why this is the load-bearing empirical condition:** Substrate D's proposed architecture is philosophically distinguishable; the empirical question is whether the philosophical distinguishability produces mechanically-distinguishable NPC behavior beyond what existing decomposition already produces. Passing Condition 1 while failing Condition 2 corresponds to "the rule-set is primary-text-grounded, but the mechanism doesn't add operational variance." That is the exact failure mode that would waste 40-80h of BUILD-side work per profile family.

### Condition 3 — One profile family at a time with source-specific tests before broader profile-catalog deployment

**Question:** does the profile-catalog operationalization architecturally hold when scaled across multiple profile families, or does inter-family interaction reintroduce armor risk?

**Procedure:** even if Conditions 1 + 2 pass for the specific profile family under audit, the V1.x operationalization proceeds for that family only. Broader profile-catalog deployment (a second philosophy family; a third; the full four-Akan-plus-additional-clusters catalog Substrate D outlined) requires re-running Conditions 1 + 2 per family AND running the inter-family interaction audit specified below.

Inter-family interaction audit (per additional family): run the prototype population with TWO profile families deployed; audit whether NPCs assigned to Family A behave differently in the presence of NPCs assigned to Family B versus in a Family-A-homogeneous population. If the presence-of-Family-B does not shift Family-A NPC decision-scoring in ways that trace to Substrate D's `TRANSITIONS-CARRY-ARMOR-RISK` clause (deterministic demographic assignment; decorative catalog labels; trauma-triggered toggles; player-facing overclaim), the multi-family deployment passes for the specific pair under audit.

**Pass criterion:** for each family added to the operational catalog, Conditions 1 + 2 pass for the family AND the inter-family interaction audit passes for every existing-family/new-family pair in the operational catalog.

**Fail criterion:** any of the sub-audits fail. Interpretation: DEMOTE the failing family to reservation-only status; keep prior families operational; document the failure mode in the profile-family's canonical status entry.

**Why this is a scale-up condition rather than a per-family condition:** Substrate D's architecture is philosophically appealing at single-family scope; the risk it inherits from the framework's Council #4 anti-armor discipline is that scaling across families reintroduces exactly the deterministic-catalog / decorative-labels failure mode Substrate B diagnosed. Condition 3 is the framework's structural safeguard against catalog-scale armor accumulation.

---

## Task decomposition across surfaces

The gate composes work across two substrates. Neither can execute the whole gate alone; the composition is what makes the gate schedulable at reduced total cost.

**Claude Code (BUILDER surface):** filesystem access, terminal execution, git operations, simulation runs against local prototype code, data export as CSV, code audit, primary-text PDF ingestion via Read tool. Owns Condition 1 in full (primary-text verification via operator PDF ingestion), Condition 2 sub-step 2a (data extraction from prototype simulation runs), Condition 3 code-side audit sub-steps, and the final canonical mutations after operator ratification.

**Comet Computer (RESEARCH-AGENT surface):** browser-driven statistical tooling (Colab / Kaggle / JASP web / Perplexity code execution), Perplexity Deep Research literature search for methodology calibration, cross-substrate methodology calibration, browser-based document synthesis. Owns Condition 2 sub-step 2b (statistical analysis) + 2c (methodology calibration + interpretation), Condition 3 literature-side audit for any additional-family primary-source verification, and the aggregate report drafting.

---

## Phase 1 — Claude Code (BUILDER surface)

**Estimated cost: 12-22 hours BUILD-side work per profile family**

**Objective:** verify Condition 1 primary-text grounding for the specific profile family under audit; produce the prototype simulation state that generates the data Comet Computer will analyze for Condition 2; export Condition 2 sub-step 2a data as a handoff CSV; execute Condition 3 code-side audit sub-steps directly.

### Phase 1 task list

1. **Condition 1 primary-text verification (3-6h).** For each rule the profile family encodes, operator ingests the primary source via CC Read tool (PDF path required; secondary-mediated sources FAIL Condition 1 for the specific rule). CC produces verbatim quotation with page citation for each verified rule; produces a per-rule verification log. Rules that FAIL Condition 1 are struck from the family's rule-set for V1.x operationalization; rules that PASS Condition 1 proceed to Phase 1 sub-step 2.
2. **Prototype normative-profile assignment heuristic (2-4h).** Throwaway code. Reads `cultural_context_tag` + `intersectional_position_tags[]` + `identity_stage` + additional pair-relational context features per Post 0128 schema; produces a `normative_profile` assignment per NPC at NPC-generation time. Design constraint: heuristic must be principled enough that Condition 2's ablation test produces meaningful comparison across the three-way Run A/B/C conditions; heuristic must NOT deterministically demographically-assign (per Substrate B's anti-armor discipline).
3. **Prototype normative-profile gate on decision-scoring (4-8h).** Throwaway code. Modifies the expected-free-energy scoring pipeline to make specific scoring terms conditional on the NPC's assigned normative profile. Design constraint: the profile-gate must be structurally distinct from the sentiment-scalar-weighted terms already in the scoring pipeline plus the HEXACO-H-weighted terms already in the scoring pipeline (else Condition 2 will trivially fail).
4. **Run prototype simulation across tycoon-population scenarios (1-3h execution + wait time).** Populations: as specified in the framework's existing population catalog per methodology-guide-ablation-gate-relationship-mode-v1.md (staff loyalty; customer patronage; league competitor). Each population runs 5-15 game-years to accumulate sufficient NPC-behavior history for meaningful statistical power.
5. **Condition 2 sub-step 2a: data export (1-2h).** Export a CSV with per-NPC rows: `npc_id`, `population_type`, `normative_profile_assignment`, `sentiment_scalar_at_context`, `hexaco_h_score`, plus decision-scoring output distributions across a sample of candidate actions per Run A/B/C conditions. This is the handoff artifact Phase 2 consumes.
6. **Condition 3 code-side audit sub-steps (1-2h).** Verify the assignment heuristic does NOT deterministically demographically-assign; verify the profile-catalog does NOT decoratively-label without operationalization; verify the transition-mechanic (if any) does NOT trauma-trigger-toggle without primary-text grounding for the transition pathway. This audit produces the Condition 3 code-side handoff artifact for Phase 2's literature-side audit.

### Phase 1 handoff artifacts to Phase 2

Produce a `~/Desktop/npc-philosophy-gate-phase-1-handoff-YYYY-MM-DD-{profile-family}/` folder containing:

- `phase-1-report.md` — Condition 1 result (per-rule PASS/FAIL + verbatim quotations + page citations); Condition 3 code-side audit summary
- `phase-1-data.csv` — the exported per-NPC data for Condition 2 statistical analysis
- `phase-1-profile-assignment-heuristic.md` — extracted prose description of the heuristic's assignment rules, for Phase 2 sub-step 2c literature grounding
- `phase-1-limitations.md` — honest weakness flags (see below)

### Phase 1 honest weakness flags to surface

- The prototype normative-profile assignment heuristic is BUILDER-judgment; production heuristic should be operator-scholarship-informed. Phase 1 heuristic is designed to enable the gate to test the ARCHITECTURE (does the profile-catalog earn its variance) not the specific rulebook.
- The `hexaco_h_score` covariate specification is the wildcard variable for Condition 2. Phase 1 produces a candidate specification (documented in the handoff) but Phase 2's methodology calibration may specify a different specification the analysis re-derives.
- Population scenarios' sim-run duration affects statistical power. 5-15 game-years is an initial anchor; if Phase 2 finds statistical power insufficient, Phase 1 re-runs at longer duration.
- Condition 1's primary-text verification is limited to sources the operator can access at direct-primary-text depth. Rules that require primary-text access the framework does not currently have will FAIL Condition 1; this is discipline not failure of the source.

---

## Phase 2 — Comet Computer (RESEARCH-AGENT surface)

**Estimated cost: 6-14 hours per profile family (Comet-driven; operator supervises)**

**Objective:** execute Condition 2 sub-steps 2b (statistical analysis) + 2c (methodology calibration + interpretation); execute Condition 3 literature-side audit sub-steps; produce aggregate PASS/FAIL report for the three-condition gate per profile family.

### Phase 2 task list

1. **Load Phase 1 handoff into Comet-accessible environment (0.5-1h).** Upload `phase-1-data.csv` to Colab / Kaggle / Perplexity code execution. Load `phase-1-report.md` + `phase-1-profile-assignment-heuristic.md` + `phase-1-limitations.md` as Comet context.
2. **Condition 2 sub-step 2b: statistical analysis (3-6h).** Run three-way partialling regression per calibrated Comet prompt below. Iterate on model specification (covariate selection, HEXACO-H operationalization, sentiment-scalar operationalization, effect-size threshold). Verify assumptions (linearity, residual distribution, multicollinearity beyond the profile-sentiment-trait axis). Produce residual-variance estimate with confidence interval.
3. **Condition 2 sub-step 2c: methodology calibration + interpretation (1-3h).** Perplexity Deep Research query set on partialling methodology for three-way covariate ablation in individual-differences research. Cross-substrate calibration on effect-size threshold: what residual size counts as "substantial enough to justify the profile catalog" versus "negligible enough to retire the family." Draft interpretation with explicit acknowledgment of methodology-choice uncertainty.
4. **Condition 3 literature-side audit sub-steps (1-3h).** For each additional-family primary-source citation required for scale-up beyond the current family, verify grounding via Perplexity Deep Research. Apply Rule 19 Marcus Reed Protocol three-condition gate: source exists / says what cited / semantically applicable (per Council #4's canonized Condition 3c name-collision screening). Flag any sources that fail the gate.
5. **Aggregate report writeup (1-2h).** Assemble the three-condition PASS/FAIL matrix. Document the residual-variance measurement + confidence interval + methodology choices. Document the literature-grounding audit outcomes. Produce two-part recommendation: (a) PASS/FAIL verdict for each condition per profile family; (b) aggregate verdict (OPERATIONALIZE if all three pass for the family; RETIRE if Condition 1 or 2 fails; DEMOTE-FAMILY-KEEP-CATALOG if Condition 3 fails for a specific inter-family interaction).

### Phase 2 calibrated Comet Computer prompt (paste into Comet)

The prompt below is calibrated per the framework's paired-n=4 substrate-discipline lesson (`~/.claude/projects/-Users-jimmy/memory/feedback_substrate_opaque_citation_format_as_risk_signal.md`) plus the Council #4 anti-fabrication empirical-validation lesson (documented in Post 0134). Do not paraphrase; paste as-is.

````
You are executing Phase 2 of an ablation gate for a procedural-character architecture decision. The Phase 1 handoff folder (~/Desktop/npc-philosophy-gate-phase-1-handoff-YYYY-MM-DD-{profile-family}/) contains four files:

- phase-1-data.csv: per-NPC prototype simulation data. Expected columns: npc_id (string); population_type (enum: staff_loyalty / customer_patronage / league_competitor); normative_profile_assignment (enum: family-specific plus UNDEFINED_OR_MIXED reference); sentiment_scalar_at_context (float, range [-1.0, 1.0]); hexaco_h_score (float, standardized); decision_score_sample_{1..N}_A (floats, Run A full-profile scoring); decision_score_sample_{1..N}_B (floats, Run B sentiment-only scoring); decision_score_sample_{1..N}_C (floats, Run C trait-only scoring); plus per-NPC covariates from the pair-summary schema.
- phase-1-report.md: Condition 1 primary-text verification results with per-rule PASS/FAIL classification.
- phase-1-profile-assignment-heuristic.md: prose description of the assignment rules.
- phase-1-limitations.md: honest weakness flags from Phase 1.

If any expected file is missing or any expected column is absent from phase-1-data.csv, STOP and escalate to the operator with an explicit "missing handoff element" report. Do not proceed with defaults.

Your objective: execute Conditions 2 (sub-steps 2b and 2c) and Condition 3 literature-side audit sub-steps of the three-condition ablation gate specified in ~/Projects/the-street-code/methodology/per-npc-philosophy-profile-reservation-and-ablation-gate-v1.md. Produce a Phase 2 aggregate report suitable for operator ratification, plus a reproducible analysis notebook.

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
CONDITION 2 sub-step 2b (STATISTICAL ANALYSIS) — DETAILED PROCEDURE:
================================================================

STEP 1 — Data validation.
Load phase-1-data.csv. Verify: all expected columns present; normative_profile_assignment values are in the specified enum; sentiment_scalar_at_context values are in [-1, 1]; hexaco_h_score is numeric non-null. Report N (total NPCs), N per population_type, N per normative_profile_assignment. If any validation fails, STOP + escalate.

STEP 2 — Three-way partialling regression (hierarchical ΔR² approach across Runs A/B/C).
The load-bearing question is: how much variance in Run A decision-scoring survives after partialling out variance predictable from sentiment_scalar_at_context (Run B baseline) AND hexaco_h_score (Run C baseline).

Pseudocode (translate to concrete pandas + statsmodels):

```
# Aggregate decision_score across sampled candidate actions per NPC for each Run
score_A = [c for c in df.columns if c.startswith('decision_score_sample_') and c.endswith('_A')]
score_B = [c for c in df.columns if c.startswith('decision_score_sample_') and c.endswith('_B')]
score_C = [c for c in df.columns if c.startswith('decision_score_sample_') and c.endswith('_C')]
df['decision_score_A_mean'] = df[score_A].mean(axis=1)
df['decision_score_B_mean'] = df[score_B].mean(axis=1)
df['decision_score_C_mean'] = df[score_C].mean(axis=1)

# Block 1: sentiment_scalar alone
M0 = smf.ols('decision_score_A_mean ~ sentiment_scalar_at_context', data=df).fit()

# Block 2: sentiment_scalar + hexaco_h_score
M1 = smf.ols('decision_score_A_mean ~ sentiment_scalar_at_context + hexaco_h_score', data=df).fit()

# Block 3: sentiment_scalar + hexaco_h_score + profile dummies (drop UNDEFINED_OR_MIXED as reference)
df['normative_profile_assignment'] = pd.Categorical(df['normative_profile_assignment'],
    categories=['UNDEFINED_OR_MIXED'] + sorted([c for c in df['normative_profile_assignment'].unique() if c != 'UNDEFINED_OR_MIXED']))
M2 = smf.ols('decision_score_A_mean ~ sentiment_scalar_at_context + hexaco_h_score + C(normative_profile_assignment)',
             data=df).fit()

# Delta R-squared for each block transition
delta_r2_M0_to_M1 = M1.rsquared - M0.rsquared  # trait contribution
delta_r2_M1_to_M2 = M2.rsquared - M1.rsquared  # profile UNIQUE contribution above sentiment + trait

# Cohen's f-squared effect size for profile UNIQUE contribution
f2_profile = delta_r2_M1_to_M2 / (1 - M2.rsquared)

# Bootstrap 95% CI for delta_r2_M1_to_M2
np.random.seed(42)
bootstrap_deltas = []
for i in range(5000):
    sample = df.sample(n=len(df), replace=True, random_state=i)
    m1_b = smf.ols('decision_score_A_mean ~ sentiment_scalar_at_context + hexaco_h_score', data=sample).fit()
    m2_b = smf.ols('decision_score_A_mean ~ sentiment_scalar_at_context + hexaco_h_score + C(normative_profile_assignment)',
                   data=sample).fit()
    bootstrap_deltas.append(m2_b.rsquared - m1_b.rsquared)
ci_lower, ci_upper = np.percentile(bootstrap_deltas, [2.5, 97.5])
```

Also run the analysis per population_type subset. Population-specific ΔR² may differ meaningfully from pooled ΔR² and is diagnostic.

STEP 3 — Assumption checks (all mandatory; report each PASS/FAIL/CONCERN with figure or statistic in the notebook + summary in the report).
- Linearity: residuals-vs-fitted scatterplot for M2; visual inspection for pattern.
- Residual normality: QQ-plot + Shapiro-Wilk (if N < 5000) or Anderson-Darling (if N >= 5000) on M2 residuals.
- Homoscedasticity: Breusch-Pagan test on M2 residuals.
- Multicollinearity: VIF for sentiment_scalar_at_context AND hexaco_h_score in M2. VIF > 5 flags collinearity that would compromise the partialling interpretation.
- Sample-size sufficiency: report per-profile N; if any profile enum has N < 30, note that stability of that profile's dummy coefficient is questionable.

STEP 4 — Report the results in aggregate-report Section 2.
Pooled analysis: delta_r2_M1_to_M2, Cohen's f² for profile UNIQUE contribution, 95% bootstrap CI, all assumption-check outcomes.
Per-population analysis: delta_r2_M1_to_M2 with 95% CI for each of the three tycoon-population subsets; note which populations pass/fail their local threshold.
Assumption-check summary: any FAIL or CONCERN flags with implications for interpretation.

================================================================
CONDITION 2 sub-step 2c (METHODOLOGY CALIBRATION) — DETAILED PROCEDURE:
================================================================

STEP 1 — Threshold anchor.
Initial anchor: delta_r2_M1_to_M2 >= 0.05 AND Cohen's f² >= 0.02 (Cohen 1988 small-effect convention; https://doi.org/10.4324/9780203771587). PASS = both thresholds cleared in pooled analysis AND bootstrap CI lower bound exceeds threshold. AMBIGUOUS = CI crosses threshold. FAIL = CI upper bound below threshold.

STEP 2 — Threshold calibration via literature.
Run the following four seed Perplexity Deep Research queries (or their close equivalents). Report the returned top-3 sources per query with URL/DOI. Update the threshold anchor if the literature specifies field-specific convention differing from Cohen 1988:

Query 1 — Methodology: "Effect-size threshold conventions for hierarchical multiple regression delta R-squared in three-way covariate ablation individual-differences research"
Query 2 — Domain: "Cross-cultural normative philosophy operationalization LLM-agent architecture empirical validation"
Query 3 — Threshold specificity: "Small vs medium delta R-squared conventions in personality-psychology versus experimental psychology"
Query 4 — Assumption diagnostics: "Regression diagnostic best practices for hierarchical multiple regression with categorical predictors and standardized continuous covariates"

Document the returned sources with URL/DOI in the verification trail. If literature specifies a different threshold, note the specification and its source; use the literature-calibrated threshold as the PASS/FAIL cutoff; note the Cohen 1988 baseline for comparison.

STEP 3 — Sensitivity analysis if borderline.
If pooled delta_r2_M1_to_M2 CI crosses the threshold OR pooled and per-population results diverge in verdict, run sensitivity analysis:
(a) Alternative HEXACO-H operationalizations: raw score vs standardized vs quartile-binned.
(b) Alternative sentiment-scalar operationalizations: raw vs standardized vs contextualized-to-npc-history.
(c) Alternative bootstrap size: 10000 iterations instead of 5000.

Report which sensitivity variations change the verdict. If verdict is robust to all sensitivity variations, mark HIGH-CONFIDENCE-VERDICT. If verdict changes under at least one variation, mark VERDICT-CONTINGENT-ON-METHODOLOGY-CHOICE + escalate.

================================================================
CONDITION 3 LITERATURE-SIDE AUDIT — DETAILED PROCEDURE:
================================================================

For each additional-family primary-source citation required for scale-up beyond the current family under audit:

STEP 1 — Extract the citation.
Identify the citation's specific claim from the phase-1-profile-assignment-heuristic.md file's scale-up-readiness notes.

STEP 2 — Run Perplexity DR to verify grounding.
Query template: "[specific scholar name] [specific philosophy family] primary-text access"
Retrieve primary sources. Prefer peer-reviewed monographs or edited-volume chapters over general secondary sources.

STEP 3 — Apply Rule 19 Marcus Reed three-condition gate to each source:
- Condition 3a — source exists: URL verified; check that the URL returns HTTP 200 and that the returned page's title matches the cited title.
- Condition 3b — source says what the rule cites it as saying: locate the primary-text passage; quote it verbatim in the report; verify the passage supports the rule's operational claim.
- Condition 3c — source is semantically applicable AND NOT a name-collision (per Council #4's canonized sub-mode): not a name-collision with unrelated construct (verify the source is about the operator's specific philosophy family, not a generic-name-collision with a homonymous framework); not a different use of the same term; applicable to the framework's procedural-character use case.

STEP 4 — Report per-source verdict.
PASS: all three conditions met.
FAIL: any condition unmet; specify which and why.
AMBIGUOUS: source exists but semantic applicability is contested.

Condition 3 literature-side aggregate: PASS if all sources PASS; FAIL if any source FAILs; MIXED if some AMBIGUOUS + rest PASS.

================================================================
BANS:
================================================================
- No persona theater ("As a research agent I will...")
- No generic methodology recap ("Partialling regression is a statistical technique that...")
- No summarization-without-citation ("The literature suggests..." without URLs)
- No claims about what "the operator" wants; execute the specified procedure and report results
- No silent methodology substitution: if you deviate from the specified regression / operationalization / threshold, explicitly flag the deviation + reason in the verification trail
- No name-collision inference: if a philosophy-family term is homonymous with an unrelated framework (e.g., "five-element" as Wu-Xing versus operator's specific five-element cross-cultural discipline elements), do NOT infer semantic applicability from the name-match. Escalate to operator with an explicit name-collision-suspected report per Council #4 Rule 19 Condition 3c canonization.

================================================================
SELF-MONITORING + ESCALATION CRITERIA:
================================================================
Escalate to the operator (do not resolve to PASS or FAIL) if any of the following fire:
1. Phase 1 handoff missing expected files or columns.
2. Regression assumption checks show CONCERN or FAIL that materially affects interpretability.
3. delta_r2_M1_to_M2 95% CI crosses the calibrated threshold in pooled analysis (AMBIGUOUS classification).
4. Pooled and per-population verdicts diverge (e.g., staff_loyalty PASS but customer_patronage FAIL).
5. Sensitivity analysis shows verdict is contingent on methodology choice.
6. Any Condition 3 literature-side source FAILS the Rule 19 three-condition gate.
7. Name-collision suspected on any philosophy-family term.
8. Preferred environment (Perplexity code execution) is unavailable AND fallback environment is unavailable.

Escalation format: aggregate report Section 6 (Aggregate verdict) uses "ESCALATE — OPERATOR JUDGMENT REQUIRED" with a numbered list of the specific escalation triggers that fired + the specific ambiguity each trigger surfaces.

================================================================
OUTPUT ARTIFACTS:
================================================================

Artifact 1 — Aggregate report in markdown. Sections in order:
(1) Verification trail (per Mandatory Verification Trail spec above)
(2) Condition 2 sub-step 2b analysis + result (pooled + per-population; assumption-check summary)
(3) Condition 2 sub-step 2c methodology calibration (4 query results; threshold anchor + any calibration adjustment; sensitivity analysis if borderline)
(4) Condition 3 literature-side audit (per-source verdict with Rule 19 three-condition gate outcomes; name-collision-suspected flags)
(5) Aggregate three-condition PASS/FAIL matrix (Condition 1 from Phase 1; Condition 2 pooled + per-population; Condition 3 code-side from Phase 1 + Condition 3 literature-side from this phase)
(6) Aggregate verdict: OPERATIONALIZE-THIS-FAMILY / RETIRE-THIS-FAMILY / DEMOTE-FAMILY-KEEP-CATALOG / ESCALATE
(7) Honest weakness flags on the analysis itself (methodology choices you defaulted; assumption-check concerns; sensitivity contingencies)

Artifact 2 — Reproducible analysis notebook. Save as .ipynb (Jupyter/Colab format). Include markdown cells explaining each analysis step; code cells with the actual regression + assumption checks + bootstrap CI; output cells with figures. Package with a top-line requirements list (pandas + numpy + statsmodels + pingouin + matplotlib) and random seed 42. Save to phase-2-analysis-artifact.ipynb.

Both artifacts hand off to Phase 3 (operator ratification + Claude Code canonical mutation).
````

### Phase 2 handoff artifacts to Phase 3

- `phase-2-aggregate-report.md` — the seven-section report specified in the Comet prompt output shape
- `phase-2-data-analysis-artifact.ipynb` (or equivalent) — the actual Colab/Kaggle notebook with the regression + assumption checks, for operator + CC re-audit
- `phase-2-limitations.md` — Comet's honest weakness flags on its own analysis

### Phase 2 failure modes + fallbacks

- **Comet stalls on the three-way partialling regression.** Fallback: Claude Code can run the analysis via local Python (scikit-learn / statsmodels / pingouin) in a Bash-executed script. Comet's advantage is speed + multi-source integration + browser-based tooling, not capability exclusivity.
- **Comet produces uncalibrated output (persona theater, no citations, opaque format).** Fallback: this is the exact failure mode the paired-n=4 substrate-discipline lesson documented. Re-run with prompt tightened per the memory's Tier 1 discipline. If second run still uncalibrated, redirect to Perplexity Deep Research directly plus Claude Code for the statistical piece.
- **Comet triggers a name-collision fabrication (per Council #4 Rule 19 Condition 3c canonization).** Fallback: escalate to operator immediately; do not proceed with contaminated verdict; operator-side primary-text spot-check required before verdict ratification.
- **Residual variance measurement is ambiguous (near-threshold value).** This is design territory, not framework-discipline territory. Phase 2 should surface the ambiguity in the aggregate report; Phase 3 (operator ratification) is where the ambiguity gets resolved via operator judgment on how much upside the operationalization needs to justify the 40-80h investment per profile family.

---

## Phase 3 — Operator ratification + write-back (Claude Code executes)

**Estimated cost: 1-2 hours operator + 2-4 hours Claude Code per profile family**

**Objective:** operator reviews Phase 2 aggregate report; ratifies the aggregate verdict (or contests it); Claude Code executes the canonical mutations that follow from the ratified verdict.

### Phase 3 task list

1. **Operator reads Phase 2 aggregate report.** Reviews the three-condition PASS/FAIL matrix, the residual-variance measurement, the literature-grounding audit outcomes, and Comet's honest weakness flags on its own analysis.
2. **Operator ratifies aggregate verdict or contests.** Per Rule 10 Conservative-Bias, ambiguous residual-variance measurements should default to RETIRE-THIS-FAMILY unless the operator has design-side reason to accept the ambiguity. Rule 19 Marcus Reed Protocol failures on Condition 3 literature-side (fabricated cross-cultural attributions; name-collision-fabricated inferences) block ratification; the profile family must be re-derived with primary-source-verified grounding before proceeding.
3. **Claude Code executes the canonical mutation matching the ratified verdict:**
   - **If OPERATIONALIZE-THIS-FAMILY ratified:** Claude Code produces a V1.x operationalization spec (new post in the framework corpus; SUMMARY.md update; post-ideas.md status update). The spec covers: production normative-profile assignment heuristic (informed by Phase 1's prototype heuristic + operator scholarship); profile-gate production implementation; test-run validation across tycoon-population scenarios. Estimated V1.x BUILD-side cost per family: 40-80h.
   - **If RETIRE-THIS-FAMILY ratified:** Claude Code produces a schema migration adjustment (reserved slot retention if catalog scale-up may re-visit the family later; slot removal if family is judged fully retired); amends Post 0135 with the empirical finding as a dated update-note (per framework's immutability convention; post body remains unchanged; the update-note documents the ablation gate outcome + retirement); updates SUMMARY.md; documents the retirement as a memory record.
   - **If DEMOTE-FAMILY-KEEP-CATALOG ratified:** Claude Code demotes the family to reservation-only status while keeping any prior-operational families operational; amends the canonical status entry for the family with the inter-family interaction failure mode documented; catalog remains stable at prior-operational size.
4. **Update auto-memory.** Regardless of verdict: memory records for the ablation gate execution + the ratified verdict + any Phase 2 methodology decisions worth preserving for future ablation-gate work.
5. **Run `~/Projects/master-setup/regen_launcher_hashes.py`** to refresh the Treasure Map / CC-nav payload if posts changed.

---

## Cost aggregation

| Phase | Surface | Estimated cost per profile family |
|---|---|---|
| Phase 1 (BUILDER) | Claude Code | 12-22h |
| Phase 2 (RESEARCH-AGENT) | Comet Computer | 6-14h |
| Phase 3 (RATIFICATION + WRITE-BACK) | Operator + Claude Code | 3-6h |
| **Total ablation gate execution per family** | **Composed** | **21-42h** |
| V1.x operationalization per family (if PASS) | Claude Code | 40-80h |
| Schema retirement per family (if FAIL) | Claude Code | 2-4h |

The ablation gate itself (21-42h per family) is a fraction of the V1.x operationalization it gates (40-80h per family). The gate's job is to prevent spending the 40-80h if the profile family will not earn its variance; the gate's cost is the price of that certainty. Full profile-catalog operationalization multiplies these costs by the number of families; the framework's Path A envelope arithmetic does not comfortably absorb full catalog operationalization at V1 or V1.x; deferral to Steam V1.0 scope is architecturally consistent with Post 0126's Wireduan generosity-ledger mechanic deferral pattern.

---

## Scheduling considerations

Per Post 0135 Decision 4's operational framing plus framework Rule 10 Conservative-Bias, three reasonable scheduling options:

1. **Now-ish, before Steam V1.0 planning (approximately 2027):** answer is known before Steam V1.0 scoping locks. Cost: 21-42h per profile family out of the pre-V1.0 R&D budget. Pro: Steam V1.0 scoping can commit or not-commit with empirical foundation. Con: pre-V1.0 budget contention.
2. **Immediately after V1 ships, before V1.x planning:** no V1 budget contention. Pro: shipped code is available for the prototype to extend. Con: V1.x scoping conversations happen without the empirical answer.
3. **Whenever V1.x scoping needs the answer:** cost falls at the exact decision moment. Pro: no waste on premature ablation. Con: V1.x planning might commit to operationalization before the ablation runs; finding out after-the-fact that the ablation fails is worse than finding out during planning.

Framework recommendation: Option 2 (defer the cost; don't spend V1 budget on a V1.x decision). But this is operator-judgment territory on how much you value knowing-early vs protecting the V1 budget.

---

## Cross-references

- **Post 0134** — Council #4 close narrative; documents how the ablation gate was synthesized (Substrate D's per-NPC-philosophy architecture composed with Substrate B's anti-armor discipline) and why Pattern B ADOPT-FOLD was the correct classification
- **Post 0135** — Seven-amendment package spec including Decision 4 per-NPC-philosophy-profile BANK at the architecture level; canonizes Rule 19 Condition-3 name-collision as a new fabrication-discipline sub-mode
- **Post 0129** — Council #1 close narrative; parallel Pattern B ADOPT-FOLD via Option B per-item deliberation precedent
- **Post 0130** — Council #1 relationship-mode reserved-slot spec; parallel schema-placeholder + ablation-gate pattern the current guide inherits structural shape from
- **Post 0128** — Schema-placeholder discipline precedent (`cultural_context_tag` + `intersectional_position_tags[]` + `identity_stage`); parallel pattern to `normative_profile` slot
- **Post 0126** — Wireduan generosity-ledger mechanic; Steam V1.0 deferral precedent for structurally-comparable normative-primitive operationalization
- **Post 0119** — Audit-first sequencing discipline under Path A; the discipline this ablation gate operationalizes
- **Post 0124** — Five-element cross-cultural disclosure discipline canonization; the discipline Council #4 audited empirically
- **`~/Projects/the-street-code/methodology/ablation-gate-relationship-mode-v1.md`** — Council #1 relationship-mode ablation gate guide; the pattern this guide extends
- **`~/Projects/the-street-code/_archive/2026-07-01-council-4-cross-cultural-discipline-audit/`** — Council #4 substrate outputs (A/A'/B/C/D) + orchestrator synthesis
- **`~/.claude/projects/-Users-jimmy/memory/project_council_4_close_pattern_b_2026-07-01.md`** — Council #4 arc close memory
- **`~/.claude/projects/-Users-jimmy/memory/feedback_rule_19_condition_3_name_collision_new_submode.md`** — Rule 19 Condition-3 name-collision sub-mode canonization memory
- **`~/.claude/projects/-Users-jimmy/memory/feedback_substrate_opaque_citation_format_as_risk_signal.md`** — paired-n=4 substrate-discipline calibration lesson informing the Phase 2 Comet prompt

---

## Guide revision protocol

Update this guide when:
- Any phase runs and surfaces a procedure refinement (Phase 1 heuristic design, Phase 2 methodology calibration, Phase 3 ratification pattern)
- A new profile family enters gate execution and the family's rule-set requires primary-text access pattern not covered by current Condition 1 procedure
- The paired-n=4 substrate-discipline lesson evolves (Comet prompt calibration changes)
- A new ablation-gate deployment against a different Council decision surfaces reusable pattern (candidate promotion from guide to general methodology template)
- Framework canonical files that this guide cross-references update in ways that affect guide content

Do NOT retroactively edit the guide's core procedure after a phase begins execution; per the framework's immutability convention, mid-execution scope changes are anti-pattern territory. Add dated update-notes at the guide's foot instead.

---

## UPDATE-NOTE 2026-07-01 late evening: family-by-family primary-text feasibility matrix (empirical grounding for Condition 1 procedure)

Post-Council-#4 Coverage Gap 4 batch (documented at `~/Projects/the-street-code/_archive/2026-07-01-comet-batch-post-council-4/`) empirically surveyed primary-text access surfaces for African philosophy scholars named at Council #4 close. The following family-by-family matrix provides empirical grounding for the guide's Condition 1 procedure (primary-text verification per profile family):

| Family | Primary-text access status | Condition 1 feasibility | Scale-up sequencing rank |
|---|---|---|---|
| Akan (Wiredu / Gyekye) | Pre-existing framework corpus (Wiredu 1992 CRVP; Gyekye 1997 primary access) | Adequate baseline | Reference / already operational |
| Ubuntu (Metz / Tempels / Ramose) | Metz 2011 SciELO PDF open; Metz 2021 PhilPapers PDF open; Tempels 1959 CYRHO PDF open (with rights caveat); Ramose 1999 institutional-only | Feasible at Metz-first + Tempels-second reduced scope | 1st (highest feasibility) |
| Menkiti's 1984 chapter | University of Saint Thomas PDF empirically verified 2026-07-01 (contains "I am because we are" quote at page 171 with Mbiti attribution footnote) | Immediate primary-text feasible | Reference / already operational |
| Igbo (Nwala / Asouzu) | Nwala 1985 via IA controlled lending; Asouzu 2007 Google Books snippet-only | Marginally feasible (single-source Nwala; snippet-only Asouzu) | 2nd |
| Yoruba (Gbadegesin) | Institutional-only; Google Books / Open Library bibliographic; no authorized open PDF | BLOCKED without library affiliation | Deferred |
| Bantu-Rwandan (Kagame full text) | KAOWARSOM PDF is EXTRAITS only; NLA reading-room-only | BLOCKED without institutional visit | Deferred |
| Mbiti primary source | See citations file update-note 2026-07-01: Menkiti 1984 footnote 1 cites Mbiti 1970 Doubleday page 141, NOT 1969 Praeger pp. 108-109 as framework's original assumption held; 1970 Doubleday acquisition required | Bibliographic-lead-only pending acquisition | Reference / update-note context |

**Condition 1 procedure amendment:** when a new profile family enters gate execution, cross-check the family's primary-text sources against this matrix before executing Phase 1 Condition 1 primary-text verification. If the family is Ubuntu, Metz-family sources are directly PDF-accessible and Condition 1 primary-text verification can begin immediately at Metz scope. If the family is Yoruba or Bantu-Rwandan, Condition 1 primary-text verification requires operator-side institutional affiliation OR library ILL pathway BEFORE Phase 1 can execute meaningfully.

**Scale-up sequencing recommendation:** the guide's Condition 3 "one profile family at a time" discipline now has empirical grounding for family-ordering. Recommended scale-up sequence (assumes operator wants primary-text-verified profile families before operationalization):

1. **Ubuntu family FIRST** (highest primary-text feasibility; Metz 2011 + Metz 2021 + Tempels 1959 all directly accessible)
2. **Igbo family SECOND** (Nwala via IA controlled lending; single-source constraint noted)
3. **Yoruba and Bantu-Rwandan DEFERRED** until library affiliation OR alternative pathway resolves

Alternative sequencing (if operator prioritizes cross-family diversity over primary-text feasibility): operator judgment territory; the guide's Condition 3 does not enforce ordering, only one-family-at-a-time discipline.

**Empirical foundation:** Perplexity DR (single-substrate; 60 sources; 45-minute wall-clock; verified 2026-07-01 22:36-22:55 PDT; archived at `_archive/2026-07-01-comet-batch-post-council-4/gap-4-perplexity-dr.md`). Operator spot-check on 3 URLs empirically verified 2 (Menkiti 1984 PDF + Metz 2011 PDF); 1 (Google Books PA108) empirically DEMOTED (returned "No eBook available"). Rule 19 3-condition gate PASSES for the 2 verified URLs; single-substrate output is ratifiable at family-by-family matrix scope.

**Companion synthesis:** `_archive/2026-07-01-comet-batch-post-council-4/gap-4-comet-synthesis.md` (family-by-family analysis + operator acquisition worklist + Council #4 Decision 7 annotation upgrade candidacy analysis).

---

## UPDATE-NOTE 2026-07-02 evening: Council #2 Decision 3 Condition 2 modification (appraisal-tag baseline block insertion before profile block)

Council #2 close (documented in Posts 0139 + 0140 in this arc) canonized a specific modification to this methodology guide's Condition 2 procedure per Substrate D's specification. The modification inserts an appraisal-tag baseline block (Block 2) BEFORE the profile-specific block (Block 3) in the hierarchical regression structure Condition 2 canonizes at the v1 core procedure.

**Modified Condition 2 hierarchical regression blocks** (per Post 0140 Decision 3 + Substrate D specification):

- **Block 0 (controls):** `sim_id` + `population_type` + game year + event family + actor/target role + dyad prior-history length + relationship strength + random intercepts for NPC nested in Sim.
- **Block 1 (existing decomposition):** valence + arousal + stress + sentiment + attachment + typed-index category + HEXACO-H + other active trait covariates.
- **Block 2 (NEW appraisal-tag baseline):** `agency_attribution` + `expectedness_delta` + `goal_congruence` + `coping_control_estimate` + deliberately-lossy `norm_violation_tag` as generic universal-tag baseline (see fail condition below).
- **Block 3 (profile-specific):** `normative_profile_assignment` + `profile_norm_violation_score` + `profile × event_norm_signature` interaction + `profile_norm_violation_score × relationship_strength` interaction + profile-family × population_type interactions.

**Modified pass criteria** (profile dispatch adds unique variance beyond appraisal-tag baseline):
- Pooled ΔR² Block 2 → Block 3 ≥ 0.05
- Cohen's f² ≥ 0.02
- Bootstrap lower confidence bound clears pre-specified threshold
- Per-population effects directionally coherent (no unexplained population-family reversal)
- Cross-validated log-loss or Brier score improves for policy choices + memory salience

**Modified fail criteria:**
- Generic appraisal-tag block absorbs same variance profile dispatch would (the generic universal-tag adequately substitutes for profile-family-specific rules)
- Profile assignment only proxies demographics (empirically-driven by demographic features rather than philosophy-family-specific normative content)
- Profile labels become decorative (labels present but don't drive behavioral divergence)
- Wiredu-vs-Gyekye distinction vanishes after sentiment + trait + structural appraisal controls (per-philosophy-family normative rule-set specificity does not survive appraisal-tag-baseline block)

**Framework rationale for the modification:** the v1 methodology guide's original Condition 2 tested whether per-NPC-philosophy-profile normative dispatch adds unique variance beyond sentiment + HEXACO baselines. Substrate D at Council #2 correctly identified that appraisal-tags at Layer 2 consolidation cadence are a plausible competitor to per-NPC-philosophy-profile normative dispatch for the norm-violation-signal-carrying question. The modified Condition 2 tests whether profile dispatch adds unique variance beyond sentiment + HEXACO + appraisal-tag baselines. This is a more rigorous empirical test that decides the norm-violation-placement question empirically rather than by prior architectural commitment.

**Cross-references:**
- `~/Projects/the-street-code/posts/0139-council-2-close-when-the-orchestrator-caught-a-template-placeholder-passed-through-verification.md` — Council #2 close narrative
- `~/Projects/the-street-code/posts/0140-council-2-spec-seven-decision-appraisal-tag-amendment-package-plus-pdf-template-placeholder-fabrication-axis-canonization.md` — Decision 3 spec
- `~/Projects/the-street-code/methodology/appraisal-tag-reservation-and-ablation-gate-v1.md` — sibling methodology guide with Substrate B's Conditions 1-4 single-Sim ablation battery + Substrate C's multi-Sim playtester protocol
- `~/Projects/the-street-code/_archive/2026-07-02-council-2-appraisal-tags/council-2-substrate-d-perplexity-dr.md` — Substrate D's specification (source of the modification)

**Guide revision protocol:** per the guide's canonical revision protocol at v1 core procedure, mid-execution scope changes are anti-pattern territory. This update-note is a POST-CANONIZATION amendment landing before any Phase 1 execution against the v1 procedure has begun; the amendment lands with Council #2 close commit alongside the appraisal-tag methodology guide + the two Council #2 posts + auto-memory entries + operational-discipline-rules v1.19 → v1.20 bump. Future amendments follow same dated update-note pattern.
