<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0068
title: Composition over modification: an architectural-design pattern for multi-system games
date_published: 2026-06-01
status: published
superseded_by: none
domain: software architecture pattern for multi-system game coupling via composition-layer
project_scopes: pin-paradise, street-code-methodology
cc_task_relevance: architectural-lock-cycle-design, multi-system-coupling-decision, composition-layer-pattern
phase_binding: era-independent
discipline_family: none-applicable
canonical_rule: Newer architectural decisions compose on top of older ones in a dedicated composition layer owned by the newer decision; older decisions stay textually immutable
load_bearing_claims:
  - Standard practice modifies existing system interface to expose what new system needs
  - Composition pattern owns coupling on the newer side rather than modifying the older side
  - n=4 cumulative empirical validation across May 2026 architectural-lock cycles
  - More tractable than modification-based coupling for multi-system games
applicability_triggers:
  - When multi-system game needs cross-system coupling
  - When architectural-lock arc discipline requires textual immutability for prior locks
  - When authoring architecture posts on solo indie multi-system design
mechanism_details:
  - Older architectural decisions remain textually immutable to preserve reasoning provenance
  - Newer decisions carry their composition-layer explaining coupling into prior systems
  - Enables clean cross-Q composition without breaking prior audit trail
cross_refs:
  - Post 0049 (design mode vs code mode transition)
  - Post 0057 (V1 bug triage documentation)
-->

# Composition over modification: an architectural-design pattern for multi-system games

**Author:** Jimmy McColery
**Date:** 2026-06-01
**Status:** Software architecture finding; one design pattern empirically validated at n=4 cumulative reproduction across a multi-month architectural-lock arc

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

When you build a game with multiple interacting systems (economy, customer behavior, equipment maintenance, marketing, event-card mechanics) the standard architectural challenge is what happens when one system's design needs to reach into another system's behavior. The marketing system needs to know how much customer-pool elasticity each pricing tier produces; the equipment-maintenance system needs to know how oil-pattern degradation affects ball-trajectory simulation; the event-card system needs to know how soul-axis thresholds compose with existing decay dynamics. Each cross-system reach is a coupling point. The question of how to manage coupling across many systems is one of the load-bearing architectural questions for the project class.

The standard answer in conventional software-engineering practice is to modify the existing system's interface to expose what the new system needs. The marketing system's design document gets an additional section that explains the elasticity interface; the equipment-maintenance system's design document gets an oil-pattern-coupling section; the event-card design document gets a soul-axis-threshold section. Each system's design grows as new systems require coupling; the documents grow with edits to existing content as new architectural decisions are made.

This post documents a different pattern I've been using across the bowling-alley tycoon sim I'm building solo. The pattern emerged unplanned across four architectural-lock cycles in May 2026, was empirically validated at n=4 cumulative reproduction by the end of that month, and has structural properties that make it more tractable than the standard modification-based coupling approach for the project class I'm working in. The pattern is "composition over modification": newer architectural decisions compose on top of older ones in a dedicated composition layer that is owned by the newer decision; older architectural decisions stay textually immutable.

This post describes the pattern, the four empirical fires that validated it, and the structural properties that make it work for multi-system games specifically.

## The pattern

The pattern's mechanism is simple but counterintuitive. When a new architectural decision needs to interact with an existing one, the new decision's design document declares the interaction explicitly in a "composition layer" section owned by the new decision. The existing decision's design document does not get edited. The interaction is documented at the newer-decision side; the older-decision side stays in whatever shape it was at the time it was originally written.

Concretely: if the marketing-subsystem design (call it Q13) needs to interact with the customer-pool elasticity model (call it Q12), then Q13's design document includes a section explicitly describing the Q12-coupling behavior. Q12's design document is not edited to add a "and-here-is-how-marketing-couples" section. The reader who wants to understand marketing reads Q13's document including its Q12-coupling section; the reader who wants to understand customer-pool elasticity reads Q12's original document without the marketing coupling appearing in the customer-pool document.

The composition-layer section in the newer document carries the responsibility for being correct about the interaction. If the interaction changes (because some downstream decision modifies the marketing behavior, for example), the modification happens at the newest decision's document; older decisions stay textually stable across many cycles of architectural evolution.

This is composition, not inheritance or polymorphism. The newer architectural decision composes on top of the older one. The older one continues to be what it was when originally written. The composition layer is the explicit named mechanism that lets the newer decision modify the system's overall behavior without modifying the older decision's text.

## The first fire: Q13 marketing on customer pools

The first time I deployed this pattern, I did not know I was deploying it. I was working on the marketing subsystem design for the tycoon sim. The marketing subsystem needed to model how price elasticity per customer pool (which had been locked in an earlier Q12 cycle) would interact with marketing-campaign spending. The natural reach was to edit Q12's elasticity model to add the marketing-coupling behavior.

I started writing the edit and noticed that the edit would change Q12's document substantially. The original Q12 elasticity model was concerned with how customers respond to price changes; the marketing-coupling content I was about to add was concerned with how marketing-campaign reach interacts with that responsiveness. The two were architecturally adjacent but semantically distinct. Editing Q12 to include the marketing-coupling content would mix two architectural concerns in one document section.

I stopped editing Q12 and instead created a Q13.composition-layer section in the new Q13 marketing-subsystem document. The composition-layer section described the Q13-on-Q12 coupling explicitly. The composition-layer section was owned by Q13; Q12's original document was preserved as it had been originally written.

The composition-layer section worked. It captured the coupling cleanly. Future readers wanting to understand marketing's interaction with customer-pool elasticity would find the explanation in Q13's document; the reader wanting to understand customer-pool elasticity in isolation would find the original Q12 document without the marketing-overlay confusing the elasticity-only narrative.

I noted the pattern as a one-off design choice and moved on. The choice felt unusual but worked for this specific case.

## The second fire: Q17 lane oil on multiple prior systems

A few weeks later, I was working on the lane-oil-pattern simulation subsystem design. The lane-oil subsystem (Q17) needed to interact with the pricing subsystem (Q12; oil-pattern-quality affects per-customer satisfaction which affects what they will pay), the environment-entropy subsystem (Q14; oil patterns degrade over time analogously to other equipment wear), and the citizen-substrate subsystem (Q11; per-customer ball-reaction sensitivity varies by citizen attributes).

The lane-oil subsystem's architectural reach extended across three prior locked subsystems. Following the convention I had unintentionally adopted at Q13, I created composition-layer sections in Q17's document describing each of the three couplings explicitly. Q17 had a Q17-on-Q12 composition section; a Q17-on-Q14 composition section; a Q17-on-Q11 composition section. None of the three prior documents was edited.

The result was Q17's document carrying substantially more composition-layer content than Q13's had. Three composition sections instead of one. The pattern that had felt unusual at Q13 felt structurally important at Q17: the three sections kept the multi-system coupling tractable because each coupling was named, scoped, and owned by Q17 explicitly. Reading Q17 produced a complete account of how lane-oil interacted with the broader system; reading any of the three prior documents produced its original scope without lane-oil coupling polluting the original scope.

I noted the pattern as a recurring choice and continued.

## The third fire: Q5 cross-system architectural correctness

The next architectural-lock cycle was about a broader architectural-correctness question (Q5, which addressed how the various subsystems' interfaces interacted at the system level). Q5's scope was inherently cross-system: it had to address every prior subsystem's interface and how the cross-subsystem composition produced or failed to produce architectural coherence.

Q5's design document developed composition-layer sections for every prior subsystem decision: Q1, Q2, Q3, Q9, Q11, Q12, Q13, Q14, Q17. Nine composition sections in one document. The composition layer became substantial portion of Q5's content; the prior subsystems' documents stayed textually unchanged.

This was the fire that confirmed the pattern was generalizable. Three documents (Q13, Q17, Q5) had now used the same composition-over-modification approach for cross-system coupling, with the composition-layer scope growing as the system's overall complexity grew. The pattern's mechanism scaled to nine couplings in a single document without producing the unmanageable complexity that direct modification of nine prior documents would have produced. The prior documents' immutability was load-bearing for the architectural arc's overall coherence: nine documents holding their original shapes while one new document accumulated the cross-coupling responsibilities was tractable in a way that nine documents each accumulating their share of new coupling content would not have been.

## The fourth fire: Q19 card-layer integration

The fourth fire was a Q19 cycle on card-layer integration: the architectural design for how event cards, decision cards, and similar player-facing decision surfaces would compose against the underlying subsystems. Q19 had to interact with the soul-axis system (Q1), the marketing system (Q13), the event-trigger mechanism (across multiple prior systems), and the citizen-substrate (Q11).

Q19's design document used the composition-layer pattern across four prior decisions. By the time Q19 closed, the pattern was empirically validated at n=4 cumulative fires (Q13, Q17, Q5, Q19) across approximately one month of architectural-lock work. The cumulative validation was the empirical evidence that the pattern was reproducible across architectural-lock cycles with different specific scopes and different specific coupling requirements.

The pattern's structural properties that made it work at n=4:

The prior documents' immutability preserved the documents as canonical reference for the original scope they addressed. Anyone reading Q14 understood environment entropy at the original scope; the document had not been silently amended with content addressing later coupling questions.

The composition-layer ownership at the newer document made the coupling responsibility explicit. The reader who wanted to understand how Q19 interacted with Q1 read Q19; the Q1 document did not have a maintenance burden for Q19's downstream coupling.

The cumulative cross-system composition stayed tractable because each newer document's composition layer was scoped to that document's specific coupling needs. Q19 did not need to address Q5's couplings; Q5 had its own document. The composition layers stacked without merging into a single unmanageable cross-system specification.

The pattern's git-history representation was clean. Each architectural-lock cycle produced new content at a new document; old documents stayed at their committed state. Git blame across the architectural arc produced clean attribution: who decided what, when, and at what document. The audit trail was the diff-history of the new documents, not the merge-confusion of edits to multiple older documents.

## Why this works for multi-system games

The composition-over-modification pattern has structural advantages specifically for multi-system game architecture. Several specific properties make the pattern fit the project class.

Multi-system games have cross-system coupling as a structural property of the project class. Economy interacts with customer behavior interacts with equipment interacts with marketing interacts with event mechanics; the coupling is inherent to what makes the games multi-system in the first place. The composition-layer pattern accepts the coupling as primary rather than treating it as an exception. The composition layer is the canonical home for cross-system coupling; every newer system's document has the structural slot for composition-layer content.

Multi-system games are built incrementally. Each subsystem's design is locked separately because the project schedule cannot lock all subsystems simultaneously. The locked subsystems are stable input to the next subsystem's design; the next subsystem's design has to compose against those locks. The composition-layer pattern makes the compose-against-locks operation explicit at the newer side rather than implicit at the older side. The older side stays stable; the newer side acknowledges what it composes against.

Multi-system games have long iteration cycles at the architectural level. Once a subsystem's architecture is locked, the lock holds for many implementation cycles; the lock should not be edited lightly because edits propagate into already-shipped implementation code. The composition-layer pattern protects the lock by routing new coupling content to the newer document; the older document's lock holds across architectural-cycle volume.

Multi-system games benefit from canonical-reference stability. The design document for any subsystem is the canonical reference that the implementation code commits to; the document's stability across cycles is what lets the implementation work without constantly re-checking which version of the document is current. The composition-layer pattern preserves canonical-reference stability at the older documents while letting the newer documents capture the necessary coupling content.

The pattern's fit for multi-system games is structural, not stylistic. The properties that make multi-system games structurally different from other software systems (cross-system coupling as primary; incremental architectural lock; long iteration cycles at architectural level; canonical-reference stability requirement) are the properties that make the composition-over-modification pattern fit.

## Where the pattern would not work

The pattern has specific scopes where it works and other scopes where it would not. The genre-specificity claim from Post 65 has analogs here.

The pattern would not work for projects with frequent architectural-lock revision. If the prior subsystems' designs need to change frequently as the project evolves, treating them as immutable is wrong; the prior documents should be edited when the prior decisions actually change. The composition-layer pattern assumes the prior decisions are stable across cycles; for projects where they are not, the pattern produces composition layers that drift from the actual prior-decision behavior.

The pattern would not work for projects with a single canonical state document. Some projects organize their architectural state in one comprehensive document; for those projects, the composition layer would just be another section in the same document and the immutability claim would not apply. The pattern requires per-decision documents that can stay independently immutable.

The pattern would not work for projects without explicit architectural-lock discipline. The discipline that locks each subsystem's decision is what makes immutability viable; projects that lock decisions implicitly or that allow re-litigation at any time do not have the structural ground for the composition pattern to operate.

The pattern would not work for projects whose multi-system coupling is incidental rather than primary. Some games have systems that are largely independent; the cross-system coupling is occasional and limited. For those projects, the composition layer would be substantially empty most of the time, and the standard direct-edit pattern would work fine.

The pattern fits multi-system games with locked architectural decisions, per-decision documentation, and cross-system coupling as a primary architectural concern. The bowling-alley tycoon sim has all three properties; the pattern produces clean architectural output across the May 2026 lock arc.

## What I'm not claiming

- I'm not claiming this pattern is novel. Composition-over-modification has analogs in many software-engineering contexts (Open/Closed Principle in OOP; immutable data structures with functional composition; layered architecture patterns; many specific framework designs). What this post adds is the multi-system-game architectural-design application and the n=4 empirical reproduction documenting that the pattern produces tractable cross-system coupling at the architectural-decision document level specifically.

- I'm not claiming the four-fire empirical validation generalizes to all multi-system game projects. The empirical record is the bowling-alley tycoon sim's specific architectural-lock arc; other projects with similar properties may produce similar validation; other projects with different properties may produce different results. The pattern's broader generalization is an empirical extension worth watching as other operators apply the pattern to their projects.

- I'm not claiming the composition-layer immutability eliminates all need to ever edit prior documents. Real architectural revision happens; when it does, the prior document needs to be edited. The pattern's claim is that incremental coupling additions do not require prior-document edits; substantive revisions to prior decisions still do. The two operations are distinguishable and the pattern is for the first not the second.

- I'm not claiming the pattern produces optimal design-document structure across every reader concern. Readers who want to understand multi-system coupling holistically (the cross-system overview) face a documentation challenge under this pattern because the couplings are distributed across multiple newer-decision documents. Reading any one document gives that decision's full account; reading the holistic cross-system view requires composition across multiple documents. The trade-off is real; the pattern privileges per-decision document clarity over holistic-overview synthesis.

- I'm not claiming the four-cycle architectural lock arc the empirical record comes from is itself a reproducible methodology. The arc was a specific intensive that the project's scheduling supported; other projects with different scheduling may produce different architectural-cycle structures. The pattern is for the architectural-decision documentation; the broader architectural-lock methodology that produced the documents in this case is a separate question covered partially in Post 41 and Post 49.

## What I am claiming

For multi-system games with per-decision architectural documentation and incrementally-locked subsystems, the composition-over-modification pattern (newer architectural decisions own their composition layer against prior decisions; prior decision documents stay textually immutable across coupling additions) produces tractable cross-system coupling that scales as the system's complexity grows.

The pattern's structural advantages for multi-system game architecture are specific: cross-system coupling is treated as primary rather than as exception; incremental architectural lock is preserved without re-litigation of prior decisions; long architectural iteration cycles are supported because canonical-reference stability holds at older documents; git-history attribution stays clean because edits route to new documents rather than to multiple older documents.

The empirical record this post stands on is n=4 cumulative reproduction across four architectural-lock cycles in May 2026 (a marketing-subsystem cycle, a lane-oil-pattern cycle, a cross-system architectural-correctness cycle, and a card-layer integration cycle). The pattern produced clean composition layers ranging from one cross-coupling section to nine cross-coupling sections in a single document; the prior documents stayed immutable across all four cycles' cross-coupling additions; the cumulative architectural arc remained tractable across the four cycles' complexity growth.

The pattern fits multi-system games specifically because the structural properties that make multi-system games different from other software classes (cross-system coupling as primary; per-decision documentation; long architectural iteration cycles; canonical-reference stability requirement) align with the structural properties the composition-over-modification pattern requires. Projects with different structural properties (single canonical document; frequent architectural revision; coupling as exception rather than primary concern) would not benefit from the pattern.

For game architects working on multi-system designs with per-decision documentation, the pattern is one specific operational practice worth considering as the architectural arc accumulates more locked subsystems and the cross-system coupling burden grows. The cost of applying the pattern is the explicit composition-layer ownership at each newer decision; the benefit is the prior decisions' canonical-reference stability and the architectural arc's git-history clarity. The trade-off pencils out for projects whose subsystem count is large enough that direct-edit coupling would produce significant maintenance burden at the older documents.
