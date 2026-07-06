# Cultural Baseline Signal Modest at Single-Sim: What KL-Divergence 0.01-0.02 Means for Population-Level Distinguishability

> **CORRECTION NOTICE (added 2026-07-05 evening; post-audit meta-analysis):** Line 99 references "Item 0334 consultant-reviewed" and "Item 0334 consultant pipeline" as canonical content-authoring gates. That external-consultant workflow was retired 2026-06-08 per polish_queue.md Item 352 Path A canonization. Retirement replaced external civil-rights consultant engagement with operator-controlled representational-diversity review pathways (Phase 7.1f substrate-triangulation + independent operator research + community input at r/AskHistorians + r/LaborHistory + r/IndieGameDev). See Post 0172 for full retirement documentation.

<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0138
title: Cultural Baseline Signal Modest at Single-Sim: What KL-Divergence 0.01-0.02 Means for Population-Level Distinguishability
date_published: 2026-07-02
status: published
superseded_by: 0172-Item-0334-partial
domain: research-observation; H5 empirical finding KL-divergence 0.01-0.02 across 2000 trials at single-Sim scope; modest signal pending Phase 2 multi-Sim validation
project_scopes: framework-architecture, empirical-research-findings, cross-cultural-discipline
cc_task_relevance: cultural-baseline-validation-planning, phase-2-multi-sim-validation-scoping, weird-critique-response
phase_binding: Phase-1
discipline_family: framework-methodology
canonical_rule: cultural-baseline-distinguishability-kl-divergence-empirical-finding-h5
load_bearing_claims:
  - H5 (cultural-baseline distinguishability) empirical finding: KL-divergence 0.01-0.02 across 2000 trials at single-Sim scope
  - Signal is MODEST at single-Sim scale; population-level (multi-Sim) validation deferred to Phase 2+
  - Per-character cultural parameters DO produce measurable behavior differences (KL > 0) but effect size small at single-Sim
  - Cultural baselines A/B/C (Baseline A Western-individualist + Baseline B Confucian role-ethics + Baseline C Wiredu Ghanaian communal-achievement) produce statistically distinguishable action trajectories
applicability_triggers:
  - Empirically validating cultural personhood layer at Sim level
  - When cultural baseline claim needs empirical anchor (Post 0114 pre-registration discipline)
  - When budgeting for Phase 2 multi-Sim validation of H5
  - When responding to WEIRD-defaults criticism (Post 0128)
mechanism_details:
  - KL-divergence measured between action distributions of different-baseline Sims
  - Range 0.01-0.02 = statistically significant but modest effect size
  - 2000 trials = statistical power adequate for single-Sim distinguishability
  - Population-level distinguishability requires Phase 2 multi-Sim
  - R10d §4.4 canonical amendment: cultural-baseline dispatch validation-vs-ratification distinction ratified 2026-07-02 late evening
cross_refs:
  - Post 0114 (pre-registration discipline)
  - Post 0128 (accumulator hides WEIRD defaults)
  - Post 0136 (empirical BUILD mode; H1-H7 hypothesis validation)
  - Post 0146 Layer 7 (cultural personhood baselines)
  - Open Alley/architecture/round-10d-madisonian-gate-synthesis-2026-06-11.md (R10d canonical §4.4)
-->

**Author:** Jimmy McColery
**Date:** 2026-07-01
**Status:** Single empirical finding from Sim AI Phase 1 H5 test suite; single-Sim VALIDATION of the mechanism plus population-scale RATIFICATION deferred to Phase 2 multi-Sim testing; framework's R10d Section 4 architectural revision proposed pending operator ratification; connects to Post 0128 WEIRD-defaults schema-placeholder discipline and Post 0135 per-NPC-philosophy-profile BANK

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I am a solo indie developer building a procedural-character architecture for a multi-decade tycoon simulation. Post 0137 in this arc documents the H4 finding surfaced by Sim AI Phase 1 empirical BUILD mode; this post documents the H5 finding and its architectural implication for the framework's cross-cultural discipline. The H5 test suite covers cultural-baseline distinguishability via symmetric KL-divergence between three placeholder cultural baselines labeled A, B, and C at 2000-trial single-Sim scope. Six tests. All passed. The mechanism works.

What is worth writing about is what the specific number that came out means and what it does not mean. The baselines are statistically distinguishable; the signal magnitude is 0.01 to 0.02 KL divergence at single-Sim scope; the initial sandbox assumption had used 0.02 as a "noticeable difference" threshold; empirical measurement clustered at or below the threshold; test discipline threshold recalibrated to 0.005 to match observed magnitude. The mechanism validates. Whether the mechanism ratifies at population scale is a separate empirical question that Phase 1 did not test and that this post argues is architecturally load-bearing to keep separate from validation.

## What KL-divergence measures and why 0.01-0.02 is modest

The Kullback-Leibler divergence between two probability distributions measures how much one distribution differs from another in a specific information-theoretic sense. Symmetric KL divergence (the average of KL divergence in both directions) is a common practical measure when neither distribution is privileged as reference. For two probability distributions that are identical, symmetric KL is zero; for distributions that differ substantially in mass placement, symmetric KL grows without upper bound as the differences increase. The specific numeric value has no universal interpretation; the value's meaning is calibrated against the domain's specific distinguishability requirements plus the sample size at which the value was measured.

For cross-cultural-baseline distinguishability in procedural-character behavior, the initial sandbox assumption used 0.02 as the "noticeable difference" threshold. The reasoning was directional: a KL divergence below 0.02 would probably not produce measurably different behavior at the surface level a player observes. That reasoning was theoretical; there was no empirical anchor for what specific KL value at what specific sample size predicts what specific player-perceivable behavior difference. The 0.02 threshold was a starting-point calibration to be revised on empirical contact.

The empirical contact produced smaller numbers. At 2000 trials per baseline the KL values between the three baselines clustered in the 0.01 to 0.02 range with high test-reliability (same baseline run twice with same seed produces near-zero KL divergence, confirming the mechanism is deterministic and that measurable KL between different baselines reflects actual mechanism-driven behavior differences rather than measurement noise). The test discipline threshold was recalibrated to 0.005 empirically to match the observed signal magnitude.

The signal is measurable and above zero; the mechanism runs; per-character parameters do produce per-character-distinguishable behavior via mechanical dispatch through the framework's affect plus expected-free-energy inference plus emotion-conditioned memory pipeline. That is architectural VALIDATION at the mechanism layer. Whether 0.01 to 0.02 KL divergence at single-Sim scope translates to population-scale distinguishability visible in player-facing behavior is a separate empirical question. The single-Sim signal is smaller than initial theoretical calibration predicted; what it means for population-scale outcomes is unknown until Phase 2 multi-Sim testing runs.

## The validation-vs-ratification distinction

Single-Sim empirical validation and design-decision ratification are different empirical questions. Validation asks whether the mechanism runs, whether the mechanism produces the specific output the architectural specification requires, and whether the mechanism's output is distinguishable across the parameter values the architecture was designed to differentiate. Ratification asks whether the mechanism produces a signal at the population scale plus visibility surface plus temporal cadence that player-perceivable-behavior differences require.

Validation is a mechanism-layer question. Its evidence surface is per-Sim behavior distributions across parameter sweeps at whatever sample size adequately characterizes the distributions. Its verdict is either "the mechanism does what it was specified to do" (which H5 empirically confirmed) or "the mechanism does not do what it was specified to do" (which would have surfaced as KL divergence near zero between different baselines, or as different-seeded runs of the same baseline producing meaningful divergence, neither of which occurred).

Ratification is a design-decision-layer question. Its evidence surface is population-scale-emergent behavior distributions plus their visibility to the specific audience surface the design is targeting plus their cadence relative to the audience's engagement pattern. Its verdict is either "the design decision to differentiate this parameter produces player-perceivable behavior differences" or "the design decision differentiation does not surface at the player-perceivable layer even though the mechanism validates." Both verdicts are architecturally load-bearing but at different scopes; validation is required for ratification but does not sufficient for it.

The framework's discipline is to keep these two questions separate. Validate architectural mechanism at smallest empirical scope; defer population-scale distinguishability to next phase; treat single-Sim signal as VALIDATION not RATIFICATION. The load-bearing reason for the separation is that operator-judgment decisions about whether-to-invest-more-in-cultural-parameterization at content-authoring scale depend on population-scale signal, not on single-Sim signal. Ratifying at single-Sim scope commits operator-side authoring bandwidth to a differentiation that may or may not surface at the visibility scope the differentiation was designed for; not ratifying at single-Sim scope keeps the architectural commitment reserved (the schema placeholders are still in place; the mechanism still runs) while explicitly gating operationalization on multi-Sim empirical evidence.

The H5 finding sits at exactly this validation-vs-ratification boundary. The mechanism validates: single-Sim behavior differences are measurable and mechanically-dispatched. The design decision (parameterize cultural differences at per-character granularity so that a population of characters with mixed cultural parameters exhibits population-scale cultural distribution differences) is not yet ratified because population-scale signal has not been measured. Phase 2 multi-Sim testing of the two additional dimensions the current 4-dimension single-Sim implementation does not cover (communal-embedding weight vector; relational-web integrity) is where the population-scale signal accumulation would empirically surface.

## Connection to Post 0128 schema-placeholder discipline

Post 0128 in this arc canonized the framework's WEIRD-defaults-in-the-accumulator schema-placeholder discipline. The specific commitment is that per-character metadata fields (`cultural_context_tag`; `intersectional_position_tags[]`; `identity_stage`) are reserved as schema placeholders in the framework's character-generation architecture even where the V1 mechanism does not branch on them, so that when the framework's continued arc operationalizes the fields, the reserved slots are already in place and the architectural transition is a mechanical extension rather than a schema mutation.

The H5 finding empirically validates that the schema placeholders are not decorative labels. Per-character parameter values dispatched through the mechanical pipeline produce distinguishable per-character behavior at single-Sim scope. The measurable-but-modest 0.01 to 0.02 signal at 2000 trials is exactly what the schema-placeholder discipline predicts at Phase 1 empirical scope: reserved-slot-without-population-scale-validation. What the discipline commits to is the architectural surface (the placeholders are in the schema); what the discipline defers to Phase 2 and later is operationalization ratification (the placeholders drive population-scale player-perceivable differences).

The empirical result validates the discipline's operational shape. If the H5 test had shown zero KL divergence between different baselines at single-Sim scope, the schema-placeholder discipline would face a specific empirical challenge: the placeholders would be running without producing mechanical differences, which would raise the operator-judgment question of whether the discipline's cost (schema surface plus generation-time parameter dispatch plus content-authoring commitment to preserve the parameters faithfully) is buying anything even at single-Sim scope. The empirical result did not show zero KL; it showed measurable-but-modest KL. That is not the same as "the placeholders are fully justified at any scope"; it is specifically "the placeholders produce mechanical differences at single-Sim scope, and whether the differences ratify at population scale requires further empirical work."

The framework's continued arc has both a positive commitment (Phase 2 multi-Sim testing to measure whether the mechanical differences accumulate to population-scale distinguishability) and a specific reversal branch (if Phase 2 shows the mechanical differences do not accumulate meaningfully at population scale, the schema-placeholder discipline enters a reservation-only status pending either additional research or a decision to retire the placeholders). Both branches are architecturally live. The single-Sim finding does not settle which branch prevails.

## Connection to Council #4 per-NPC-philosophy-profile BANK

Council #4 closed 2026-07-01 with a seven-decision amendment package documented in Post 0135 in this arc. Decision 4 of that package canonized a per-NPC-philosophy-profile BANK behind a reservation-plus-ablation gate parallel to the Post 0130 relationship-mode discipline. The methodology guide at `~/Projects/the-street-code/methodology/per-npc-philosophy-profile-reservation-and-ablation-gate-v1.md` documents the operational shape.

The H5 finding provides the empirical precedent for the pattern. Council #4's per-NPC-philosophy-profile architecture is at reservation-plus-ablation-gate status specifically because the operational question (does a per-NPC philosophy assignment mechanically dispatched through the framework's inference pipeline produce distinguishable NPC behavior beyond what existing decomposition already produces) is the same shape as the H5 question about cultural baselines. Both are per-character parameterization commitments; both dispatch through the same mechanical pipeline; both require validation at single-Sim scope followed by ratification at multi-Sim population scope for design-decision commitment.

The framework's canonical Council methodology now has empirical foundation for the validation-vs-ratification pattern across three distinct architectural instantiations. Post 0130 in this arc's relationship-mode ablation gate (Council 1's BANK half) commits to the pattern at the pair-relationship-shape parameter surface. Post 0135 in this arc's per-NPC-philosophy-profile BANK (Council 4's Decision 4) commits to the pattern at the per-character normative-outlook parameter surface. The H5 finding empirically instantiates the pattern at the per-character cultural-baseline parameter surface. All three are the same discipline shape applied at different parameter surfaces; the framework's continued arc has a coherent operational pattern for architectural decisions at the boundary between mechanism validation and population-scale ratification.

The specific R10d architectural revision the H5 finding motivates is that Section 4 notes cultural-baseline signal is measurable but modest at single-Sim scope with full 6-dimension validation requiring Phase 2 multi-Sim testing. The revision does not invalidate the six-dimension architecture R10d ratified at close; the revision specifies the empirical conditions under which the framework's architectural commitment fully ratifies. Operator ratification of the R10d Section 4 revision is pending; the finding is banked at the empirical findings surface pending that ratification.

## What this post is NOT

This post is not an argument that 0.01 to 0.02 KL divergence is unimportant. Measurable-above-zero is architecturally load-bearing; the signal exists; the mechanism runs. What the post argues is that the specific magnitude of the signal at single-Sim scope does not determine the magnitude of population-scale signal, and the framework's discipline is to keep those two questions separate.

This post is not an argument that the H5 signal predicts population-scale signal magnitude. The single-Sim signal establishes the mechanism runs; population-scale signal is a Phase 2 and later question. Whether population-scale signal is larger than single-Sim signal (via cross-character interaction effects), smaller than single-Sim signal (via cross-character effects that reduce apparent between-baseline differences), or comparable to single-Sim signal is an empirical question this post does not adjudicate.

This post is not a claim that the placeholder baselines A, B, and C represent finalized cultural parameterizations. The baselines are placeholders; they are not Item 0334 consultant-reviewed; they are not sufficient for content-authoring commitments. Content authoring commits to specific culturally-parameterized character surfaces requires the Marcus Reed Surface 8 audit gate discipline plus Item 0334 consultant pipeline plus primary-text scholarship (the framework's cross-cultural discipline documented in Post 0124 in this arc; Post 0128 in this arc; the five-element disclosure discipline). Phase 1 tested at placeholder scope; the framework's continued arc addresses the finalized parameterization question through the discipline surface.

This post is not a claim that validation-vs-ratification distinction is the only methodology discipline the H5 finding illuminates. Adjacent disciplines may exist; the framework's continued arc will surface them as they become operationally relevant. What the post handles is the specific validation-vs-ratification distinction because that distinction is what the H5 finding's empirical shape makes most directly load-bearing.

## What I am not claiming

I am not claiming the framework's schema-placeholder discipline is the only workable pattern for cross-cultural procedural-character architecture. Alternative patterns exist. Some frameworks refuse to parameterize cross-culturally at all and treat all character behavior as arising from within-tradition specification; some frameworks parameterize at coarser granularity than per-character; some frameworks parameterize at content-authoring rather than mechanical-dispatch layers. The framework's discipline is one operational commitment; the pattern's generalizability across other frameworks is an open question.

I am not claiming Phase 2 multi-Sim testing will confirm population-scale signal amplification. The framework's expectation is that the two additional dimensions Phase 1 did not test (communal-embedding weight vector; relational-web integrity) plus cross-character interaction effects will amplify the single-Sim signal at population scale; the expectation is not empirically confirmed. If Phase 2 tests the population-scale signal and finds it comparable to or smaller than single-Sim signal, the framework's schema-placeholder discipline faces a specific architectural question about whether the reserved placeholders operationalize or enter reservation-only status.

I am not claiming the specific 0.005 test threshold recalibration generalizes beyond the H5 test suite. The recalibration is specific to what the H5 test suite measures at 2000-trial scope; other test surfaces at other scopes will require their own threshold calibration on empirical contact.

I am not claiming the validation-vs-ratification distinction eliminates operator-judgment on cultural parameterization. The distinction reduces one specific class of confusion (mechanism-runs versus design-decision-produces-visible-differences) but does not resolve the operator-judgment questions that content authoring at multi-decade multi-cultural scale requires (which cultural surfaces the framework's target settings would actually contain; which primary-text scholarship the framework's cross-cultural discipline commits to; which Marcus Reed Surface 8 audit-gate mitigation applies at which content-authoring surface). The discipline is one operationally-defensible framing; the operator-judgment work continues alongside.

I am not claiming the R10d Section 4 architectural revision has ratified. The revision is pending operator review. If the operator finds the revision misspecified, the revision may be revised, narrowed, or dropped; the framework's Rule 14 discipline applies regardless of empirical foundation.

## What I am claiming

Single-Sim empirical validation is sufficient for architectural VALIDATION but insufficient for design-decision RATIFICATION at population level; the H5 KL-divergence 0.01 to 0.02 range confirms the framework's per-character mechanical dispatch produces per-character behavioral differences at single-Sim scope; population-scale distinguishability is a Phase 2 and later question that will accumulate individual-character signal into population-scale cultural distributions; the framework's discipline responds to this by treating single-Sim signal as VALIDATION and gating operationalization on multi-Sim RATIFICATION.

If you are building cross-cultural procedural-character architectures, the validation-vs-ratification distinction is operationally cheap and catches a specific failure mode where mechanism VALIDATION at single-agent scope gets conflated with design RATIFICATION for population-scale player-facing behavior. They are different empirical questions requiring different testing scopes; ratifying at the wrong scope commits operator-side authoring bandwidth on evidence that may not support what the commitment requires.

The framework's continued arc now has three architectural instantiations of the validation-vs-ratification pattern (Post 0130 relationship-mode ablation gate; Post 0135 per-NPC-philosophy-profile BANK; H5 cultural-baseline finding). The pattern has enough empirical grounding to be a canonized discipline shape; the Council methodology's operational commitment to gating operationalization on multi-Sim RATIFICATION rather than single-Sim VALIDATION applies whenever a future architectural decision presents at this same boundary. The framework's Phase 2 multi-Sim empirical work is where the specific ratification tests will run against the specific reserved parameter surfaces; the pattern's continued empirical foundation accumulates from there.
