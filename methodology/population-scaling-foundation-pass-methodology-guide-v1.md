# Population-Scaling Foundation Pass Methodology Guide v1

**Filed:** 2026-07-04 late afternoon per Council #6 close ratification
**Purpose:** Operational methodology guide for the population-scaling-foundation pass ratified at Council #6 close 2026-07-04 as prerequisite to Memory Lanes V1 BUILD resumption. Documents the pass's scope + scale harness design + mitigation primitives + observability requirements + iteration criteria + close conditions.
**Council #6 context:** Rule 14 Pattern B ADOPT-FOLD via Option B per-item deliberation at 4-of-4 substrate NO-GO convergence on framework foundational readiness go/no-go question. Ratified fold-set covers 3 foundational gaps requiring pre-V1 resolution.

## Pass scope

Three foundational gaps ratified as pre-V1 blockers. This pass addresses all three:

**Gap 1: Population-scaling foundation.** Framework's empirical validation is at 2-Sim sandbox scope; Memory Lanes V1 design targets 500-concurrent Sims; realistic V1-post-pause population may be 1000 to 5000-plus NPCs. Scaling arithmetic from 2 to 5000+ is open.

**Gap 2: Room to Life Universe persistence contract implementation.** Architecture ratified 2026-06-09 but implementation deferred. Cross-product entity persistence is architectural, not aspirational; canonical entity ID plus schema versioning plus generated-biography provenance plus migration harness plus contract tests must exist before Memory Lanes V1 mints canonical NPCs.

**Gap 3: Scale observability and session logger emission wiring.** consolidation_boundary plus audit_run plus branch_factor_selection helpers exist but not yet called from tick loop. Population-scale simulation requires empirical adjudication substrate; without observability, cannot distinguish emergence from silent artifact.

Estimated cumulative scope: 3-6 weeks focused Phase 2.x per substrate concordance across the three gaps.

## Phase A: session logger emission wiring (weeks 1-2)

Complete Phase 2.x-7 continuation queue item. Emission tags wired to high-performance non-blocking logging bus (ring buffers pushing to separate thread). Tick-cadence rules for when consolidation_boundary is legally reached mathematically defined and locked into test suite.

Deliverables:
- consolidation_boundary emission wired to tick loop (fires at yearly consolidation cadence per a7Memory tick integration or at appropriate proxy trigger like day-change until a7Memory integration lands)
- audit_run emission wired to tick loop or audit-invocation trigger
- branch_factor_selection emission wired to per-decision cadence in inferenceLoop
- Bounded log taxonomy defined + documented
- Sampling/aggregation rules for high-frequency events specified
- Deterministic replay guaranteed for fixed seed
- Audit-boundary snapshots captured at consolidation boundaries
- Developer queries: "why did this population-level pattern appear" — trace path from population-level observation to source events
- Log retention policy scale-safe at 500/1000/5000 NPC scope

Verification: session logger emits at 2-Sim sandbox test scope; population-scale emission verified in Phase B.

## Phase B: population-scale harness (weeks 2-4)

Build progressive-scale test harness: 50 NPC → 500 NPC → 1000 NPC → 5000 NPC runs. Each scale tier measures observable properties + failure-budget breach conditions.

Measurements per scale tier:
- **Tick cost:** wall-clock milliseconds per simulation tick at target framerate constraint
- **Memory cost:** heap allocation + resident memory growth per NPC
- **Consolidation cost:** wall-clock milliseconds spent at consolidation boundary per NPC per year
- **Event volume:** landmark events + pair-history events + memory-encoding events per tick per NPC
- **Sentiment graph density:** ordered-pair sentiment scalar count vs sparse-vs-dense representation cost
- **Replay validity:** deterministic replay match at bit level for fixed seed
- **Branch-factor distributions:** branch_factor_selection statistics per DecisionContext across NPC population
- **Long-run degradation:** measurements over representative Memory Lanes gameplay durations (multi-year game time)

Failure-budget definitions per tier (adopted per ChatGPT 5.5 substrate contribution at Council #6):
- **500 NPCs:** acceptable degraded behavior TBD; hard tick-time ceiling TBD
- **1000 NPCs:** acceptable degraded behavior TBD; hard tick-time ceiling TBD
- **5000 NPCs:** acceptable degraded behavior TBD; hard tick-time ceiling TBD

Failure-budget definitions ratified at pass execution time per operator judgment on target hardware plus V1 performance envelope.

Mitigation primitives to implement iteratively as scale-tier measurements demand:
- **Spatial partitioning:** quadtrees or octrees for co-witness attention culling (per Gemini substrate contribution at Council #6). Limit landmark ripple propagation to spatially-proximate NPCs rather than global broadcast.
- **Priority queue on concurrent EFE re-evaluations:** hard algorithmic cap per tick. If 100 NPCs witness a landmark, prioritize N-most-proximate or N-most-neurotic (Layer 3 Emotionality/Anxiety) for immediate processing; queue remainder over subsequent frames.
- **Sparse vs dense pair-relational state representation:** determine at scale-tier measurement whether sparse (per-relationship stored only when non-zero) or dense (per-pair pre-allocated) matrix is more memory-efficient at target population density.
- **Agent LOD (level-of-detail):** off-screen NPCs may simulate at reduced tick cadence or reduced layer complexity to save compute.
- **Batched consolidation:** stagger consolidation boundaries across NPCs to avoid synchronization spikes.

Verification: each mitigation primitive validated at scale-tier measurement level (does it close the arithmetic gap?).

## Phase C: Room to Life Universe minimum canonical registry contract (weeks 3-5)

Implement minimum contract required for Memory Lanes V1 to mint canonical NPCs. Contract components:

- **Canonical entity ID:** UUID-strategy + collision-avoidance + product-scope disambiguation
- **Schema versioning:** version field + migration rules + backward-compatibility contract
- **Generated-biography provenance:** which system generated each biographical field + when + under what circumstance schema (Scene circumstance context)
- **Immutable-vs-mutable field discipline:** which fields are frozen at creation + which fields can mutate at runtime + which can be updated at migration
- **Product-scoped projections:** how does Memory Lanes read/write vs Rooms read/write vs 90s Life Builder read/write against the shared canonical registry
- **Migration harness:** version-N-to-version-N+1 migration path with round-trip test coverage
- **Contract tests:** round-trip a character through Memory Lanes plus stub Rooms projection; verify canonical state preserved across products
- **Asynchronous handoff queue design:** JSON or binary serialization payloads for Layer 4 memory matrices sent to canonical registry without blocking main simulation thread
- **Stress test:** local-to-canonical state synchronization under extreme concurrency (500 actors saving state simultaneously per Gemini substrate contribution at Council #6)

Verification: contract tests pass at 500-NPC concurrency without deadlock or race condition.

## Phase D: iteration (weeks 4-6)

Iterate Phase B scale-harness measurements + Phase C canonical registry stress-tests until scaling arithmetic is closed at 5000-NPC scope OR explicitly mitigated with documented performance envelope trade-offs.

Iteration convergence criteria:
- All measurements within tier-defined failure budgets at 500-NPC scope
- All measurements within tier-defined failure budgets at 1000-NPC scope (may require mitigation primitive activation)
- All measurements within tier-defined failure budgets at 5000-NPC scope (may require multiple mitigation primitives)
- Canonical registry contract tests pass at 500-NPC concurrency
- Deterministic replay validated at 500-NPC scope over multi-year game time durations

Iteration divergence conditions (trigger architectural revision):
- Population-emergence collapse into low-variety attractors at 500-NPC scope (per Grok + ChatGPT 5.5 dominant-risk framings)
- Compute cost exceeds target hardware envelope by factor >10x at 100-NPC scope (per Grok Paranoid Stoner premortem)
- Canonical registry serialization schemas fundamentally incompatible with tick-loop memory pool structures (per Gemini architectural risk)
- Sentiment homogenization or routine synchronization patterns emerge at population scope invalidating small-n validated hypotheses (per Grok Paranoid Stoner premortem)

If divergence conditions trigger, architectural revision returns to Council methodology for adjudication.

## Close conditions

Pass close conditions ratified at Council #6:

1. All 4-of-4 substrate-concordant scale-tier measurements produced at 500 + 1000 + 5000 NPC scope
2. Failure-budget definitions ratified per tier at operator judgment
3. Room to Life Universe minimum canonical registry contract implemented + contract tests passing
4. Session logger emission wiring complete + deterministic replay validated at population scope
5. Scaling arithmetic closed or explicitly mitigated with documented performance envelope

Pass close triggers next-work-session decision:
- **If scaling arithmetic closed cleanly:** framework's Council #6 NO-GO verdict reverses to GO for Memory Lanes V1 BUILD resumption
- **If scaling arithmetic mitigated with trade-offs:** operator ratifies whether trade-offs meet Memory Lanes V1 product envelope; if yes, GO for BUILD resumption; if no, further Council methodology adjudication warranted
- **If scaling arithmetic intractable at target population scope:** architectural revision required; new Council #7+ deployment on architecture revision candidate

## Cross-references

- Council #6 close narrative: `~/Projects/the-street-code/posts/0147-*.md`
- Council #6 spec: `~/Projects/the-street-code/posts/0148-*.md`
- Council #6 close memory: `~/.claude/projects/-Users-jimmy/memory/project_council_6_close_pattern_b_2026-07-04.md`
- Phase 2.x continuation queue: `~/.claude/projects/-Users-jimmy/memory/project_sim_ai_phase_2_continuation_queue_2026-07-03.md`
- Post 0119 audit-first sequencing (architectural commitment underlying the pass): `~/Projects/the-street-code/posts/0119-*.md`
- Post 0132 branch-factor discipline (integrated in current inferenceLoop): `~/Projects/the-street-code/posts/0132-*.md`
- Post 0136 empirical BUILD-mode-as-hypothesis discipline (foundational to the scale harness design): `~/Projects/the-street-code/posts/0136-*.md`
- Post 0142 Council #5 Decision 3 (instrumentation requirement propagation to Open Alley scope): `~/Projects/the-street-code/posts/0142-*.md`
- Room to Life Universe architecture: memory `project_room_to_life_universe_architecture_2026-06-09.md`
