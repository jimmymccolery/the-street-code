<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0132
title: The Consolidation-Pass Benchmark Harness and the Post 0119 Operational-Contract Amendment: What V1 Must Measure Before Building
date_published: 2026-07-01
status: published
superseded_by: none
domain: Council #3 spec output; Swift on-device benchmark harness for consolidation-pass regime R3 tractability; Post 0119 operational-contract amendment adding branch-factor discipline (B_max) plus probability-threshold pruning plus BTAI/MCTS expansion budget K plus sparse factor-graph interruptible message passing
project_scopes: framework-architecture, framework-methodology
cc_task_relevance: benchmark-harness-planning, post-0119-amendment-authoring, active-inference-tractability-measurement
phase_binding: Phase-1
discipline_family: framework-architecture
canonical_rule: benchmark-harness-adjudicates-consolidation-pass-cadence-tractability-before-130-230h-apparatus-build
load_bearing_claims:
  - Swift on-device benchmark harness at meta-architecture level adjudicates tractability for V1 target scale
  - Post 0119 operational-contract amendment adds branch-factor discipline B_max + probability-threshold pruning budget + BTAI/MCTS-style expansion budget K + sparse factor-graph interruptible message passing
  - Sequencing rationale: run harness pre-V1 before ~130-230h sophisticated-active-inference apparatus build
  - META-level commitments only; harness-specific mocked-component semantics + candidate-action-set operationalization + generative-model dimensionalities scoped to commercial channels
applicability_triggers:
  - Council #3 spec output implementation
  - Deciding whether sophisticated active inference at consolidation cadence fits V1 target scale
  - Amending Post 0119 operational contract
mechanism_details:
  - Harness at meta-architecture level; standalone-executable Swift on-device procedure
  - Branch-factor discipline B_max = cap on action-tree branching
  - Probability-threshold pruning = drop low-probability branches
  - BTAI/MCTS-style expansion budget K = bounded tree-search expansion cap
  - Sparse factor-graph interruptible message passing = anytime message-passing under interrupt budget
cross_refs:
  - Post 0131 (Council #3 close narrative companion)
  - Post 0119 (audit-first active inference sequencing; amendment target)
  - Post 0133 (V1-pause forward-reference amendment; sequencing changes)
  - Methodology guide: active-inference-tractability-benchmark-harness-v1.md
-->

# The Consolidation-Pass Benchmark Harness and the Post 0119 Operational-Contract Amendment: What V1 Must Measure Before Building

**Author:** Jimmy McColery
**Date:** 2026-07-01
**Status:** V1 architecture-spec addendum documenting the framework's Council #3 close output at meta-architecture level; specs the Swift on-device benchmark harness Substrate B specified for consolidation-pass regime R3 tractability adjudication; specs the Post 0119 operational-contract amendment adding branch-factor discipline (B_max), probability-threshold pruning budget, BTAI/MCTS-style expansion budget K, and sparse factor-graph interruptible message passing; documents the sequencing rationale for running the harness pre-V1 before the ~130-230h sophisticated-active-inference apparatus build; companion to post 0131 in this arc which documents the Council #3 close narrative and the Rule 14 Pattern B ADOPT-FOLD adjudication

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I am a solo indie developer building a procedural-character architecture for a multi-decade tycoon simulation. This post specs the framework's concrete architectural output from Council #3 (documented in post 0131 in this arc; the framework's second Rule 14 Madisonian Gate deployment against a specific architectural decision). The output is a Swift on-device benchmark harness that adjudicates whether sophisticated active inference at consolidation-pass cadence fits the framework's V1 target scale plus a Post 0119 operational-contract amendment adding the branch-factor discipline the Council record surfaced as a spec gap.

The post operates at the META-architecture level. The framework's commercial product has specific NPC roster details and specific commercial-scope architectural surfaces that the framework's soft-disclosure discipline keeps out of public posts. The META-level commitments below are the architectural-decisions layer; the harness's specific mocked-component semantics, the specific candidate-action-set operationalization heuristics, and the specific generative-model dimensionalities remain scoped to commercial channels. The methodology guide at `~/Projects/the-street-code/methodology/active-inference-tractability-benchmark-harness-v1.md` documents the standalone-executable Swift on-device procedure for the harness at operational-detail scope beyond this post's META-level commitments.

## The benchmark harness at meta-architecture level

The harness Substrate B specified is not the real game engine. It is a faithful cost model of one sophisticated-inference decision plus a driver that replays it at three candidate frequencies across the swept parameters. The harness has five meta-architecture components:

**Component 1: Mocked NPC state.** A fixed-size structure holding a factorized belief Q(s) over the hidden-state factors the framework's NPCs actually carry. The mock is parameterized by n_s (hidden states per factor) and n_f (number of factors). Substrate B recommends a deliberately generous default (n_s equal to 16; n_f equal to 2; effective 32-state space) so the envelope is conservative rather than flattering.

**Component 2: Mocked generative model.** Likelihood matrix A of dimension n_o by n_s and transition matrix B of dimension n_s by n_s by n_actions filled with plausible sparse-ish values. These drive the belief-propagation matrix-vector products and the KL divergence plus utility reductions that constitute the load-bearing computational cost.

**Component 3: Mocked sophisticated policy evaluator.** The recursive expected-free-energy tree per Friston et al. 2021 "Sophisticated Inference." At each depth the evaluator branches over allowable actions and, for each action, over the likely observations, recursing to depth τ. The evaluator exposes two knobs the harness must sweep: horizon τ from 1 through 3 and observation branching factor b_o (the number of distinct predicted outcomes expanded per action; the harness's most consequential hidden variable). The evaluator implements optional Occam-window pruning (drop branches below a posterior-probability threshold) as a toggle, because pruning is the single biggest lever between pessimistic and optimistic envelopes.

**Component 4: Mocked action-set generator.** Returns 3, 5, or 8 candidate actions per decision. The mock sets the tree's branching arity per the framework's target realistic candidate-action range.

**Component 5: Driver.** Replays decisions at three regime frequencies (per-frame at 30 frames per second; per-game-minute throttled; per-consolidation-trigger batched) across NPC counts of 20, 50, and 100 across consolidation windows of 1, 5, and 10 game-years. The driver's job is aggregating single-decision cost measurements into population-scale wall-clock envelopes at each regime.

## The sweep design

Full factorial across A (3 values) by N (3 values) by W (3 values) by regime (3 values) by τ (3 values) is 243 cells. Substrate B specifies a fractional design that reduces the sweep to approximately 27 microbenchmark cells plus 9 headline integration cells. Full A by τ by b_o factorial for the single-decision microbenchmark (the cheap part) sweeps 3 by 3 by 3 equal to 27 cells. Three corner NPC-scale integration runs (N equal to 100 at A equal to 3, 5, 8, each in R1, R2, R3) sweeps 3 by 3 equal to 9 cells. The fractional design captures the axis interactions that matter for adjudication at solo-dev-feasible sweep count.

## The metrics the harness reports

Substrate B specifies five metrics per Kalibera and Jones 2013 "Rigorous Benchmarking in Reasonable Time" (DOI 10.1145/2464157.2464160) rigorous-benchmarking discipline. Report distributions with confidence intervals rather than single means. Use warmup, many iterations, and report median plus median absolute deviation plus bootstrap confidence interval plus explicit outlier counts (Tukey classification), because iOS thermal throttling and E-core plus P-core scheduling inject heavy-tailed noise.

**Metric 1: Per-decision wall-clock time in microseconds.** Median, interquartile range, 95% confidence interval, for each cell of the A by τ by b_o factorial. This is the atomic cost.

**Metric 2: Per-consolidation-pass wall-clock time in milliseconds.** For each cell of N by W by A: total time to run inference for all NPCs due at a window boundary. This is the number that must be time-sliced across real frames.

**Metric 3: Per-NPC-year cumulative inference compute in milliseconds per NPC per game-year.** Normalizes cost to the simulation's economic clock; allows the operator to compare against how much real time a game-year occupies at target play speed.

**Metric 4: Per-frame budget-envelope utilization as percentage of 33 milliseconds.** For regime R1 the fraction of a single frame consumed by all due decisions; for regimes R2 and R3 the fraction consumed by the per-frame slice of a time-sliced pass. Report both mean and p95 frame utilization, plus count budget-overrun frames (frames where AI exceeded its allotted slice), because a single 33 millisecond overrun is a visible hitch per Apple Metal Best Practices Frame Rate guidance.

**Metric 5: Supporting metrics.** Peak transient memory of the tree via XCTMemoryMetric; CPU-core occupancy via XCTCPUMetric to detect whether work landed on efficiency-cores rather than performance-cores.

## The three-tier pass/fail thresholds

Substrate B specifies three verdict tiers the harness produces. The tier depends on the specific measurement outcomes at N equal to 100 across regime R1, R2, R3 with A equal to 5 and τ equal to 3 as the target-cell benchmark.

**Tier 1 PASS: V1-CRITICAL as runtime-critical claim upheld.** At N equal to 100, in at least one deployable regime, p95 per-frame AI utilization is at most approximately 10 milliseconds (30 percent of the 33 millisecond frame budget) AND zero budget-overrun frames over a 10-game-year replay, with A at least 5 and τ equal to 3.

**Tier 2 CONDITIONAL PASS: V1-CRITICAL as consolidation-pass machinery.** N equal to 100 fails R1 (as the pre-run envelope arithmetic predicts) but passes R3 with p95 slice at most approximately 10 milliseconds AND total pass latency amortizable within one consolidation window without starving other systems. The player-facing consolidation-pass tolerance layered on: per-consolidation-pass wall-clock within player-facing game-year-transition tolerance (Substrate C's inference range is 30 seconds to 5 minutes acceptable; more than 10 minutes as the demote trigger; the exact tolerance inside that band is operator judgment).

**Tier 3 FAIL: DEMOTE-TO-AUDIT-METAPHOR.** Even R3 at N equal to 100, A equal to 3, τ equal to 3 with pruning cannot keep the time-sliced per-frame contribution under budget without the consolidation pass spilling across so many frames that NPC decisions lag the game clock unacceptably. Per Substrate C's dependency-2 explicit trigger, a FAIL outcome also triggers Path-A-ratification re-evaluation; the 80 to 150 hour extension the operator ratified into V1 critical-path was purchased specifically to absorb this apparatus.

## Cost arithmetic

The harness cost per Substrate B's own itemized breakdown is approximately 3.5 to 4.5 focused solo dev-days, equivalent to approximately 28 to 36 hours of BUILD-side operator attention at 8 hour dev-days. The Council #3 orchestrator layer caught a discrepancy between the Council brief's characterization of the cost as approximately 30 to 40 hours and Substrate B's actual figure; the corrected figure is 28 to 36 hours.

The harness cost fits within the framework's Path A envelope (270 to 410 hours iOS V1 per post 0119 in this arc) via Substrate C's identified cut candidates: cut candidate 5 (methodology plus posts maintenance reduction, 10 to 20 hours recoverable) plus partial cut candidate 4 (defer Councils #2, #4, #5 canonical mutations post-V1, 30 to 60 hours recoverable) yields 40 to 80 hours of cumulative recoverable headroom without touching the 130 to 230 hour sophisticated-active-inference apparatus components. The harness cost is 28 to 36 hours; the cut candidates provide 40 to 80 hours; the harness fits with margin.

The harness sequencing rationale is that running the harness BEFORE the 130 to 230 hour apparatus build inverts the risk ordering. If the harness surfaces a FAIL outcome (DEMOTE-TO-AUDIT-METAPHOR), the framework avoids spending 130 to 230 hours building an apparatus that does not ship at V1. If the harness surfaces a Tier 2 CONDITIONAL PASS (the expected outcome per Substrate B's prior), the apparatus build proceeds with confidence and the specific consolidation-pass regime parameters the harness validated.

## The Post 0119 operational-contract amendment

Substrate A's finding on post 0119 in this arc stands independent of the harness outcome: post 0119 emphasizes horizon depth τ at most 3 as the named computational defense but does not explicitly impose a maximum candidate-action branch factor per decision. That is a spec gap relative to Champion et al. 2022 formulation which makes the branch factor B_max (variable |U| in the paper's notation) part of the exponential term (|U|^T policy count).

The framework's operational-contract amendment adds four discipline elements. The amendment is a NEW post per the framework's immutability convention (posts do not retroactively edit; corrections arrive as forward references from subsequent posts). Post 0119 remains unchanged; this post specifies the amendment via forward reference to the harness plus explicit new discipline statements.

**Amendment element 1: Explicit B_max discipline per audit-time decision context.** The framework's operational contract commits to a stated maximum candidate-action count per decision. The B_max value is per audit-time decision context (staff-loyalty decisions may have different B_max than customer-patronage decisions than league-competitor decisions). The B_max is not an emergent property of content design; the B_max is an explicit runtime plus audit parameter. Content design must be filtered through the B_max discipline at decision-scoring time; the sophisticated-inference evaluator sees only the context-gated B_max-bounded candidate set.

**Amendment element 2: Probability-threshold pruning budget per Friston 2021 style.** Per Friston et al. 2021 "Sophisticated Inference" (DOI 10.1162/neco_a_01351 arXiv:2006.04120) the sophisticated-scheme evaluator terminates action or outcome branches whose prior or predictive probability falls below a configured threshold. The paper's example threshold is one-sixteenth. The framework's operational contract commits to a stated probability-threshold pruning budget as a distinct parameter from B_max. The pruning threshold is per audit-time decision context and per horizon depth; longer horizons may permit tighter thresholds because deeper branches carry less probability mass by construction.

**Amendment element 3: BTAI/MCTS-style expansion budget K per Champion et al. 2022.** Champion et al. 2022 (DOI 10.1016/j.neunet.2022.03.036) proposes replacing exhaustive policy-list evaluation with a dynamically expanded branching-time generative model guided by tree search. The BTAI space complexity is O([K plus t] times |S|) where K is the number of tree expansions actually performed. The framework's operational contract commits to a stated K expansion budget as a distinct parameter from B_max plus the pruning threshold. K plus B_max plus pruning threshold together constitute the framework's branching-plus-pruning discipline; the harness measures the empirical consequences of specific parameter choices.

**Amendment element 4: Sparse factor-graph plus interruptible reactive message passing per de Vries 2023.** Per de Vries 2023 "Toward Design of Synthetic Active Inference Agents by Mere Mortals" (arXiv:2307.14145) sparse factor-graph plus message-passing designs support interruptible inference that degrades accuracy gracefully rather than causing frame failure. The framework's operational contract commits to interruptibility as a first-class implementation requirement. If a consolidation pass runs long enough that the pass would exceed the player-facing game-year-transition tolerance (30 seconds to 10 minutes range per Substrate C's inference), the pass must interrupt gracefully with partial results rather than block indefinitely.

## The consolidation-pass cadence terminology refinement

The framework adopts "consolidation-pass cadence" as the precise term in this amendment, replacing the more ambiguous "audit-first sequencing" language from post 0119 in this arc where cadence-specific implementation shape is at stake. The audit-first sequencing language remains valid for the buildup discipline (the audit layer builds before runtime promotion is considered); the consolidation-pass cadence language pins down the specific implementation shape at V1 (sophisticated inference at consolidation cadence yearly; never per-frame).

The reframing does not require any prior published post to be edited or retracted. Post 0119's audit-first sequencing framing remains published; the reframing surfaces as forward reference from this post plus post 0131 in this arc. Future post 0119 amendments or references use "consolidation-pass cadence" for cadence-specific claims and "audit-first sequencing" for buildup-discipline claims. The two terms are compatible; the reframing simply distinguishes the two claims the earlier language conflated.

## The Council #1 comparison

Council #3's canonical output shape parallels Council #1's canonical output shape (documented in posts 0129 plus 0130 in this arc) with specific structural differences. Both Councils produce Pattern B ADOPT-FOLD via Option B per-item ratification. Both Councils produce a schema-slot-plus-gate structure (Council #1: reserved relationship_mode enum plus four-condition ablation gate; Council #3: no reserved schema slot but four-element operational-contract amendment plus benchmark harness gate). Both Councils produce methodology guides in the framework's methodology corpus (Council #1: ablation-gate-relationship-mode-v1.md; Council #3: active-inference-tractability-benchmark-harness-v1.md).

The specific structural difference: Council #3's ADOPT sub-action (the operational-contract amendment) is benchmark-independent and does not require the harness outcome to trigger canonical mutation. Council #1's ADOPT half (the reserved slot) was similarly benchmark-independent (the ablation gate outcome triggers V1.x operationalization, not V1 ADOPT). Both Councils' BANK halves are gated on future empirical measurement. The two Councils together establish that Pattern B composite verdicts can carry benchmark-independent ADOPT sub-actions plus benchmark-dependent BANK sub-actions in the same canonical mutation.

## What I am not claiming

I am not claiming the specific pass/fail thresholds are portable to other tycoon simulations at similar target scale. The framework's specific 10 millisecond AI slice allocation is a design decision the operator ratifies; other operators may adopt different slice allocations based on their specific per-frame budget priorities. The Tier 1 versus Tier 2 versus Tier 3 verdict-tier structure is portable; the specific numeric thresholds are framework-specific.

I am not claiming the four operational-contract amendment elements exhaust the branch-factor plus pruning-discipline design space. The amendment addresses the four specific complexity-reduction techniques the Council #3 substrates surfaced (B_max discipline; probability-threshold pruning; BTAI expansion budget K; sparse factor-graph interruptibility). The broader active-inference literature has additional complexity-reduction techniques (learned action priors; belief-state approximation; deep active inference) that the framework may adopt at post-V1 scope depending on the harness outcome plus post-V1 research arc findings.

I am not claiming the harness outcome will produce Tier 2 CONDITIONAL PASS. The pre-run envelope predicts Tier 2 as the expected outcome for A equal to 3 and marginally for A equal to 5. The empirical measurement may produce Tier 1 (unlikely; would require per-node cost at the optimistic ~0.5 microsecond end plus aggressive pruning) or Tier 3 (possible if per-node cost lands at the pessimistic 10 to 20 microsecond end with b_o equal to 4 without pruning). The commitment is to the harness measurement; the verdict tier is what the measurement produces.

I am not claiming the ~28 to 36 hour harness cost estimate is precise. The estimate is planning-phase order-of-magnitude figure per Substrate B's own itemized breakdown. The actual cost is subject to the operator's Swift plus Xcode fluency (Substrate B assumes fluent baseline; less-fluent operators may need additional ramp time) and to the specific microbenchmark environment plus optional pymdp correctness oracle deployment complexity.

## What I am claiming

The framework's Council #3 close produces a Swift on-device benchmark harness that adjudicates sophisticated active inference tractability at consolidation-pass cadence for the framework's target scale of 80 to 100 NPCs at τ at most 3. The harness has five mocked components (state; generative model; sophisticated policy evaluator; action-set generator; driver) that replay one sophisticated-inference decision across a fractional sweep of approximately 36 cells at approximately 28 to 36 hours of BUILD-side cost. The harness produces five metrics with rigorous-benchmarking discipline (distributions with confidence intervals; median plus MAD plus bootstrap CI; Tukey outlier classification) that adjudicate the verdict at three tiers: Tier 1 PASS as runtime-critical; Tier 2 CONDITIONAL PASS as consolidation-pass machinery (the expected outcome); Tier 3 FAIL as DEMOTE-TO-AUDIT-METAPHOR triggering Path-A-ratification re-evaluation.

If you are building procedural-character architectures with sophisticated decision-scoring requirements at production-deployment scale, the running-the-harness-before-building-the-apparatus discipline is one operationally-defensible response to the tractability question that the literature alone cannot adjudicate. The discipline costs the harness work plus the correctness-oracle work plus the sweep automation plus the on-device Instruments profiling; the discipline produces empirical evidence that supports building the 130 to 230 hour apparatus with confidence or retiring the apparatus at near-zero apparatus-build sunk cost. The alternative (building the apparatus without empirical adjudication) inverts the risk ordering.

The framework's Post 0119 operational-contract amendment adds explicit B_max discipline per audit-time decision context plus probability-threshold pruning budget per Friston 2021 style plus BTAI/MCTS-style expansion budget K per Champion et al. 2022 plus sparse factor-graph interruptible message passing per de Vries 2023. The amendment is benchmark-independent; it does not wait for the harness to run. The terminology refinement from "audit-first sequencing" to "consolidation-pass cadence" pins down the specific implementation shape at V1 without deprecating the earlier audit-first-sequencing language for buildup-discipline claims.

The framework's canonical rules ledger now carries n=2 empirical foundation for Rule 14 Pattern B ADOPT-FOLD classification across Council #1 (post 0129 in this arc) plus Council #3 (post 0131 in this arc) with distinct-but-related discriminators (preserved live reversal branches gated on empirical outcome; convergent-arithmetic partial adjudication banked from record). The methodology guide at `~/Projects/the-street-code/methodology/active-inference-tractability-benchmark-harness-v1.md` documents the standalone-executable Swift on-device procedure for the harness; the guide is the operational reference the framework's continued V1 execution depends on for the specific harness deployment.
