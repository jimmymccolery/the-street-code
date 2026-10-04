# Phase 3.8.1 Ship 2 — M9 K≥3 Activation Cascade — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

6-site activation cascade for M9 socialIdentityFactionDynamics at K≥3 per Phase 3.8.1 v.next unlock. Activates 4 never-called active-mutation helpers + 3 read-only helpers previously inert at 2-Sim mode.

## §2 6-Site Activation Cascade

- **Site A (detectFactionFormationTrigger):** K≥3 gate; fires when goal misalignment ≥ SHERIF.RESOURCE_CONFLICT_HOSTILITY_THRESHOLD (0.4)
- **Site B (formCoalitionGroupFromBoehm):** F2 wire — EXPOSED for Ship 3 consumption
- **Site C (applyGossipIntergroupDrift):** F4 wire — EXPOSED for Ship 4 consumption
- **Site D (computeIngroupSociometerLift):** M1 composition active — direct write to self_esteem_b
- **Site E (computeIngroupRelatednessSatLift + computeOutgroupRelatednessFrustLift):** M5 composition active — direct write to relatedness sat/frust
- **Site F (applySuperordinateGoalReduction):** Sherif shared-threat wire — symmetric at both partner_death branches

`tickSocialIdentityFaction` at `islandWorld.ts:3963` no longer short-circuits at empty groups when `isNSimMode(state)` = true.

## §3 Non-Inertness Gate Verdict — 5/5 PASS @ 100%

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship2M9KGTE3Activation.test.ts` (40 tests exactly per spec)

- **H1 PRIMARY (Tajfel-Turner):** 8 tests PASS — K=2 gate + K=3 divergent goals → groups form within 500 ticks + idempotence
- **H2 PRIMARY (Brewer 1991):** 6 tests PASS — drift toward 0.5 from >0.9 + <0.1 + at-target
- **H3 PRIMARY (Sherif 1961):** 5 tests PASS — superordinate reduction ≥15pp + symmetric + K=2 no-op
- **H4 VALIDITY (Fiske 1992):** 6 tests PASS — AR/EM/MP/CS routing + K=4 ≥2 model surface + updateGroupRelationalModel
- **H5 VALIDITY (M1+M5 composition):** 7 tests PASS — ingroup SE ≥5pp + relatedness_sat/frust helpers

Plus 8 site integration tests (A/B/C/D/E/F + backward-compat K=2 zero m9_* emit).

## §4 Empirical Anchors (K=2 verified from M9 candidacy corpus)

- Tajfel-Turner 1979 Austin-Worchel Eds pp. 33-47 Brooks/Cole
- Turner 1987 Blackwell
- Sherif 1961 U Oklahoma
- Brewer 1991 PSPB 17(5):475-482
- Fiske 1992 Psych Review 99(4):689-723

## §5 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE (preserved from Phase 3.10 M9):**
- SHERIF.RESOURCE_CONFLICT_HOSTILITY_THRESHOLD = [omitted]
- BREWER.OPTIMAL_DISTINCTIVENESS_TARGET = [omitted]
- SHERIF.SUPERORDINATE_GOAL_REDUCTION_MAGNITUDE = [omitted]

**NEW CALIBRATION-CHOICE:** categorical-difference goal-misalignment v1 (identity-goal category match=0 / mismatch=1) — direction anchored to Sherif 1961 tournament-phase; boolean-projection scalar is CALIBRATION-CHOICE per spec

**REJECT-STALE:** None

## §6 Framework Methodology Firsts

- FIRST M9 6-site activation cascade wire at K≥3
- FIRST Tajfel-Turner 1979 group formation empirical validation at substrate scope
- FIRST Sherif 1961 superordinate goal reduction wire (partner_death shared threat → intergroup perceivedThreat drop)
- FIRST goal-misalignment matrix (M3 → M9 composition bridge)
- FIRST M9 CrossPlaneEvent additions (`m9_faction_formation_triggered` + `m9_superordinate_goal_reduction_applied` + `m9_ingroup_sociometer_lift`)

## §7 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/87 files
- sim-ai full test suite: **2858 PASS** (baseline 2818 → +40 Ship 2 tests across 145 test files)
- sim-ai postmortem: 2 preexisting anomalies waived (inherited from Ship 1 parent pattern)
- roomtolife precheck: vendor-sync verified

## §8 Deviations from Spec

**LOC scope 230→483 substrate** — delta absorbed by:
1. New emit helpers + count fields in crossPlaneTraceAggregator (~97 LOC)
2. Explicit per-Sim Layer 3 self_esteem_b dispatch in Sites D/E (canonical `a` → top-level, `b` → simB slot, others → sims map — required because no `applySelfEsteemDeltaBySimId` dispatch helper existed in Ship 1)
3. Symmetric Site F wire in both partner_death branches

Test file 887 LOC (spec ~40 tests → 40 tests exactly).

**Sites B and C expose-only** — underlying functions already exported from M9 module; Ship 2 does NOT invoke them from islandWorld.ts (Ship 3 F2 wire + Ship 4 F4 wire will). Test file includes visibility-gate tests (Site B + C callable) per H4/site integration section.

## §9 Council #11 Candidacy

**Item 232 filed:** Phase 3.8.1 Ship 2 M9 K≥3 activation cascade ratification.

Sub-items:
- 232.1 6-site activation cascade discipline
- 232.2 tickSocialIdentityFaction short-circuit removal at K≥3
- 232.3 Explicit per-Sim SE dispatch pattern (deferred Ship-1 helper alternative)
- 232.4 M9 CrossPlaneEvent additions (3 new event types)
- 232.5 Categorical-difference goal-misalignment CALIBRATION-CHOICE

## §10 Downstream Impact

**Enables Ship 3** (F2 Boehm coalition → M9 group spawn via `formCoalitionGroupFromBoehm`).

**Enables Ship 4** (F4 witness triangle → M9 perception drift via `applyGossipIntergroupDrift`).

Ships 3+4 can now run in parallel (both consume Ship 2 helpers; different substrate modules — no collision).

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
