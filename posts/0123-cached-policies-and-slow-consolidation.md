# Cached Policies and Slow Consolidation: The Project Zomboid Offscreen Storylet Pattern Applied to Active Inference

<!-- CC-OPTIMIZED-SUMMARY v1.0
post_id: 0123
domain: framework-architecture
canonical_rule: cached-policies-slow-consolidation-project-zomboid-pattern
load_bearing_claims:
  - Project Zomboid offscreen-storylet pattern formalized for active-inference machinery
  - Cached policies at runtime (per-frame budget); slow consolidation offline (yearly)
  - Consolidation passes as episodic character reflection points (align with Post 0118 yearly cadence)
  - Cached policies as pre-computed character decision caches (avoid per-frame active inference computation)
  - Runtime + consolidation split is load-bearing for population-scale performance
applicability_triggers:
  - Designing per-frame vs offline computation split for NPC decision-making
  - When active inference is too expensive to run per-frame at population scale
  - When offscreen character updates need pattern (analogy: Project Zomboid offscreen storylet)
  - Choosing consolidation cadence for character state updates
mechanism_details:
  - Cached policies = pre-computed decision caches indexed by state
  - Consolidation cadence = yearly game-time boundaries
  - Offscreen storylet pattern = characters continue evolving via cheap updates when not player-visible
  - Active inference sophisticated deployment at consolidation only; naive/cached deployment at runtime
cross_refs:
  - Post 0111 (procedural persons Bayesian; τ ≤ 3 planning)
  - Post 0118 (recency + yearly consolidation)
  - Post 0119 (audit-first active inference sequencing)
  - Post 0121 (Park 2023 backbone; hybrid architecture)
  - Post 0122 (multi-graph memory typed indexes)
  - Post 0146 Layer 5 + Layer 10 (EFE + audit)
CC-OPTIMIZED-SUMMARY -->

**Author:** Jimmy McColery
**Date:** 2026-06-29
**Status:** Hybrid-path closer for the framework's runtime-architecture commitments; documents the cached-policies-with-slow-consolidation pattern; cites the Project Zomboid offscreen-storylet architecture as the production-precedent analog; meta-level discussion of commercial-product implementation without enumerating cached-policy tuning specifics

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Project Zomboid shipped a multi-decade simulation game on indie budget by separating cheap-per-frame visible behavior from slow-offscreen-simulation deeper state. The framework I am developing adopts that exact pattern as the cornerstone of its runtime architecture; the framework's NPCs run cheap cached active-inference policies for per-frame decision-scoring and run sophisticated active-inference apparatus at consolidation-pass boundaries to update the cached policies based on accumulated experience. The pattern is what makes the framework's V1 deployment fit within iOS V1 per-frame budget envelope while preserving the architectural commitments that the framework's Path A operator ratification ratified into V1 critical-path.

This post closes the hybrid-path block by tying together the prior posts' commitments. The cached-policies-with-slow-consolidation pattern (this post) operates over the multi-graph memory typed-indexes pattern (post 0122 in this arc); the typed indexes feed the cached-policy lookups at O(1) cost. The cached policies are regenerated at the consolidation-pass cadence (post 0118 in this arc); the consolidation pass runs the sophisticated active-inference apparatus on the past game-year's accumulated state to produce the next-game-year cached policies. The audit-first sequencing (post 0119 in this arc) ensures the sophisticated active-inference apparatus operates at audit-layer cadence rather than per-frame cadence; the audit-layer use is what earns the runtime promotion empirically.

The pattern's borrowing-and-extending decomposition is honest: cached policies plus slow-consolidation is borrowed from Project Zomboid (the commercial-precedent analog); typed indexes are borrowed from MAGMA-style research architecture (adapted to single-store deployment); Park 2023 generative-agents three-process decomposition supplies the conceptual backbone (substituted at the implementation layer with the framework's hybrid commitments); active-inference state-space-content discipline is the framework's own contribution at the integration layer. The combination is the contribution; the components are each grounded in canonical precedent.

## What Project Zomboid showed

The 2022 Indie Stone development-blog post "the zuckerverse" (published at the Project Zomboid developer-blog at projectzomboid.com/blog/news/2022/03/the-zuckerverse/; the URL is the commercial-precedent reference for the architecture; verify the URL remains active at the time of subsequent reading) documents the offscreen-simulation architecture the game ships with. The architecture decomposes character behavior into two tiers:

Per-frame visible behavior. NPCs in the player's perceptual window run cheap state-machine policies plus cached lookups; the per-frame compute per NPC is bounded by simple-policy lookups rather than by per-decision deep simulation; the per-frame budget supports the player's expected framerate even at populations of dozens of visible NPCs.

Offscreen storylet simulation. NPCs outside the player's perceptual window continue to exist and accumulate state via lower-cadence simulation passes (typically once per game-day or game-week at Project Zomboid's specification); the offscreen NPCs are not rendered per-frame; the offscreen simulation runs deeper logic (relationship updates; backstory progression; long-term consequence accumulation) at the lower cadence; the offscreen state is loaded back into per-frame visible behavior when the player enters the offscreen NPCs' area.

The architecture supports multi-zone game maps with dozens of NPCs across multi-day simulation at indie production quality. The architecture's commercial track record is operationally substantial; the architecture has shipped in Project Zomboid at consumer scale across years of active deployment; the architecture is the canonical commercial-precedent for the kind of cached-versus-offscreen separation the framework adopts.

## The two-tier pattern formalized for the framework

The framework's adoption of the two-tier pattern is structurally similar to Project Zomboid's architecture with specific framework-adaptations. The two tiers are:

Tier 1 (runtime; cheap; per-frame). The NPC's decision-scoring runs cached active-inference policies plus sentiment-override lookups plus trait-modulated heuristics. The cached policies are pre-computed at the consolidation-pass boundary (Tier 2 work); the lookups are O(1) per the typed-indexes architecture (post 0122 in this arc); the trait-modulated heuristics are constant-time per decision. The NPCs visible to the player respond at the iOS V1 target framerate of approximately 30 frames per second without LLM calls per decision; the per-frame budget is preserved.

Tier 2 (consolidation; slow; per-game-year). The consolidation pass runs at game-year boundaries (per post 0118 in this arc); the pass evaluates the past year's accumulated experience using sophisticated active-inference apparatus (per the framework's Path A operator ratification; post 0119 in this arc); the pass updates the cached policies for the upcoming game-year. The Tier 2 compute cost is amortized across the year of player interaction; the per-frame budget is unaffected by the Tier 2 cost; the operational tractability is what makes the sophisticated-inference apparatus deployable at V1 without breaking the per-frame budget.

Audit-layer use of sophisticated inference (per post 0119 in this arc). The audit layer runs at Tier 2 cadence; the audit verifies that the cached-policy decisions still align with the framework's structural-only-position-(a) discipline (the audit's primary check); the audit flags policy-discipline violations for developer review or for cached-policy regeneration at the next consolidation boundary. The audit-layer use is what earns the framework's discipline claims at the production-deployment layer; the audit-layer use is what makes the cached-policy approach safe to ship.

The cross-references across the hybrid-path posts compose into the framework's complete runtime architecture. Park 2023's three-process decomposition (post 0121 in this arc) handled at Tier 2; multi-graph memory typed indexes (post 0122 in this arc) available at Tier 1 and Tier 2; the consolidation pass (post 0118 in this arc) triggers Tier 2 work; the audit-layer sophisticated inference (post 0119 in this arc) operates at Tier 2 cadence; the V1 spec (post 0120 in this arc) is the META-level commitment that the implementation runs against.

## Per-frame computational budget walkthrough

The arithmetic at the framework's target scale supports the two-tier pattern's operational tractability. The framework's design surface targets:

iOS V1 target framerate of approximately 30 frames per second produces a per-frame budget of approximately 33 milliseconds.

NPC population in the order of approximately 80 to 100 characters total per the V1 spec; not all NPCs are visible at any given moment. The active NPCs (NPCs in the player's perceptual window or otherwise rendering-relevant) are in the order of approximately 8 to 12 maximum at typical play moments; most NPCs at any moment are either stationary or in cheap-cached-policy mode that does not require per-frame decision-scoring.

Per active NPC per frame, the runtime cost includes: cached-policy lookup (in the order of approximately 10 to 100 microseconds; the lookup reads the cached-policy from the per-NPC cached-policy store and produces the candidate-action scoring); sentiment-override apply (in the order of similar microsecond-range cost; the override reads the pair summary from the entity index per post 0122 in this arc and modulates the candidate-action scoring); rendering and physics and audio handled separately by the engine's per-frame pipeline.

The total per-active-NPC runtime cost is in the order of approximately 100 to 500 microseconds at typical play moments. Multiplied across 8 to 12 active NPCs, the total decision-pipeline cost is in the order of approximately 1 to 6 milliseconds per frame. The cost fits comfortably within the per-frame budget; the cost leaves substantial headroom for the rest of the per-frame pipeline (rendering; input processing; physics; audio); the cost scales linearly with the active NPC count rather than with the per-NPC event count.

The arithmetic is operationally informative. The cached-policy approach produces per-frame cost that fits within the budget envelope; the alternative (per-frame sophisticated active inference) would produce per-frame cost that exceeds the budget envelope at the framework's target scale; the cached-policy approach is what makes the V1 deployment operationally tractable.

## The decay anchor's interaction with cached-policy invalidation

The framework's 0.995-per-game-hour decay anchor (documented in post 0118 in this arc) interacts with the cached-policy invalidation question. Specifically:

When does a cached policy need invalidation? When the underlying state (the character's accumulator state; the character's trait scalars; the character's pair-relational history) has drifted beyond a threshold from when the cached policy was originally baked. The drift is the load-bearing signal for invalidation; the drift detection is the operational discipline that the framework's runtime implementation runs.

Drift detection is a cheap per-frame check on a few key state scalars. The framework's runtime implementation compares the current accumulator state against the accumulator state when the cached policy was baked; the comparison is bounded by the few key scalars rather than by the full character state; the comparison is constant-time per check. If the threshold is exceeded, the runtime implementation marks the cached policy for re-bake at the next consolidation boundary; the cached policy continues to drive runtime decisions until the next consolidation boundary, but the marking ensures the policy is regenerated at the next Tier 2 pass.

Most cached policies last most of a game-year unchanged. The framework's accumulator dynamics (the 0.995 decay anchor; the consolidation-pass-driven Layer 2 promotions; the trait-modulated encoding pathway) produce state drift at game-week-scale cadence; the cached-policy threshold is set such that game-week-scale drift does not trigger invalidation; the policy stays valid across most of the game-year until the consolidation boundary regenerates it. The unchanged-most-of-the-game-year pattern is the cost-saving the hybrid path delivers; the alternative (per-frame policy regeneration) would produce per-frame cost that exceeds the budget envelope at the framework's target scale.

## Comparison: full per-frame sophisticated inference versus cached-policies-with-slow-bake

The two architectural alternatives produce different cost-and-quality profiles worth comparing directly.

Full per-frame sophisticated inference. The runtime decision-scoring pipeline would run sophisticated active inference per decision per frame; the per-decision cost at sophisticated-scheme recursion depth (per Friston 2017 Appendix F and Friston 2021 *Sophisticated Inference*) is in the order of milliseconds per decision at the framework's policy-search breadth; multiplied across 8 to 12 active NPCs at the framework's interaction density of approximately 10 decisions per game-minute, the per-game-hour decision count is in the order of tens of thousands and the per-frame cost would be in the order of tens to hundreds of milliseconds. The cost breaks the per-frame budget by an order of magnitude or more; the deployment is operationally infeasible at the framework's target scale.

Cached policies with slow bake. The runtime decision-scoring pipeline runs cached active-inference policies (Tier 1; per-frame cost in the microsecond range per NPC); the Tier 2 sophisticated active-inference apparatus runs at consolidation-pass boundaries to regenerate the cached policies; the Tier 2 cost is amortized across a game-year of player interaction; the per-frame budget is preserved. The cost fits the budget envelope; the deployment is operationally tractable at the framework's target scale.

The quality trade-off is real. Cached policies are static within a game-year; the policies do not adapt to mid-year state changes faster than the drift-detection-and-mark-for-rebake cadence; characters will not surprise the player with mid-year policy changes that the cached policy did not anticipate. The trade-off is acceptable for the framework's cozy-sim design surface (the design surface does not require per-frame adaptive policy changes; the multi-decade scope means that within-year policy stability is design-appropriate rather than a design limitation); the trade-off would be a problem for combat-driven gameplay where mid-fight adaptive policy changes are design-critical. The framework's design surface aligns with the trade-off; the architectural choice is operationally defensible at the framework's design surface.

## Audit-layer integration with cached policies

The audit-layer apparatus (per post 0119 in this arc) integrates with the cached-policy architecture at the consolidation-pass boundary. Specifically:

At the consolidation-pass boundary, sophisticated active inference runs in audit-layer mode. The audit reads the past game-year's NPC decisions (the cached-policy decisions the runtime pipeline produced) and re-evaluates them under the sophisticated-inference apparatus. The re-evaluation produces specific audit verdicts: do the cached-policy decisions align with position-(a)-compatible EFE-minimization under the updated state; does any cached policy now require sophisticated-inference-style metacognitive recursion that the cached form does not support; does any cached policy violate the framework's state-space-content discipline.

Failed audit triggers cached-policy regeneration. The cached policies that failed the audit are regenerated with sophisticated-inference apparatus operating on the past game-year's accumulated state; the regenerated policies become the cached policies for the upcoming game-year; the characters whose cached policies needed regeneration get fresh policies starting at the next game-year boundary. The regeneration is what makes the audit-layer apparatus operationally consequential; the audit produces specific actionable outputs that the framework's V1 runtime architecture absorbs.

Audit logs are operational artifacts. The framework's operator can review which cached policies needed regeneration across game-years; the review surfaces patterns in cached-policy invalidation (e.g., specific trait profiles that show consistent invalidation; specific design-surface contexts that produce invalidation more often than others); the patterns inform subsequent cached-policy generation work (e.g., specific cached-policy baking pre-conditions that reduce invalidation rates). The audit-log review is what makes the cached-policy approach iteratively-improvable over the framework's continued V1.x and post-V1 development.

## V1 implementation cost

The two-tier pattern implementation includes specific components. The Tier 1 cached-policy lookup infrastructure (the data structures that hold cached policies per NPC; the lookup interface that produces decision-scoring inputs); the Tier 2 sophisticated-inference apparatus for cached-policy regeneration (the sophisticated-scheme implementation that runs at consolidation-pass cadence); the drift-detection logic (the per-frame check that marks cached policies for regeneration); the audit-pass integration (the audit-layer apparatus that operates on cached-policy decisions and produces audit verdicts plus regeneration triggers).

The implementation cost estimate at the framework's planning phase was roughly 30 to 50 hours of BUILD-side work; the estimate includes the four components above plus the test-run validation across multi-game-year scope. The cost is operationally tractable within the framework's V1 budget under the Path A ratification's budget extension; the cost is what the two-tier pattern actually costs at the implementation layer.

## Honest scope: where cached-policy plus slow-consolidation fails

The pattern is not universally applicable; specific failure modes are worth naming directly.

Rare-event-driven cached-policy invalidation does not handle gracefully. The player can mid-year trigger a cached-policy mismatch by doing something extraordinary that the cached policy did not anticipate; the cached policy will continue to drive runtime decisions until the next consolidation boundary regenerates it; the in-year mismatch produces character behavior that does not respond to the extraordinary event as the framework's design predictions would suggest. The mismatch is operationally bounded (the next consolidation boundary regenerates the policy; the in-year mismatch is at most a year-scale duration); the mismatch is a known limitation of the cached-policy approach; the framework's V1 commitment is to accept the limitation rather than to address it through per-event cached-policy regeneration (which would re-introduce the per-frame cost the cached-policy approach is designed to avoid).

Cross-NPC interaction depth is not addressed by the per-NPC cached-policy approach. The cached policies are per-NPC; the policies do not coordinate across NPCs; multi-NPC interactions where one NPC's behavior should depend on multiple other NPCs' coordinated behavior are not fully handled by the per-NPC cached-policy pattern. The framework's broader architecture commitments address some multi-NPC interaction patterns through the pair-relational mechanism and the sentiment-override dynamics; broader multi-NPC coordination requires additional architectural commitments that the V1 spec does not include.

The pattern does not scale beyond cozy-sim cadence. Combat-driven gameplay would invalidate the cached-policy assumption (the per-frame policy changes required for combat decision-scoring break the cached-policy approach); fast-paced multi-decision contexts where the cached-policy approach's within-year stability is a design problem rather than a design fit would require different architectural commitments. The framework's design surface is cozy-sim; the design surface aligns with the cached-policy approach; the alignment is what makes the approach defensible at the framework's V1 commitment.

## What this changed in my workflow

Two specific changes. First, when the framework adopts a runtime-layer architectural pattern, I now explicitly check the pattern's per-frame cost arithmetic at the framework's target scale before the adoption is ratified. The discipline catches per-frame-budget-exceeding patterns at the planning phase; the discipline produces runtime-layer architectures that fit the budget envelope; the discipline is what made the cached-policy-with-slow-consolidation pattern visible as the appropriate response to the full-per-frame-sophisticated-inference alternative at V1.

Second, when the framework's runtime-layer architecture combines per-frame-cached approaches with slower-cadence regeneration approaches, I now explicitly document the drift-detection-and-regeneration discipline that the architecture depends on. The discipline catches drift-handling failure modes (where the cached approach is adopted without addressing the drift-detection question; the cached approach continues to drive decisions under state conditions the cache was not baked under); the discipline produces architectures whose cached-approach-versus-regeneration boundary is operationally well-defined; the discipline is what makes the cached-policy approach safe to ship at production scale.

## What I am not claiming

I am not claiming the cached-policies-with-slow-consolidation pattern is the only operationally-defensible response to the per-frame-budget question for procedural-character architectures. Other patterns may produce different operationally-defensible architectures; the framework's pattern is one defensible response to the framework's specific budget and design-surface constraints, not the only defensible response. Operators in similar design surfaces may adopt different patterns that fit their specific budget and deployment-platform constraints.

I am not claiming the Project Zomboid offscreen-storylet architecture is the only commercial-precedent analog for the cached-versus-slow pattern. Other commercial games may implement similar patterns under different specific architectural commitments; the Project Zomboid architecture is the most directly-borrowed commercial-precedent the framework's research arc surfaced; the borrowing is operationally clean and the precedent is well-documented in the developer's public blog. Other commercial precedents may exist that the framework's research arc did not survey in depth.

I am not claiming the cached-policy approach handles all NPC-behavior questions the framework's design surface raises. The approach handles per-NPC decision-scoring at per-frame cadence; the approach does not handle all multi-NPC coordination questions; the approach does not handle rare-event-driven mid-year policy adaptation gracefully. The framework's broader architecture commitments address some of the questions the cached-policy approach does not; the broader architecture is what makes the cached-policy approach defensible at V1.

I am not claiming the framework's V1 implementation will deliver the cached-policy approach at the framework's target NPC scale without empirical surprises. The V1 implementation is the apparatus that produces the empirical evidence; the empirical evidence may support the cached-policy approach at scale, may surface specific tuning refinements, or may surface architectural-discipline questions that the V1 spec did not anticipate. The V1 budget includes a buffer for implementation variance; the post-V1 work would address any architectural-discipline questions that surface in V1 implementation.

I am not claiming the audit-layer regeneration discipline eliminates all cached-policy-discipline-failure modes. The audit catches discipline violations at consolidation-pass cadence; violations that occur within a game-year between consolidation passes are not caught by the audit until the next pass; the audit's coverage is operationally bounded. The framework's broader discipline (the four-audit mandatory test surface; the broader marketing-copy discipline; the broader operator-side scope discipline) extends beyond the consolidation-pass audit's coverage; the audit is one layer of the discipline, not the complete discipline.

## What I am claiming

The cached-policies-with-slow-consolidation pattern is the framework's operational response to the per-frame-budget question for active-inference-grounded NPC decision-scoring at the framework's target scale. Tier 1 cached active-inference policies drive per-frame visible NPC behavior cheaply; Tier 2 sophisticated active-inference apparatus runs at consolidation-pass boundaries to regenerate the cached policies based on the past game-year's accumulated experience; the audit-layer apparatus integrates at Tier 2 cadence to verify cached-policy discipline-alignment and trigger regeneration when discipline-violations surface.

If you are building procedural-character architectures with sophisticated decision-scoring requirements at production-deployment scale with tight per-frame budget constraints, the borrow-the-cached-pattern-substitute-the-slow-apparatus discipline is operationally cheap and produces architectures whose per-frame cost fits the budget envelope while preserving the architectural-commitment depth that the design surface requires. The discipline costs the cached-policy infrastructure work plus the consolidation-pass regeneration work; the discipline produces architectures whose runtime decision-scoring pipeline is operationally tractable at scale; the alternative (full per-frame sophisticated inference) breaks the budget envelope at the target scale.

The hybrid path is three borrowings plus one combination: Park 2023 backbone (post 0121 in this arc) plus MAGMA-style typed indexes (post 0122 in this arc) plus Project Zomboid offscreen-storylet pattern (this post) plus active-inference state-space-content discipline (the framework's own integration commitment). The combination is novel; the components are not. The discipline is honest enough to ship at V1; the V1 ship is the first instance of the combination at the production-deployment layer; the empirical validation is the multi-pilot multi-year research program that the framework's commitments extend over.
