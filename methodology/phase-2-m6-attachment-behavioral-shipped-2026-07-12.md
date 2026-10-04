# Phase 2 M6 attachmentBehavioralSystem SHIPPED — Third Tier 2 Mechanism (Tier 2 COMPLETE)
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate + wire sites shipped; downstream F1/F5/M4/D3 explicit mutations via helper exposure deferred to Ship 5+)
**Ship commits:** sim-ai + manifest; roomtolife pushed

---

## §1 Scope

Ships M6 attachmentBehavioralSystem — third Phase 2 Tier 2 mechanism. **COMPLETES Phase 2 Tier 2** (M4+M5+M6 all shipped 2026-07-12 same session as Tier 1 M1+M3+M2 = 6 mechanisms aggregate).

Bowlby 4-component behavioral system operationalized (Mikulincer-Shaver 2003 AESP 35 canonical framing per Council #11 Item 202 — NOT "4-phase" which refers to developmental sequence):
1. Proximity-seeking (softmax logit boost + hyperactivation/deactivation branch)
2. Safe-haven (attachment-style-modulated retreat routing)
3. Secure-base exploration (multiplier when partner co-located + alive)
4. Separation-protest (~200-tick acute Bowlby Vol 3 Stage 1; distinct from D4 chronic Stage 4)

**Leverages EXISTING substrate:** `attachmentStyle.ts` (Fraley-Waller-Brennan 2000 ECR-R + 4 discrete + classifier) + `pairRelationalPlane.ts` attachment consumption (17+ file consumers) + spatial primitives (`position.x/y`, `coLocatedTicks`, Chebyshev distance) + threat primitives (`EmergencyState`, `threatType`, `threatPosition`, `retreat_inside`) + Main-Solomon 1990 classifier bridge (from D4 ship 2026-07-12).

## §2 Empirical Anchors (K=2 verified: 11 primary + 3 secondary)

- **Bowlby, J. (1969/1982)** *Attachment and Loss, Vol. 1: Attachment.* Basic Books
- **Bowlby, J. (1973)** *Attachment and Loss, Vol. 2: Separation.* Basic Books
- **Bowlby, J. (1980)** *Attachment and Loss, Vol. 3: Loss.* Basic Books
- **Mikulincer, M., & Shaver, P. R. (2003)** Adult attachment behavioral system. *AESP* Vol 35:53-152
- **Mikulincer, M., & Shaver, P. R. (2016)** *Attachment in Adulthood* 2nd ed. Guilford
- **Fraley, R. C. (2002)** Attachment stability. *PSPR* 6(2):123-151
- **Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978)** *Patterns of Attachment.* Erlbaum
- **Main, M., & Solomon, J. (1990)** Disorganized/disoriented D-attachment. In *Attachment in the Preschool Years* pp. 121-160. U Chicago Press
- **Hazan, C., & Shaver, P. R. (1987)** *JPSP* 52(3):511-524
- **Brennan, K. A., Clark, C. L., & Shaver, P. R. (1998)** ECR chapter pp. 46-76. Guilford
- **Simpson, J. A., & Rholes, W. S. (2017)** *Curr Opin Psych* 13:19-24
- **Waters, E., Merrick, S., Treboux, D., Crowell, J., & Albersheim, L. (2000)** 20-year attachment stability. *Child Development* 71(3):684-689 (N-84 K=2 CONVERGENT correction from Waters-Beauchaine 2003)
- **Van IJzendoorn, M. H., & Kroonenberg, P. M. (1988)** Strange Situation cross-cultural. *Child Development* 59(1):147-156
- **Judge, T. A., & Ilies, R. (2002)** *JAP* 87(4):797-807 HEXACO composition

## §3 Architecture

**Substrate module:** `~/Projects/sim-ai/src/sim-ai/scenes/island/attachmentBehavioralSystem.ts` (~670 LOC with JSDoc)

**Attachment-style branching (Mikulincer-Shaver 2003 canonical):**
- Secure: monotonic + calibrated
- Anxious (hyperactivation): amplified proximity-seeking under low threat
- Avoidant (deactivation): suppressed proximity + flee-away safe-haven
- Disorganized: contradictory approach-avoid + unstable [-1, +1] flip

**Separation-protest 200-tick acute window** (Bowlby 1980 Vol 3 canonical Stage 1 protest distinct from D4 chronic Stage 4 detachment). Handoff to D4 when tick > separationTick + 200.

## §4 Wire Sites in `tickIslandWorld` (7)

1. `createInitial2SimWorldState` + biographies variant + injectSimB: seed `attachmentBehavioralState`
2. `tickIslandWorld` post-decay: `tickSeparationProtestDecay` + evaluate proximity-seeking activation
3. `updateEmergencyState`: hook safe-haven attachment-style routing (helper exposure per Council #11 Item 198)
4. `decideNextAction`: logit modulation helpers exposed (`computeF1LoyaltyBoostMultiplier` + `computeF5ForgivenessAccelMultiplier` + `computeM4ExplorationEfficacyBoost` + `computeD3CognitiveLoadMultiplier`); direct downstream mutation DEFERRED to Ship 5+
5. `partner_death` block (both directions): `checkSeparationProtestOnset`
6. `partner_rescued_departure` block: `checkSeparationProtestOnset` (M13 handoff)
7. Protest ledger → D4 chronic handoff when tick > separationTick + 200

## §5 Composition Wires (5)

- **W1** proximity-seeking activation → F1 loyalty boost (Bowlby + Rusbult) — helper exposed
- **W2** safe-haven activation → F5 forgiveness gate acceleration (secure = quicker repair) — helper exposed
- **W3** secure-base exploration active → M4 exploration_skill efficacy update boost (Bandura + Bowlby)
- **W4** separation-protest onset → D4 pre-chronic gate opens (Bowlby Vol 3 Stage 1 vs Stage 4)
- **W5** hyperactivation/deactivation → D3 empathic cognitive load modulator (Klimecki-Singer 2014 + Bowlby)

## §6 Rule 19 Flags Surfaced

**CITATION-CORRECTION:**
- **N-84 K=2 CONVERGENT** — Waters et al. 2000 Child Development 71(3):684-689 (NOT Waters-Beauchaine 2003 which was my original prompt error)

**CITATION-DISAMBIGUATION:**
- N-81 Van IJzendoorn 1996 AAI meta vs 1988 infant Strange Situation
- N-82 Feeney 2004 → Feeney-Collins 2004 chapter Rholes-Simpson Guilford pp. 300-338
- N-83 Roisman 2007 → Roisman et al. 2007 JPSP AAI-vs-self-report empirical

**CALIBRATION-CHOICE:** All BOWLBY thresholds + ATTACHMENT_STYLE_MULTIPLIERS + HEXACO_BOWLBY coefficients + M6_COMPOSITION multipliers + 200-tick window

**EMPIRICAL-TRANSLATION:** W1 proximity → F1 loyalty + W2 safe-haven → F5 acceleration + W4 protest → D4 pre-chronic gate

**CONTESTED-MODERATE:** Van IJzendoorn cross-cultural + Rothbaum 2000 critique (already in substrate); prototype vs revisionist stability resolved to revisionist per Council #11 Item 203 (Waters 2000 + Fraley 2002 + Roisman-Fraley 2013 evidence)

**REJECT-STALE:** None

## §7 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/attachmentBehavioralSystem.test.ts` (30 tests across 9 describe blocks)

- **H1 PRIMARY (Bowlby + Mikulincer-Shaver 2003):** stress > threshold → anxious ≥ secure ≥ avoidant logit ordering; ≥15pp hyperactivation lift — **PASS**
- **H2 PRIMARY (Bowlby safe-haven):** secure = flee_toward 100% + avoidant = flee_away 100% + anxious = freeze + disorganized = contradict — **PASS**
- **H3 PRIMARY (Bowlby secure-base):** partner co-located + low stress → exploration lift; partner absent/distant/dead → no boost — **PASS**
- **H4 VALIDITY (Waters 2000):** attachment-branch classification stable across 500 ticks in stable conditions (no substrate-side drift) — **PASS**
- **H5 VALIDITY (Bowlby Vol 3):** protest peaks 0-200 window; transitions to D4 chronic post-200; NO overlap in high magnitudes (protestLevel=0 once transitioningToChronic true) — **PASS**

**Verdict:** PASS 5/5 @ 100% clear rate

## §8 Framework Methodology Firsts

- FIRST Bowlby 4-component behavioral system substrate
- FIRST hyperactivation/deactivation branching per Mikulincer-Shaver 2003
- FIRST separation-protest ledger with D4 chronic handoff
- FIRST secure-base exploration Bowlby ↔ M4 SE composition
- FIRST attachmentStyle-behavioral bridging via existing classifier + spatial + threat primitives
- **COMPLETES Phase 2 Tier 2** (M4+M5+M6 all shipped same session as Tier 1 = 6 Phase 2 mechanisms aggregate)

## §9 Deviations from Synthesis

**Wire sites 3+4 kept as read-only helper exposure** per Council #11 Item 198 M5 precedent. Helpers `computeF1LoyaltyBoostMultiplier`, `computeF5ForgivenessAccelMultiplier`, `computeM4ExplorationEfficacyBoost`, `computeD3CognitiveLoadMultiplier` exposed; direct downstream mutation of F1/F5/M4/D3 state DEFERRED to Ship 5+. Preserves upstream test invariants; matches M5 exact composition-wire deferral pattern.

**Test count 30 vs target 28:** +2 observability tests (baseline slot fallback + HEXACO Openness modulation on secure-base). Matches M5 precedent.

**8 new CrossPlaneEventType candidates enumerated in module JSDoc header but NOT added to `crossPlaneTraceAggregator.ts`** — enum extensions deferred to observability polish ship per M5 precedent.

## §10 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/84 files
- sim-ai full test suite: **2293 passed** (baseline 2263 → +30 M6 tests)
- sim-ai postmortem: 1 preexisting anomaly waived (signal_for_rescue_without_rescue_outcome unrelated to M6)
- roomtolife precheck: GREEN (237 vendored files)

## §11 Council #11 Disposition

**RATIFY-PROVISIONAL M6 substrate + wire sites** on evidence:
- 14 K=2 verified empirical anchors (Rule 19 clean)
- Non-Inertness Gate PASS 5/5 @ 100% clear rate
- Leverages existing substrate (attachmentStyle.ts + spatial + threat + Main-Solomon bridge)
- Helper-exposure discipline per M5 precedent (composition-scope reads without direct mutation)

**Council #11 candidacy sub-items filed:**
- **Item 199** M6 substrate ratification
- **Item 200** N-81/N-82/N-83 Van IJzendoorn/Feeney-Collins/Roisman disambiguation
- **Item 201** N-84 Waters 2000 NOT Waters-Beauchaine 2003 (K=2 CONVERGENT)
- **Item 202** Bowlby "4-phase" ambiguity → "4-component behavioral system" per Mikulincer-Shaver 2003 canonical
- **Item 203** Prototype vs revisionist stability → revisionist chosen (Waters 2000 + Fraley 2002 + Roisman-Fraley 2013)
- **Item 204** Downstream v2 items deferred (multi-figure hierarchies + intergenerational + working-models continuity)

## §12 Next Phase 2 Mechanism

**Tier 2 COMPLETE.** Next per roadmap Tier 3 (speculative empirical uncertainty per line 72): **M7 traumaAppraisalCoping** (Lazarus-Folkman + Meichenbaum + DSM-5 PTSD; extends D4 general trauma).

**M7 K=2 anchor pair in flight** (launched in parallel with M6 implementation).

Tier 3 recommended order per roadmap: M7 → M9 → M8.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
