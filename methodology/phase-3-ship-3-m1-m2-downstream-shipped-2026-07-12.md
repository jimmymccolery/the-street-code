# Phase 3 Ship 3 M1 + M2 Downstream Composition Wires — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

First Phase 3 composition wire cascade ship. Activates 7 wires deferred from Phase 2 Ship 1 (M1 downstream) + Ship 3 (M2 dormant helpers activation).

**M1 sociometer downstream (4 wires from M1 §7 deferrals):**
- W1 low SE (< 35) → F1 EVLN exit-vs-voice threshold shift (Wieselquist 1999)
- W2 low SE (< 30) → D5 shame Attack-Self amplifier (Nathanson 1992 self-derogation)
- W3 low SE (< 35) → D3 empathic-distress-fatigue accelerator (Klimecki-Singer 2012)
- W4 low SE (< 35) → F5 grievance severity inflation (perceived-harm-greater-when-SE-low)

**M2 appraisal downstream (3 dormant helpers activated to direct mutation):**
- W5 M2 norm_compatibility < -0.4 → D5 moralEmotionsLedger amplifier (`computeD5NormViolationAmplifier` direct)
- W6 M2 agency=other → F5 attribution charitability (`computeF5CharitabilityAdjustment` DORMANT→ACTIVE)
- W7 M2 Higgins collapsed self-worth-threat > 0.5 → M1 sociometer amplification at ostracism-cascade sites (attacked_by + grievance_recorded)

## §2 Empirical Anchors (K=2 verified; all traced to existing K=2 corpus)

- **Wieselquist, Rusbult, Foster, Agnew (1999)** commitment × SE F1 EVLN threshold
- **Nathanson (1992)** *Shame and Pride* Compass of Shame Attack-Self branch
- **Klimecki, Singer (2012)** empathic-distress-fatigue self-worth cost
- **Struthers (2008)** attribution × apology charitability
- **Higgins (1987)** *Psych Review* 94(3):319-340 CONTESTED-MODERATE (collapsed self-worth-threat channel per M2 Item 184 discipline)

## §3 Architecture

Modified consumer modules:
- `accommodationResponse.ts` — W1 selfEsteemB softmax input
- `moralEmotionsFamily.ts` — W2 routeCompassOfShame extension (30% RNG-sampled Attack-Self override per deterministic-branching preservation)
- `empathyDualSystem.ts` — W3 tickCompassionFatigue selfEsteemB param
- `forgivenessProcess.ts` — W4 activateGrievance perceiverSelfEsteemB + W6 charitabilityAdjustment
- `islandWorld.ts` — 7 wire sites (F1:5003, D5 shame:7410, D3 CF:2971/2976, F5 grievance:4975/7355, W5:3317, W6:2873, W7:7296/7387)

**W7 architectural note:** applied at ostracism-cascade sites (attacked_by SE delta + grievance-recorded SE delta) using inline HIGGINS_COLLAPSED constant reads. Existing `computeM1SociometerAmplifier` signature preserved (agency=self scope only — Phase 2 M2 v1 backward-compat). W7 broadens amplifier reach at physical ostracism sites where self-worth-threat elevated. Additive overlay preserved.

## §4 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship3M1M2Downstream.test.ts` (37 tests: W1-W7 wire-by-wire + H1-H5 + backward-compat)

- **H1 PRIMARY (Wieselquist 1999):** low SE Sim → ≥15pp F1 exit lift — PASS
- **H2 PRIMARY (Nathanson 1992):** low SE Sim → ≥15pp shame Attack-Self selection lift over 500 trials — PASS
- **H3 PRIMARY (Klimecki-Singer 2012):** low SE Sim → CF accum rate above baseline — PASS
- **H4 VALIDITY (Struthers 2008):** M2 agency=other → F5 charitability delta ≥0.15 — PASS
- **H5 VALIDITY (Higgins collapsed):** M2 self-worth-threat > 0.5 → M1 SE delta × 1.5 measurable in ostracism cascade — PASS

**Verdict:** PASS 5/5 @ 100% clear rate

## §5 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE:**
- SE thresholds 35 (W1/W3/W4) + 30 (W2)
- F1 logit magnitudes +0.15 exit / -0.10 voice (W1)
- 30% W2 Attack-Self override rate (Nathanson 1992 direction anchor; magnitude EMPIRICAL-TRANSLATION)
- [omitted]× W3 CF factor
- [omitted]× W4 grievance severity
- 0.7/1.3 W6 F5 charitability adjustments
- [omitted]× W7 amplifier per M2 v1 HIGGINS_COLLAPSED constants preservation

**EMPIRICAL-TRANSLATION:**
- W2 30% override formulation (deterministic RNG per-tick) vs "boost prob by +30%" continuous formulation — architectural choice preserving deterministic-branching discipline; H2 gate verifies ≥15pp Attack-Self lift over 500 trials
- W7 amplifier extension to physical ostracism sites (attacked_by + grievance_recorded) beyond M2 v1 agency=self scope

**CONTESTED-MODERATE preserved:**
- Higgins 1987 collapsed self-worth-threat channel per M2 Item 184 discipline
- No dejection-vs-agitation dissociation introduced at Ship 3

**REJECT-STALE:** None

## §6 Framework Methodology Firsts

- FIRST activation of amplifier-helper DORMANT-to-DIRECT pattern (M2 helpers)
- FIRST M1 sociometer 4-wire downstream cascade (F1/D5/D3/F5)
- FIRST Phase 3 composition wire ship
- FIRST deterministic-branching preservation on RNG-sampled override (W2 vs continuous formulation)
- FIRST W7 amplifier reach extension without signature change (backward-compat scope broadening at consumer sites)

## §7 Deviations from Spec

**W2 formulation:** probability-30% RNG-sampled deterministic override rather than continuous "boost prob by +30%" — preserves deterministic-branching architecture. H2 gate passes with ≥15pp Attack-Self lift over 500 trials.

**W7 amplifier scope:** inline HIGGINS_COLLAPSED constant reads at ostracism-cascade sites, not extending `computeM1SociometerAmplifier` signature. Preserves M2 v1 wire site #6 backward-compat.

**Deferred per M2 §5 v2+:** M2-W1 (D3 vicarious via Wondra-Ellsworth 2015) + M2-W2 (D4 trajectory sense-making via Folkman 1997) — spec listed only W5/W6/W7 for M2 downstream at Ship 3. Wondra-Ellsworth D3 + Folkman D4 remain v2+ per M2 candidacy §5.

## §8 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/85 files
- sim-ai full test suite: **2415 total** (2414 pass + 1 preexisting phaseD flaky documented environmental flake; baseline 2378 → +37 M1/M2 downstream tests)
- sim-ai postmortem: 1 preexisting anomaly (signal_for_rescue_without_rescue_outcome; reproduces at baseline; waived per rescue-arrival calibration issue unrelated to composition wires)
- roomtolife `verify-vendor` PASS + precheck GREEN

## §9 Council #11 Candidacy

**Item 213 filed:** Phase 3 Ship 3 M1 + M2 downstream composition wire ratification.

Sub-items:
- 213.1 M1 SE < 35/30 threshold discipline (W1-W4)
- 213.2 M2 dormant helper activation discipline (W5/W6/W7)
- 213.3 W2 30% RNG-sampled override deterministic-branching preservation
- 213.4 W7 amplifier reach extension backward-compat pattern
- 213.5 Higgins CONTESTED-MODERATE collapsed-channel discipline preserved

## §10 Downstream Impact

**Enables Phase 3 Ship 4** (M4 downstream — 3 wires; independent).

**Deferred M2 v2+:** Wondra-Ellsworth 2015 D3 vicarious + Folkman 1997 D4 trajectory sense-making per M2 §5.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
