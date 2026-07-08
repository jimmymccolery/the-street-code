# Perpetual-Surprise Compression Edge Case: Where Sparse Coding Assumes and Where It Breaks

<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0137
title: Perpetual-Surprise Compression Edge Case: Where Sparse Coding Assumes and Where It Breaks
date_published: 2026-07-02
status: published
superseded_by: none
domain: framework-architecture; sparse coding perpetual-surprise edge case; structurally-disrupted characters 100% encoding rate; R10d 6.3.1 canonical amendment 5-10x baseline storage budget
project_scopes: framework-architecture, npc-memory
cc_task_relevance: memory-budget-sizing-for-disrupted-characters, sparse-coding-edge-case-planning, phase-3-2-combat-trauma-integration
phase_binding: Phase-1
discipline_family: framework-architecture
canonical_rule: sparse-coding-perpetual-surprise-compression-edge-case
load_bearing_claims:
  - Sparse coding for NPC memory assumes prediction-error distribution follows normal patterns
  - When every event surprises model = 100% encoding rate (edge case: structurally-disrupted characters)
  - Structurally-disrupted characters incur higher storage cost due to perpetual-surprise compression failure
  - R10d §6.3.1 canonical amendment: memory storage cost variance for structurally-disrupted characters ratified 2026-07-02 late evening
applicability_triggers:
  - Character with sustained trauma, PTSD, addiction, or other structural disruption
  - When character's world-model repeatedly fails to predict events
  - When budgeting memory storage at population scale
  - When designing structurally-disrupted character archetypes (combat_trauma per Phase 3.2)
mechanism_details:
  - Sparse coding = encode only prediction errors (deviations from expected)
  - Normal operation: ~15% encoding rate (85% of events predicted correctly)
  - Perpetual-surprise: 100% encoding rate; sparse coding collapses to dense coding
  - R10d §6.3.1 amendment budget structurally-disrupted characters at 5-10x baseline storage
cross_refs:
  - Post 0118 (three-horizon memory + consolidation architecture)
  - Post 0120 (V1 memory spec)
  - Post 0136 (empirical BUILD mode; H4 finding surfaced this edge case)
  - Post 0146 Layer 4 (memory architecture)
  - primary-backend-project/architecture/round-10d-madisonian-gate-synthesis-2026-06-11.md (R10d canonical §6.3.1)
-->

**Author:** Jimmy McColery
**Date:** 2026-07-01
**Status:** Single empirical finding from Sim AI Phase 1 H4 test suite; architecturally consequential for procedural-character populations at scale where the population includes structurally-disrupted characters whose event streams break the compression scheme's core assumption; framework's R10d Section 6.3 architectural revision proposed pending operator ratification

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I am a solo indie developer building a procedural-character architecture for a multi-decade tycoon simulation. Post 0136 in this arc documents what the framework's V1 pause bought at Sim AI Phase 1 empirical scope; among the seven architectural hypotheses labeled H1 through H7 that Phase 1 validated, H4 addresses prediction-error sparse encoding as the memory-compression strategy underwriting the framework's population-scale storage arithmetic. The core H4 claim empirically held: routine event streams produced less than 10 percent encoding rate; one-week simulated storage stayed under 1MB per character; reconstruction via predicted-plus-stored-error reproduced actual state deltas within five-decimal float tolerance. All 15 tests in the H4 test suite passed.

What is worth writing about is what the test suite additionally surfaced. Buried in H4's coverage of the compression scheme's common-case behavior is a specific finding about what happens when the compression scheme's core assumption breaks. When every event surprises the prediction model, encoding rate hits 100 percent and the sparse coding scheme provides zero compression benefit. This is not a bug in the mechanism. It is a revelation about what the compression scheme's cost model actually assumes and what happens architecturally when a subset of the framework's characters violate that assumption.

## What sparse coding is and why it works

Sparse coding as a memory-compression strategy for procedural characters descends from a specific line of computational-neuroscience work. Olshausen and Field's 1996 paper on emergence of simple-cell receptive field properties through sparse coding for natural images (Nature 381 pages 607 through 609; DOI 10.1038/381607a0) established the core insight that natural signal streams admit efficient compression when the signal source's statistical structure makes prediction-matching the common case and prediction-error the rare case. The framework's Sim AI subsystem operationalizes that insight for procedural-character event streams via active-inference-coupled sparse coding grounded in Friston's active-inference process theory (Friston et al. 2017 Neural Computation 29 pages 1 through 49; DOI 10.1162/NECO_a_00912).

The mechanism is straightforward. Each character carries a prediction model that produces expected impact for baseline events; when an actual event matches the predicted impact, prediction error is near zero and no memory trace is created. When an actual event deviates from the predicted impact, prediction error exceeds a threshold and the specific delta between predicted and actual is encoded as a trace. Reconstruction of the character's actual state at any past tick is via combining the predicted impact at that tick with any stored error delta at that tick; if no trace was stored, the predicted impact is the reconstruction.

The cost model that makes this scheme underwrite population-scale storage arithmetic depends on prediction-matching being the common case. If a character's event stream is 95 percent routine (matches prediction) and 5 percent landmark (deviates from prediction), storage cost per character is roughly 5 percent of the naive full-state storage cost. Across a population of 1,000 to 5,000 characters, that 20-fold compression is the difference between storage arithmetic that fits inside the framework's per-character memory budget and storage arithmetic that does not.

The scheme's mechanical property that makes it work is that most events pass silently. In the H4 test suite this shows up as fewer than 10 percent of routine events triggering trace creation, mixed routine-and-landmark streams at 5 percent landmark rate producing 1 to 15 percent encoding rate, and one-week simulated storage staying under 1 MB per character. These specific numbers are what the framework's population-scale storage arithmetic depends on.

## The empirical finding: when every event surprises

The H4 test suite includes a deliberately-constructed test case for a state where every event exceeds the prediction-error threshold. The setup constructs an event stream where the prediction model has no reliable baseline to compress against; every event's actual impact deviates from the predicted impact by more than the trace-creation threshold. The empirical result is that encoding rate hits 100 percent, storage grows linearly with event count, and the compression scheme provides zero compression benefit. Every single event creates a trace. The mechanism still works in the sense that reconstruction succeeds (predicted-plus-stored-error accurately reproduces actual state); the mechanism just does not compress.

That result is architecturally consequential in a specific way. Sparse coding's cost model implicitly bets on prediction-matching being common. When the operator paints a character as "structurally-disrupted" (a war-refugee character; a character in ongoing trauma; a character in perpetual instability; a character whose baseline is that every day surprises them), the mechanism is honestly recording that state's cost. The character genuinely has more to remember because more of the character's experience genuinely deviates from routine prediction. The compression scheme cannot fix that because the compression scheme was designed to exploit routine-dominance, and routine-dominance is exactly what a structurally-disrupted character does not have.

The test suite logs this as deliberate documentation rather than as a failure. Nothing in the mechanism is broken; the mechanism is doing what active-inference-coupled sparse coding is supposed to do, which is to encode surprise and let expected events pass. When every event is surprise, every event encodes. That is the mechanism's honest behavior at that population-segment's boundary.

## Architectural implication for population-scale procedural characters

If sparse coding underwrites the "population scale is affordable" claim, and if sustained-crisis characters carry higher per-character memory storage cost, then the framework's population-budgeting arithmetic must account for elevated encoding rate per structurally-disrupted character. The compression-makes-scale-affordable argument applies most cleanly to routine-dominant population segments; it applies with reduced margin to mixed populations that include structurally-disrupted characters; it applies with essentially no margin to populations that are dominated by structurally-disrupted characters.

The framework's target population for the tycoon simulation includes both routine-dominant characters (a working-class family running the bowling alley across decades; a customer who visits every Saturday for thirty years; a league bowler with stable weekly rhythm) and structurally-disrupted characters (a Vietnam War refugee whose 1970s decade compresses badly; a character navigating the 1980s AIDS crisis in a small town; a character whose family is displaced by economic collapse). The two population segments produce different per-character storage cost profiles. If the framework attempts to budget storage as if both segments compress equally, either the routine-dominant segment gets over-budgeted (waste) or the structurally-disrupted segment gets under-budgeted (compression failure at scale).

The content-authoring implication is that representing structurally-disrupted characters has both authoring cost and runtime memory cost, and the two costs are architecturally independent. Authoring a structurally-disrupted character requires research, cross-cultural discipline, and often Marcus Reed Surface 8 audit surface engagement; runtime cost is separate and comes from the mechanical fact that the compression scheme cannot compress what has no routine baseline. A framework that only budgets authoring cost will discover the runtime cost the hard way when the population reaches the mechanical scale at which per-character memory becomes a load-bearing constraint.

The R10d architectural revision the finding motivates is that Section 6.3 acknowledges the elevated memory storage cost for structurally-disrupted characters in the framework's cozy-sim register. The "acknowledge, never resolve" authoring discipline that R10d already carries at the authoring-cost surface (the framework's specific commitment to not narratively resolving trauma or structural disruption; the framework's specific commitment to letting characters carry unresolved conditions across their arcs) applies at the runtime memory-cost surface as well. The compression scheme's honest behavior is to record the cost of structural disruption at the same time the authoring discipline records the character's condition. Both costs are load-bearing; both are architecturally independent; both are what the framework's discipline commits to representing rather than resolving.

## What the framework is doing about it

The R10d cascade revision is proposed but not ratified. The Sim AI Phase 1 empirical findings memo (canonical at the primary backend project's Phase 1 findings surface) proposes the Section 6.3 update as one of two architectural revisions surfaced by Phase 1 empirical findings. Operator ratification is pending. The framework's Rule 14 Madisonian Gate discipline applies to canonical mutations regardless of empirical foundation; if the revision is ratified, R10d Section 6.3 gains a specific note about the elevated memory storage cost; if not, R10d remains at its 2026-06-11 PM close state and the finding is banked at the empirical findings surface without canonical propagation.

The immediate operational implication for the framework's continued planning is that population-budgeting math should account for the memory-storage-cost variance between routine-dominant and sustained-crisis character populations. Content-authoring for structurally-disrupted characters should factor per-character memory-storage cost projection alongside authoring cost and runtime compute cost. The framework's continued Sim AI phases will test the specific cost variance at multi-Sim and population scales; Phase 4 explicitly includes prediction-error compression scale tests plus storage benchmarks at realistic population. What Phase 4 will empirically settle is the specific magnitude of the cost variance and whether extensions to the sparse coding scheme (learned prediction models; hierarchical predictions; adaptive threshold discipline) can reduce the perpetual-surprise-edge-case severity below architectural significance.

## What this post is NOT

This post is not a general claim about sparse coding as a compression strategy. Sparse coding descends from a substantial research literature and works well in the domains where its assumptions hold; the finding I write about is specific to procedural-character architecture at the boundary where the framework's target population includes characters whose event streams violate routine-dominance. Other applications of sparse coding may not encounter this boundary at all.

This post is not a proposal that the framework abandon sparse coding. The empirical H4 validation confirms sparse coding works as designed for routine-dominant characters; the mechanism is architecturally load-bearing for the framework's population-scale storage arithmetic. What the finding motivates is honest accounting of the mechanism's cost variance across population segments, not replacement of the mechanism.

This post is not a full account of how the framework will handle structurally-disrupted characters at population scale. The R10d revision proposes acknowledging the elevated cost; the framework's continued planning has not yet specified whether structurally-disrupted characters will be budgeted at a fixed per-character memory ceiling, whether their history will be tiered differently, or whether some other architectural response applies. Phase 2 through Phase 5 empirical work is where the specific response will emerge; this post handles the finding and its immediate architectural implication only.

This post is not an argument that the framework's target population should exclude structurally-disrupted characters. The opposite is closer to what the framework's cross-cultural discipline commits to: representing the range of characters a multi-decade multi-generational tycoon simulation's target settings would actually contain, including characters whose experience does not compress to routine. The compression cost is what the framework accepts as the price of that representation, not a reason to narrow the representation.

## What I am not claiming

I am not claiming sparse coding is the only memory-compression strategy for procedural characters. Learned prediction models that adapt to character-specific baselines, hierarchical predictions that let higher-level context compress lower-level surprise, and adaptive threshold discipline that varies per-character based on observed prediction-error distributions are all candidate alternatives; some of them are candidate extensions to the current mechanism. Phase 4 or later empirical work may identify the specific extension that reduces the perpetual-surprise-edge-case severity.

I am not claiming sustained-crisis characters break the framework's memory budget. The finding raises per-character cost for structurally-disrupted characters; whether that raises overall population memory cost above the framework's budget depends on population mix. A population that is 90 percent routine-dominant and 10 percent structurally-disrupted budgets differently from one that is 60 percent routine-dominant and 40 percent structurally-disrupted; the specific arithmetic applies to specific populations, not to the mechanism in general.

I am not claiming the perpetual-surprise edge case exhausts the failure modes of prediction-error sparse coding. Adjacent edge cases (characters whose prediction models drift over long timespans; characters whose event streams have long-tail distributions rather than routine-plus-landmark bimodal structure; characters in transition between routine-dominant and structurally-disrupted regimes) may produce their own compression-cost variances. The framework's continued Phase-2-and-later empirical work is where those edge cases would surface.

I am not claiming the single-Sim empirical finding generalizes uniformly to population scale. The specific 100 percent encoding rate at perpetual-surprise state is a single-Sim mechanical measurement. Whether the population-scale cost variance is proportional to single-Sim variance or exceeds it (via cross-character interaction effects that Phase 1 did not test) is a Phase 2 and later question this post does not adjudicate.

I am not claiming the R10d Section 6.3 architectural revision has ratified. The revision is pending operator review. If the operator finds the revision misspecified or over-scoped, the revision may be revised, narrowed, or dropped; the framework's Rule 14 discipline applies regardless of empirical foundation.

## What I am claiming

Sparse coding as memory-compression strategy for procedural characters assumes prediction-matching is the common case; the perpetual-surprise edge case is where the assumption breaks; this is architecturally consequential for procedural-character populations that include structurally-disrupted characters at scale; the framework's response is to account for the memory-storage-cost variance in population-budgeting math rather than pretending the compression scheme underwrites all character classes equally.

If you are building procedural-character architectures relying on prediction-error sparse coding for memory compression, budget the perpetual-surprise-state variance explicitly. The compression scheme's cost model implicitly bets on prediction-matching being common; when a subset of your characters violate that bet, the memory-storage cost lands on that subset rather than smoothing across the population. Content-authoring for structurally-disrupted characters carries both authoring cost and runtime memory cost; the two are architecturally independent and both need budgeting.

The framework's continued Phase 4 empirical work will test the specific magnitude of the cost variance at population scale plus whether extensions to the sparse coding scheme reduce the edge-case severity below architectural significance. What Phase 1 empirically established is the finding's existence at single-Sim scale plus its architectural implication for population-scale budgeting; the specific population-scale numbers are Phase 4 territory. The mechanism's honest behavior at its boundary is what the framework's discipline commits to representing at the runtime memory-cost surface alongside the authoring-cost surface, in the same "acknowledge, never resolve" register R10d already carries at the authoring layer.
