# Phase 2 M5 basicPsychNeedFrustration SHIPPED — Second Tier 2 Mechanism
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate + wire sites shipped; downstream F1 exit / B2 arbitration explicit wires deferred to Ship 5+)
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

Ships M5 basicPsychNeedFrustration — second Phase 2 Tier 2 mechanism per roadmap order M4→M5→M6. Per-Sim 3-need × 2-channel (satisfaction + frustration) = 6-scalar world-scope module paralleling M4 selfEfficacyState + M3 goalHierarchyState + B2 habitStrengthState. NOT Layer 3 extension — preserves 9-channel Layer 3 semantic.

## §2 Empirical Anchors (K=2 verified: 10 primary + 2 secondary)

- **Ryan, R. M., & Deci, E. L. (2000)** SDT and facilitation of intrinsic motivation. *Am Psychol* 55(1):68-78
- **Deci, E. L., & Ryan, R. M. (2000)** The "what" and "why" of goal pursuits. *Psych Inquiry* 11(4):227-268
- **Vansteenkiste, M., Ryan, R. M., & Soenens, B. (2020)** Basic psychological need theory. *Motivation and Emotion* 44(1):1-31
- **Chen, B., Vansteenkiste, M., et al. (2015)** BPNSFS across four cultures. *Motivation and Emotion* 39(2):216-236
- **Bartholomew, K. J., Ntoumanis, N., Ryan, R. M., & Thøgersen-Ntoumani, C. (2011)** PNTS scale. *JSEP* 33(1):75-102 (N-80 author correction — singular Thøgersen-Ntoumani, no trailing s)
- **Deci, E. L., & Ryan, R. M. (1985)** *Intrinsic Motivation and Self-Determination in Human Behavior.* Plenum
- **Cerasoli, C. P., Nicklin, J. M., & Ford, M. T. (2014)** *Psych Bull* 140(4):980-1008
- **Sheldon, K. M., & Hilpert, J. C. (2012)** BMPN scale. *Motivation and Emotion* 36:439-451
- **Ryan, R. M., & Deci, E. L. (2017)** *Self-Determination Theory.* Guilford (§22 canonical Leary sociometer ≠ SDT relatedness distinction)
- **Ng, J. Y. Y., Ntoumanis, N., et al. (2012)** SDT × health. *Perspectives* 7(4):325-340
- **Murphy et al. 2022** PMID 36442044 CONTESTED-MEASUREMENT (N-79 replaces original Heissel 2024 attribution; roadmap already corrected at)
- **Judge, T. A., & Ilies, R. (2002)** *JAP* 87(4):797-807 HEXACO composition

## §3 Architecture

**Substrate module:** `~/Projects/sim-ai/src/sim-ai/scenes/island/basicPsychNeed.ts` (~460 LOC)

**3 SDT needs (Ryan-Deci 2000 canonical):**
- autonomy (self-directed action)
- competence (effective interaction with environment; M4 SE anchor)
- relatedness (belonging/care; INDEPENDENT of M1 sociometer per Ryan-Deci 2017 §22)

**2 channels per need (Chen 2015 + Bartholomew 2011 empirically separate factors — NOT signed anti-correlated):**
- satisfaction (baseline 40)
- frustration (baseline 10)

**Asymmetric baselines** per Chen 2015 empirical: participants report higher baseline satisfaction than frustration on 7-pt Likert.

**Critical architectural constraint:** M5 substrate uses THEORETICAL 3×2 architecture per Bartholomew 2011 PNTS + Vansteenkiste 2020; NOT tied to BPNSFS scale operationalization (Murphy 2022 CONTESTED-MEASUREMENT critique is scale-artifact NOT theoretical).

**Critical distinction:** M5 relatedness_sat/frust INDEPENDENT of M1 self_esteem_b (Leary sociometer ≠ SDT relatedness per Ryan-Deci 2017 §22). H5 validity test verifies Pearson r ≤ 0.5 over 30 independent-stream simulations.

## §4 Wire Sites (6 in tickIslandWorld + 3 seed sites)

1. `createInitial2SimWorldState` + 2 seed variants: seed `basicPsychNeedState`
2. `tickIslandWorld` post-decay: `tickPsychNeedDecay`
3. `completeAction`: W1 autonomous goal complete → autonomy_sat + W2 M4 mastery → competence_sat
4. `detectAndApplyPairInteractions`: W3 share_food/comforted → relatedness_sat + W4 attacked_by → relatedness_frust
5. `decideNextAction`: W5 high autonomy_frust → F1 exit-adjacent action proxies (read only)
6. `decideNextAction`: W6 autonomy_frust → B2 habit-consonant action allowlist boost (read only)

## §5 Composition Wires (6)

- **W1** M3 autonomous goal completed → autonomy_sat +3 (Ryan-Deci 2000 + M3)
- **W2** M4 mastery source fired → competence_sat +3 (guarded read of M4 selfEfficacyState)
- **W3** share_food / comforted received → relatedness_sat +3 (Ryan-Deci 2000)
- **W4** attacked_by → relatedness_frust +5 (Bartholomew 2011 need thwarting)
- **W5** High autonomy_frust → F1 exit-adjacent action proxies (read only; Council #11 Item 198 discipline)
- **W6** High autonomy_frust → B2 habit-consonant action allowlist boost (forage_coconuts + drink_from_stream + rest + sleep)

## §6 Rule 19 Flags Surfaced

**CITATION-DRIFT:**
- N-79 K=2 CONVERGENT (Heissel 2024 → Murphy 2022 PMID 36442044) — roadmap already corrected
- **N-80** Bartholomew 2011 4th author = Thøgersen-Ntoumani (singular, no trailing s)

**CALIBRATION-CHOICE:**
- SDT_EVENT_DELTAS magnitudes
- Asymmetric baseline 40/10 (Chen 2015 empirical anchor)
- HEXACO composition magnitudes
- AUTONOMY_FRUST_HIGH_THRESHOLD = [omitted]

**EMPIRICAL-TRANSLATION:**
- W5 autonomy_frust → F1 exit-adjacent proxies
- W6 autonomy_frust → B2 habit-consonant action allowlist
- W2 M4 SE guarded read

**CONTESTED-MEASUREMENT:**
- BPNSFS scale operationalization per Murphy 2022 method-artifact critique
- Substrate uses THEORETICAL 3×2 per Bartholomew 2011 PNTS + Vansteenkiste 2020 — NOT scale-tied to BPNSFS

**REJECT-STALE:** None

## §7 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/basicPsychNeed.test.ts` (25 tests across 7 describe blocks)

- **H1 PRIMARY (Ryan-Deci 2000):** Sustained autonomous goal completion → autonomy_sat ≥15pp lift — **PASS**
- **H2 PRIMARY (Chen 2015 BPNSFS):** attacked_by cascade → relatedness_frust ≥15pp lift with relatedness_sat preserved (empirical factor separation) — **PASS**
- **H3 PRIMARY (Bartholomew 2011 PNTS):** frust events feed frust aggregate; sat events feed sat aggregate; cross-channel preservation verified — **PASS**
- **H4 VALIDITY (Judge-Ilies 2002 HEXACO):** high-C vs low-C competence_sat spread ≥ 0.2 — **PASS**
- **H5 VALIDITY (Ryan-Deci 2017 §22):** Leary sociometer ≠ SDT relatedness Pearson r ≤ 0.5 over N=30 independent-stream simulations — **PASS**

**Verdict:** PASS 5/5 @ 100% clear rate

## §8 Framework Methodology Firsts

- FIRST SDT substrate in framework (3×2 need architecture)
- FIRST 6-scalar compact world-scope module
- FIRST Leary sociometer / SDT relatedness distinction preserved in substrate (Ryan-Deci 2017 §22 canonical)
- SECOND Phase 2 Tier 2 mechanism (following M4 same day)

## §9 Deviations from Synthesis

**H5 test rewrite:** Initial synthesis-strict version used pseudorandom rates that inadvertently correlated (r ≈ 0.66). Rewritten with two independent LCGs per sample to genuinely decouple sociometer and relatedness event streams. Substrate architecture (separate perSim map, no shared reducer path) guarantees independence; the empirical test now verifies no hidden coupling.

**W6 arbitration proxy:** Synthesis specified reading M5's B2 boost via `chosen === 'habit'` + `primedActionId` check, but `lastArbitrationInfo` in existing state carries `dominantHabitualCount` + `anyMatch` only. Substituted with `dominantHabitualCount > 0` gate + habit-consonant action allowlist (forage_coconuts + drink_from_stream + rest + sleep). Read-only per Council #11 Item 198 discipline.

## §10 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/83 files
- sim-ai full test suite: **2263 passed** (baseline 2238 → +25 M5 tests via +25 net delta)
- sim-ai postmortem: 1 preexisting anomaly waived (signal_for_rescue_without_rescue_outcome; unrelated to M5)
- roomtolife precheck: GREEN (vendor-sync clean)

## §11 Council #11 Disposition

**RATIFY-PROVISIONAL M5 substrate + wire sites** on evidence:
- 12 K=2 verified empirical anchors (Rule 19 clean)
- Non-Inertness Gate PASS 5/5 @ 100% clear rate
- Follows M4/M3/B2 world-scope-module precedent
- Preserves Leary sociometer ≠ SDT relatedness distinction (Ryan-Deci 2017 §22)
- BPNSFS CONTESTED-MEASUREMENT properly bypassed via theoretical 3×2 architecture

**Council #11 candidacy sub-items filed:**
- **Item 193** M5 substrate ratification
- **Item 194** N-79 Heissel 2024 → Murphy 2022 PMID 36442044 K=2 CONVERGENT (roadmap corrected at)
- **Item 195** N-80 Bartholomew 2011 author correction (Thøgersen-Ntoumani singular)
- **Item 196** Leary sociometer ≠ SDT relatedness discipline (H5 anchor)
- **Item 197** BPNSFS scale operationalization deferred (Murphy 2022 CONTESTED-MEASUREMENT); framework uses theoretical 3×2 not scale-tied
- **Item 198** Downstream F1 exit / B2 arbitration explicit wires deferred to Ship 5+

## §12 Next Phase 2 Mechanism

Per roadmap Tier 2: **M6 attachmentBehavioralSystem** (Bowlby 4-component behavioral system).

**M6 K=2 anchor pair COMPLETE** (launched in parallel with M5 implementation):
- 11 primary anchors verified (Bowlby 1969/1982 + 1973 + 1980 + Mikulincer-Shaver 2003 + Fraley 2002 + Ainsworth 1978 + Main-Solomon 1990 + Hazan-Shaver 1987 + Brennan 1998 + Simpson-Rholes 2017 + Mikulincer-Shaver 2016)
- K=2 CONVERGENT: all 4 Bowlby components SHIPPABLE at 2-Sim scope; existing substrate leverage (`attachmentStyle.ts` + spatial + threat primitives + Main-Solomon classifier bridge)
- N-81/N-82/N-83 disambiguation candidacies + N-84 Waters 2000 NOT Waters-Beauchaine 2003 K=2 CONVERGENT
- Bowlby "4-phase" ambiguity → recommend "4-component behavioral system" per Mikulincer-Shaver 2003 canonical

**M6 integrated design synthesis:** `/tmp/m6-integrated-design-synthesis.md` (ready for implementation)

M6 COMPLETES Phase 2 Tier 2 upon ship.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
