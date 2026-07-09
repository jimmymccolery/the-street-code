---
name: A2 Phase C extension status — event-scope canonical registry candidacy DEFERRED to Phase 8.x post-V1
scope: Cluster A2 population-scaling foundation Phase C — extension candidacy analysis for 6 newly-wired event categories
filed: 2026-07-09 late
supersedes: none (net-new status artifact — Phase C minimum shipped 2026-07-04 remains canonical)
disclosure: Section 6 UNVERIFIED convention applies — see §6 below
---

# A2 Phase C extension status — event-scope canonical registry candidacy DEFERRED

## 1. Purpose

This artifact documents the framework's judgment on whether Phase C of the Council-#6-ratified population-scaling-foundation-pass methodology requires an **extension** to accommodate the 6 event categories newly-wired at Phase A close-out earlier this session:

- **Stage 3:** first_encounter, attractiveness_assessed, charisma_perceived
- **Stage 4:** demand_withdraw_pattern
- **Stage 5:** capital_conversion, habitus_field_mismatch_detected

The framework's conclusion after research and analysis: **NO Phase C extension is warranted at V1 scope. Filing a Council #9 candidacy item for post-V1 event-registry scoping instead.**

## 2. Prior Phase C state (canonical)

Phase C minimum canonical registry contract SHIPPED 2026-07-04 per Post 0151 at `~/Projects/sim-ai/src/ecosystem-registry/canonicalRegistry.ts` v0.1.0-phase-c-minimum-contract. Delivered:

- Canonical entity ID (UUID + product-scope disambiguation)
- Schema versioning + migration rules
- Generated-biography provenance (which system + when + which schema)
- Immutable-vs-mutable field discipline (HEXACO + attachment + cultural baseline + birth year = immutable; lifeline = mutable)
- Product-scoped projections (Memory Lanes / Rooms / 90s Life Builder / The Living Room)
- Migration harness
- Contract tests (round-trip through Memory Lanes + stub Rooms)

Phase C extensions ALSO shipped 2026-07-04:
- Marcus Reed Surface 8 audit scaffold (`marcusReedAuditScaffold.ts`)
- Cross-product entity tracking (`crossProductEntityTracking.ts`)
- Lifeline generator (`lifelineGenerator.ts` v0.2.0-post0189-bundle-aware)
- Sim AI binding (`simAiBinding.ts`)

## 3. The question — does Phase C need an event-scope extension?

Given that:
1. Phase A closed the composition-scope wiring gap for 6 previously-unwired event categories (this session earlier)
2. Phase B validated operational-equivalence at all 4 Council-#6-ratified tiers with all 6 newly-wired emits firing correctly (this session earlier)
3. The 12 emit categories exist as observability telemetry via `crossPlaneTraceAggregator.ts` — separate from canonical entity biography

Does the registry need to be extended so events cross product boundaries + are canonical-registered?

## 4. Framework judgment — NO extension warranted at V1

### 4.1 The registry is entity-scoped, not event-scoped

The Phase C minimum contract at `canonicalRegistry.ts:64-69` establishes InnateProperties (immutable HEXACO + attachment + cultural baseline + birth year) + Lifeline (mutable biography via BiographyField provenance). This is **entity-scoped canonical persistence**. The 12 event categories are cognitive-architecture observability telemetry (via ring-buffered `CrossPlaneEventLog`), fundamentally different from entity biography.

### 4.2 Non-Inertness Gate check (Item 132)

The Non-Inertness Gate 4-question check (per `a2-non-inertness-gate-planning-2026-07-09.md`):

1. **Does building event-scope registry extension alter any state, output, or downstream consumer at V1?** NO — no V1 consumer needs cross-product event synchronization; Memory Lanes NPCs stay in the Memory Lanes Scene at V1. Room to Life memory 2026-06-09: "cross-product migration is deferred to Phase 8.x post-V1 by default; V1 keeps entities in their assigned Scene."
2. **Is there a test that would fail if event-scope registry extension reverted?** NO — no test currently references cross-product event synchronization.
3. **Is there a downstream consumer that will read/act on event registry?** NO at V1 — Marcus Reed Surface 8 audit operates on realized lifelines (entity distribution + trait extremity), not event flows; already-shipped Phase C extensions cover Surface 8 scope.
4. **Would substrate-scope disable of the extension disable any measurable effect at V1?** NO — event emits at composition scope + observability via ring-buffered log both remain intact; canonical registry doesn't need to know about them.

**Gate FAILED for building extension at V1** — all 4 questions answered NO. Building event-scope canonical registry extension at V1 would be classic accretion pattern (per Round 5 Opus diagnosis) — mechanically producible but empirically inert.

### 4.3 Cross-product-vs-product-scoped analysis for the 6 events

If future operator ratification opens cross-product event synchronization, this taxonomy would apply:

| Event | Cross-product candidacy | Rationale |
|---|---|---|
| first_encounter | LOW | Scene-local perception snapshot; both parties must be co-present |
| attractiveness_assessed | LOW | Perceiver-local judgment; not identity-attached |
| charisma_perceived | LOW | Same as above |
| demand_withdraw_pattern | MEDIUM | Attachment-behavioral marker; could be lifeline-significant if pattern persists across contexts |
| capital_conversion | MEDIUM-HIGH | Bourdieu capital forms (cultural/social/symbolic) ARE identity markers that would matter across products (a sim's embodied cultural capital acquired in Memory Lanes IS the same sim's cultural capital in Rooms) |
| habitus_field_mismatch_detected | MEDIUM | Habitus-field tension IS identity-relevant; may or may not matter cross-product depending on Room to Life 3-layer architecture read of "field position" |

**None of these are V1-blocking.** The MEDIUM/HIGH cross-product candidacies (capital_conversion + habitus_field_mismatch_detected) are the specific candidates worth Phase 8.x post-V1 review.

## 5. Council #9 candidacy filing

Filed as Council #9 Item 140 candidacy (to be added to `council-9-review-agenda-draft-2026-07-05.md`):

**Item 140 candidacy — Event-scope canonical registry extension review at Phase 8.x post-V1**

**Framework body:** Framework should adjudicate at Phase 8.x post-V1 whether the 6 newly-wired event categories (first_encounter, attractiveness_assessed, charisma_perceived, demand_withdraw_pattern, capital_conversion, habitus_field_mismatch_detected) — or a subset thereof — should be canonical-registered via extension of the Phase C minimum contract, enabling cross-product synchronization.

**Empirical anchor:** Phase A (composition wiring) + Phase B (operational-equivalence at 4 tiers) are shipped. Event emits are stable + deterministic + within failure budget. Phase 8.x review benefits from empirical foundation.

**Cross-product candidacies to review:** MEDIUM/HIGH candidates (capital_conversion + habitus_field_mismatch_detected). LOW candidates (Stage 3 perception events + demand_withdraw_pattern) likely stay observability-only.

**Trigger condition for Council review:** Cross-product migration surfaces V1-post ship (per Room to Life memory 2026-06-09).

## 6. UNVERIFIED disclosure (per section-6-unverified-disclosure-convention-2026-07-09.md)

Claims investigated but not confirmed to primary-source full-text verification standard at authoring:

1. **Room to Life 3-layer architecture rationale for cross-product deferral**
   - Attempted verification: `project_room_to_life_universe_architecture_2026-06-09.md` memory
   - Verification outcome: memory-scope reference (not re-verified at authoring time)
   - Downstream constraint: this artifact does NOT invent cross-product deferral policy — it references the prior memory decision. Council #9 Item 140 candidacy would re-examine.
2. **Post 0151 documenting Phase C minimum + extensions shipped 2026-07-04**
   - Attempted verification: research report referenced Post 0151 without re-fetch at this artifact's authoring
   - Verification outcome: not re-verified
   - Downstream constraint: Council #6 close artifact + `canonicalRegistry.ts:1-22` header both confirm Phase C minimum ship + version tag; Post 0151 reference is corroborative not load-bearing.
3. **Bourdieu capital forms cross-product identity claim**
   - Attempted verification: framework-scope Wacquant + Bourdieu citations at sim-ai substrate scope
   - Verification outcome: framework-canonical citations exist at habitusPlane.ts substrate; not re-fetched at this artifact's authoring
   - Downstream constraint: §4.3 MEDIUM-HIGH cross-product candidacy assessment for capital_conversion is deferred to Phase 8.x Council #9 review; this artifact does not load-bear it.

Downstream consumers: none of these 3 claims are load-bearing in code or verdict. This artifact's load-bearing claim is only that Phase C minimum is shipped + event-scope registry extension is NOT V1-blocking.

## 7. What Phase C extension status does NOT foreclose

- **Phase 8.x post-V1 review** — Council #9 Item 140 candidacy explicitly preserves the extension question for later. If Phase 8.x brings cross-product migration into V1+ scope, event-scope registry extension may become relevant.
- **Ad-hoc event export** — nothing in this artifact prevents Memory Lanes from exporting specific event streams for analytical purposes (e.g., debug logs, replay verification, session snapshots). Ad-hoc export is separate from canonical-registry-integration.
- **Ring-buffer event log at scale** — Phase B validated composition-engaged path at 4 tiers with full 11-of-12 event categories firing. Post 0190 amortized-O(1) eviction discipline preserves the log at long horizons. None of this changes.

## 8. Cross-references

- Council #6 close artifact: Decision 2 Room to Life Universe persistence contract RATIFIED FOUNDATIONAL at 3-of-4 substrate convergence
- Population-scaling foundation methodology guide: `~/Projects/the-street-code/methodology/population-scaling-foundation-pass-methodology-guide-v1.md`
- A2 Phase A close-out: `~/Projects/the-street-code/methodology/a2-phase-a-close-out-2026-07-09.md`
- A2 Phase B close-out: `~/Projects/the-street-code/methodology/a2-phase-b-close-out-2026-07-09.md`
- A2 Non-Inertness Gate planning: `~/Projects/the-street-code/methodology/a2-non-inertness-gate-planning-2026-07-09.md`
- Section 6 UNVERIFIED convention: `~/Projects/the-street-code/methodology/section-6-unverified-disclosure-convention-2026-07-09.md`
- Council #9 candidacy Item 140 (Event-scope canonical registry Phase 8.x review) — filed by this artifact
- Council #9 candidacy Item 132 (Non-Inertness Gate) — empirical foundation applied here
- Room to Life Universe architecture memory: `~/.claude/projects/-Users-jimmy/memory/project_room_to_life_universe_architecture_2026-06-09.md`
- Canonical registry: `~/Projects/sim-ai/src/ecosystem-registry/canonicalRegistry.ts` v0.1.0-phase-c-minimum-contract
- Post 0197 empirical-validation-harness-parallel-to-diagnostic-UI discipline — this Phase C status is recursive re-application at "research-revealed-no-fold" scope

## 9. Status

**Phase C extension for event-scope canonical registry: DEFERRED to Phase 8.x post-V1 review via Council #9 Item 140 candidacy.**

Phase C minimum contract (shipped 2026-07-04) remains canonical. Phase A + Phase B extensions (this session) validated composition-scope observability at Cluster A2 scope. Cluster A2 close-out proceeds without Phase C extension work.

Framework operator confirmation would reverse this deferral IF (a) V1 scope changes to include cross-product event synchronization OR (b) Phase 8.x review at Council #9 Item 140 ratifies event-scope registry extension as V1+ scope.
