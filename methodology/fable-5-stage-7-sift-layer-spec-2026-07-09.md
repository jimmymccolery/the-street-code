# Stage 7 Proposal — The Sift Layer: Story-Sifting Pattern Schema

**Status:** PROPOSAL — authored outside the framework (external substrate: Perplexity Computer), grounded in a dedicated deep-research dossier (`research/story_sifting_dossier.md`, 39 verified citations, 9 flagged-UNVERIFIED claims). Not canonical. Subject to multi-substrate review and Rule 24 discipline on adoption.
**Date:** 2026-07-09
**Format lineage:** Stages 2–6 — research grounding per-source, module + typed-event-bus integration, numbered hypothesis harness with quantitative pass criteria, architectural-fix-not-test-criteria discipline, cultural-bundle conditionality, deterministic seeded replay, performance gates, premortem, Council items.
**Dependency note:** Independent of Stage 6 (conversation plane) except pattern #19 (Scandal), which requires gossip transport and degrades gracefully to deferred status without it.

---

## 1. Position in the Architecture

### 1.1 What the Sift Layer is
A **recognition layer, not a generation layer.** Per the curationist position of Ryan's dissertation ([Curating Simulated Storyworlds, UCSC 2018](https://escholarship.org/uc/item/1340j5h2)) and the canonical problem definition from [Kreminski, Dickinson & Wardrip-Fruin, Felt, ICIDS 2019](https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf):

> "The challenge, then, is to sift the wheat from the chaff, identifying event sequences that seem to be of particular narrative interest or significance and bringing them to the attention of a human player or interactor."

The Sift Layer matches declarative patterns against (a) the typed event stream and (b) plane-state time series, emitting `StoryInstance` records that downstream diegetic channels (newspapers, league newsletters, diaries, trophy plaques, reporter NPCs) render. It never invents events, never runs an LLM, and never writes to simulation state.

### 1.2 Architectural home: Layer 10
The sifter is a **Layer 10 (offline audit) citizen**. The honest engineering datum from the literature: Winnow's published benchmark is **912ms per incoming event** while maintaining 1,000 partial pattern matches (Firefox, 2019 MacBook Pro, 30 event types, 5 characters) ([Winnow, AIIDE 2021](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)). That is ~1,000x over the per-tick budget (0.896ms/tick at N=5,000). Conclusion: incremental acceptors are the right formalism (Winnow's acceptor semantics allow partial matches to be surfaced before completion — useful for reporter NPCs "working a story"), but match-pool maintenance runs **at consolidation boundaries only**, batched, off the hot path — exactly where sophisticated inference already lives. No sifting work occurs inside the tick.

### 1.3 The two-matcher-family decision
The literature contains two distinct, complementary sifting formalisms; this spec adopts both:

- **Family I — Event-graph acceptors** (Felt/Winnow lineage): declarative queries over typed event predicates with bound character variables, evaluated incrementally with acceptor semantics ([Felt](https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf); [Winnow](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)).
- **Family II — Trajectory matchers** (Arc Sift lineage): Dynamic Time Warping similarity between reference fortune-arc shapes and simulation time series, per Arc Sift (Leong, Porteous & Thangarajah, AAMAS 2022), which built Dynamic Character Networks over relationship scores and matched drawn arcs against them using DTW — with the six Reagan et al. shapes as its validated query vocabulary (dossier §1.10, §3.7).

Family II is the strategically decisive one for this framework: the corpus's central empirical finding is that **personhood lives in baseline drift, not event response** (Post 0197). Every prior sifter matches events. Trajectory matchers over plane time series (sentiment, capital position, communal standing, HEXACO baselines, vitality) can recognize stories that contain **no single salient event at all** — the slow estrangement, the quiet decline. No shipped system does this over psychologically-grounded state (dossier §2 cross-cutting observation); it is a plausible second genuinely-novel contribution alongside intersection nodes (Post 0192 precedent for claiming it carefully).

### 1.4 Salience prefilter: memory as the first sifter
Story candidacy is gated on the existing sparse prediction-error encoding: **an event sequence is a story candidate only if at least one participant encoded at least one of its events as a memory trace.** Rationale: (a) tractability — the profusion problem in Felt's definition is solved by a filter that already exists; (b) fidelity to McAdams — narrative identity is built from what people remember, "integrating the reconstructed past and imagined future" ([McAdams & McLean 2013](https://journals.sagepub.com/doi/10.1177/0963721413475622)); (c) it makes the game's stories and the NPCs' self-narratives the same objects. Drift stories (Family II) are exempt from the event-trace gate and instead gated on drift magnitude thresholds — by definition their participants may not have noticed them, which is part of their truth.

### 1.5 Schema shape (Schema v0.2 conformance)
`SiftingPattern` is a Schema v0.2 authored object compiled to runtime matchers, each row carrying the 5-attribute minimum (`valid_time`, `place_scope`, `evidence_quality`, `consultation_policy_id`, `display_transform_id`) per Post 0191. Consequences:
- **Patterns are era- and place-scoped.** Some shapes are near-universal; their *tellability* is not. Labov's evaluation component defines a story as that which is "strange, uncommon, or unusual... worth reporting" (Labov 1972, quoted in dossier §3.9) — and reportability is culture- and era-relative.
- **Patterns carry consultation policy.** Which paper covers whose stories is itself historically loaded (see §5).
- **Patterns carry display transforms.** The same `StoryInstance` renders differently in a 1948 sports page, a league newsletter, and a diary.

```
SiftingPattern (authored, compiled)
  patternId, family: EVENT_ACCEPTOR | TRAJECTORY
  grounding: CitationRef[]            // per-source, R19-verified
  signature: WinnowStyleAcceptorSpec | ArcSpec{shape, channel, DTWtolerance}
  roles: CharacterVariable[]          // bound at match time
  saliencePrereq: MEMORY_TRACE | DRIFT_THRESHOLD
  tellabilityWeights: per-bundle scalar map   // cultural conditionality (H6)
  cooldown + noveltyConstraints       // anti-repetition (H7)
  valid_time, place_scope, evidence_quality, consultation_policy_id, display_transform_id

StoryInstance (emitted)
  patternId, boundRoles, eventRefs[] | trajectorySlice
  provenance: full replay pointer (seed + tick range)   // every story is auditable
  privacyClass: PUBLIC | WITNESSED | PRIVATE            // CK3 precedent, dossier §2
  status: PARTIAL | COMPLETE                            // Winnow acceptor semantics
```

`privacyClass` matters: Crusader Kings III's memory system distinguishes private memories (murder, affairs) hidden from other characters (dossier §2) — for you, `PRIVATE` instances are exactly the detective's and gossip system's raw material: stories that exist but that no diegetic channel may surface until knowledge propagates.

---

## 2. The Pattern Taxonomy — 20 Foundational Story Shapes

Grounding per-source; matcher family; primary observation channels; surface channels. All Family II shapes use the six-arc vocabulary verified in [Reagan et al. 2016, EPJ Data Science 5:31](https://epjdatascience.springeropen.com/) (SVD + Ward clustering + SOM over 1,327 Gutenberg books) and validated as a *query* vocabulary by Arc Sift (dossier §1.10). Nine dossier UNVERIFIED flags respected: no pattern below relies on Tobias plots 12–20 or Polti situations 33–36.

### Family II — Fortune arcs (trajectory matchers)
Channel is a parameter: any of pair sentiment, capital position (habitus plane), communal standing, vitality, or league standing. One shape, many stories.

| # | Shape | Arc | Grounding | Example instantiation |
|---|-------|-----|-----------|----------------------|
| 1 | Rags to Riches | rise | Reagan et al. 2016; Booker | Pinboy to proprietor across the 1950s boom |
| 2 | Riches to Rags | fall | Reagan et al. 2016; Booker (Tragedy) | Proprietor ruined in the 1962 Brunswick repossession wave |
| 3 | Man in a Hole | fall–rise | Reagan et al. 2016 | Injury, lost season, comeback league title |
| 4 | Icarus | rise–fall | Reagan et al. 2016 | Local star turns pro, flames out (PBA-era) |
| 5 | Cinderella | rise–fall–rise | Reagan et al. 2016 | Underdog team's championship run with mid-season collapse |
| 6 | Oedipus | fall–rise–fall | Reagan et al. 2016 | Recovery arc that ends in relapse — the hardest, saddest true shape |

### Family I — Relational shapes (event-graph acceptors over pair-relational plane + Stage 6 acts)

| # | Shape | Signature sketch | Grounding |
|---|-------|-----------------|-----------|
| 7 | Slow-Burn Friendship | reciprocal disclosure–responsiveness loops → intimacy threshold, over ≥ K co-locations | Reis & Shaver 1988; Altman & Taylor 1973 (Stage 6 canon) |
| 8 | Betrayal | sustained high trust → violation event → trust collapse + avoidance behavior | McAdams contamination subtype "betrayal" (dossier §4.1); Polti "Crime Pursued by Vengeance" |
| 9 | Erosion | four-horsemen accumulation, repair_attempt count ≈ 0, trust monotone decline | Gottman 1994 (Post 0199 mechanics — the acceptor reads events Stage 4 already emits) |
| 10 | Reconciliation | rupture → repair attempts → sentiment-override-gated restoration | Gottman 1994; Holmes & Rahe rank #9, "Marital reconciliation," LCU 45 (dossier §4.2) |
| 11 | Rivalry | repeated competitive co-location + status contests; sentiment stable-negative with arousal spikes; neither exits | Tobias plot #8, Rivalry (verified subset, dossier §3.4) |
| 12 | Mentorship / Passing the Torch | sustained advice/disclosure asymmetry + skill transmission + role handoff event | Wacquant apprenticeship timescale (Stage 5 canon); Propp donor-function analogue (dossier §3.1) |

### Family I/II hybrid — Life-course shapes (biographical records + lifelineGenerator)

| # | Shape | Signature sketch | Grounding |
|---|-------|-----------------|-----------|
| 13 | Redemption Sequence | valence transition bad→good WITH agency marker; subtypes sacrifice / recovery / growth / learning | McAdams (dossier §4.1, exact subtype list); coding constructs Agency + Meaning-making |
| 14 | Contamination Sequence | good→bad transition + suppressed retrieval of the prior good state (memory-trace access decline as the computational analogue of McAdams's "inability to recall") | McAdams (dossier §4.1); subtypes victimization, betrayal, loss, failure, illness, disillusionment |
| 15 | Turning Point | transition event whose downstream trajectory diverges from the counterfactual replay fork beyond threshold | Elder's life-course transitions/turning points (via Mortimer 2021, dossier §4.3); **certified by deterministic replay — see H4, a capability no other sim has** |
| 16 | Linked-Lives Cascade | one NPC's high-LCU event (weights from SRRS table, dossier §4.2) propagating measurable state change across ≥2 relationship hops | Elder's Linked Lives principle (dossier §4.3); Holmes & Rahe 1967 |
| 17 | Coming of Age | age-window threshold crossings (first job, league debut, first wage) clustering into a coherent-biography span | Habermas & Bluck 2000 (life-story emergence in adolescence; abstract-verified, taxonomy attribution flagged UNVERIFIED — pattern uses only the verified core claim); corpus age×era framework rule (n=3) |

### Family I/II — Communal & place shapes (venue/city scale; aggregation over `crossProductTraceAggregator`)

| # | Shape | Signature sketch | Grounding |
|---|-------|-----------------|-----------|
| 18 | Rise and Fall of an Institution | venue-level aggregate: gradual rise then precipitous decline | The characteristic Dwarf Fortress arc per [Kreminski & Mateas, Toward Narrative Instruments, ICIDS 2021](https://mkremins.github.io/) (dossier §1.8); historical template: Brunswick +1,590% → 131 repossessions |
| 19 | Scandal | PRIVATE StoryInstance → gossip propagation crossing a publicity threshold, with per-hop mutation | Talk of the Town knowledge mutation/decay (dossier §1.9); Gossamer (CoG 2023); **requires Stage 6 gossip transport — deferred without it** |
| 20 | Exodus / Arrival | migration flow restructuring venue-level field positions and league composition | Elder's Time-and-Place principle (dossier §4.3); bundle-grounded historical migrations (resettlement, Great Migration contexts already in bundles A/E) |

**Taxonomy governance:** 20 is the founding set, not a cap; additions require per-source grounding + the §4 consumer gate. Patterns are versioned BIBFRAME-style like bundles (Post 0191). The McAdams coding constructs (agency, communion, exploratory processing, coherent positive resolution, meaning-making — dossier §4.1) are **annotations computed on StoryInstances**, not separate patterns — they feed display transforms (a redemption story is *narrated* differently than it is *matched*).

---

## 3. Research Grounding — Tracks and the Consumer Gate

### 3.1 The three research tracks (from prior session design, now gated)
1. **Story-pattern library** → consumer: sifting matchers (§2). Sources: Propp/ATU/Motif-Index for event-grammar shapes; Reagan et al. for arcs; McAdams/Elder/Holmes-Rahe for life-course shapes.
2. **Life-event taxonomy** → consumers: `lifelineGenerator` + biographical records (event vocabulary) AND prediction-error priors (SRRS LCU weights as encoding-salience priors — a high-LCU event should be more memorable, which then feeds §1.4).
3. **Era texture corpora** → consumer: display transforms only (narration templates, period register). Extractor-under-attestation, R19.

### 3.2 The Non-Inertness Gate (funding rule — generalizes the M10 lesson)
**No research track is funded until it names, in writing: (a) the consumer mechanism, (b) the junction where content enters it, (c) the measurable delta expected at an observation surface, (d) the kill criterion that defunds the track.** The M10 postmortem (Post 0201) is the type case: 33-source bundle content wired through a scalar modulator produced ≤4% behavioral contribution. Content without a named consumer is presumptively inert. This gate is filed as a rule candidate (§8) because it applies to every future content-research effort, not just these three tracks.

Worked application:
- Track 1: consumer = matchers; junction = pattern compilation; delta = surfaced-story yield and H5 human ratings; kill = pattern family matching <1 instance per 10 sim-years at N=5,000 or failing H7 diversity.
- Track 2: consumer = lifelineGenerator + encoding priors; junction = spawn-time biography + memory encoding; delta = measurable change in trace distributions and life-course pattern yield; kill = LCU priors moving trace distributions <5% vs uniform.
- Track 3: consumer = display transforms; junction = narration; delta = era-authenticity human ratings; kill = raters can't distinguish era-textured from generic narration.

---

## 4. Hypothesis Harness (H1–H8)

Headless Vitest, `--no-file-parallelism`, deterministic seeds; 5 seeds × 2 scenarios baseline, **100-seed sweep before any meta-claim** (Post 0182 discipline). Scenarios: (S1) league-night long-run (100k ticks, 8+ NPCs, mixed bundles); (S2) decade-scale venue run with historical shock injection (a 1962-style credit contraction) to exercise Family II and pattern #18.

Per dossier §5.2, deterministic matchers are **exact by construction** — precision/recall against the chronicle is not the scientific question. The harness therefore splits computational gates (H1–H4, H6–H8) from the human study (H5), mirroring Winnow's separation of latency benchmarking from perceived-story evaluation.

| H | Claim | Pass criterion |
|---|-------|----------------|
| **H1** | Determinism: sift output is byte-identical across replays per seed, including PARTIAL instance states | Exact match, all seeds; replay-pointer provenance resolves for 100% of instances |
| **H2** | Salience prefilter works: memory-trace gating cuts candidate volume ≥90% while retaining ≥95% of stories that ungated sifting finds | Both bounds, 100-seed sweep; if retention <95%, fix the encoding priors (architectural), not the bound |
| **H3** | **Drift stories exist and are unreachable by event acceptors:** ≥25% of Family II matches contain no single event above the SRRS-prior salience threshold | Threshold met at 100 seeds — this is the empirical warrant for the novelty claim in §1.3, and if it fails, the claim is retracted (Post 0192 discipline for novelty claims) |
| **H4** | **Turning-point certification:** replay-forked counterfactuals diverge (d ≥ 0.5 on affected channels) for flagged turning points and do not (d < 0.2) for matched non-flagged transitions | Both directions required — certifying only positives is validation theater |
| **H5** | **Human precision study (the core gate):** blind raters judge sifted stories vs matched-noise controls (same characters, same length, same event-type marginals, sampled from the same chronicle, not pattern-matched). Preregistered (OSF, per the Post 0114 X-Phi precedent); 15–20 lay raters per AIIDE norms (dossier §5.4); Likert "this reads as a real story" + pairwise forced choice | Sifted > noise at d ≥ 0.8; ≥70% of sifted items above the noise median; Krippendorff's α reported with xRR-aware interpretation (no fixed-threshold worship, per Wong, Paritosh & Aroyo, ACL 2021 — dossier §5.3); convergence across two independent rater batches |
| **H6** | **Cultural tellability non-inertness:** per-bundle tellability weights produce measurably different surfaced-story mixes across bundle-A/D/E-dominant venues | Bundle assignment explains ≥15% of variance in surfaced-story-type mix (Stage 6 standard); grounding: McAdams's six "languages of redemption" are American master narratives (dossier §4.1) — redemption-weighting itself must be bundle-conditional, and gaman (bundle E) plausibly suppresses public tellability of suffering narratives — that hypothesis is itself consultation-gate material, see §5 |
| **H7** | **Anti-repetition (the Wildermyth failure mode, dossier §2):** no single pattern >20% of surfaced stories per sim-decade; bound-role novelty enforced (same role-pair may not resurface in the same pattern within cooldown) | Both constraints hold at 100 seeds without starving yield below the H8 floor |
| **H8** | **Throughput and yield:** full sift pass at consolidation boundary ≤50ms at N=5,000 with partial-match pool bounded (per-pattern per-venue caps); surfaced-story yield within band (floor: ≥1 front-page-worthy instance per sim-week per venue; ceiling: ≤20 — a dead newspaper and a firehose are both failures) | All three, sustained over decade-scale S2 run; zero hot-path cost (verified by tick-time regression vs Stage 5 baseline) |

**Anchor-integrity side gates:** sifting is read-only — verified by state-hash comparison of simulation runs with sifter on/off (must be identical; the sifter must never become a Heisenberg observer).

---

## 5. Consultation Gate and the Segregated-Press Problem

Surfacing stories diegetically in 1940s–1960s America means deciding **which paper tells whose stories.** Period-accurate mainstream dailies systematically under-covered or miscovered Black, Tejano, and Japanese-American communities; the Black press (e.g., the Philadelphia Tribune in Anchor A's city) existed precisely because of that erasure. Three honest options, all consultation-gate territory: (a) model the segregated press truthfully (two papers, biased sifters — historically honest, heavy, and the richest design); (b) a single ahistorical evenhanded paper (safer, era-dishonest); (c) restrict diegetic surfacing to community-internal channels (newsletters, diaries) until the gate resolves. **Recommendation: (c) ships first; (a) is filed as the target pending named-reviewer sign-off — same posture as intersection nodes and Stage 6 dialect norms.** Note that option (a) is implementable *with zero new machinery*: a reporter NPC's sifter access is simply scoped by the paper's `place_scope` and `consultation_policy_id` — bias as configuration, documented and auditable, rather than bias as code.

---

## 6. Premortem (named failure modes)

1. **Second M10** — patterns authored, matched, and surfaced into a channel nobody reads. *Mitigation:* §3.2 gate; H8 yield band ties patterns to a living surface.
2. **Caves-of-Qud rationalization risk** (dossier §2) — narration glossing noise into story-shaped text. *Mitigation:* H5's matched-noise control is specifically designed to catch this; if noise rates as story, the display transform is doing illegitimate work.
3. **Wildermyth repetition** — template pool exposure. *Mitigation:* H7 diversity + cooldowns; taxonomy growth path via governed additions.
4. **Latency creep onto the hot path** — incremental matching drifting into the tick. *Mitigation:* architectural (Layer 10 residency); H8 tick-time regression gate.
5. **Fabricated grounding** — the dossier already flags 9 UNVERIFIED claims; the taxonomy above uses none of them load-bearingly. *Mitigation:* R19 verification round before canonization; UNVERIFIED list travels with the spec.
6. **Novelty-claim inflation** — "first drift-story sifter" claimed without the H3 evidence. *Mitigation:* claim is conditional on H3 passing, per the Post 0192 novelty-recognition discipline.
7. **Observer effect** — sifter mutating state. *Mitigation:* read-only enforcement + state-hash gate (§4).

---

## 7. Interactions with the Rest of the Ecosystem

- **Reporter NPCs (prior session):** a reporter is a sifter with scoped access — their beat is a `place_scope`, their paper's bias a `consultation_policy_id`, their fallibility the ToT knowledge-mutation model (dossier §1.9). PARTIAL acceptor states are literally "a reporter working a story" (Winnow semantics, §1.2).
- **Detectives:** `PRIVATE` StoryInstances are the case file that exists before anyone knows it does; the evidence graph is the instance's `eventRefs` with knowledge-propagation gating.
- **Sentiment plateau (0.78):** pattern #9 (Erosion) and #10 (Reconciliation) give the plateau question empirical story-level stakes — if sentiment can't decay, Erosion can never complete, which is now a *player-visible* wrongness rather than an internal parameter debate. Strengthens the Stage 6.1 case.
- **City sim (planned):** Family II over aggregate channels + patterns #18/#20 are the city sim's newspaper, obituary column, and census-anomaly feed with no new sifting machinery.
- **RoomToLife:** StoryInstances written to biographical records via the entity registry become the provenance behind bedroom artifacts — the trophy resolves to a replayable 1962 league final.
- **Chronological Challenge:** tellability weights are era-scoped rows — what counts as news in 1948 vs 1975 shifts by data, not code.

## 8. Council #9 Items to File

1. **Non-Inertness Gate as a framework rule candidate** (consumer + junction + delta + kill criterion before any content research is funded) — generalizes Post 0201's M10 finding; n=1 pending first enforcement.
2. Sift Layer scope amendment (Layer 10 citizenship; read-only invariant as a META-rule candidate).
3. Segregated-press adjudication (§5, options a/b/c) — consultation-gate dependency, ships (c)-first.
4. Novelty-claim registration for drift-story sifting, conditional on H3 (Post 0192 Item 45 lineage).
5. SRRS-LCU-weights-as-encoding-priors: cross-layer change to Layer 4 requiring its own mini-harness before H2 depends on it.
6. Pattern-taxonomy governance (versioning, addition procedure, per-source grounding requirement).

## 9. Elevator Pitch (empirically honest; sentences map to gates)

> **The simulation doesn't write stories — it notices them.** Twenty grounded story shapes, from Cinderella arcs to slow-burn friendships to turning points, are recognized in the lives your NPCs actually lived — and every surfaced story carries a replay pointer proving it happened [H1]. It finds the stories no event log can see: the quiet drift of two friends growing apart with no fight to blame [H3]. It can certify a turning point by replaying the life that would have happened otherwise [H4]. Blind readers rate its stories as real stories, not simulation noise [H5]. And what counts as tellable changes with who's telling it, in whose community, in whose newspaper — measurably [H6], honestly [§5].

*(Per Post 0197 discipline: any failed gate deletes its sentence.)*

## 10. Out of Scope (explicit)

Surface text generation (display transforms consume Track 3 templates — separate workstream); player-authored sifting queries (an Arc Sift-style "draw the arc" player tool is a compelling future feature, deferred); multi-venue federation-level story aggregation (deferred to city sim); Scandal (#19) until Stage 6 ships gossip transport; any LLM involvement at any layer of this system.
