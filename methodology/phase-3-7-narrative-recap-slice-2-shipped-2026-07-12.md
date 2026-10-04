# Phase 3.7 Narrative Recap Slice 2 (Layer 4 midHorizon) — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** sim-ai; roomtolife pushed

---

## §1 Scope

Post-Phase-1 close-out §9 option #7 executed. Ships Slice 2 substrate + UI per Kreminski Loose Ends + Park 2023 reflection depth extension + Wildermyth Legacy Scrapbook + RimWorld anti-pattern toast overlay + DF Legends-Mode Chronicle scroll + autonomous directionlessness detector.

**Slice 1 preserved:** 33 existing tests still PASS; 77/77 narrative recap tests green aggregate.

**Slice 3 (Qud rationalization + Wildermyth Legacy carryover + Synthesifter) DEFERRED** per Agent 5 boundary review — product-scope not substrate-scope.

## §2 Substrate Extensions

**New state primitives:**
- `OpenPlotThread { threadId, openedAtTick, description, participants: SimId[], ttlTicks: 500 }`
- `ClosedPlotThread { threadId, closedAtTick, closureReason }`
- `ScrapbookEntry { epochStart, epochEnd, keyLandmarks: LandmarkEvent[], beliefSnapshot }`
- `ChronicleEntry { tick, actor: SimId | 'world', event, importance }`
- `threadOpenCloseHistory: readonly (OpenPlotThread | ClosedPlotThread)[]`

**7 new pure functions** (5 spec + 2 additions):
- `detectDirectionlessness(state, simId, tick): boolean`
- `applyDirectionlessnessDetection` (reducer wrapper — separates detection from side-effect per H5 discipline)
- `advanceScrapbookEpoch(state, tick): NarrativeRecapState`
- `appendToChronicle(state, entry): NarrativeRecapState`
- `getToastCandidates(state, tick): OpenPlotThread[]`
- `getBeatToastCandidates` (beat-scope UI surface)
- `emitDepthOneMetaBelief(state, simId, tick): NarrativeRecapState`

**Extended existing:**
- `ingestLandmarkEvent` — spawns OpenPlotThread on {rivalry_to_reconciliation, prestige_acquisition, grief_trajectory_shift, rescue_departure}
- `consolidateReflection` — Park 2023 belief accretion with depth escalation
- `tickPlotThreadExpiration` per-tick maintenance (unlisted addition — TTL enforcement)

## §3 UI Extensions (roomtolife §10.7 NarrativeRecapPanel)

- Open-thread sub-panel (active OpenPlotThread list with elapsed ticks)
- Toast overlay (RimWorld-style notification bounded max 3 concurrent)
- Scrapbook drawer (per-epoch landmark digest)
- Chronicle scroll (DF Legends-Mode + CK2 chronicle-fill analog per Agent 5 correction)
- Directionlessness badge (visible when Sim directionless > 200 ticks)

## §4 Empirical Anchors (K=2 verified from Slice 1 + Agent 5 research)

- **Kreminski Loose Ends** AIIDE 2022 — OpenPlotThread pattern
- **Park 2023 UIST** reflection subsystem — depth-1 meta-belief
- **RimWorld toast anti-pattern** — Fable 5 dossier §2 + RimWorld Wiki
- **DF Legends-Mode Chronicle** analog — Agent 5 correction (NOT CK3; CK3 has per-character Memory Viewer only)
- **CK2 chronicle-fill** — legacy narrative source pattern
- **Wildermyth Legacy Scrapbook** — commercial anchor
- **Qud (Grinblat-Bucklew 2017)** — Slice 3 deferred
- **Synthesifter (Kreminski INT 2020)** — Slice 3 deferred

## §5 Non-Inertness Gate Verdict

Test file: `~/Projects/sim-ai/src/sim-ai/narrativeRecapSlice2.test.ts` (44 tests across 8 describe blocks; +2000-iter preservation harness)

- **H1 PRIMARY (Kreminski Loose Ends):** OpenPlotThread spawned per closed match of 4 baseline patterns — PASS (8 §1 tests)
- **H2 PRIMARY (Park 2023 reflection depth):** depth-1 meta-belief at importance sum threshold; escalation monotone — PASS (6 §6 tests)
- **H3 PRIMARY (RimWorld anti-pattern):** toast candidate emission bounded max 3 concurrent; overflow discarded — PASS (5 §5 tests)
- **H4 VALIDITY (Wildermyth Legacy):** ScrapbookEntry preserves belief snapshot across epoch boundaries; no field-nuke — PASS (5 §3 tests)
- **H5 VALIDITY (directionlessness detector):** landmark absence + goal stagnation → detects within 200-tick sensitivity window — PASS (7 §2 tests including hysteresis)

**Verdict:** PASS 5/5 @ 100% clear rate

## §6 Rule 19 Flags Surfaced

**CK3 ATTRIBUTION CORRECTION APPLIED** per Agent 5 research: Chronicle rebranded as DF Legends Mode + CK2 chronicle-fill analog; CK3 has per-character Memory Viewer only. Comments + tooltips reflect this.

**CALIBRATION-CHOICE:**
- `DIRECTIONLESSNESS_RATIO_THRESHOLD = [omitted]` (documented in constant)
- `EPOCH_TICK_DURATION = [omitted]` (semantic-caution documented)

**DIRECTED-EXTRAPOLATION:**
- `PLOT_THREAD_TTL_TICKS = [omitted]` (Loose Ends is mixed-initiative human-driven; substrate needs autonomous closure)

**K=1 flags (defer to K=2 verification):**
- OpenPlotThread state-shape K=1 pending PDF re-read of LooseEnds_AIIDE2022.pdf
- Chronicle cross-actor aggregation K=1 commercial-precedent-only
- Park 2023 K=1 believability ablation carries forward from Slice 1

**REJECT-STALE:** None

## §7 Deviations from Spec

**Test count 44 vs target ~30:** +14 above target. Extra tests from 7 §2 directionlessness + 5 §5 toast exceeding "3 tests per section" scope. Chose full coverage since H1-H5 hypotheses each warranted multiple boundary tests.

**Function additions beyond spec (2):**
1. `tickPlotThreadExpiration` per-tick maintenance — TTL expiration would otherwise only fire on landmarks; needed for autonomous closure discipline per Rule 19 DIRECTED-EXTRAPOLATION
2. `applyDirectionlessnessDetection` reducer wrapper alongside pure predicate — separates detection (H5 hypothesis test) from side-effect (chronicle append + hysteresis lock)
3. `getBeatToastCandidates` alongside `getToastCandidates` — thread-scope + beat-scope toast surfaces both needed by UI; H3 discipline preserved (non-mutating)

## §8 Framework Methodology Firsts

- FIRST OpenPlotThread substrate (Kreminski Loose Ends adaptation)
- FIRST autonomous directionlessness detector
- FIRST toast letter overlay signal (RimWorld anti-pattern with cap discipline)
- FIRST Scrapbook epoch consolidation
- FIRST Chronicle scroll (DF Legends-Mode analog per Agent 5 CK3 correction)
- FIRST Park 2023 reflection depth-1 emission at substrate scope
- FIRST Layer 3 encoding-time snapshot on beliefs

## §9 Ship Verification

- sim-ai typecheck: CLEAN (`npx tsc --noEmit --skipLibCheck`)
- sim-ai Rule 28 audit: CLEAN 0/85 files
- sim-ai full test suite: **2621 total** (2620 pass + 1 preexisting phaseDMeasurement H32g wall-clock flake documented; passes on isolation re-run; baseline 2577 → +44 Slice 2 tests)
- sim-ai postmortem: 2 preexisting anomalies (Item 164 rescue calibration; waived)
- roomtolife `npm run precheck`: GREEN (Vercel build; 13/13 static routes; verify-vendor 247/247 files)

## §10 Council #11 Candidacy

**Item 219 filed:** Phase 3.7 Narrative Recap Slice 2 Layer 4 midHorizon ratification.

Sub-items:
- 219.1 OpenPlotThread substrate + autonomous TTL closure discipline
- 219.2 Autonomous directionlessness detector with 200-tick hysteresis
- 219.3 Toast overlay bounded max 3 concurrent (RimWorld anti-pattern)
- 219.4 Scrapbook epoch consolidation (Wildermyth Legacy adaptation)
- 219.5 Chronicle DF Legends-Mode analog (CK3 correction applied)
- 219.6 Park 2023 depth-1 meta-belief substrate emission

## §11 Downstream Impact

**Enables Phase 3.8 Group substrate Path A** — narrative recap can span multi-Sim goal/pattern threads once group substrate ratified.

**Slice 3 (Qud + Wildermyth Legacy carryover + Synthesifter)** deferred to Phase 3+ per product-substrate boundary review.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
