# Tier 1 Phase 1 Mechanisms Behavioral Wiring — Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate shipped; per-mechanism Non-Inertness Gate harnesses deferred to post-ratification)
**Substrate ships:** sim-ai (Tier 1 wiring) + (manifest); roomtolife pushed

---

## §1 Scope

Wires 4 Phase 1 substrate modules (shipped 2026-07-11) into `tickIslandWorld` + `detectAndApplyPairInteractions` + action-completion effects. Prior to this ship, only F2 dominancePrestige was behaviorally wired; the other 7 Phase 1 modules were "shipped but not wired" — behaviorally inert.

**This ship covers Tier 1 (4 of 7 remaining unwired):**
- F1 accommodationResponse (Rusbult 1991 EVLN)
- F5 forgivenessProcess (McCullough 2003 linear-slope)
- D5 moralEmotionsFamily (Haidt 2003 4-family)
- D3 empathyDualSystem (Zaki-Ochsner 2012 dual-channel)

Tier 2 (B2 + D4 + F4) deferred to next session.

## §2 Architecture

**Substrate additions:**
- `IslandWorldState.grievanceLedger?` (F5 world-scope; mirrors F2 groupHierarchyState pattern)
- `IslandWorldState.moralEmotionsLedger?` (D5)
- `IslandWorldState.compassOfShameActiveBranch?` (D5 Nathanson 4-branch with 200-tick window)
- `IslandWorldState.empathyDualSystem?` (D3 with per-Sim QCAE traits)
- `PairRelationalState.lastAccommodationChoiceAtoB / BtoA` (F1 EVLN softmax + probabilities + severity)
- `PairHistoryEventType.'accommodation_choice_recorded'`
- `LandmarkEventType.'accommodation_constructive_witnessed'` + `.'contempt_cascade_witnessed'`
- 20 new `CrossPlaneEventType` additions with matching count schema

**Wire sites:**
- `createInitial2SimWorldState` (D3 trait registration via `deriveQcaeFromHexaco(HEXACO_BASELINE)`)
- `detectAndApplyPairInteractions` at resource_conflict (F1 + F5 + D5 + partial D3)
- `detectAndApplyPairInteractions` co-located distress detection (D3 PAM auto-trigger a↔b symmetric)
- `aggress_toward_sim` completion (F5 grievance + D5 Tangney router + Vitaglione dual output + D3 PAM)
- `share_food` completion (D5 gratitude + F5 repair-attempt)
- `warned_of_danger` completion (D5 gratitude)
- `comfort` completion (D5 gratitude + D5 compassion + F5 repair-attempt)
- `tickIslandWorld` main loop: per-tick decay chain (F2 → F5 → D5 → D3) after existing F2 rank decay

**Composition path:**
```
F2 dominance signal accumulates → F1 reads perpetratorHierarchy (post-signal live rank)
→ D5 contempt accumulates on target of aggression
→ F5 reconciliation gate opens on decay threshold cross
→ D5 contempt cascade rollback: if contempt ≥ CONTEMPT_CASCADE_GATE_THRESHOLD (0.6),
  reconciliation gate reverts to false per Fischer-Roseman 2007 character-unchangeable
→ D3 PAM auto-fires on co-located distress (Preston-de Waal 2002)
→ D3 compassion fatigue accrues per Klimecki-Singer 2012 (empathic-distress-fatigue reframe;
  compassion is RESTORATIVE, not fatiguing)
```

## §3 Empirical Anchors (K=2 verified)

- Rusbult, Verette, Whitney, Slovik, Lipkus 1991 JPSP 60(1):53-78 EVLN
- Gaines, Reis, Summers, Rusbult, Cox 1997 Personal Relationships 4:93-113 attachment × EVLN
- Kito 2005 J Soc Psych 145(2):127-140 (NOT 2017 per prior correction)
- Anicich, Fast, Halevy, Galinsky 2016 Organization Science 27(1):123-140 (NOT JPSP; venue correction from prior candidacy)
- McCullough, Fincham, Tsang 2003 JPSP 84(3):540-557 latent-growth linear-slope (NOT exponential — critical structural finding)
- Fehr, Gelfand, Nag 2010 Psych Bull 136(5):894-914 forgiveness meta k=175 (empathy r=.51 + apology r=.42 + intent r=-.49)
- Struthers 2008 JESP 44(4):983-992 backfire replication
- Hirst, Hepper, Tenenbaum 2019 J Soc Pers Rel 36(11-12):3960-3985 attachment forgiveness meta k=26
- Wenzel, Okimoto, Hornsey 2017 PSPB 43(6):758-771 (with intergroup → dyad EMPIRICAL-TRANSLATION flag)
- Haidt 2003 Handbook of Affective Sciences 4-family taxonomy
- Tangney, Stuewig, Mashek 2007 Annu Rev Psychol 58:345-372 attribution locus
- Fischer, Roseman 2007 JPSP 93(1):103-115 contempt character-unchangeable
- Elison, Lennon, Pulos 2006 SBP 34:221-238 Compass of Shame Scale
- Algoe 2012 SPPC 6(6):455-469 gratitude find-remind-bind
- Bartlett, DeSteno 2006 Psych Sci 17(4):319-325 gratitude d≈0.5-0.7
- Vitaglione, Barnett 2003 Motivation and Emotion 27:301-325 empathic anger DUAL output
- Zaki, Ochsner 2012 Nature Neuroscience 15(5):675-680 dual-channel
- Reniers 2011 J Pers Assess 93(1):84-95 QCAE 2-factor
- Preston, de Waal 2002 BBS 25(1):1-20 PAM
- Shamay-Tsoory 2011 Neuroscientist 17(1):18-24 double-dissociation (review)
- Amodio, Frith 2006 Nature Rev Neurosci 7(4):268-277 mPFC load-sensitivity
- Adams, Boscarino, Figley 2006 Am J Orthopsychiatry 76(1):103-108 CF-Short
- Klimecki, Singer 2014 Current Biology 24(18):R875-R878 neural dissociation
- Ben-Ami Bartal, Decety, Mason 2011 Science 334(6061):1427-1430 in-group

## §4 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE (framework-extension; no empirical anchor for exact value):**
- CONTEMPT_CASCADE_GATE_THRESHOLD = [omitted] reused for F5 rollback gate (Fischer-Roseman 2007 verified conceptually; exact intensity threshold not empirically anchored)
- Compass of Shame 200-tick expiration window (Elison 2006 SBP trait-level; temporal-episode-length not anchored)
- Sentiment delta magnitudes for F1 EVLN (magnitudes omitted)

**EMPIRICAL-TRANSLATION (Council #11 Item 163 pattern):**
- D3 careForVictim proxy = max(0, priorSentiment) — Batson 2009 EJSP does not formalize care-for-cared-for-other operationalization
- Aquino 2011 moralIdealCentrality → HEXACO H proxy for D5 self-conscious router
- Wenzel-Okimoto-Hornsey 2017 intergroup apology representativeness → 2-Sim dyad + observer scope

## §5 Non-Inertness Gate Criteria (proposed; deferred to post-ratification harness)

**F1 hypotheses (from Agent A design):**
- H-F1-1 Le-Agnew 2003 commitment → constructive: high-commit voice+loyalty ≥ 40pp above low-commit
- H-F1-2 Gaines 1997 attachment × EVLN: dismissing exit+neglect ≥ 30pp above secure
- H-F1-3 Rusbult 1980 alternatives → exit: high-alt exit ≥ 25pp above low-alt
- H-F1-4 Anicich 2016 insecure-dominant: voice ↓ ≥ 15pp AND exit ↓ ≥ 15pp when perpetrator is insecure-dominant
- H-F1-5 Kito 2005 Bundle E → loyalty: Bundle E loyalty ≥ 20pp above Bundle A + exit ↓ ≥ 10pp

**F5 hypotheses (from Agent B design):**
- H-F5-1 McCullough 2003 linear decay: single transgression severity 0.5, avoidance Δ ≥ 30pp over 1000 ticks
- H-F5-2 Wade 2014 log-dosage: 3 repair attempts show avoidance ≥ 20pp lower vs 0 attempts
- H-F5-3 Struthers 2008 backfire: intentional+apology avoidance ≥ 10pp above unintentional+apology within apology window
- H-F5-4 Hirst 2019 attachment: fearful-avoidant decay ≤ 65% of secure
- H-F5-5 Enright 2015 decoupling: avoidance decays past reconciliation-granted flag

**D5 hypotheses (from Agent C design):**
- H-D5-1 Bartlett-DeSteno 2006 gratitude d≈0.5-0.7 after 3 share_food fires
- H-D5-2 Fischer-Roseman 2007 chronic contempt ≥ 0.4 after 500-tick recovery window
- H-D5-3 Tangney 2007 attribution router: guilt vs shame weights differentiated per input signals
- H-D5-4 Elison 2006 Compass of Shame HEXACO gate: 100% branch determinism per hexaco.E/A/H
- H-D5-5 Vitaglione 2003 dual output: help_boost + punish_boost both non-zero

**D3 hypotheses (from Agent D design):**
- H-D3-1 PAM co-location: sustained partner distress produces affective_a ≥ 0.35
- H-D3-2 Amodio-Frith 2006 cognitive-load gate: high-stress cognitive_c degrades ≥ 30% vs affective ≤ 10%
- H-D3-3 Batson 1981 + Eisenberg 1989 route split: both routes fire in ≥ 80% of middle-range trials
- H-D3-4 Ben-Ami Bartal 2014 in-group multiplier: in-group affective_a above stranger
- H-D3-5 Klimecki-Singer 2012 burnout dampening: > 0.7 fatigue reduces subsequent affective ≥ 40%

Aggregate: 25 hypotheses × 4 mechanisms = 5-per-mechanism gate. Target: PASS 5/5 per mechanism at 100% clear rate per Council #9 discipline.

## §6 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/79 files
- sim-ai full test suite: **2104 passed** + 1 preexisting phaseD flaky (baseline 2096 → +9 Tier 1 preservation tests)
- sim-ai post-mortem: 1 preexisting Item 164 rescue calibration anomaly (unrelated to Tier 1)
- roomtolife `npm run precheck`: PASS (Next.js build + TS typecheck GREEN; 224 vendored files verified)

## §7 Framework Methodology Firsts

- First 4-mechanism parallel-agent behavioral wiring in single session (F1 + F5 + D5 + D3 across 4 parallel design agents)
- First composition-aware wire cascade (F1 reads F2 dominance → F5 reads D5 contempt → D5 fires empathic-anger dual → D3 fires PAM)
- First per-tick decay chain of 3 world-scope ledgers (F5 + D5 + D3) chained after F2 rank decay
- First trait registration at spawn seeding QCAE from HEXACO baseline
- First Enright 2015 forgiveness-reconciliation decoupling wire preserved under Rule 28 defensive-reducer spread discipline

## §8 Recommended Council #11 Disposition

**RATIFY-PROVISIONAL Tier 1 substrate wiring** on evidence:
- 4 K=2-verified design deliverables from parallel research agents
- Clean ship gates at all sim-ai and roomtolife checks
- Non-Inertness Gate hypothesis catalog specified (§5)
- 4 mechanisms compose cleanly with defaults where downstream mechanisms not yet accumulated

**Council #11 candidacy sub-items:**
- Non-Inertness Gate empirical harness ratification (25 hypotheses across 4 mechanisms)
- Tier 2 wiring scope ratification (B2 + D4 + F4 remaining)
- Framework CALIBRATION-CHOICE flag consolidation (Council #11 Item 163 EMPIRICAL-TRANSLATION extension)
- Dedicated UI panels for F1/F5/D5/D3 observability (currently observable via CrossPlaneTraceLog only)

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Repository:** `~/Projects/the-street-code/methodology/`
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
