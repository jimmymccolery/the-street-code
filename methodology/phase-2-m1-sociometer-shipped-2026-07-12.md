# Phase 2 M1 sociometerSelfEsteem SHIPPED — First Phase 2 Mechanism
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (substrate + tests + wire sites shipped; downstream compositions to F1/D5/D3/F5 deferred to Phase 2 Ship 1)
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

Ships M1 sociometerSelfEsteem — first mechanism from Phase 2 lifelikeness roadmap draft (methodology/phase-2-lifelikeness-roadmap-draft-2026-07-12.md). Adds 9th Layer 3 accumulator channel `self_esteem_b` per Leary-Baumeister 2000 sociometer theory.

**Substrate architecture:** Extends Post 0146 ten-layer NPC architecture with 9th Layer 3 channel following exact `relational_integrity_b` (R10d Dimension 4) + `communal_standing_b` (Post 0185 Wireduan generosity-ledger) precedent. No new world-scope state field required — sociometer state lives in `Layer3State.self_esteem_b` per-Sim.

## §2 Empirical Anchors (K=2 verified via WebSearch)

- **Leary, M. R., & Baumeister, R. F. (2000)** The nature and function of self-esteem: Sociometer theory. *AESP*, Vol. 32, pp. 1–62. Academic Press.
- **Leary, M. R., Tambor, E. S., Terdal, S. K., & Downs, D. L. (1995)** Self-esteem as an interpersonal monitor: The sociometer hypothesis. *JPSP*, 68(3), 518–530. (5 studies N≈400 total; ostracism → state self-esteem drop d≈0.7)
- **Anthony, Wood, & Holmes (2007)** *JESP*, 43(3), 425-432. Intimate-interaction reassurance repair.
- **Denissen, Penke, Schmitt & Van Aken (2008)** *JPSP*, 95(1), 181-196. Daily-level intraindividual variance around trait mean.
- **MacDonald & Leary (2005)** *Psych Bull*, 131(2), 202-223. Social exclusion pain overlap.
- **Robins, Trzesniewski, Tracy, Potter, & Gosling (2001)** *JRP*, 35(4), 463-482. Self-esteem × personality correlations (r_Extraversion=+0.38; r_Neuroticism=-0.50).

## §3 Architecture

**Substrate additions:**
- `Layer3State.self_esteem_b?: number` (9th channel; 0-100 scale; baseline 50)
- `LAYER3_BASELINE.self_esteem_b = 50`
- `applySelfEsteemDelta(state, delta)` helper (mirrors `applyRelationalIntegrityDelta` + `applyCommunalStandingDelta`)
- `computeSelfEsteemCharacterBaseline(hexaco)` HEXACO composition function
- `applyDecay` signature extended with 4th arg `selfEsteemBaseline`
- 10 event delta constants

**HEXACO character baseline formula** (Robins 2001 anchors):
```
baseline = 50
  [weighted personality term omitted]
clamped [10, 90]
```

**Event delta constants:**
- `SELF_ESTEEM_ATTACKED_BY_DELTA = [omitted]` (strongest ostracism analog per Leary 1995 d≈0.7)
- `SELF_ESTEEM_RESOURCE_CONFLICT_DELTA = [omitted]`
- `SELF_ESTEEM_GRIEVANCE_RECORDED_DELTA = [omitted]`
- `SELF_ESTEEM_PARTNER_RESCUED_DEPARTURE_DELTA = [omitted]`
- `SELF_ESTEEM_NEGATIVE_GOSSIP_TARGET_DELTA = [omitted]`
- `SELF_ESTEEM_WITNESSED_AGGRESSION_DELTA = [omitted]` (3-Sim reserved)
- `SELF_ESTEEM_GIFT_GIVEN_DELTA = [omitted]`
- `SELF_ESTEEM_COMFORTED_DELTA = [omitted]` (Anthony-Wood-Holmes 2007 reassurance)
- `SELF_ESTEEM_WARNED_OF_DANGER_DELTA = [omitted]`
- `SELF_ESTEEM_FORGIVENESS_GRANTED_DELTA = [omitted]` (repair asymmetry)

**Wire sites (6 in tickIslandWorld):**
1. `applyDecay` call site (both Sim A + Sim B) with HEXACO-derived character baseline
2. `attacked_by`: target Layer 3 -12 (strongest ostracism analog)
3. `share_food` recipient: +3
4. `comforted` recipient: +2.5
5. `warned_of_danger` recipient: +1.5
6. `grievance_recorded` (victim): -4 (rejection-cue on top of attacked_by primary hit)

## §4 Rule 19 Flags Surfaced

**CALIBRATION-CHOICE:**
- HEXACO H coefficient (-0.05) K=2 FLAG — Robins 2001 uses Big Five (no H); direction inferred from Zeigler-Hill 2013 chapter (HEXACO-adjacent secondary)
- Magnitude values (attacked_by -12, gift_given +3, etc.) all CALIBRATION-CHOICE per Council #11 Item 163 pattern

**EMPIRICAL-TRANSLATION:**
- Wieselquist 1999 × SE F1 composition — architectural extrapolation (Wieselquist reports commitment × trust; SE composition K=2 flag)
- Klimecki-Singer 2012 CF acceleration by low SE — architectural rationale only; magnitude CALIBRATION-CHOICE
- Bandura 1997 vicarious mastery for D3 lift — architectural rationale only

## §5 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/sociometerSelfEsteem.test.ts` (19 tests)

**H1 primary (ostracism producing measurable drop):** PASS — 3 sequential attacked_by events produce 36pp drop > Council #9 base 15pp threshold

**H2 validity (forgiveness repair reversal):** PASS — forgiveness_granted > grievance_recorded avoidance level

**H3 validity (prosocial-received lift):** PASS — gift_given + comforted lifts sociometer above baseline

**Preservation harness:** 1000-iter applyDecay cycle bounded [0, 100]; sign directions verified

**Verdict:** PASS 19/19 @ 100% clear rate

## §6 Framework Methodology Firsts

- **FIRST Phase 2 mechanism SHIPPED** (opens Phase 2 lifelikeness roadmap execution)
- **FIRST 9th Layer 3 accumulator channel** (extends Post 0146 ten-layer architecture beyond guilt_b 8th; canonical extension pattern preserved per Post 0185 precedent)
- **FIRST HEXACO-derived character-baseline computation for a Layer 3 channel** (computeSelfEsteemCharacterBaseline; extends existing ExtendedBiographicalTemplate baseline discipline)
- **FIRST intra-Sim sociometer channel** (complementary mirror of communal_standing_b external social-standing accumulator; closes internal-perception-of-relational-value gap flagged in Phase 2 roadmap agent findings as "largest Layer 3 architectural gap")

## §7 Downstream Compositions (Deferred to Phase 2 Ship 1)

Per Phase 2 roadmap Ship 1 scope:
- Low sociometer → **F1 EVLN exit-vs-voice threshold shift** (Wieselquist 1999 commitment × self-esteem interaction K=2 flag)
- Low sociometer → **D5 shame Attack-Self amplifier** (Nathanson 1992 self-derogation loop)
- Low sociometer → **D3 empathic-distress-fatigue accelerator** (Klimecki-Singer 2012 self-worth cost of empathy)
- Low sociometer → **F5 grievance severity inflation** (perceived harm greater when self-esteem low)

## §8 Ship Verification

- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/79 files
- sim-ai full test suite: **2147 passed** (baseline 2128 → +19 sociometer tests)
- roomtolife precheck: PASS (227 vendored files verified)

## §9 Council #11 Disposition

**RATIFY-PROVISIONAL M1 substrate + wire sites** on evidence:
- 6 K=2 verified empirical anchors
- Non-Inertness Gate PASS 19/19 @ 100%
- Follows exact Post 0185 + R10d Dimension 4 canonical precedent
- Extends ten-layer architecture (Post 0146) without disrupting existing 8 channels

**Council #11 candidacy sub-items:**
- Item 175 M1 sociometer substrate ratification
- Item 176 K=2 verification of HEXACO H → SE direction (Robins 2001 Big-Five-only; Zeigler-Hill 2013 chapter secondary)
- Item 177 Downstream composition wires deferred (F1/D5/D3/F5) — Phase 2 Ship 1 scope

## §10 Next Phase 2 Mechanism

Per Phase 2 roadmap recommended order: **M3 autonomousGoalHierarchy** — Carver-Scheier 1998 + Locke-Latham 2002 + Gollwitzer 1999 implementation intentions d+=0.65. Larger scope than M1 (per-Sim goal tree ~3 levels + 5-8 goal categories). Bridges B2 automaticity with autonomous goal-setting; universal commercial precedent per Agent B findings.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Repository:** `~/Projects/the-street-code/methodology/`
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
