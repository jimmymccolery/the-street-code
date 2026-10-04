# Phase 3.8.1 Ship 5a — M5+M1+M2+M3 N-Sim Composition Wire Propagation — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

Low-risk N-Sim composition wire propagation wave — 4 mechanisms shipped in single ship due to independence + smaller individual scopes:
- **M5** basic psych needs (~80 LOC + 12 tests) — lowest risk
- **M1** sociometer (~180 LOC + 18 tests) — dispatch helper canonicalization
- **M2** appraisal (~130 LOC + 15 tests) — Weiner attribution disambiguation
- **M3** goal hierarchy (~110 LOC + 12 tests) — Baumeister-Leary substitutability

## §2 Architecture

### M5 — SDT multi-source aggregation
- Multi-source relatedness_sat/frust = **additive Σ per_source_delta** per Ryan-Deci 2000 + Reis-Sheldon-Gable 2000 + Bartholomew PNTS
- `SDT_MULTI_SOURCE_CAPS.RELATEDNESS_SAT_MULTI_SOURCE_CAP = [omitted]` + `RELATEDNESS_FRUST_MULTI_ATTACKER_CAP = [omitted]` (3× single-source; CALIBRATION-CHOICE anchored to Chen 2015 within-day boundedness + Williams 2007 pile-on saturation)
- New helper `applyMultiSourceRelatednessDelta`

### M1 — sociometer dispatch canonicalization
- **NEW `applySelfEsteemDeltaBySimId(state, simId, delta)`** in `groupSubstrate.ts` (deviation from R1 spec — see §7)
- Canonicalizes Ship 2 M9's ad-hoc three-branch pattern (canonical `a` → top-level; canonical `b` → simB slot; N-Sim → sims map)
- Williams Cyberball 2-vs-1 ostracism = **2× single-Sim ostracism** magnitude
- 20+ SE ternaries refactored (high-value sites: M3 W6 partner_death both sides + M4 W7 aggregate SE + M7 W4 trauma SE + Ship 2 M9 Site D)

### M2 — attribution disambiguation
- ADD optional `attributedOtherSimId?: SimId` on `AppraisalVector` + `PendingSecondaryEntry`
- `buildAppraisalContext` @ 3512 SimId-generic dispatch (canonical 'a'/'b' preserved; K≥3 iterates)
- Weiner 1985 attribution theory: at K≥3, "other" agency attribution disambiguates to specific Sim (EMPIRICAL-TRANSLATION from K=2 dyadic canonical scope)
- `ingestPrimaryAppraisal` 6th arg + `appraiseEventSecondary` propagation

### M3 — belonging goal substitutability + partner co-location widening
- **`isBelongingGoalUnreachableForSim`** in `groupSubstrate.ts` — belonging goal only unreachable when ALL other Sims dead (Baumeister-Leary 1995 substitutability)
- **`anyPartnerCoLocated`** in `groupSubstrate.ts` — Chebyshev radius 1 (preserves K=2 wire's ≤1 predicate); widens for implementation-intention firing + goal-progress context at K≥3
- `markIdentityGoalUnreachable('belonging')` @ 2874 gated on ALL other Sims dead

## §3 Non-Inertness Gate Verdict — 56/56 PASS @ 100%

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship5aM5M1M2M3NSimPropagation.test.ts`

- **M5 basicPsychNeed:** 12/12 PASS — H1 additive-relatedness_sat + H2 pile-on frust + H3 caps saturation + V1 K=2 backward-compat + V2 Rule 28 preservation
- **M1 sociometerSelfEsteem:** 18/18 PASS — H1 dispatch correctness (canonical A / canonical B / N-Sim map) + H2 Leary 1995 linear-sum + H3 Williams Cyberball 2-vs-1 + V1 K=2 bit-identical + V2 Rule 28 preservation
- **M2 appraisalTendency:** 15/15 PASS — H1 SimId-generic ingestPrimaryAppraisal at K=3 + H2 Weiner 1985 attributedOtherSimId propagation + H3 K=3 SE dispatch + V1 K=2 vector-shape preservation + V2 Rule 28 preservation
- **M3 autonomousGoalHierarchy:** 11/11 PASS — H1 Baumeister-Leary 1995 substitutability at K=3+K=4 + H2 K=2 partner_death unreachable preserved + H3 anyPartnerCoLocated widening + V1 K=2 legacy delegation + V2 Rule 28 preservation

## §4 Empirical Anchors (K=2 verified)

- **Ryan-Deci 2000** Am Psych 55(1):68-78 SDT canonical
- **Reis-Sheldon-Gable 2000** daily-diary relatedness
- **Bartholomew 2011** PNTS
- **Chen 2015** BPNSFS within-day boundedness
- **Williams 2007** pile-on saturation (Cyberball)
- **Williams Cyberball** 2-vs-1 ostracism
- **Leary 1995** linear-sum
- **Weiner 1985** attribution theory
- **Baumeister-Leary 1995** substitutability

## §5 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE:**
- `SDT_MULTI_SOURCE_CAPS.RELATEDNESS_SAT_MULTI_SOURCE_CAP = [omitted]` + `RELATEDNESS_FRUST_MULTI_ATTACKER_CAP = [omitted]` (3× single-source; anchored to Chen 2015 + Williams 2007)
- `anyPartnerCoLocated` Chebyshev radius 1 (preserves K=2 wire's ≤1 predicate)

**EMPIRICAL-TRANSLATION:**
- Weiner 1985 K≥3 `evt.to → attributedOtherSimId` (Weiner K=2 dyadic canonical scope extrapolated)
- Baumeister-Leary 1995 substitutability at K=2 reduces to legacy sole-partner-dead wire (degenerate case)

**REJECT-STALE:** None

## §6 Framework Methodology Firsts

- FIRST `applySelfEsteemDeltaBySimId` dispatch helper canonicalizing Ship 2 M9's ad-hoc three-branch pattern
- FIRST multi-source Williams Cyberball ostracism linear-sum with CALIBRATION-CHOICE saturation cap
- FIRST M2 `attributedOtherSimId` Weiner 1985 attribution disambiguation threaded from primary-ingestion → PendingSecondaryEntry → Stage 2 secondary
- FIRST M3 Baumeister-Leary 1995 belonging-goal substitutability gate at N-Sim with K=2 backward-compat via degenerate case
- FIRST M3 `anyPartnerCoLocated` widening for implementation-intention firing + goal-progress context at K≥3

## §7 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/87 files
- sim-ai full test suite: **2987 PASS** (baseline S4 close 2931 → +56 Ship 5a tests across 148 test files)
- sim-ai postmortem: 1 anomaly (`signal_for_rescue_without_rescue_outcome` @ tick 6000; PRE-EXISTING rescue-arrival calibration; unrelated to Ship 5a K≥3 gated wires; waived)
- roomtolife: precheck GREEN + vendor sync verified

## §8 Deviations from Spec

**`applySelfEsteemDeltaBySimId` location:** Placed in `groupSubstrate.ts` (alongside `getSimStateById` peer dispatch helpers) rather than `layer3Accumulators.ts` per R1 design. Rationale: `layer3Accumulators.ts` is project-scope; importing `IslandWorldState` would create downstream-import cycle. DEVIATION-DOC noted in helper JSDoc.

**Refactored scope:** Refactored SE dispatch ternaries in high-value sites (M3 W6 partner_death both sides + M4 W7 aggregate SE + M7 W4 trauma SE + Ship 2 M9 Site D). Perspective-swap sites inside `completeAction` / `tickSingleSim` / `tickSimB` (grievance + share_food + warned_of_danger + comforted + attacked_by direct writes) PRESERVED because they operate in actor-relative coordinate frames managed by tick-foundation refactor (Ship 1) rather than raw canonical SimIds — deferring these to future Ship 1 tick-foundation-extension consistent with R1 §1 wire-site scope.

## §9 Council #11 Candidacy

**Item 235 filed:** Phase 3.8.1 Ship 5a M5+M1+M2+M3 N-Sim propagation ratification.

Sub-items:
- 235.1 M5 additive-relatedness aggregation + saturation caps (CALIBRATION-CHOICE)
- 235.2 applySelfEsteemDeltaBySimId dispatch helper (canonicalizes Ship 2 ad-hoc)
- 235.3 M1 Williams Cyberball linear-sum + 2-vs-1 anchor
- 235.4 M2 attributedOtherSimId Weiner 1985 attribution disambiguation
- 235.5 M3 Baumeister-Leary substitutability + anyPartnerCoLocated widening
- 235.6 Location deviation for applySelfEsteemDeltaBySimId (import cycle avoidance)
- 235.7 Perspective-swap site refactor deferral to Ship 1 tick-foundation-extension

## §10 Downstream Impact

**Enables Ship 5b** (M6+M4+M7 higher-scope wave):
- M6 Bowlby 1969 Ch11 multi-figure hierarchy (~250 LOC / 25 tests — largest single-mechanism scope in Phase 3.8.1)
- M4 Kline 2015 signal-based + evaluative-feedback teaching typology UNLOCK at K≥3 (~200 LOC / 22 tests)
- M7 DSM-5 Criterion A4 witness-set trauma propagation + Alisic 2011 tertiary-witness reduced magnitude (~180 LOC / 20 tests)

**Enables Ship 6** UI extensions + **Ship 7** H4 N=8 performance harness after 5b completes.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
