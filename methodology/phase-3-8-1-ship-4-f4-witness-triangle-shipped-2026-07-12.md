# Phase 3.8.1 Ship 4 — F4 Sommerfeld Witness Triangle Activation — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai (co-ship w/S3 substrate) + (S3 test scaffold closure); roomtolife pushed

---

## §1 Scope

F4 Sommerfeld witness triangle activation at K≥3. Previously `witnessAntisocialAct` at :534 had 3-party-shaped signature but sole call site at `islandWorld.ts:~9405` (line drift from :8508 spec due to Ship 2/3 additions) passed `witnessId = targetSimId` (2-Sim victim=witness collapse — no true triangulation).

## §2 Architecture

### Activation site in detectAndApplyPairInteractions
For `aggress_toward_sim` events at K≥3:
- Gate: `isNSimMode(state) && simCount >= 3`
- Iterate all non-victim non-perpetrator Sims via `iterateAllSims` (Ship 1 primitive)
- **Proximity-gate:** filter by `WITNESS_OBSERVATION_RADIUS = [omitted]` (new CALIBRATION-CHOICE constant; DIRECTED-EXTRAPOLATION from Willis-Todorov 2006 close-contact range — Sommerfeld 2007 publishes no metric radius)
- Per witness: fire `witnessAntisocialAct` + `updateReputationFromDirect`

### Per-tick gossip propagation reducer
- Gossip listener discovery: `GOSSIP_LISTENER_RADIUS = [omitted]` + `GOSSIP_LISTENER_TRUST_THRESHOLD = [omitted]`
- Reputation updates propagate to listener's own reputation ledger via `updateReputationFromGossip`
- **Sommerfeld 2008 multi-source concordance amplification** auto-fires at listener reputation update

### Third-party sanction from gossip receivers
- At `SANCTION.BASE_RATE = [omitted]` (Fehr-Fischbacher 2003) × Balliet 2014 `d=0.32` ingroup amplifier (1.32×)
- Sanction reduces perpetrator's F2 dominance

### M9 composition wire
`applyGossipIntergroupDrift` (Ship 2 M9 wire exposed now consumed) — witness+victim ingroup vs perpetrator outgroup → intergroup perception drift.

## §3 Non-Inertness Gate Verdict — 33/33 PASS @ 100%

Test file: `~/Projects/sim-ai/src/sim-ai/scenes/island/ship4F4WitnessTriangle.test.ts`

- **H1 PRIMARY (Sommerfeld 2007 PNAS 104(44):17435-17440):** 6/6 PASS — K≥3 aggress_toward_sim event → all proximate non-victim non-perpetrator Sims fire witnessAntisocialAct
- **H2 PRIMARY (Sommerfeld 2008 Proc Roy Soc B):** 5/5 PASS — multi-source concordance amplifies reputation drop at 3+ witnesses
- **H3 PRIMARY (Fehr-Fischbacher 2003 Nature 425(6960):785-791):** 7/7 PASS — third-party sanction from gossip receivers at 60% base rate reduces perpetrator dominance
- **H4 VALIDITY (Balliet 2014 d=0.32 ingroup):** 4/4 PASS — M9 intergroup perception drift via applyGossipIntergroupDrift measurable
- **H5 VALIDITY:** 6/6 PASS — proximity-gate correctness (Sims outside WITNESS_OBSERVATION_RADIUS do NOT witness)
- Rule 28 K=2 backward-compat preservation: 5/5 PASS

## §4 Empirical Anchors (K=2 verified from Phase 1 Tier 2 F4 corpus)

- **Sommerfeld 2007** PNAS 104(44):17435-17440 (gossip-based indirect reciprocity)
- **Sommerfeld 2008** Proc Roy Soc B 275(1650):2529-2536 (multi-source concordance)
- **Fehr-Fischbacher 2003** Nature 425(6960):785-791 (60% third-party sanction)
- **Balliet 2014** Psych Bull 140(6):1556-1581 (d=0.32 ingroup amplifier)
- **Willis-Todorov 2006** (close-contact range for WITNESS_OBSERVATION_RADIUS extrapolation)

## §5 Rule 19 Flags Surfaced

**4 NEW CALIBRATION-CHOICE constants:**
- `WITNESS_OBSERVATION_RADIUS = [omitted]` (Sommerfeld 2007 publishes no metric radius; DIRECTED-EXTRAPOLATION from Willis-Todorov 2006)
- `URGENCY.EMISSION_THRESHOLD = [omitted]` (Feinberg 2012 physiological release direction anchor without empirical scalar)
- `GOSSIP_LISTENER_RADIUS = [omitted]` (grapevine face-to-face proximity extrapolation)
- `GOSSIP_LISTENER_TRUST_THRESHOLD = [omitted]` (Post 0116 modest-invested sentiment cutoff extrapolation)

**REJECT-STALE:** None

## §6 Framework Methodology Firsts

- FIRST F4 Sommerfeld witness triangle activation at K≥3 (3-party signature no longer collapsed)
- FIRST multi-source concordance amplification wire (Sommerfeld 2008 auto-fires at listener updateReputationFromGossip)
- FIRST third-party sanction from gossip receivers (Fehr-Fischbacher 60% × Balliet 1.32× reducing perpetrator F2 dominance)
- FIRST F4→M9 intergroup perception drift composition (applyGossipIntergroupDrift at witness-triangle + gossip-listener-receipt sites)
- FIRST parallel-flight co-ship with test-scaffold closure follow-up (S3+S4 shared sim-ai commit; e9af981 aligned S3 emit-fn field name expectations)

## §7 Ship Verification

- sim-ai typecheck: PASS
- sim-ai Rule 28 audit: CLEAN 0/87 files
- sim-ai full test suite: **2931 PASS** (baseline S2 close 2858 → +73 across S3+S4 co-ship; Ship 4 tests +33 exactly per spec)
- roomtolife precheck: PASS + vendor-manifest verify 255/255

## §8 Deviations from Spec

1. **Co-shipped with Ship 3 F2 Boehm** — Ship 3 code and test file already in working tree from prior session; Ship 4 imports depend on Ship 3's `formCoalitionGroupFromBoehm` wire being present. Shipped together in. Follow-up closed 17 remaining Ship 3 test-scaffold assertions (emit-fn metadata field alignment: cause→reason, duration_expired→duration_cap_reached, boehmExtraDecay).

2. **roomtolife IslandSimulation.tsx counter registration** — 7 new counter fields added to two `crossPlaneSnapshot.counts` baseline literals + switch dispatch cases (Ship 2 M9 x3 + Ship 3 F2 Boehm x3 + Ship 4 F4 x1) to satisfy vendored `CrossPlaneEventCount` interface shape. Downstream fanout from sim-ai substrate changes.

3. **K=2 backward-compat preservation** — witness-triangle block gates on `isNSimMode(state)`; K=2 mode continues existing 2-Sim victim=witness collapse code path bit-identical (H1a + Rule 28 preservation tests verify).

4. **Line drift note** — sole existing call site referenced at `islandWorld.ts:8508` in task spec; actual line is `~9405` in current tree due to interim Ship 2/3 additions. Semantics unchanged.

## §9 Council #11 Candidacy

**Item 234 filed:** Phase 3.8.1 Ship 4 F4 Sommerfeld witness triangle activation ratification.

Sub-items:
- 234.1 F4 witness triangle 3-party activation at K≥3
- 234.2 Per-tick gossip propagation reducer + concordance amplification
- 234.3 Third-party sanction from gossip receivers (Fehr-Fischbacher × Balliet)
- 234.4 F4→M9 intergroup perception drift composition
- 234.5 4 CALIBRATION-CHOICE constants
- 234.6 Parallel-flight co-ship + roomtolife counter registration cascade

## §10 Downstream Impact

**Enables Ships 5a+5b** (M1-M7 N-Sim composition wire propagation) + **Ship 6** (UI extensions) + **Ship 7** (N=8 performance harness).

Both parallel-flight ships (S3+S4) now complete. Ship 5a can proceed with M5+M1+M2+M3 low-risk wave.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
