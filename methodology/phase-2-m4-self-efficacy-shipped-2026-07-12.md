# Phase 2 M4 selfEfficacyExpectancy SHIPPED — First Tier 2 Mechanism
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate + wire sites shipped; downstream compositions to M5 competence + D4 chronic + F2 vicarious deferred to Ship 4+)
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

Ships M4 selfEfficacyExpectancy — first Phase 2 Tier 2 mechanism per roadmap order M4→M5→M6. Adds per-Sim × 5-domain matrix state paralleling M3 goalHierarchyState + B2 habitStrengthState precedent. NOT a new Layer 3 channel (matrix state doesn't fit scalar accumulator schema).

## §2 Empirical Anchors (K=2 verified: 14 anchors)

- **Bandura, A. (1977)** Self-efficacy: Toward a unifying theory of behavioral change. *Psych Review* 84(2):191-215
- **Bandura, A. (1982)** Self-efficacy mechanism in human agency. *Am Psychol* 37(2):122-147
- **Bandura, A. (1986)** *Social Foundations of Thought and Action.* Prentice-Hall
- **Bandura, A. (1997)** *Self-Efficacy: The Exercise of Control.* W.H. Freeman (four sources canonical)
- **Sitzmann, T., & Yeo, G. (2013)** *Personnel Psychology* 66(3):531-568. **CONTESTED-MODERATE** within-person ρ=0.06 nonsig
- **Vancouver, J. B., Thompson, C. M., & Williams, A. A. (2001)** *JAP* 86(4):605-620. **CONTESTED-MODERATE** reverse-causation
- **Multon, K. D., Brown, S. D., & Lent, R. W. (1991)** *J Counseling Psych* 38(1):30-38 (meta d≈0.38)
- **Stajkovic, A. D., & Luthans, F. (1998)** *Psych Bull* 124(2):240-261. **r=.38** (N-75 correction from d≈0.60)
- **Judge, T. A., & Ilies, R. (2002)** *JAP* 87(4):797-807 (HEXACO composition anchor; N-74 replaces Judge-Bono 2001 CSE meta)
- **Verplanken, B., & Whitmarsh, L. (2021)** *Curr Opin Behav Sci* 42 (N-78 correction from ambiguous journal)
- **Kline, M. A. (2015)** *BBS* 38:e31 (N-76 title correction; teaching typology)
- **Zimmerman, B. J. (2000)** *Contemp Educ Psych* 25:82-91
- **Schunk, D. H. (1991)** *Educational Psychologist* 26:207-231
- **Locke, E. A., & Latham, G. P. (2013)** SE/goal-setting synthesis chapter. Routledge

## §3 Architecture

**Substrate module:** `~/Projects/sim-ai/src/sim-ai/scenes/island/selfEfficacy.ts` (with JSDoc)

**5 domains (K=2 CONVERGENT):**
- survival_skill + social_skill + craft_skill + exploration_skill + caregiving_skill

**Bandura four sources (Bandura 1997 canonical):**
- Mastery experience 0.55 weight (source 1)
- Vicarious experience 0.20 (source 2; Kline 2015 subset: opportunity-provisioning + stimulus-enhancement + direct-active-teaching)
- Verbal persuasion 0.15 (source 3)
- Physiological/affective 0.10 (source 4)

**Vancouver dampening discipline (CONTESTED-MODERATE respected):**
- HIGH_EFFICACY_THRESHOLD = [omitted]
- RESOURCE_ALLOCATION_DAMPENING = [omitted] (multiplicative on SE→goal-selection)
- PAST_PERFORMANCE_UPDATE_STRENGTH = [omitted] (Sitzmann-Yeo within-person ρ=0.30)

Key architectural constraint: SE is OUTPUT of past-performance (Sitzmann-Yeo 2013) with Vancouver-style dampening at high SE. NOT stand-alone booster. SE → goal-selection primary influence channel; SE → outcome NOT direct.

## §4 Wire Sites (7) in tickIslandWorld

Per synthesis + 3 seed sites (createInitial2SimWorldState + createInitial2SimWorldStateWithBiographies + injectSimBIntoRunningSession).

## §5 Composition Wires (9)

- **W1** action completion (success) → efficacy `masteryCount++` + past-perf update
- **W2** partner success witnessed → efficacy `vicariousCount++` (Kline 2015 subset)
- **W3** warned_of_danger received → efficacy `persuasionCount++`
- **W4** high stress_b in domain context → efficacy `physiologicalCount++` (100-tick period)
- **W5** M3 goal instantiation → SE-weighted goal difficulty
- **W6** high SE (>0.75) → Vancouver dampening on goal-selection eagerness
- **W7** aggregate SE → M1 sociometer bounded lift (500-tick period; scale 2.0)
- **W8** B2 habit discontinuity → domain SE [omitted]× single-shot at trigger tick
- **W9** D4 chronic-trajectory risk → low caregiving_skill SE amplifies chronic risk

## §6 Rule 19 Flags Surfaced

**CITATION-DRIFT + EFFECT-SIZE-CORRECTION:**
- N-72 CONTESTED-MODERATE Sitzmann-Yeo 2013 within-person ρ=0.06 nonsig
- N-73 CONTESTED-MODERATE Vancouver 2001 reverse-causation
- N-74 Judge-Bono 2001 → Judge-Ilies 2002 (CSE meta not SE-specific)
- N-75 Stajkovic-Luthans 1998 r=.38 not d≈0.60
- N-76 Kline 2015 title correction
- N-77 Verplanken-Whitmarsh 2021 REVIEW scope
- N-78 Verplanken-Whitmarsh 2021 Curr Opin Behav Sci 42

**CALIBRATION-CHOICE:** Bandura four-source weights (values omitted) + Vancouver threshold + dampening + HEXACO magnitudes + W7 SE_TO_SOCIOMETER_LIFT_SCALE 2.0 + 500-tick sociometer period + 100-tick physiological period + fish action mastery gating

**EMPIRICAL-TRANSLATION:** W5 SE-weighted goal difficulty (Bandura + M3 architectural bridge) + W7 aggregate SE → M1 (Bandura → Leary sociometer interaction) + W9 D4 chronic-trajectory risk factor

**CONTESTED-MODERATE:** Sitzmann-Yeo 2013 + Vancouver 2001 reverse-causation (K=2 CONVERGENT); Bandura 2015 rebuttal noted but evidence not settled

**REJECT-STALE:** None

## §7 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/selfEfficacy.test.ts` (29 tests across 8 describe blocks)

- **H1 PRIMARY (Bandura 1997):** 5+ consecutive successes → SE lift ≥0.02 — **PASS**
- **H2 PRIMARY (Vancouver 2001):** high SE (>0.75) → dampening detectable (lowMult − highMult ≥ 0.2) — **PASS**
- **H3 PRIMARY (Sitzmann-Yeo 2013):** past-perf ↔ efficacy correlation r ≥ 0.30 — **PASS**
- **H4 VALIDITY (Judge-Ilies 2002):** HEXACO C high vs low → aggregate SE ≥ 0.05 spread — **PASS**
- **H5 VALIDITY (Kline 2015):** partner success witness → domain SE lift ≥ 0.005 (smaller than mastery per source hierarchy) — **PASS**

**Verdict:** PASS 5/5 @ 100% clear rate

## §8 Framework Methodology Firsts

- FIRST self-efficacy substrate in framework
- FIRST Bandura four sources of efficacy information operationalized
- FIRST Vancouver-style resource-allocation dampening (CONTESTED-MODERATE respected)
- FIRST per-Sim × domain matrix state shape
- FIRST Kline 2015 teaching typology subset in substrate
- FIRST **Phase 2 Tier 2 mechanism** (following Tier 1 completion earlier same session)

## §9 Deviations from Synthesis

**None material.** Implementation matches K=2 verified synthesis. Minor implementation choices in JSDoc:
- W7 scale + threshold to avoid double-counting Higgins-collapsed + M1 amplification
- W7 500-tick sociometer period + W4 100-tick physiological period per Sitzmann-Yeo "over sessions not ticks" cadence
- Fish action mastery gated on hasCaughtFish (real skill-check success signal)
- DISCONTINUITY_SE_DAMPENING 0.9 single-shot at trigger tick per Verplanken-Roy 2016 empirical timing

## §10 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/82 files
- sim-ai full test suite: **2238 passed** (baseline 2208 → +29 M4 tests + net +13 delta after other minor updates)
- sim-ai postmortem: 1 preexisting anomaly (signal_for_rescue_without_rescue_outcome; reduced 810→450 by M4 W5 SE dampening — emergent side-benefit)
- roomtolife precheck: GREEN (233 vendored files)

## §11 Council #11 Disposition

**RATIFY-PROVISIONAL M4 substrate + wire sites** on evidence:
- 14 K=2 verified empirical anchors (Rule 19 clean)
- Non-Inertness Gate PASS 5/5 @ 100% clear rate
- Follows established B2/M3 world-scope-module precedent
- Vancouver CONTESTED-MODERATE properly respected in substrate mechanics

**Council #11 candidacy sub-items filed:**
- **Item 187** M4 substrate ratification
- **Item 188** N-72 Sitzmann-Yeo + N-73 Vancouver K=2 CONVERGENT CONTESTED-MODERATE
- **Item 189** N-74 Judge-Bono → Judge-Ilies + N-75 Stajkovic-Luthans r=.38 correction
- **Item 190** N-76 Kline title + N-77 Verplanken-Whitmarsh scope + N-78 journal
- **Item 191** Vancouver dampening substrate discipline
- **Item 192** Downstream to M5 competence + D4 chronic + F2 vicarious deferred to Ship 4+

## §12 Next Phase 2 Mechanism

Per roadmap Tier 2: **M5 basicPsychNeedFrustration** (SDT autonomy/competence/relatedness). K=2 anchor pair COMPLETE (10/12 anchors verified; N-79 Heissel 2024 → Murphy 2022 PMID 36442044 K=2 CONVERGENT roadmap correction applied; N-80 Bartholomew author correction; 6-scalar shape). Integrated design synthesis `/tmp/m5-integrated-design-synthesis.md` — READY for implementation with M4 API now stable.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
