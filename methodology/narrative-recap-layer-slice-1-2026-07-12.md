# Narrative Recap Layer — Slice 1 MVP Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL (Slice 1 shipped; slices 2+3 deferred; Council #11 review window when opened)
**Substrate ship:** sim-ai (code) + (manifest); roomtolife commit pending in same session
**Cross-refs:**
- `fable-5-story-sifting-dossier-2026-07-09.md` — full 265-line story-sifting literature dossier that seeded this candidacy
- `fable-5-stage-7-sift-layer-spec-2026-07-09.md` — prior spec that this candidacy operationalizes
- `track-1c-reagan-arc-close-out-2026-07-09.md` — Reagan 6-arc classifier substrate (adjacent; consumed at Open Alley)

---

## §1 Motivation

Grok voice brainstorm 2026-07-11 (session transcript captured in-thread) surfaced the observation: the framework's substrate emits ~30 event types across dominance/prestige/pair-relational/rescue/co-shelter/grief mechanisms, but **has no player-facing surface that narrativizes them**. The dashboards render Layer 3 accumulators + landmarks + cross-plane events, which is research/observability, not gameplay.

Fable 5 independently identified the same gap in the story-sifting dossier §Cross-cutting observation §5.1: "Only Dwarf Fortress, Caves of Qud, and (partially) Talk of the Town treat narrative shape recognition as a first-class problem the way the academic story-sifting literature does; RimWorld, CK3, and The Sims solve the adjacent-but-distinct problem of pacing or content-triggering from structured event/memory state without attempting to recognize which sequences constitute a 'story' worth surfacing."

**Two independent convergences on the same finding qualify per Rule 11 substrate-diversity + K=2 quorum discipline.**

## §2 Architecture Summary

Slice 1 ships 6 architectural pieces at `sim-ai/src/sim-ai/scenes/island/narrativeRecap.ts`:

1. **NarrativeBeat** — LandmarkEvent + computed salience + novelty + valenceSign
2. **SiftingPattern grammar** (Kreminski Felt/Winnow lineage): `EventClause` with logic-variable binding `?a` + `?b` + `NegativeClause` for `unlessBetween` constraint. MVP ships 4 patterns: `rivalry_to_reconciliation`, `prestige_acquisition`, `grief_trajectory_shift`, `rescue_departure`.
3. **PartialMatch pool** (Winnow incremental acceptor semantics) with `MAX_ACTIVE_PARTIAL_MATCHES = [omitted]` cap (conservative for 2-Sim scope; Kreminski Winnow report 912ms/event at 1000 concurrent).
4. **Select-the-Unexpected unexpectedness** score with per-pattern per-role property frequency table + additive Laplace smoothing (k=1). K=1 flag: exact scoring formula (geometric vs arithmetic mean) UNVERIFIED; MVP uses arithmetic mean; document as ASSUMED.
5. **Belief struct** (Park 2023 non-LLM analog): `targetKind + targetId + valenceToward + arousalToward + confidence + sourceRefs + parentBeliefRefs + depth + importance`. Consolidated via clustering visibleBeats by target + weighted-mean valence + sigmoid confidence `1 - exp(-k · Σsalience)` with `CONFIDENCE_K = [omitted]`.
6. **HEXACO composition** (framework extension; no empirical anchor — needs own Non-Inertness Gate): Openness lowers reflection threshold via `effectiveThreshold = [formula omitted]`; Emotionality amplifies belief valence via `valenceAmplifier = [formula omitted]`.

Reducer wiring at islandWorld.ts:
- `narrativeRecap?: NarrativeRecapState | null` field on IslandWorldState
- `ingestLandmarkEvent` call at `fireLandmarkEvent` (every landmark → beat)
- `shouldTriggerReflection` + `consolidateReflection` call per Sim in tickIslandWorld main loop
- `decayBeliefs` call at 500-tick cadence

UI at roomtolife `IslandStage345Panels.tsx §10.7 NarrativeRecapPanel`:
- Per-Sim chronological beat log (last 15) with witness-gated visibility (CK3 Memory Viewer precedent)
- Salience-weighted valence coloring (positive green / negative red)
- Belief accretion display (top 5 by confidence) with target + valence direction + confidence %
- Story-shape recognitions display (closed sifting matches with surface rank + headline)

## §3 Empirical Anchors

### K=2 verified
- **Kreminski, Dickinson, Wardrip-Fruin 2019** "Felt: A Simple Story Sifter" ICIDS 2019 LNCS 11869 pp.267-281 — primitive sifting-pattern grammar (event predicates + logic-variable binding).
- **Kreminski, Dickinson, Mateas 2021** "Winnow: A DSL for Incremental Story Sifting" AIIDE 2021 — incremental acceptor semantics; `unlessBetween` negative constraint syntax quoted verbatim in agent-verified search results.
- **Kreminski, Dickinson, Wardrip-Fruin, Mateas 2022** "Select the Unexpected" ICIDS 2022 LNCS 13762 pp.292-308 — rarity-inverted ranking (verbal quote of heuristic definition verified K=2; exact formula K=1 flagged).
- **Kreminski et al 2022** "Loose Ends: A Mixed-Initiative Creative Interface" AIIDE 2022 18(1):120-128 (Best Artifact) — plot threads as first-class primitive.
- **Kreminski, Mateas 2021** "Toward Narrative Instruments" ICIDS 2021 (Best Short Paper finalist) — retellings + authorship-oriented play framing.
- **Grinblat, Bucklew 2017** "Subverting historical cause & effect: generation of mythic biographies in Caves of Qud" FDG 2017 — rationalization pass (deferred to slice 3).
- **Reagan, Mitchell, Kiley, Danforth, Dodds 2016** "The emotional arcs of stories are dominated by six basic shapes" EPJ Data Science 5:31 DOI:10.1140/epjds/s13688-016-0093-1 — 6 fortune-arc shapes (framework's Track 1c already implements at Open Alley).

### K=1 flagged
- **Park, O'Brien, Cai, Morris, Liang, Bernstein 2023** "Generative Agents: Interactive Simulacra of Human Behavior" UIST arXiv:2304.03442. Reflection subsystem details verified from paper text. **K=1 flag:** believability ablation Cohen's d=8.16 is single-study; no independent replication located.
- **Kreminski Select-the-Unexpected exact scoring formula** (geometric vs arithmetic mean; Laplace smoothing detail). Verbal quote K=2 verified; formula K=1 flagged. MVP uses arithmetic mean + Laplace k=1 as ASSUMED.

### Framework-extension (no external anchor)
- **HEXACO composition of reflection cadence + belief valence extremity** (Openness lowers threshold; Emotionality amplifies extremity). Analogous to shipped F2/F1/D5/D3/B2 HEXACO composition patterns. **Needs own Non-Inertness Gate before ratification** — mirrors Phase 1 lifelikeness roadmap process (F1/F5/D5/D3/B2/D4/F4).
- **Ranking function weights** (SALIENCE_WEIGHTS defaults) — chosen per commercial-precedent recon §5 recommendation; needs calibration against Non-Inertness Gate target (surfaced-events / total-emitted ratio ∈ [5%, 15%]).

## §4 Non-Inertness Gate Criteria (proposed for ratification)

Per Council #9 Rule 27 canonization, Slice 1 needs Non-Inertness Gate empirical harness before full ratification. Proposed 5 hypotheses (H1-H3 primary + H4-H5 validity):

**H1 (Recap Surface Ratio):** Over 3000-tick seed-42 run, `state.narrativeRecap.visibleBeats.length` / total LandmarkEvents fired ∈ [30%, 100%] (all beats retained up to `RECAP_MAX_VISIBLE_BEATS = [omitted]`).

**H2 (Belief Formation Cadence):** At baseline HEXACO, reflection fires 2-4x per 1000-tick horizon per Sim (matches Park 2023 "roughly two or three times a day" cadence).

**H3 (Pattern Closure):** At least 1 of the 4 baseline patterns closes at least once in 3000-tick seed-42 run (validates sifting-pattern grammar is not architecturally dead).

**H4 Validity (Openness moderator):** High-Openness Sims (O=100) trigger reflection ≥ 20% more frequently than low-Openness Sims (O=0) at equivalent event stream.

**H5 Validity (Emotionality moderator):** High-Emotionality Sims (E=100) produce beliefs with valence extremity ≥ 30% higher than low-Emotionality Sims (E=0) at equivalent event stream.

Verdict target: PASS 5/5 at 100% clear rate per Council #9 discipline.

## §5 Deferred Slices

### Slice 2 (post-ratification)
- Full Loose Ends plot-thread state model (structured OpenPlotThread with opening/closing clauses + expiration)
- Directionlessness detector (Kreminski failure-mode 1): track new-match/closed-match ratio; warn when > DIRECTIONLESSNESS_RATIO_THRESHOLD
- Toast letter surface (RimWorld pattern): dismissable severity-thresholded popup for high-salience beats
- Scrapbook per-actor per-epoch snapshot (Wildermyth pattern): single frozen "defining scene" per epoch
- World Chronicle cross-actor aggregation (CK3 pattern; fills CK2 → CK3 regression gap)
- Multi-level reflection tree beyond depth 1 (Park 2023 tree property; capped at MAX_BELIEF_DEPTH = [omitted])
- Layer 3 encoding-time snapshot on beliefs (Park's encodedLayer3 analog for emotion-congruent retrieval)

### Slice 3 (product-scope; needs product ratification)
- Qud-style rationalization grammar for prose realization (Grinblat-Bucklew 2017)
- Wildermyth-style Legacy carryover (dead-actor LandmarkEvents → world-persistent priors for future generations)
- Synthesifter example-driven pattern induction (Kreminski-Wardrip-Fruin 2020 INT workshop)

## §6 Rule 19 Citation Corrections Surfaced

None new this ship. Prior corrections at `rule-24-addendum-track-1c-close-out-corrections-2026-07-09.md` (Reagan corpus n=1,737 → v3=1,327 version-provenance) remain load-bearing. Anicich 2016 correction (Organization Science 27(1):123-140 NOT JPSP 110(2):176-194 per F2 wiring session) remains open for Council #11 filing.

## §7 Framework Methodology Firsts

- First substrate module consuming Kreminski/Winnow declarative sifting grammar with logic-variable unification
- First Park 2023 reflection implementation with non-LLM adaptation (weighted-mean valence + sigmoid confidence + evidence pointers)
- First Select-the-Unexpected ranking heuristic in framework substrate
- First framework HEXACO composition of reflection cadence
- First narrative-recap substrate architecture responding to Grok voice-brainstorm audit + Fable 5 dossier convergence
- First §10.7 sub-numbered panel insertion between existing sections without downstream renumbering (mirrors §10.5 HierarchyStatusPanel precedent)

## §8 Ship Verification

Ship gates + manifest:
- sim-ai typecheck: CLEAN
- sim-ai Rule 28 audit: CLEAN 0/79 files
- sim-ai full test suite: 2096 passed / 2096 total (+33 narrativeRecap; preexisting phaseD flaky didn't fire this run)
- sim-ai post-mortem: 1 preexisting anomaly (Item 164 rescue calibration; not narrativeRecap-related)
- roomtolife `npm run precheck`: PASS (Next.js build + TS typecheck GREEN; 223 vendored files verified)

## §9 Recommended Council #11 Disposition

**RATIFY-PROVISIONAL Slice 1** on evidence:
- 2 independent Rule 11 substrates converged on gap identification (Grok voice-brainstorm + Fable 5 dossier)
- 3 background research agents (Kreminski/commercial/Park 2023) delivered K=2 quorum-verified architectural inputs
- Slice 1 substrate + wiring + UI ships clean at all gates
- Non-Inertness Gate criteria specified (§4) with empirical harness to be run post-ratification

**Downstream candidacy items** (for Council #11 filing alongside this):
- Non-Inertness Gate empirical harness ratification (H1-H5)
- Slice 2 scope ratification (Loose Ends threads + directionlessness detector + toast letters + Scrapbook + World Chronicle)
- HEXACO composition Non-Inertness Gate (framework-extension needs its own empirical harness per Phase 1 lifelikeness pattern)
- Select-the-Unexpected exact scoring formula verification (K=1 → K=2 quorum via primary PDF re-read)

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Repository:** `~/Projects/the-street-code/methodology/`
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
