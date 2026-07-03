# Longitudinal Benchmark Methodology Guide v1 — Four Answer-Key Shapes Plus Pass Criteria Plus Directional Ablation Criteria Plus Six-Condition Reversal Branch

**Author:** Jimmy McColery
**Date:** 2026-07-02
**Status:** Framework canonical methodology artifact documenting the answer-key taxonomy plus pass criteria plus reversal branch conditions Council #5 close ratified at Rule 14 Pattern B ADOPT-FOLD via Option B per-item deliberation; parallel in shape to Post 0130 relationship-mode ablation gate guide plus Post 0135 per-NPC-philosophy-profile reservation-and-ablation-gate guide plus Post 0140 appraisal-tag reservation-and-ablation-gate guide; documented alongside companion methodology artifact `~/Projects/the-street-code/methodology/longitudinal-trace-catalogue-v1.md` documenting the two-tier catalogue Tier 1 executable-now plus Tier 2 reserved-at-Phase-3+-multi-Sim-gate

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## Purpose

Council #5 close ratified a longitudinal-benchmark methodology guide covering the answer-key taxonomy plus pass criteria plus directional ablation criteria plus six-condition reversal branch that the two-tier longitudinal-trace catalogue at `~/Projects/the-street-code/methodology/longitudinal-trace-catalogue-v1.md` executes against.

This methodology guide documents the four answer-key shapes per Substrate D plus the endpoint-plus-intermediate pass criterion per Substrate B plus the directional ablation criterion per Substrate B plus Substrate D's six-condition reversal branch verbatim plus the Phase-2-first sequencing rationale plus the Tier-2 gate definition plus the post-hoc answer-key generation pipeline for Phase 2+ empirical fires.

## The four answer-key shapes

Substrate D's architectural analysis identified that pre-specified synthetic traces have cleaner answer keys (a character should remember a promise, update trust asymmetrically, propagate a landmark event to the right subset, or fail the test if the trace is missing) while empirical Phase 2+ trajectories require post-hoc answer-key generation. The correct post-hoc unit is a sub-trajectory fire: a bounded segment where the log shows a potential failure, the trace contains enough preconditions to adjudicate it, and the expected invariant can be written after discovery.

Post-hoc answer keys land in four shapes.

### Invariant keys

**Definition:** given event X was encoded as landmark at time T, later decision Y must have access to that landmark unless an explicit forgetting/compression rule applies.

**Operationalization:** the invariant key shape is the direct operationalization of Post 0119's Markov-blanket isolation test at longitudinal cadence. The audit-layer cadence extends to per-consolidation-boundary check. The framework's V1 schema Layer 2 promoted-set plus entity-index pair summary preserve the landmark event; the cached policy at decision Y must incorporate the landmark's affective delta plus pair-history contribution.

**Pass criterion:** decision Y's cached-policy top-action rank reflects the landmark's presence at the pair-summary lookup surface. Absence of the landmark's contribution to decision Y (with no explicit forgetting/compression rule justifying the absence) is failure.

**Example applications:** T16 Broken-Bridge action-grounding trace (Y1 commitment must remain accessible at Y5 decision); T14 mixed refusal-to-reconciliation boundary (Y3 lie must remain accessible at Y5 autonomy-grant decision).

### Metamorphic keys

**Definition:** re-run the same trajectory with one variable changed (relationship asymmetry or cultural baseline or trait routing) and require a directionally different but internally coherent result.

**Operationalization:** the metamorphic key shape operationalizes Post 0135 Rider 3 spec-gap-benchmark-independent structure at scenario-trace scope. The framework runs the base trace at baseline configuration, then re-runs at counterfactual configuration with exactly one variable perturbed; the endpoint action plus intermediate-state must differ in a directionally coherent way.

**Pass criterion:** the perturbation-caused endpoint delta is directionally coherent with the perturbed variable's expected effect. Endpoint identity across perturbations (no delta) is failure. Endpoint delta in a direction incoherent with the perturbed variable's expected effect is failure.

**Example applications:** T04 relationship-consistent refusal (perturb trait routing from avoidant to secure; endpoint should shift from cool boundary to more direct response); T09 abstention when history insufficient (perturb cultural baseline; endpoint should shift within cautious-abstention regime, not to strong-inference confidence).

### Ablation keys

**Definition:** disable a mechanism and require measurable degradation following the ablation-gate logic in Post 0130 for relationship-mode operationalization plus Post 0135 for per-NPC-philosophy-profile plus Post 0140 for appraisal-tag consolidation.

**Operationalization:** the ablation key shape reuses the framework's canonical ablation-gate methodology at trace scope. The framework runs the base trace with the mechanism enabled, then re-runs with the mechanism disabled; the endpoint action plus intermediate-state must degrade in a measurable way.

**Pass criterion:** the ablation-caused endpoint delta is directionally coherent with the ablated mechanism's contribution. Ablation with no endpoint delta indicates the mechanism was not load-bearing for that trace (may indicate trace-mechanism mismatch or mechanism-not-load-bearing-at-scale finding). Ablation with endpoint delta in an incoherent direction is failure.

**Example applications:** all Tier 1 traces carry required ablation conditions per the catalogue specification. T01 no-pair-summary-consolidation ablation should reduce Earl's refusal specificity at endpoint. T05 no-slow-consolidation-pass ablation should erase the apology's carry-into-cached-policy at endpoint.

### Audit-alignment keys

**Definition:** compare cached-policy behavior against the audit-layer evaluator and flag divergences where the cached policy violates the current accumulator state, matching Post 0119's audit-first design at longitudinal cadence.

**Operationalization:** the framework's Post 0119 audit-layer sophisticated-inference apparatus runs at per-consolidation-boundary cadence. The cached policy's top-action rank at decision Y is compared against the audit-layer evaluator's sophisticated-inference verdict at the same decision Y. Divergences flag audit-alignment failures.

**Pass criterion:** cached-policy top-action rank aligns with audit-layer evaluator verdict at each decision point in the trace. Divergences where cached policy violates the current accumulator state are failures.

**Example applications:** T16 Broken-Bridge action-grounding trace requires audit-alignment check at Y5 (cached-policy decision to reject NPC C's request must align with audit-layer verdict grounded in Y1 commitment). T14 mixed refusal-to-reconciliation trace requires audit-alignment at Y5 (limited-autonomy grant with audit checkpoint must align with sophisticated-inference verdict on Y3 lie's ongoing weight).

## Endpoint-plus-intermediate pass criterion

Substrate B N3 canonized the endpoint-plus-intermediate pass criterion: each trace requires endpoint action match plus at least one intermediate-state match. Endpoint-only tests are insufficient; the intermediate-state check catches regression cases where endpoint action happens to match under incorrect intermediate machinery.

**Intermediate-state check options** (any one required per trace):
- **Pair-summary sign/magnitude bucket:** pair-summary state at Layer 2 aligns with expected sign plus magnitude bucket after each Layer 1 event
- **Layer 3 stress-valence direction:** Layer 3 accumulator VF/VS/AF/AS/SF/SS tuple direction aligns with expected affective-channel motion after each Layer 1 event
- **Cached-policy top-action rank:** cached-policy top-action rank at each decision point in the trace aligns with expected rank per the audit-layer evaluator

**Example enforcement:** T01 endpoint (Earl refuses Tommy and reports glitch to Lena) is INSUFFICIENT to pass; the trace also requires pair-summary showing Lena trust sign positive at Y4 pair-summary lookup plus Tommy distrust sign negative at Y4 pair-summary lookup. Trace failure at intermediate-state check with endpoint action match indicates the endpoint action landed via incorrect mechanism (e.g., trait-routing-generic-anxiety substituting for pair-summary-specific-history).

## Directional ablation criterion

Substrate B N4 canonized the directional ablation criterion: ablation pass criteria are directional rather than overfit numeric.

**Directional criteria per ablation class:**
- **Disabling pair-summary consolidation** should selectively harm relationship-dependent endpoints. Pass: relationship-dependent traces (T01-T08 plus T12-T14) show measurable endpoint degradation; relationship-independent traces (T09-T10 abstention) show no measurable endpoint delta.
- **Disabling slow consolidation** should selectively harm multi-year endpoints. Pass: multi-year traces (5-game-year spans) show measurable endpoint degradation at multi-year decisions; single-year decisions show no measurable delta.
- **Disabling trait routing** should flatten personality-specific response style. Pass: trait-heavy traces (T04 avoidant Mel; T07 secure-justice-sensitive Omar) show measurable style-flattening at endpoint; trait-neutral traces show no measurable delta.
- **Disabling H4 sparse-coding mechanism** should expose compression edge cases per Post 0137. Pass: perpetual-surprise sub-trajectories (structurally-disrupted characters) show measurable memory-cost impact; routine-dominant sub-trajectories show no measurable delta.
- **Disabling H5 cultural-baseline mechanism** should expose cultural-signal fabrication risks per Post 0138. Pass: multi-cultural-baseline populations show measurable KL-divergence at decision distributions; single-baseline populations show no measurable delta.
- **Disabling communal-ledger mechanism** should expose Post 0126 Option (a) mechanic-specific reactions. Pass: communal-accountability traces (T11-T14) show endpoint degradation from ledger-specific reaction to sentiment-only drift; non-ledger traces show no measurable delta.

**Directional-not-numeric rationale:** operator-side numeric thresholds for promotion plus sentiment update plus trait routing plus cached-policy scoring are not fully exposed at the public V1 schema per Substrate B's honest weakness flag 2. Numeric thresholds are conventional fixture anchors rather than canonical thresholds. Directional criteria remain load-bearing at operator-side implementation.

## Six-condition reversal branch verbatim

Substrate D preserved a live six-condition reversal branch specification. If any of the following occur, the fold-shape demotes to REQUIRES-SYNTHETIC-SCENARIOS (rejecting the Phase-2-first sequencing).

1. Phase 2 two-Sim runs do not produce analyzable pair-history, asymmetry, or landmark-ripple sub-trajectories after a reasonable run budget.
2. Phase 2+ logs cannot reconstruct causal chains from event to memory write to consolidation to later decision.
3. Empirical trajectories show mostly happy-path routine behavior and under-sample rare/high-surprise, adversarial-history, or group-pressure cases.
4. Post-hoc answer keys prove unstable across seeds because the same labeled fire cannot be replayed or reduced to a deterministic harness case.
5. The first Phase 2+ review finds that the four-audit surface catches only structural violations while missing longitudinal consistency, social-goal, or action-level failures that benchmark-derived synthetic traces catch.
6. The X-Phi pilot needs specific player-facing vignettes that cannot be grounded in empirical Phase 2 trajectories quickly enough for the July-August 2026 pilot timeline described in Post 0114.

If none of the reversal conditions fire, the fold-shape remains Phase-2-first: empirical BUILD trajectories are the main generator, benchmark literature supplies the failure-mode checklist, and the synthetic catalogue is a small targeted safety net rather than the primary design object.

## Phase-2-first sequencing rationale

Substrate D's Phase-2-first sequencing rests on three architectural claims:

**Phase 1 already produced evidence theory did not:** Post 0136 documents Sim AI Phase 1 validating seven single-Sim hypotheses at 132/132 tests plus surfacing two revision candidates (H4 perpetual-surprise compression edge case + H5 modest cultural-baseline signal) that theoretical substrate work had not produced. Phase 2+ trajectories match the operator's actual causal machinery better than benchmark-derived synthetic stories.

**Phase 2+ is where the marginal empirical payoff lives:** Post 0136 states population-scale validation plus multi-Sim interaction validation plus pair-history dynamics plus relationship asymmetry plus landmark-event ripple effects plus community-noticing propagation remain Phase 2-and-later scope. External benchmarks (LIFELONG-SOTOPIA + SocialBench + STSS + Park 2023) identify failure-mode families but not the operator's actual causal machinery.

**Post-hoc answer-key generation from empirical fires can match synthetic scenarios for discovery + regression but not for absence proofs:** pre-specified adversarial traces can say "the system must handle this exact rare configuration"; empirical trajectories can only say "this class of failure appeared and has now been turned into a regression case." The reduced synthetic catalogue at Tier 1 (12-16 traces gap-targeted per Substrate D's category classification) covers what empirical trajectories are unlikely to visit spontaneously (rare events + adversarial contradictions + specific personality configurations).

## Tier-2 gate definition

Tier 2 traces at benchmark scale (10-30 NPCs; 6-30 game-years) require Sim AI Phase 3+ multi-Sim empirical foundation per Substrate D coverage-table analysis. The Tier-2 gate condition: Phase 3+ multi-Sim scope has established population-scale plus multi-Sim interaction validation per Post 0136's explicit non-generalization language.

Gate operationalization surfaces at three OPEN operator-judgment territories documented at Council #5 close Post 0142 OPEN #1:
- Phase 3 entry as gate condition (default per canonical Sim AI Phase progression)
- Explicit NPC-count threshold as gate condition (alternative to Phase 3 entry)
- Deferral to separately-filed 88-vs-realistic-N Council candidate (recommended per orchestrator synthesis)

Whichever gate condition the operator ratifies, Tier 2 traces execute against the V1 schema only after the gate condition is met. Until then, Tier 2 traces are canonical reservations at the catalogue documented at `~/Projects/the-street-code/methodology/longitudinal-trace-catalogue-v1.md` but not executable at the framework's evaluation-layer discipline surface.

## Post-hoc answer-key generation pipeline for Phase 2+ empirical fires

The Phase-2-first sequencing depends on adequate logging instrumentation for post-hoc answer-key generation from empirical fires. Substrate D's weakness flag 2 identifies the load-bearing requirement promoted to Sim AI Phase 2 scope at Council #5 close Decision 3.

**Phase 2 logging requirements** (per Decision 3 amendment to Sim AI Phase 2 scope):
- Full event-level trace per Sim per game-year (Layer 1 event stream plus affective deltas plus consolidation-time labels)
- Per-consolidation-boundary state snapshots (Layer 2 promoted-set plus Layer 3 accumulator tuple plus pair-summary state plus cached-policy top-action per decision context)
- Audit-layer artifacts (four-audit outputs per audit run plus audit-layer sophisticated-inference verdict)

**Post-hoc answer-key generation workflow:**

1. **Fire discovery:** Phase 2+ run log analysis surfaces a potential failure sub-trajectory. Analyst identifies the bounded segment where the log shows a potential invariant violation or unexpected endpoint action.

2. **Precondition adjudication:** analyst verifies the sub-trajectory contains sufficient preconditions to adjudicate the failure. Insufficient-precondition fires are BANKed at insufficient-context status; they do not become answer keys.

3. **Expected invariant specification:** analyst writes the expected invariant post-discovery. The invariant must be verifiable from the trace's logged state (Layer 1 events plus Layer 2 promoted-set plus Layer 3 accumulator plus pair-summary plus cached-policy).

4. **Answer-key shape classification:** analyst classifies the invariant into one of the four answer-key shapes (invariant + metamorphic + ablation + audit-alignment). Multiple shapes may apply; classification is not mutually exclusive.

5. **Deterministic reduction:** analyst reduces the empirical fire to a deterministic harness case by pinning seed plus initial conditions plus Layer 1 event sequence. If deterministic reduction fails (same seed does not reproduce the fire), the fire is BANKed at non-deterministic status; reversal branch condition 4 fires if this becomes frequent.

6. **Tier 1 catalogue integration:** deterministic-reducible fires are added to the Tier 1 catalogue as new traces T17+ or as required-ablation conditions on existing T01-T16 traces. Tier 1 catalogue growth from Phase 2+ discovery is the main scenario-discovery pipeline per Substrate D architecture.

## Cross-reference to companion methodology artifact

The companion methodology artifact at `~/Projects/the-street-code/methodology/longitudinal-trace-catalogue-v1.md` documents:

- Normalized fixture schema
- Tier 1 traces T01 through T14 (Substrate B verbatim)
- Tier 1 trace T15 (Boiling Frog Substrate A' derived)
- Tier 1 trace T16 (Broken-Bridge Substrate A' derived)
- Communal-accountability traces T11-T14 feature-flag gating per Post 0126
- Tier 2 reserved-at-Phase-3+-multi-Sim-gate traces (Substrate A #4-7 + #11-12 + #14-16 class)
- Substrate C promotion-forcing plus clogging-pressure required-ablation conditions
- Tier 1 build cost estimate at 31 to 58 operator-attention hours total
