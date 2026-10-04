# Phase 3.10 M9 socialIdentityFactionDynamics — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

Second Phase 2 Tier 3 mechanism (deferred from Phase 2 v1 close per 4+Sim requirement; unblocked by Phase 3.8 group substrate SCAFFOLD ratification). Ships Tajfel-Turner SIT + Turner self-categorization + Sherif Robbers Cave + Brewer optimal distinctiveness + Fiske 4 relational models substrate operationalization.

## §2 Empirical Anchors (K=2 verified via WebSearch)

- **Tajfel-Turner (1979)** In Austin-Worchel Eds. *The Social Psychology of Intergroup Relations* pp. 33-47 Brooks/Cole (canonical range; SciRP lists pp. 33-37 minor drift)
- **Turner-Hogg-Oakes-Reicher-Wetherell (1987)** *Rediscovering the Social Group: A Self-Categorization Theory* Blackwell Oxford & New York (239 pp.)
- **Sherif-Harvey-White-Hood-Sherif (1961)** *Intergroup Conflict and Cooperation: The Robbers Cave Experiment* University of Oklahoma Book Exchange (originally 1954 field study)
- **Brewer (1991)** *PSPB* 17(5):475-482 "The Social Self: On Being the Same and Different at the Same Time"
- **Fiske (1992)** *Psych Review* 99(4):689-723 "The Four Elementary Forms of Sociality"

## §3 Architecture

**Substrate module:** `~/Projects/sim-ai/src/sim-ai/scenes/island/socialIdentityFactionDynamics.ts` (828 LOC; leaner than 1000-1300 estimate due to Phase 3.8 group substrate primitive leverage)

**Type primitives:**
- `SocialIdentityGroup { id + memberSimIds + founderId + formedAtTick + cohesionLevel }`
- `GroupIdentificationScalar { simId + groupId + identificationStrength [0,1] }`
- `IntergroupPerception { fromSimId + groupId + perceivedThreat [-1,1] + perceivedStatus [-1,1] }`
- `SocialIdentityFactionState { groups + identifications + intergroupPerceptions }`

**Constants:**
- TAJFEL_TURNER.MIN_GROUP_SIZE = [omitted] (dyad + observer scaffold)
- SHERIF.RESOURCE_CONFLICT_HOSTILITY_THRESHOLD = [omitted] (Robbers Cave superordinate-goal reduction)
- BREWER.OPTIMAL_DISTINCTIVENESS_TARGET = [omitted] (halfway between total assimilation + total differentiation)
- FISKE.RELATIONAL_MODEL_DEFAULT = 'communal_sharing' (2-Sim baseline)
- SUPERORDINATE_GOAL_REDUCTION_MAGNITUDE = [omitted]
- IDENTIFICATION_DRIFT_RATE = [omitted] per tick
- TAJFEL_TURNER.H_ON_INGROUP_FAVORITISM_DAMPENING = [omitted]

## §4 Wire Sites (3 seed + 1 tick)

Additive-overlay per Phase 3.8 Path A discipline:
- `createInitial2SimWorldState` seed (empty SocialIdentityFactionState at 2-Sim spawn)
- `createInitial2SimWorldStateWithBiographies` variant seed
- `injectSimBIntoRunningSession` seed
- `tickIslandWorld` per-tick decay reducer

**Composition helpers exposed** (read-only per Council #11 Item 198 discipline; active mutation deferred to Phase 3.8.1 consumer-scope wiring at K ≥ 3):
- `spawnGroup(state, founderId, tick)`
- `formCoalitionGroupFromBoehm(state, coalition, tick)` (F2 composition hook)
- `detectFactionFormationTrigger(state)` (K ≥ 3 activation cascade)
- M1/M5/F4 composition helpers per Rule 19 EMPIRICAL-TRANSLATION discipline

## §5 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/socialIdentityFactionDynamics.test.ts` (95 tests; exceeded 75 target due to Rule 28 preservation harness + Path A additive-overlay discipline suite)

- **H1 PRIMARY (Tajfel-Turner):** 3-Sim scenario forms 2 groups within 500 ticks when misalignment ≥ Sherif 0.4 threshold — PASS (+ negative case at subthreshold)
- **H2 PRIMARY (Brewer optimal distinctiveness):** identification strength drifts toward 0.5 over 1000 ticks from above (0.9) and below (0.1) — PASS
- **H3 PRIMARY (Sherif superordinate goal reduction):** perceivedThreat reduces ≥15pp when superordinate goal introduced — PASS
- **H4 VALIDITY (Fiske 4 relational models):** 4-Sim scenario surfaces ≥2 distinct relational-model preferences — PASS
- **H5 VALIDITY (M1 sociometer relatedness):** in-group interaction → self_esteem_b lift ≥5pp; out-group → relatedness_frust lift > 0 — PASS (+ backward-compat negative case)

**Verdict:** PASS 5/5 @ 100% clear rate

## §6 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE (5):**
- SHERIF.RESOURCE_CONFLICT_HOSTILITY_THRESHOLD 0.4
- BREWER.OPTIMAL_DISTINCTIVENESS_TARGET 0.5
- SUPERORDINATE_GOAL_REDUCTION_MAGNITUDE 0.20
- IDENTIFICATION_DRIFT_RATE 0.002 per tick
- TAJFEL_TURNER.H_ON_INGROUP_FAVORITISM_DAMPENING 0.30

**EMPIRICAL-TRANSLATION (3):**
- Sherif 1961 qualitative hostility-index → substrate perceivedThreat scalar [-1,1]
- Brewer 1991 curvilinear identification-vs-inclusiveness → substrate linear drift
- Fiske 1992 4-model inventory → HEXACO-driven preference is substrate operational rule

**CITATION drift (minor):**
- Tajfel-Turner 1979 canonical page range 33-47; SciRP citation lists 33-37 (drift noted; substrate cites canonical 33-47)

**REJECT-STALE:** None

## §7 Framework Methodology Firsts

- FIRST group formation substrate in framework
- FIRST Tajfel-Turner SIT operationalization
- FIRST Sherif superordinate goal reduction substrate wire
- FIRST Brewer optimal distinctiveness drift
- FIRST Fiske relational models substrate operationalization
- SECOND Phase 2 Tier 3 mechanism (M7 was FIRST)
- FIRST substrate ship leveraging Phase 3.8 group substrate primitives
- FIRST additive-overlay preservation of 2-Sim mode with K ≥ 3 activation cascade

## §8 Deviations from Spec

**Test count 95 vs target 75:** +20 overshoot. Comprehensive Rule 28 preservation harness + Path A additive-overlay discipline suite added value.

**Wire sites 3 seed + 1 tick vs target ~5:** substrate exposes M1/M5/F2/F4 composition helpers as read-only per Council #11 Item 198 discipline; active mutation deferred to Phase 3.8.1 consumer-scope wiring at K ≥ 3.

**LOC 828 vs target 1000-1300:** leaner due to Phase 3.8 group substrate primitive leverage (getSimStateById + iterateAllPairs + isNSimMode).

**Additive overlay:** M9 substrate seeded EMPTY at 2-Sim spawn; group formation requires K ≥ 3 activation. Preserves H1 backward-compat invariant from Phase 3.8.

## §9 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/87 files (+2 from Phase 3.8 baseline 85 due to new M9 + groupSubstrate additions)
- sim-ai full test suite: **2780 PASS** (baseline 2685 → +95 M9 tests)
- sim-ai postmortem: 2 preexisting anomalies (Item 164 rescue calibration; not M9-caused)
- roomtolife precheck: verify-vendor 251/251 files PASS

## §10 Council #11 Candidacy

**Item 225 filed:** Phase 3.10 M9 socialIdentityFactionDynamics ratification.

Sub-items:
- 225.1 M9 substrate ratification with K=2 empirical anchor verification
- 225.2 5 CALIBRATION-CHOICE constants ratification
- 225.3 3 EMPIRICAL-TRANSLATION architectural bridges ratification
- 225.4 Additive-overlay preservation of 2-Sim mode + K ≥ 3 activation cascade
- 225.5 Tajfel-Turner 1979 pp. 33-47 vs SciRP 33-37 citation-drift correction (minor)

## §11 Downstream Impact

**Phase 2 v1+ substrate coverage COMPLETE for social identity axis** (M9 shipped).

**M8 sleepMemoryConsolidation still deferred** per roadmap explicit low-ROI rationale (line 85).

**Phase 3.8.1 v.next scope** (deferred from Phase 3.8):
- M9 composition wire N-Sim propagation activation
- F2 Boehm coalition + F4 witness triangle activation at K ≥ 3
- UI N-tab + N-Sim CharacterViewer + N-Sim CrossPlaneCouplingMatrix
- Full behavioral tick for additionalSims
- H4 N=8 performance harness
- ~135 additional tests

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
