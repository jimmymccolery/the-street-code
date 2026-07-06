# What Communal Accountability Would Require in Code: The Generosity-Ledger Mechanic the Framework Specced and Banked as a Steam V1.0 Candidate

<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0126
title: What Communal Accountability Would Require in Code: The Generosity-Ledger Mechanic the Framework Specced and Banked as a Steam V1.0 Candidate
date_published: 2026-06-29
status: published
superseded_by: none
domain: framework-architecture; Wireduan communal-accountability generosity-ledger mechanic; Steam V1.0 candidate deferred from iOS V1; ablation-gate discipline
project_scopes: framework-architecture, cross-cultural-discipline, framework-scope-boundaries
cc_task_relevance: v1-vs-steam-scope-decisions, communal-accountability-mechanic-design, ablation-gate-application
phase_binding: Phase-4+
discipline_family: framework-architecture
canonical_rule: wireduan-communal-accountability-generosity-ledger-mechanic-steam-v1-candidate
load_bearing_claims:
  - Wireduan communal-accountability mechanic specced (Option A from Round 7 deliberation) as Steam V1.0 candidate
  - Generosity-ledger mechanic tracks pair relationships over time; personhood-as-striving mechanics
  - Communal accountability as personality mechanic distinct from HEXACO trait (Post 0125 category-error correction)
  - Banked for Steam V1.0 (deferred from iOS V1); requires meaningful implementation cost to avoid ornamental deployment
applicability_triggers:
  - When operationalizing Wireduan personhood-as-achievement WITH real mechanic (Element 1 option a)
  - When designing generosity-ledger accumulator alongside HEXACO H
  - When deciding what belongs in iOS V1 vs Steam V1.0
  - When ablation-gating a cross-cultural mechanic implementation
mechanism_details:
  - Generosity ledger = per-pair accumulator tracking give/receive imbalance over time
  - Personhood-as-striving = standing improves via consistent generosity + relational care
  - Ablation gate required before operationalization (per-npc-philosophy-profile-reservation-and-ablation-gate-v1.md at the-street-code/methodology/)
  - Steam V1.0 scope = post-iOS-launch; sophisticated inference runtime promoted
cross_refs:
  - Post 0112 (Wiredu personhood-as-achievement structural inspiration)
  - Post 0116 (pair-relational sentiment mechanics)
  - Post 0117 (Wiredu mapping failure)
  - Post 0124 (five-element disclosure discipline)
  - Post 0125 (procedural test NOT trait dimension)
  - Methodology: per-npc-philosophy-profile-reservation-and-ablation-gate-v1.md
  - Post 0146 Layer 6 + Layer 7 (relationships + cultural personhood)
-->

**Author:** Jimmy McColery
**Date:** 2026-06-29
**Status:** Cross-cultural sequence post specifying the implementation-layer requirements for a Wireduan communal-accountability mechanic; carries high cross-cultural exposure; applies the framework's five-element disclosure discipline; documents the Steam V1.0 candidate scope without committing to ship at iOS V1; cites Wiredu Chapter 9 *Person and Community* (Wiredu and Gyekye 1992) directly per the framework's primary-text-verified citation chain

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I am a solo indie developer drawing on structural elements of cross-cultural philosophical traditions for a procedural-character architecture in a tycoon sim I am building. I am not representing any tradition. I decline paid scholar review and carry the interpretive risk solo. I invite knowledgeable correction. The retraction condition I am committing to applies: if a knowledgeable critic in the Akan-philosophy tradition demonstrates that the framework's structural-borrowing materially misrepresents Wiredu's reading or the Akan tradition more broadly, I will retract the cross-cultural framing within 14 days while preserving the technical content that stands independently.

I dropped the Wiredu mapping from the framework's V1 mechanics (post 0117 in this arc documents the drop; post 0125 in this arc documents the category-error reasoning). This post asks the more interesting question: what would it take to actually implement Wireduan communal accountability in code? The post specs the Option (a) build from the framework's Round 7 deliberation cycle (the option the framework considered but did not adopt at V1; the option that would have required substantial additional V1 budget; the option that is potentially absorbable at Steam V1.0 scope). The spec is at the meta-architecture level (the framework's soft-disclosure discipline keeps the operator-side implementation specifics private); the spec is publishable because the mechanic's substantive content is documented in the framework's broader research arc and the public publication is part of the framework's commitment to discipline accountability.

The post is a "what would it actually cost" post. The post is not a commitment to ship the mechanic at any specific framework scope; the post documents the spec so that the framework's cross-cultural-philosophy community engagement has a public reference for what the mechanic would look like if the framework's operator-side judgment supports the Steam V1.0 scope inclusion. The reference is operationally useful for the framework's discipline accountability; the reference is what makes the framework's Option (c) drop at V1 a publicly-defensible decision rather than a quiet shelving.

## What Option (a) from the framework's Round 7 deliberation was

The framework's Round 7 R6 Section 3 deliberation considered three options for the Wiredu-HEXACO H mapping question:

Option (a). Retain Wiredu as load-bearing AND build a real communal-accountability mechanic. The option would have implemented the substantive content the Wiredu citation claims; the option would have required design work plus code work to deliver the mechanic; the option would have substantially extended the V1 budget; the option would have produced V1 NPCs whose behavior genuinely instantiates Wireduan personhood-as-striving plus communal accountability rather than statistical cooperation re-labeled as Wireduan.

Option (b). Decouple HEXACO H from Wiredu philosophical grounding entirely. The option would have removed the philosophical-grounding claim from the framework's HEXACO H trait commitments; the option was rejected at the deliberation cycle because the rejection would have discarded defensible philosophical framing (the HEXACO H trait's empirical-cooperation-prediction validation literature is broader than the Wiredu engagement; the trait's validity does not depend on the Wiredu engagement; the decoupling would have lost the structural philosophical framing without delivering an offsetting benefit).

Option (c). Drop the Wiredu mapping as load-bearing V1 mechanics; retain only as philosophical framing in the lead philosophical-inspiration post (post 0112 in this arc), the framework paper, and the self-correction post (post 0117 in this arc). The option is the operator's choice at the deliberation cycle; the option is documented in post 0117 in this arc; the option is the framework's V1 commitment.

The cost arithmetic at the deliberation was specific. Option (a) was approximately 8 to 18 hours of design work plus 25 to 70 hours of code work; the total was 33 to 88 hours; the framework's V1 budget at the time of the deliberation did not absorb the upper end of the cost range without scope-cuts elsewhere. The Path A operator ratification (the subsequent ratification that promoted sophisticated active inference and structural-only self-reflection to V1 critical-path) is documented in post 0119 in this arc; the Path A ratification's framing ("most comprehensive solution") makes the Option (a) reconsideration potentially viable for Steam V1.0 plus the 143-day-runway accommodation that the broader framework planning addresses. The reconsideration is an open question; the framework's V1 commitment is Option (c); the framework's Steam V1.0 consideration may revisit Option (a) if the operator-side judgment supports the reconsideration.

## The generosity-ledger mechanic

The Option (a) mechanic the framework specced has two architectural elements: a generosity ledger that tracks accumulated relational obligations and a community-accountability mechanic that surfaces obligations when characters interact. The two elements compose into the communal-accountability architecture that the Wireduan philosophical grounding would require to be operationally honest.

The generosity-ledger spec is operationally specific. Each character in the V1 NPC population would maintain two ledgers: an outgoing ledger and an incoming ledger.

The outgoing ledger records events where the character gave generosity to another character. The ledger entries are tagged with: the pair (giver, receiver); the event game-time; the generosity type (tip; favor; defense in a social conflict; time given to a request; attention given to a relational context); the magnitude (the specific generosity event's measured contribution; the magnitude is a scalar bounded by the type-specific magnitude range).

The incoming ledger records events where the character received generosity from another character. The ledger entries are tagged with the same schema as the outgoing ledger; the entry references the giver-receiver pair from the receiver's perspective.

The ledgers persist via the framework's Layer 2 consolidation pass (the consolidation pass mechanism documented in post 0118 in this arc; the consolidation pass would extend to include the ledger maintenance as part of the per-character consolidation work). The ledgers integrate with the framework's typed indexes (the multi-graph memory typed-indexes architecture documented in post 0122 in this arc; the entity-index would extend to include the per-pair generosity-ledger summaries as part of the per-pair retrievable content). The ledger maintenance is bounded per character per game-year by the per-character generosity event frequency; the ledger storage cost is operationally tractable within the V1-extended-by-Option-(a) budget envelope.

## The community-accountability mechanic

The community-accountability mechanic operates at decision-scoring time. When a character considers a candidate action that would affect another character (or that would affect the character's own ledger position), the decision-scoring layer reads the character's outgoing and incoming ledgers and integrates the read into the action-scoring calculation. The integration produces two scoring contributions:

The individual-preference contribution (the framework's existing scoring layer per the V1 spec; the HEXACO-trait modulation plus the accumulator-state modulation plus the pair-history modulation; the contribution that drives the framework's V1 NPC behavior without communal accountability).

The communal-accountability adjustment (the additional scoring contribution that the Option (a) mechanic would add; the adjustment reads the character's accumulated relational obligations and modifies the action-scoring to either maintain or violate the obligations; an action that would violate the obligations gets a scoring penalty that scales with the obligation's magnitude; an action that would honor the obligations gets a scoring bonus).

The adjustment is a second term in the expected-free-energy decomposition that the framework's decision-scoring uses (the EFE decomposition under Path A's sophisticated active inference; the decomposition is part of the framework's Round 9 generative-model formalization arc work). The second-term integration matters because the action-scoring's existing terms (the individual-preference contributions) are denominated in the same units (EFE-comparable scoring contributions); the second term integrates cleanly without requiring a separate scoring pipeline.

The implementation cost estimate for the community-accountability mechanic specifically is in the order of approximately 25 to 50 hours of BUILD-side work within the Option (a) total cost range. The cost includes: the ledger storage and maintenance; the decision-scoring integration; the audit-layer extension to verify the integration's discipline-alignment (the audit-layer apparatus from post 0119 in this arc would extend to include the communal-accountability discipline-checks); the test-run validation across multi-game-year scope to verify the mechanic produces the design-predicted character behavior.

## A bowling-alley scenario walkthrough

The mechanic's operational shape becomes legible through a specific scenario. The scenario: a pinboy character has a long-running pair-relational history with a bowler character; the bowler character has tipped the pinboy weekly across five game-years; the bowler character stops tipping at game-year six; the framework's V1 specification (without the Option (a) mechanic) versus the Option (a) extension produce different downstream character behavior.

Without communal-accountability (framework's V1 commitment under Option (c) drop). The bowler tips quarterly per the framework's existing decision-scoring layer (HEXACO H plus accumulator-state plus pair-history); the pinboy responds per the pinboy's own state (the pinboy's pair-relational sentiment toward the bowler; the pinboy's accumulator state; the pinboy's HEXACO H plus attachment style modulation). When the bowler stops tipping at game-year six, the pinboy's pair-relational sentiment slowly drifts (the sentiment scalar updates per the decay-toward-current-plus-drift-from-history formula from post 0116 in this arc; the drift produces a softer reduction in sentiment that is not specifically reactive to the missing tipping pattern). The pinboy's interactions with the bowler at game-year six and beyond proceed at the new sentiment-modulated baseline; the player observes a slight change in the pinboy's behavior toward the bowler over multiple subsequent game-weeks.

With communal-accountability (Option (a) extension). The bowler tips quarterly per the same existing decision-scoring layer; the pinboy's incoming ledger registers each tip event with its specific magnitude; the pinboy's accumulated incoming ledger from the bowler has five game-years of weekly entries. When the bowler stops tipping at game-year six, the pinboy's incoming ledger registers the loss of accumulated incoming generosity; the loss is reflected as a specific obligation-shift in the decision-scoring layer for the pinboy's interactions with the bowler. The pinboy's responses to the bowler now factor the obligation-shift; the pinboy's behavior becomes more pointedly cool until reciprocity resumes (the bowler tips again, restoring the pattern) or until the relationship resets (the obligation magnitude decays back to baseline through the framework's consolidation pass over multiple subsequent game-years).

The player observation matters. Without communal accountability, the pinboy's behavior change is a gradual sentiment-shift that the player may or may not notice. With communal accountability, the pinboy's behavior change is specifically reactive to the missing tipping pattern, and the change is observable in specific subsequent interactions in ways the player can recognize as connected to the change in the bowler's behavior. The player experiences characters whose memory of accumulated favors and slights operates at a deeper level than sentiment-override alone provides; the player experiences Wireduan relational personhood operationalized: action evaluated in the context of accumulated relational obligations.

## Why this is a Steam V1.0 candidate, not iOS V1

The framework's iOS V1 scope does not include the Option (a) mechanic. The reasoning has four components:

Cost. The Option (a) mechanic's 33-88 hour total cost is a substantial fraction of the framework's LEAN V1 budget (190-260 hours at the LEAN estimate; the Path A ratification extends to 270-410 hours under Path A); even Path A's extended budget does not fit comfortably with the Option (a) addition. The V1 commitment is bounded; the V1 commitment does not absorb the Option (a) mechanic; the Steam V1.0 reconsideration would have a different budget envelope.

Marketing-copy discipline. Communal accountability raises the cross-cultural exposure of the player-facing experience. The framework's Marcus Reed Surface 8 audit gate (the framework's audit gate for representational-stakes content; documented in post 0113 in this arc and elsewhere) would require additional substrate-triangulation work for any V1 deployment of the Option (a) mechanic; the substrate-triangulation cycle is part of the framework's broader discipline; the cycle requires additional operator-attention investment that the V1 timeline does not absorb. The Steam V1.0 timeline has the runway for the additional substrate-triangulation work; the iOS V1 timeline does not.

Multi-decade payoff. The communal-accountability ledger's payoff is most visible at the Steam V1.0 Chronological Challenge mode (the multi-decade NPC arcs where ledgers accumulate over decades; the cross-era progression that the Chronological Challenge mode supports); the iOS V1 cozy-1950s baseline does not amortize the ledger's complexity across the same depth of player engagement that the Chronological Challenge mode would. The mechanic's design-payoff-to-implementation-cost ratio is better at Steam V1.0 scope than at iOS V1 scope.

iOS V1 baseline sufficiency. The framework's iOS V1 cozy-1950s baseline does not strictly require the Option (a) mechanic. Wiredu's framework can remain at the framework-paper inspiration layer for the V1 ship; the V1 ship is operationally defensible without the Option (a) mechanic; the mechanic is the natural slot for the Steam V1.0 scope because the Steam V1.0 deeper-engagement-baseline benefits more from the mechanic's complexity than the iOS V1 cozy-baseline does.

## Honest scope: what this spec doesn't solve

The Option (a) mechanic does not solve all cross-cultural-grounding-related architecture questions. Specific failure modes that the mechanic does not address:

Cross-cultural breadth. The Wiredu-derived ledger mechanic respects Wiredu's framework but does not automatically respect other communal-ethics traditions (Confucian role ethics; Ubuntu; Maori manaakitanga; and others). The mechanic operationalizes one tradition's specific structural commitments; the mechanic is not a universal communal-ethics mechanic. The framework's broader cross-cultural-disclosure discipline applies; the discipline's element 1 (acknowledgment language) would frame the mechanic as inspired by Wiredu's specific reading rather than as a universal communal-accountability mechanic.

Performance scaling. Adding ledger lookups per decision increases the per-frame budget cost. The framework's V1 per-frame budget at the iOS V1 target framerate is tight; the additional ledger-lookup cost would compound the existing cached-policy-lookup cost; the broader cached-policies-with-slow-consolidation pattern (post 0123 in this arc) would need extension to include the ledger summary as part of the cached-policy-input pre-computation. The extension is operationally tractable but adds implementation complexity.

Cached-policies-with-slow-consolidation pattern coexistence. The Option (a) mechanic is an additional input to cached-policy regeneration at consolidation boundaries (post 0123 in this arc) rather than a replacement for the cached-policies approach. The ledger summary at the consolidation pass feeds into the sophisticated-inference re-evaluation that regenerates the cached policies; the regenerated policies include the communal-accountability adjustment in their cached form; the per-frame runtime continues to use the cached policies without paying the per-decision sophisticated-inference cost.

Cross/Crenshaw V1 SCHEMA-PLACEHOLDER discipline. The framework's broader cross-cultural sequence includes multi-traditional engagement (the Cross-Nigrescence and Crenshaw-intersectionality schema-placeholders documented in post 0128 in this arc); the Option (a) mechanic addresses one specific tradition's commitments and does not address the broader multi-traditional engagement; the framework's broader discipline addresses the multi-traditional engagement through the schema-placeholder approach at iOS V1 and through the post-V1 work that would extend the operationalization.

## What this post is and what it is NOT

This post is a "what would it cost" post for the cross-cultural-philosophy and game-design community. The post documents what the framework's Option (a) mechanic would actually require at the implementation level; the documentation is publishable because the mechanic's substantive content is methodology rather than commercial-scope implementation specifics; the public documentation serves the framework's discipline-accountability commitment.

This post is documentation of Option (a) as a banked Steam V1.0 candidate. The framework's planning considers Option (a) as a Steam V1.0 candidate; the planning has not committed to ship the mechanic at any specific framework scope; the documentation makes the consideration visible publicly so the framework's cross-cultural-engagement is accountable to a specific public commitment.

This post is NOT a commitment to ship Option (a). The framework's V1 commitment is Option (c) drop; the framework's Steam V1.0 commitment is open; the operator may still choose to ship Option (c) drop indefinitely across all framework scopes. The post documents the Option (a) cost and reasoning; the post does not commit the framework to the Option (a) ship.

This post is NOT a claim of Wireduan authenticity for the Option (a) mechanic. The mechanic is INSPIRED BY Wireduan philosophy at the structural level; the mechanic does not claim to represent the Akan tradition; the mechanic does not deliver the full substantive content of Wiredu's reading at the implementation layer (the mechanic operationalizes the communal-accountability structural commitment specifically; the broader Wireduan philosophical content stays at the framework-paper inspiration layer). The structural-borrowing-only commitment from post 0124 in this arc applies; the post's discipline is operational.

## Closing humility paragraph (mandatory per element 4)

This post specs what the framework's Wireduan communal-accountability mechanic would look like at the implementation layer. The spec is at the meta-architecture level (the framework's soft-disclosure discipline keeps the operator-side implementation specifics private); the spec is publishable because the mechanic's substantive content is methodology and the public publication is part of the framework's discipline-accountability commitment.

The post is honest about the spec's scope. The spec is a Steam V1.0 candidate; the spec is not an iOS V1 commitment; the spec is not a guarantee of Steam V1.0 deployment. The framework's V1 commitment is Option (c) drop; the framework's Wiredu engagement at V1 stays at the framework-paper inspiration layer per the structural-borrowing-only discipline.

The retraction condition applies. The 14-day response timeline applies. The primary-text-defensibility standard applies. I invite knowledgeable correction from in-tradition scholars; the framework is held accountable to the discipline this post operates under. The Akan-philosophy engagement in this post is structural-borrowing only; the engagement cites Wiredu directly with primary-text grounding; the engagement does not claim representation of the Akan tradition or of Wireduan philosophy in any operationalization sense.

## What I am not claiming

I am not claiming the Option (a) mechanic is the only operationally-defensible implementation of Wireduan communal accountability. The mechanic is one specific implementation; other implementations may produce different operationally-defensible mechanics; the framework's spec is operator-judgment supported by the framework's deliberation cycle. Other procedural-character frameworks engaging Wiredu's philosophical content may implement different specific mechanics; the spec is the framework's specific shape.

I am not claiming the Option (a) mechanic would deliver "authentic" Wireduan personhood-as-striving in the player-facing experience. The mechanic operationalizes one structural commitment (the communal-accountability aspect); the broader Wireduan content (the procedural-moral-test aspect; the relational-constitution aspect; the recoverability aspect with full Akan-tradition framing) stays at the framework-paper inspiration layer. The mechanic's authenticity claim is bounded to the communal-accountability structural commitment; the bounding is operational.

I am not claiming the Steam V1.0 reconsideration of Option (a) will result in adoption. The reconsideration is an open question; the framework's Steam V1.0 planning may or may not adopt the mechanic; the adoption decision is operator-judgment that the framework's broader planning addresses. The Steam V1.0 timeline is approximately October 2027; the decision-making is post-iOS-V1-ship work that has not yet happened.

I am not claiming the Marcus Reed Surface 8 audit gate requirements are operationally bounded. The audit gate work for the Option (a) mechanic deployment would include substrate-triangulation cycles, primary-text-grounding verification for the cross-cultural-content, and operator-side scope-discipline review; the cost of the audit gate work is real and is part of the broader Steam V1.0 candidate consideration. The framework's commitment to the audit gate discipline is operational; the discipline is not optional.

I am not claiming the mechanic's communal-accountability adjustment would integrate cleanly with all framework V1 architectural commitments. The adjustment is a second EFE-decomposition term; the integration requires the Round 9 generative-model formalization work to specify the adjustment's specific mathematical form; the formalization is currently in execution; the formalization's outcomes will inform the eventual operational integration. The integration is operationally feasible but is not pre-specified at the post's drafting moment.

## What I am claiming

The framework's Option (a) mechanic for Wireduan communal accountability requires a generosity ledger that tracks accumulated relational obligations plus a community-accountability mechanic that integrates the ledger into the decision-scoring layer. The implementation cost is approximately 33 to 88 hours of BUILD-side work (the framework's deliberation-cycle estimate; the cost includes ledger storage and maintenance, decision-scoring integration, audit-layer extension, and test-run validation). The mechanic operationalizes one structural commitment from Wiredu's reading at the implementation layer; the broader Wireduan philosophical content stays at the framework-paper inspiration layer per the structural-borrowing-only discipline.

If you are designing procedural-character architectures and considering cross-cultural philosophical traditions as sources of mechanic-grounding (not just framework-paper inspiration), the spec above is one operational shape for what the operationalization would actually require. The operationalization is real implementation cost; the cost is not optional if the philosophical claim is to be honest; the alternative (the framework's Option (c) drop at V1) is operationally defensible when the operationalization cost exceeds the available budget envelope. The discipline of choosing between Option (a) and Option (c) is operator-judgment supported by the framework's broader cross-cultural-disclosure discipline; the discipline produces decisions that are accountable to the framework's discipline-accountability commitments.

The mechanic is a Steam V1.0 candidate. The framework's iOS V1 commitment is Option (c) drop. The Steam V1.0 reconsideration is open. The framework's broader planning addresses the reconsideration as part of the post-iOS-V1-ship work. The retraction condition applies; the 14-day response timeline applies; the primary-text-defensibility standard applies; the framework is held accountable to the discipline this post operates under.
