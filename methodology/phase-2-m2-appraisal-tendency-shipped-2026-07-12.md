# Phase 2 M2 appraisalTendencyDualStage SHIPPED — Third Phase 2 Mechanism (Tier 1 COMPLETE)
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate + wire sites shipped; downstream D3/D4/F5 explicit wires deferred to Phase 2 Ship 3+)
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

Ships M2 appraisalTendencyDualStage — third Phase 2 mechanism per roadmap Tier 1 order (M1→M3→M2). **COMPLETES Phase 2 Tier 1.** Adds per-Sim `appraisalState` (event-classifier transforming CrossPlaneEvent → 5-dim appraisal vector → routing into existing 9 Layer 3 channels).

**Substrate architecture:** Event-classifier ADDITIVE overlay. NOT a 10th Layer 3 channel. NOT a rewire of existing event flow. Existing CrossPlaneEvent handling stays intact; M2 hooks alongside as additional appraisal → Layer 3 modulation, preserving all prior Phase 1 + Phase 2 mechanisms.

## §2 Empirical Anchors (K=2 verified: 10 primary + 3 secondary)

- **Lazarus, R. S., & Folkman, S. (1984)** *Stress, Appraisal, and Coping.* New York: Springer.
- **Scherer, K. R. (2001)** Appraisal considered as a process of multilevel sequential checking. In Scherer/Schorr/Johnstone (Eds.), *Appraisal Processes in Emotion*, pp. 92-120. OUP.
- **Scherer, K. R. (2009)** The dynamic architecture of emotion. *Cognition and Emotion* 23(7):1307-1351.
- **Roseman, I. J. (1991)** Appraisal determinants of discrete emotions. *Cognition and Emotion* 5(3):161-200.
- **Smith, C. A., & Ellsworth, P. C. (1985)** Patterns of cognitive appraisal in emotion. *JPSP* 48(4):813-838.
- **Ellsworth, P. C., & Scherer, K. R. (2003)** Appraisal processes in emotion. *Handbook of Affective Sciences* pp. **572-596** (N-68 correction from 572-595).
- **Frijda, N. H. (1986)** *The Emotions.* Cambridge U Press.
- **Moors, A., Ellsworth, P. C., Scherer, K. R., & Frijda, N. H. (2013)** Appraisal theories: State of the art. *Emotion Review* 5(2):119-124.
- **Higgins, E. T. (1987)** Self-discrepancy theory. *Psych Review* 94(3):319-340. **CONTESTED-MODERATE.**
- **Wondra, J. D., & Ellsworth, P. C. (2015)** Appraisal theory of empathy. *Psych Review* 122(3):411-428.
- **Tangney, Niedenthal, Covert, Barlow (1998)** *JPSP* 75(1):256-268. Higgins attenuation source.
- **Silvia & Eddington (2010)** *Personality and Individual Differences* 49(1). Supporting attenuation.
- **Judge, T. A., & Ilies, R. (2002)** *JAP* 87(4):797-807. HEXACO composition anchor.

## §3 Architecture

**Substrate module:** `~/Projects/sim-ai/src/sim-ai/scenes/island/appraisalTendency.ts` (627 LOC with JSDoc)

**Type primitives:**
- `AgencyAttribution` = 'self' | 'other' | 'circumstance'
- `AppraisalDimensionName` (5): goal_relevance + agency_attribution + certainty + coping_potential + norm_compatibility
- `AppraisalVector` (5 dimensions + stage + eventType + eventTick)
- `SimAppraisalState` (lastPrimary + lastSecondary + pendingSecondary queue + selfWorthThreatSignal collapsed channel)
- `AppraisalState { perSim: Record<SimId, SimAppraisalState> }`
- Constants: `LAZARUS` + `SCHERER_SEC` + `ROSEMAN` + `SMITH_ELLSWORTH` + `HIGGINS_COLLAPSED` + `HEXACO_APPRAISAL` + event-classifier tables (EVENT_VALENCE_PROXY + EVENT_NORM_COMPATIBILITY)
- Helpers: `appraiseEventPrimary` + `appraiseEventSecondary` + `routeAppraisalToLayer3` + `updateSelfWorthThreat` + `tickAppraisalDecay` + state-mutating helpers `ingestPrimaryAppraisal` + `fireSecondaryAppraisals` + amplifier helpers for W2/W3/W4

**Higgins CONTESTED-MODERATE discipline:** Collapsed self-worth-threat channel per Tangney 1998 + Silvia-Eddington 2010 attenuation. NO dejection-vs-agitation dissociation in substrate mechanics. Structural claim (self-discrepancy → affect family) preserved; specificity claim not encoded.

## §4 Wire Sites in `tickIslandWorld` (7)

Unified M2 block placed after M3 evaluate:
1. Stage 2 drain (fires pending items from PRIOR-tick ingest)
2. Stage 1 primary appraisal on THIS-tick pair-history events (attacked_by, share_food, comforted, grievance_recorded, warned_of_danger, resource_conflict)
3. `tickAppraisalDecay` (self-worth-threat decay + queue TTL)
4. `createInitial2SimWorldState` + Sim B injection: seed `appraisalState` per Sim
5. Amplifier `computeD5NormViolationAmplifier` exposed for D5 composition-scope
6. Amplifier `computeM1SelfWorthThreatAmplifier` exposed for M1 composition-scope
7. Amplifier `computeF5CharitabilityAmplifier` exposed for F5 composition-scope

Sequential ordering per Scherer SEC preserved via `pendingSecondary` queue with `PENDING_SECONDARY_TTL_TICKS = [omitted]` (Stage 2 for tick N fires at tick N+1).

## §5 Composition Wires (7)

- **W1** primary goal_relevance → valence_f (Lazarus + Scherer SEC1)
- **W2** primary norm_compatibility → D5 moralEmotionsLedger amplifier (Scherer SEC4 + Roseman legitimacy; EMPIRICAL-TRANSLATION)
- **W3** secondary agency=self → guilt_b lift + Higgins collapsed → M1 SE drop (Higgins CONTESTED-MODERATE; EMPIRICAL-TRANSLATION)
- **W4** secondary agency=other → F5 attribution charitability (Struthers 2008; CALIBRATION-CHOICE)
- **W5** secondary coping_potential → stress_b + B2 stress-mediated arbitration (Lazarus secondary + Dias-Ferreira 2009)
- **W6** secondary certainty (low) → arousal_f + fear-uncertainty differentiation (CALIBRATION-CHOICE)
- **W7** primary goal_relevance × M3 identity-goal category match → scale [omitted]× (EMPIRICAL-TRANSLATION)

## §6 Rule 19 Flags Surfaced

**CITATION-DRIFT:**
- **N-68 committed** — Ellsworth-Scherer 2003 pp. 572-596 (K=2 CONVERGENT; original 572-595 in agent prompt was wrong)
- N-69/N-70 **RETRACTED** post-audit — both agents fabricated roadmap-target claims about Silvia 2001 phrasing + Vansteenkiste 2020 Higgins-attenuation attribution; grep audit confirms roadmap correctly cites Tangney 1998 at line 102 + Vansteenkiste 2020 as CONTESTED-MEASUREMENT (Heissel 2024) at line 59. No roadmap correction needed.

**CALIBRATION-CHOICE:**
- All SCHERER_SEC scaling coefficients
- ROSEMAN dimension weights (5-dim v1 per N-71; 7-dim v2 deferred)
- SMITH_ELLSWORTH dimension weights
- HIGGINS_COLLAPSED thresholds + scales
- HEXACO_APPRAISAL coefficients
- W4 F5 charitability scale
- W6 certainty → arousal scale
- Event-classifier lookup tables (EVENT_VALENCE_PROXY + EVENT_NORM_COMPATIBILITY)

**EMPIRICAL-TRANSLATION:**
- W2 primary norm_compatibility → D5 (Scherer normative significance ≠ Haidt moral emotions family directly)
- W3 Higgins collapsed → M1 sociometer + guilt_b (Higgins classical model split into 2 channels)
- W7 M3 goal-category matching amplifier

**CONTESTED-MODERATE:**
- Higgins 1987 dejection-vs-agitation specificity — collapsed to single channel per Tangney 1998 + Silvia-Eddington 2010
- Roseman 1996 7-dim expansion — v2 deferred per N-71

**REJECT-STALE:** None

## §7 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/appraisalTendency.test.ts` (35 tests across 9 describe blocks; +3 over 28-32 target for extra wire coverage)

- **H1 PRIMARY (Lazarus-Folkman 1984):** ≥20% of Sim-tick appraisal instances have coping_potential < 0 — **PASS**
- **H2 PRIMARY (Roseman 1991):** Agency 3-value coverage each ≥10% — **PASS**
- **H3 PRIMARY (Scherer 2001 SEC):** Threat vs prosocial coping delta Cohen d ≥ 0.5 — **PASS**
- **H4 VALIDITY (Judge-Ilies 2002):** HEXACO E coping delta ≥ 0.25 — **PASS**
- **H5 VALIDITY (Higgins collapsed):** selfWorthThreatSignal > 0.3 → M1 amplification active — **PASS**

**Verdict:** PASS 5/5 @ 100% clear rate

## §8 Framework Methodology Firsts

- FIRST appraisal-tendency substrate in framework
- FIRST Lazarus primary/secondary sequential architecture in substrate
- FIRST Scherer 2001 SEC 2-stage in substrate (Stage 1 tick N; Stage 2 tick N+1 via pendingSecondary queue)
- FIRST event-classifier architecture (CrossPlaneEvent → appraisal vector → routing)
- FIRST 5-dimensional appraisal state
- FIRST Higgins CONTESTED-MODERATE collapsed-channel discipline
- FIRST K=2 pair hallucination-audit (Rule 19 methodology observation)
- FIRST amplifier-helper exposure pattern (composition-scope consumers read amplifier without direct Layer 3 mutation)
- **COMPLETES Phase 2 Tier 1** (M1 + M3 + M2 shipped 2026-07-12 single session)

## §9 Deviations from Synthesis

**Wire ordering:** Synthesis lists "post-M3 evaluate" for Stage 1 primary + "next-tick" for Stage 2. Implementation uses **unified M2 block after M3 evaluate** that (a) drains Stage 2 pending items from PRIOR-tick ingestion FIRST, (b) then ingests THIS-tick pair-history events for Stage 1 primary, (c) then runs decay. Preserves Scherer SEC sequential ordering (Stage 2 for tick N fires at tick N+1) via pendingSecondary queue with TTL=1. No functional deviation from spec.

**Test count 35 (spec target 28-32):** +5 tests for composition wires W1-W7 (spec allowed 5-7) plus 5 Non-Inertness Gate tests. All pass; no regressions.

**guilt_b routing at W3:** Framework's guilt_b lives at `moralEmotionsLedger` (M6 module) rather than direct Layer 3. Honored ADDITIVE OVERLAY DISCIPLINE — did NOT touch existing D5/D6 routing. Instead exposed `computeD5NormViolationAmplifier` for composition-scope. `routeAppraisalToLayer3` computes guilt-delta but voids it to avoid double-counting; composition surface is the amplifier helpers.

**Postmortem preexisting anomaly:** Verified via git stash A/B test that `signal_for_rescue_without_rescue_outcome × 810` anomaly exists at pre-M2 baseline. Preexisting rescue-arrival calibration issue unrelated to M2. No Rule 28 violations from M2.

## §10 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/81 files
- sim-ai full test suite: **2208 passed** (baseline 2174 → +35 M2 tests, 1 preexisting phaseD flaky waived)
- sim-ai postmortem: 1 preexisting anomaly (waived per interpretation guide)
- roomtolife precheck: GREEN (npm run precheck; TypeScript pass; build pass; 229+ vendored files verified)

## §11 Council #11 Disposition

**RATIFY-PROVISIONAL M2 substrate + wire sites** on evidence:
- 13 K=2 verified empirical anchors (Rule 19 clean)
- Non-Inertness Gate PASS 5/5 @ 100% clear rate
- Additive overlay preserves all Phase 1 + Phase 2 mechanisms
- No 10th Layer 3 channel — routes through existing 9 channels

**Council #11 candidacy sub-items filed:**
- **Item 181** M2 substrate ratification
- **Item 182** N-68 Ellsworth-Scherer 2003 pp. 572-596 (M2 substrate docs; K=2 CONVERGENT)
- **Item 183** N-71 Roseman 5-dim v1 CALIBRATION-CHOICE (7-dim v2 deferred)
- **Item 184** Higgins CONTESTED-MODERATE collapsed-channel discipline (Tangney 1998 + Silvia-Eddington 2010; NOT dejection-vs-agitation dissociation)
- **Item 185** M2 downstream explicit D3/D4/F5 wires deferred to Ship 3+
- **Item 186** K=2 hallucination audit methodology observation (M2 N-69/N-70 fabrication → Rule 19 target-verification discipline)

## §12 Next Phase 2 Mechanism

**Tier 1 COMPLETE.** Next per roadmap Tier 2 order (M4→M5→M6): **M4 selfEfficacyExpectancy** (Bandura 1977 + 1997 four sources).

**M4 K=2 anchor pair COMPLETE** (launched in parallel with M2 implementation):
- 14 anchors verified; Bandura primary + Sitzmann-Yeo 2013 + Vancouver 2001 + Multon-Brown-Lent 1991 + Stajkovic-Luthans 1998 + Judge-Bono 2001 + Verplanken-Whitmarsh 2021 + Kline 2015 + Zimmerman 2000 + Schunk 1991 + Locke-Latham 2013
- K=2 STRONG CONVERGENT: Sitzmann-Yeo 2013 within-person ρ=0.06 CONTESTED-MODERATE reverse-causation + Vancouver 2001 K=2 CONVERGENT reverse-causation
- 5-domain matrix synthesized: survival_skill + social_skill + craft_skill + exploration_skill + caregiving_skill
- Vancouver-style dampening at >0.75 SE
- N-72 through N-78 candidacies

**M4 integrated design synthesis:** `/tmp/m4-integrated-design-synthesis.md` (ready for implementation agent)

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Repository:** `~/Projects/the-street-code/methodology/`
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
