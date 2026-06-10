# Drafting brief — Post 97 "Multi-Graph Memory Without the Research-System Overhead"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 97 within Posts 96-98 hybrid-path block. Per R5 design: MAGMA justifies separating semantic, temporal, causal, and entity views; V1 implements typed indexes + pair summaries rather than full research-system overhead.
**Scope verdict:** SAFE — methodology + MAGMA + commercial-precedent META-level discussion. No protected scope.
**Length target:** 3000-4500 words.

## Thesis

MAGMA (arXiv:2601.03236; 2026 research paper on multi-graph agent memory architectures) provides the conceptual justification for separating procedural-character memory into multiple typed views: semantic memory (what concepts mean), temporal memory (sequence of events), causal memory (why-it-happened links), and entity memory (who-was-involved relationships). The research-system overhead of fully separate graph databases per view is unaffordable for indie-budget V1. Modified-C-bis adopts the MAGMA TYPING DECOMPOSITION as architectural guidance while implementing the actual storage as TYPED INDEXES over the three-layer memory architecture (Layer 1 raw + Layer 2 encoded + Layer 3 accumulator) + PAIR SUMMARIES at consolidation boundaries. Post 97 explains the MAGMA grounding + the V1 typed-index implementation that captures MAGMA's separability benefits without MAGMA's storage overhead.

## Sections (outline)

1. **Hook:** "Modified-C-bis has a multi-decade memory architecture. Pure-relational tables wouldn't scale. Multiple separate graph databases would over-engineer it. MAGMA shows the in-between."

2. **What MAGMA contributes.** Brief recap of the MAGMA paper (arXiv:2601.03236):
   - Procedural agents need different RETRIEVAL patterns from memory
   - Semantic retrieval: "what does X mean to this character?"
   - Temporal retrieval: "what happened with X recently?"
   - Causal retrieval: "why did X do Y last time?"
   - Entity retrieval: "what's the relationship state between A and B?"
   - One uniformly-typed memory store can't serve all four efficiently
   - MAGMA proposes separated graph databases per view; benchmarks show retrieval speedups

3. **Why direct MAGMA adoption doesn't fit V1.**
   - Multiple graph DBs = multiple persistence engines = save-file complexity
   - V1 ships on iOS with hard save-file constraints (5MB iCloud baseline; user expectations of save-time < 2s)
   - Indie operator can't maintain N separate database engines at production quality
   - MAGMA is a research artifact; production indie game needs simpler implementation

4. **The typed-index adaptation Modified-C-bis adopts.**
   - Single underlying memory store (the three-layer architecture)
   - TYPED INDEXES over the store, one per MAGMA-style view:
     - **Semantic index:** trait-based concept tags ("polite," "regular," "high-tipper"); lookup by tag
     - **Temporal index:** game-time ordered; lookup by recency window or game-year
     - **Causal index:** event-to-event links via outcome-modifier tags ("because-of-X-then-Y" pointers)
     - **Entity index:** pair-relationship-keyed; lookup by ordered-pair (A, B)
   - Each index points back to the same underlying memory entries
   - Adding an event updates all four indexes atomically; the multi-view retrieval pattern works
   - Storage cost: O(N events × ~80 bytes pointer overhead per event) — affordable

5. **Pair summaries at consolidation boundaries.**
   - At yearly consolidation pass (per Post 93), entity-index entries that have accumulated > N events get summarized into pair-summary entries
   - Pair summary = compressed representation of accumulated pair history; bounded size; deterministic compression algorithm
   - Original events still in memory store; pair summary is the FAST-RETRIEVAL form for runtime use
   - Sims 4 Sentiments + RimWorld opinions are the commercial precedent for this pair-summary-as-runtime-access pattern (per Post 91)

6. **Walk through a retrieval scenario.** Pinboy needs to decide whether to be deferential to incoming bowler A:
   - Entity-index lookup: get (A, pinboy) pair summary in O(1)
   - Pair summary returns: accumulated sentiment scalar + last-3-events tagged + trait-relevant flags
   - Sentiment scalar + traits feed into active-inference decision-scoring (per Post 94 audit-vs-runtime sequencing)
   - Pinboy decision rendered without touching the bulk memory store
   - Compare to: naive retrieve-all-events-then-decide = O(N) per decision = breaks per-frame budget

7. **What the typed-index adaptation gives up.**
   - Doesn't get MAGMA's full retrieval benchmark performance (separated DBs would be faster at deep semantic queries)
   - Doesn't support complex graph-traversal queries (e.g., "find all events causally downstream of event X across all entities") — would require backing store schema additions
   - Trade-off accepted: V1 doesn't need those queries; future Steam V1.0 might revisit

8. **V1 implementation cost.** Schema-level work: 4 typed indexes + pair-summary structure + consolidation-pass write-through. ~24-40 hours BUILD-side estimated.

9. **Honest scope: where this diverges from MAGMA's research direction.**
   - MAGMA scopes to research-system architecture; Modified-C-bis adapts for indie game
   - MAGMA likely will improve further in subsequent research; framework adopts current MAGMA at point-of-V1-ship; future improvements are post-V1 enrichment
   - Modified-C-bis is a research-application case study, not a research contribution to memory-architecture literature

10. **Closing.** "MAGMA showed me what separating views buys you. The typed-index adaptation gets most of the benefit at indie-budget cost."

## Key citations

- **MAGMA (Multi-Graph Agent Memory Architecture):** arXiv:2601.03236 (2026). [Note: R5 surfaced this citation; R2 should primary-text-verify when reading the paper directly. Mark as `[PRIMARY-TEXT-PENDING — R2 verify]` until verified.]
- **Sims 4 Sentiments commercial precedent** (cross-referenced from Post 91).
- **Park 2023 Generative Agents** (cross-referenced from Post 96).

## Cross-links

- LINKS BACK TO: Post 91 (sentiment override + pair-specific memory; pair summaries are the MAGMA-entity-view adaptation) + Post 93 (consolidation pass triggers pair summary writes)
- LINKS FORWARD TO: Post 98 (cached policies + slow consolidation; multi-graph memory supports the cached-policy lookup pattern)
- IMPLEMENTATION TIE: Round 9 Q3 belief-update + Q4 EFE decomposition reference typed-index retrieval pattern

## Drafting prerequisites

- MAGMA arXiv:2601.03236 primary-text full read (~3-4h; R2 should also verify the citation for the framework).
- Operator-side typed-index schema sketch (~2h technical exercise).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision + MAGMA verification + schema sketch. Target 3000-4500 words.
