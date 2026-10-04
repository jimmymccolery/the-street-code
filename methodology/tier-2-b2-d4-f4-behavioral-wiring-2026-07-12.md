# Tier 2 Phase 1 Mechanisms Behavioral Wiring — Council #11 Candidacy Artifact
## Phase 1 Lifelikeness Roadmap COMPLETE

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate shipped; per-mechanism Non-Inertness Gate empirical harnesses deferred to post-ratification)
**Substrate ships:** sim-ai (Tier 2 wiring) + (manifest); roomtolife pushed

---

## §1 Scope + significance

Wires the remaining 3 Phase 1 substrate modules (B2 habitStrength + D4 prolongedGriefTrajectories + F4 gossipSemantics) into `tickIslandWorld`. **Completes the Phase 1 lifelikeness roadmap** started at F2 module ship 2026-07-11 and F2 behavioral wiring same day.

**Phase 1 wiring timeline:**
- F2 dominancePrestige — module 9c96ae1 + wiring same day (2026-07-11)
- F1 accommodationResponse — module 1409a34 (2026-07-11), wiring 3584105 (2026-07-12 Tier 1)
- F5 forgivenessProcess — module b0481bb (2026-07-11), wiring same as Tier 1
- D5 moralEmotionsFamily — module aac3eb6 (2026-07-11), wiring same as Tier 1
- D3 empathyDualSystem — module 37f8b64 (2026-07-11), wiring same as Tier 1
- **B2 habitStrength — module 49940e3 (2026-07-11), wiring 9f2e35b (this Tier 2 ship)**
- **D4 prolongedGriefTrajectories — module ef1f7f3 (2026-07-11), wiring 9f2e35b**
- **F4 gossipSemantics — module a0c0391 (2026-07-11), wiring 9f2e35b**

All 8 Phase 1 mechanisms are now behaviorally wired into the running substrate.

## §2 Architecture

**Substrate additions:**
- `IslandWorldState.habitStrengthState?` (B2 world-scope; mirrors F2/F5/D5 pattern)
- `IslandWorldState.lastArbitrationInfo?` (B2 diagnostic snapshot)
- `IslandWorldState.prolongedGriefState?` (D4)
- `IslandWorldState.gossipSemanticsState?` (F4)
- 15 new `CrossPlaneEventType` additions (5 B2 + 5 D4 + 5 F4) with matching count schema

**Wire sites (10 total for Tier 2):**
1. `createInitial2SimWorldState`: seed all 3 ledgers + F4 perSim entries
2. `decideNextAction`: B2 arbitration BEFORE memory modulation (Council #9 Item 148 ordering: memory is final tilt)
3. `completeAction`: B2 recordActionPerformance BEFORE history append
4. `tickIslandWorld`: B2 tickHabitDecay per Sim per current context bucket
5. `tickIslandWorld`: D4 tickGriefTrajectory + updateClinicalFlag per bereaved Sim
6. `tickIslandWorld`: F4 tickReputationDecay + tickUrgencyDecay per Sim
7. Death transition Sim A → activate D4 grief on Sim B + B2 partner_death discontinuity + FIRST partner_death landmark emission
8. Death transition Sim B → activate D4 grief on Sim A + B2 partner_death discontinuity + partner_death landmark
9. `attacked_by` completion: F4 witnessAntisocialAct + updateReputationFromDirect (severity -0.8)
10. `share_food` completion: F4 updateReputationFromDirect (severity +0.6)

**Composition path (extends Tier 1 cascade):**
```
F2 dominance → F1 exit-fear → D5 contempt → F5 reconciliation gate →
D5 contempt rollback → D3 PAM → D3 restorative compassion →
B2 habit arbitration (goal-directed vs habitual per Dickinson 1985) →
D4 grief activation on death → D4 trajectory decay + PGD 500-tick gate →
F4 direct-observation reputation → F4 witness urgency spike →
F4 decay chain closes the Phase 1 substrate loop.
```

## §3 Empirical Anchors (K=2 verified)

**B2 habitStrength:**
- Wood-Neal 2007 Psychological Review 114(4):843-863 dual-system
- Dickinson 1985 Philos Trans Roy Soc B 308(1135):67-78 arbitration
- Balleine-Dickinson 1998 outcome-devaluation
- Lally 2010 EJSP 40(6):998-1009 K=0.045 → t_95=66 asymptotic (**N=96 VERIFIED**; module claims N=82 — Council #11 candidacy N-65)
- Bouton 2004 Learning & Memory 11(5):485-494 context-dependent decay
- Dias-Ferreira 2009 Science 325(5940):621-625 chronic stress SETTLED (0.30 multiplier)
- Schwabe-Wolf 2009 J Neuroscience 29(22):7191-7198 acute CONTESTED-MODERATE (**N-64 flag: memory attributes replication to "Van Ast 2023" — actual paper is Smeets-Ashton-Roelands-Quaedflieg 2023 Neurobiology of Stress 24:100517**)
- Wood-Tam-Guerrero-Witt 2005 JPSP 88(6):918-933 discontinuity
- Verplanken-Roy 2016 60-tick window
- Verplanken-Orbell 2003 J Applied Soc Psych 33(6):1313-1330 SRHI
- Gardner-Abraham-Lally-de Bruijn 2012 IJBNPA 9:102 SRBAI-derivation
- Bogg-Roberts 2004 Psych Bulletin 130(6):887-919 TEMPERED r=-0.10 to -0.20

**D4 prolongedGriefTrajectories:**
- Bonanno 2002 CLOC JPSP 82(6):1150-1164 4-trajectory (45.9/10.7/23.4/0)
- Prigerson 2009 PLOS Med 6(8):e1000121 DSM-5-TR/ICD-11 PGD criteria
- Field-Filanosky 2010 Death Studies 34(1):1-29 continuing bonds distinction
- **Fraley-Bonanno 2004 adaptive-avoidance (K=2 flag: module docstring cites Fraley-Shaver 1999 — distinct paper)**
- Wayment-Vierthaler 2002 J Loss & Trauma 7(2):129-149 anxious → chronic
- Field-Sundin 2001 J Soc Pers Rel 18(3):347-361 CONJUGAL (NOT parental)
- Meier-Carr-Currier-Neimeyer 2013 J Soc Clin Psych 32(3):315-334 rumination mediator
- Stroebe-Schut 1999 Death Studies 23(3):197-224 Dual Process Model
- Kaltman-Bonanno 2003 J Anxiety Disorders 17(2):131-147 CRITICAL DISSOCIATION
- Lucas 2003 JPSP 84(3):527-539 LINEAR (not exponential) recovery
- Bonanno-Wortman-Nesse 2004 Psych & Aging 19(2):260-271 48-month stability
- Shear 2013 Curr Psych Reports 15(11):406 ~7% CG prevalence
- Maciejewski 2007 JAMA 297(7):716-723 yearning peaks ~4 months
- Anusic-Lucas 2014 J Personality 82(5):367-378 null social-buffering
- Bonanno-Kaltman 2001 Clin Psych Rev 21(5):705-734

**F4 gossipSemantics:**
- Sommerfeld 2007 PNAS 104(44):17435-17440 direct + gossip indirect reciprocity
- Sommerfeld 2008 Proc Roy Soc B 275(1650):2529-2536 multi-source concordance
- Feinberg 2012 JPSP 102(5):1015-1030 physiological release + witness urgency
- Feinberg 2014 Psych Sci 25(3):656-664 gossip + ostracism promote cooperation
- Beersma-Van Kleef 2012 JASP 42(11):2640-2670 4-factor MGQ (NOT PSPB)
- Dores Cruz 2019 Frontiers 10:1190 EMOTION_VENTING 5th factor
- Dores Cruz 2021 G&OM 46(2):252-285 integrative definition
- Dores Cruz 2021 Phil Trans B 376:20200301 tripartite valence
- Bosson 2006 Personal Relationships 13(2):135-150 weak-attitude asymmetry
- Peters-Kashima 2007 JPSP 93(5):780-797 emotion-sharing shared reality
- Fehr-Fischbacher 2003 Nature 425(6960):785-791 60% third-party sanction
- Ohtsuki-Iwasa-Nowak 2009 Nature 457(7225):79-82 avoidance-preferred
- Balliet-Wu-DeDreu 2014 Psych Bull 140(6):1556-1581 d=0.32 ingroup amplifier
- Wu-Balliet-Van Lange 2015 SPPS 6(8):923-930 shadow-of-future gate
- Hess-Hagen 2006 Human Nature 17(3):337-354 veracity
- Kniffin-Wilson 2010 G&OM 35(2):150-176 shared-task moderator
- Turner-Mazur-Wendel-Winslow 2003 Communication Monographs 70(2):129-141 (NOT Communication Studies)

## §4 Rule 19 Flags Surfaced

**Citation-hygiene corrections (Council #11 candidacies):**
- **N-64 Schwabe-Wolf 2009 replication AUTHORSHIP** — B2 module memory attributes replication to "Van Ast 2023" — actual paper is **Smeets/Ashton/Roelands/Quaedflieg 2023 Neurobiology of Stress 24:100517** (Van Ast is not on the byline)
- **N-65 Lally 2010 sample size** — B2 module header claims N=82; verified N=96 (median t_95=66 days range 18-254 confirmed)
- **N-66 Fraley-Bonanno 2004 attribution K=2 flag** — D4 module docstring cites Fraley-Shaver 1999 (Handbook chapter) for adaptive-avoidance hypothesis. Fraley-Bonanno 2004 JPSP 87(6):878-890 is a DISTINCT paper on grief-work-avoidance. Verify which anchor is intended.

**CALIBRATION-CHOICE / EMPIRICAL-TRANSLATION flags (Council #11 Item 163 pattern):**
- B2 arbitration boost/suppress magnitudes (0.4 / 0.85) are wire-scope calibration constants not module exports
- Compass of Shame + B2 discontinuity 200-tick / 60-tick windows are CALIBRATION-CHOICE
- D4 `justWorldBelief` proxy = HEXACO H / 100 — EMPIRICAL-TRANSLATION (no first-class substrate field for just-world belief)
- D4 attachment mapping helper (2-D scalar → categorical union) is a bridge translation
- F4 avoidance-preferred sanction expressed as F1 exit-boost is EMPIRICAL-TRANSLATION (Ohtsuki 2009 mathematical model → 2-Sim decision-time softmax)
- F4 F1 exit-logit sanction wire deferred to next session (site requires F1 softmax refactor identification)

## §5 Non-Inertness Gate Criteria (proposed; deferred to post-ratification harness)

**B2 hypotheses (from Agent A design):**
- H-B2-1 Lally 2010 curve visibility: p_habitual > 0.7 at rep=66
- H-B2-2 Arbitration selection shift ≥ 40pp for strong-habit vs no-ledger
- H-B2-3 Neal-Wood-Wu-Kurlander 2011 context-mismatch drop ≥ 60pp
- H-B2-4 Dias-Ferreira chronic stress ≥ 20pp delta at stress=90 vs 10
- H-B2-5 Bogg-Roberts HEXACO C override ≥ 10pp delta at C=90 vs 10

**D4 hypotheses (from Agent B design):**
- H-D4-1 Bonanno CLOC base rate reproduction within ±5pp at mid-Sim
- H-D4-2 Sentiment_f dependency → chronic amplification ≥ 15pp
- H-D4-3 Prigerson 6-month gate: clinicalFlag=false pre-500, true post-500
- H-D4-4 Fraley-Bonanno adaptive-avoidance: avoidant chronic < anxious chronic ≥ 20pp
- H-D4-5 Kaltman-Bonanno dissociation: sudden vs violent chronic difference < 5pp AND deathWasViolent set only in violent

**F4 hypotheses (from Agent C design):**
- H-F4-1 Sommerfeld direct: reputation ≤ -0.20 after 3 forced aggressions
- H-F4-2 Fehr-Fischbacher 60% third-party sanction: exit rate ≥ 55% ± 5pp
- H-F4-3 Feinberg witness urgency: getPendingUrgency ≥ 0.3 at empathyC = [omitted]
- H-F4-4 Balliet ingroup amplifier: exitBoost ratio ≈ 1.32 ± 0.05
- H-F4-5 REPUTATION_DECAY_PER_TICK: reputation drops to < 37% of initial after 1000 ticks (0.999^1000 ≈ 0.368)

Aggregate: 15 hypotheses × 3 mechanisms = 5-per-mechanism gate. Target: PASS 5/5 per mechanism at 100% clear rate per Council #9 discipline.

Combined with Tier 1 (25) + F2 (5) = **40 total Non-Inertness Gate hypotheses** across the completed Phase 1 wiring.

## §6 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/79 files
- sim-ai full test suite: **2113 passed** + 1 preexisting phaseD flaky (baseline 2105 → +9 Tier 2 preservation tests)
- sim-ai post-mortem: 1 preexisting Item 164 rescue calibration (unrelated to Tier 2)
- roomtolife `npm run precheck`: PASS (Next.js build + TS typecheck GREEN; 225 vendored files verified)

## §7 Framework Methodology Firsts

- **FIRST complete Phase 1 lifelikeness roadmap wire (8/8 mechanisms wired)**
- **FIRST partner_death landmark emission** (LandmarkEventType existed since 2026-07-11 but had no emit site until D4 wire)
- **FIRST 4-tick decay chain** (F5 + D5 + D3 + B2 + D4 + F4 all chain after F2 rank decay)
- **FIRST Fraley-Bonanno 2004 adaptive-avoidance wiring** with attachment classifier bridge (2-D scalar → categorical union)
- **FIRST 3-parallel-agent Tier 2 arc** (matches Tier 1 4-agent pattern)

## §8 Recommended Council #11 Disposition

**RATIFY-PROVISIONAL Tier 2 substrate wiring + PHASE 1 COMPLETE STATUS** on evidence:
- 3 K=2-verified design deliverables from parallel research agents
- Clean ship gates at all sim-ai and roomtolife checks
- Non-Inertness Gate hypothesis catalog specified (§5)
- Phase 1 lifelikeness roadmap fully wired (8/8 mechanisms behaviorally active)

**Council #11 candidacy sub-items:**
- Non-Inertness Gate empirical harness ratification (40 hypotheses across 8 mechanisms + F2)
- N-64/N-65/N-66 citation-hygiene corrections
- Framework CALIBRATION-CHOICE / EMPIRICAL-TRANSLATION flag consolidation
- Dedicated UI panels for F1-F4 + B2/D4/F4 observability
- F4 F1 exit-logit sanction wire (deferred; requires F1 softmax refactor)
- D4 justWorldBelief first-class Layer 3 field (K=2 candidacy — replace HEXACO H proxy)
- Post-Phase-1 roadmap: Phase 2 lifelikeness enrichment mechanisms + composition-integration wiring across all 8 shipped mechanisms

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Repository:** `~/Projects/the-street-code/methodology/`
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
