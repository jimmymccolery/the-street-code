---
name: Rule 24 addendum — Council #9 Items 132-140 amendments per Fable 5 adversarial audit
scope: Comprehensive amendments to Items 132/133/134/137/139/140 addressing Fable audit findings §A.1.1 + §B.2 + §B.3 + §B.4 + §B.5 + §C.2 + §C.3.3 + §D.3
filed: 2026-07-09 late (post Fable audit ingestion)
disclosure: Section 6 UNVERIFIED convention applies
supersedes: does NOT supersede Council agenda body; APPENDS amendment-body per Rule 24 immutability
---

# Rule 24 addendum — Council #9 Items 132-140 amendments per Fable adversarial audit

## 1. Purpose

Fable 5 adversarial audit `fable-5-adversarial-audit-2026-07-09.md` identified specific amendment-worthy issues in Council #9 Items 132-140 bodies. This addendum files consolidated amendment proposals per Rule 24 canonical-file correction protocol (prior Council #9 agenda body preserved immutable; amendments appended discoverable).

Council #9 review at 2026-09-05 to 2026-10-05 window will adjudicate whether to accept each amendment.

## 2. Item 132 (Non-Inertness Gate) — 3 amendments per Fable §A.1.1 + §A.1.2 + §A.4

### 2.1 Pilot-data relabeling (Fable §A.1.1)

**Current Item 132 body (`AGD:2814`):** "**Confidence calibration:** HIGH — direct generalization of empirically-validated A1 finding; operationally simple 4-question check; failure modes (blocked substantive tracks; prohibitive overhead) empirically testable at first enforcement."

**Fable finding:** Item 132 body cites "3 PASS + 1 FAIL calibration data point" across Cluster A2 Phase A/B/C/D applications as empirical anchor. Fable §A.1.1: this is self-administered — "the entity applying the gate (operator + CC), the entity generating its calibration record, and the entity that will present that record to Council are the same entity." Round 5 Opus's globally-self-sealing diagnosis applies at small scale.

**Amendment proposal:** Relabel the 4 Cluster A2 applications as **PILOT data** in Item 132 body. Pre-register the ratification-relevant discriminating test: **the first application where the gate's verdict CONFLICTS with what the operator/CC wanted to do anyway** is the first real calibration point. Track separately:
- Gate verdicts that CHANGED a decision (informative — discriminative power evidence)
- Gate verdicts that CONFIRMED a decision (uninformative — self-consistency evidence)

Ratify Item 132 on the former, not the latter.

### 2.2 Confidence calibration split (Fable §A.4)

**Fable finding:** HIGH is defensible for the four-question check's operational simplicity; it is NOT yet defensible for discriminative power.

**Amendment proposal:** Split the calibration:
- **HIGH on cost/simplicity** (operational overhead ≤ 30 minutes per planning arc; check structure is deterministic + reviewable)
- **UNKNOWN on false-negative rate pending first adversarial application** (whether the gate catches things operator/CC would have missed vs merely confirming already-made judgments)

### 2.3 Scope-extension attribution split (Fable §A.1.2)

**Fable finding:** Item 132 body extends scope to "future architectural mutation (new planes, layers, subsystems)" (`AGD:2796`) — this extension is defensible + arguably the more valuable half, but is framework's extension, not Fable's proposal. Under framework's own attribution discipline, this should be split.

**Amendment proposal:** Explicit attribution split in Item 132 body:
- **Four-question core (consumer + junction + delta + kill criterion):** Fable 5 (Stage 7 spec §8 item 1 + Stage 6 spec §9 item 2 variant)
- **Architectural-mutation scope extension:** framework (post-Fable-ingestion extension applying gate beyond research-track scope to any new subsystem)

Designate Item 132 body as single canonical wording; version-lock; make planning artifact `a2-non-inertness-gate-planning-2026-07-09.md` cite Item 132 body by item+line rather than restating.

## 3. Item 133 (Stage 7 Sift Layer) — 4 amendments per Fable §A.2 + §B.1 + §B.2 + §C.1

### 3.1 Confidence recalibration HIGH → MEDIUM (Fable §B.2)

**Current Item 133 body (`AGD:2855`):** "**Confidence calibration:** HIGH — 7/7 high-load-bearing citations verified; empirically-grounded per-source pattern taxonomy; Layer 10 residency architecturally defensible per Winnow benchmark; H-harness discipline consistent with framework's Post 0197 posture; A6 candidacy respects V1-blocker sequencing."

**Fable finding:** HIGH not defensible on H24 evidence + hypothesis substitution + one-sample effect + champion-configuration failure (enriched never beats k=5 baseline champion at 73.3% permP=0.003).

**Amendment proposal:** Recalibrate to **MEDIUM** pending:
- H24b nested-CV multi-seed replication with pre-registered protocol (Fable §B.2 concrete next step)
- H3 Stage 7-lite empirical test (Fable §D.4 Stage-7-lite proposal executable without H5 human study)
- H5 pathway operationalization (Fable §B.6 provided concrete costed protocol)

Spec-quality + citation-verification grounds for confidence are real + now double-verified by Fable audit; but empirical anchor is one sample on substituted hypothesis + filed prerequisites (H5 + Item 137) unmet.

### 3.2 Arc Sift attribution retention (Fable §A.2.3)

**Current Item 133 body (`AGD:2823`):** "Arc Sift AAMAS 2022 + IJCAI 2022 companion" (no authors).

**Fable finding:** Framework's clean-room guide proposed injecting fabricated authors (Kumaran et al.); Fable independently verified actual attribution is Leong, Porteous, Thangarajah 2022 IJCAI-22 pp. 4950-4956.

**Amendment proposal:** Retain no-authors phrasing OR restore verified authors per `rule-24-addendum-track-1c-close-out-corrections-2026-07-09.md` §3. Framework must NOT execute clean-room guide's proposed correction (would inject fabrication).

### 3.3 Reagan corpus scope retention (Fable §A.2.4)

**Current Item 133 body (`AGD:2851`):** Fable's original Stage 7 spec §2 references "1,327 Gutenberg books" (verbatim per published EPJ Data Science). Framework's clean-room guide proposed "correcting" to 1,737; correction was contested + backwards.

**Amendment proposal:** Retain n=1,327 with journal DOI attribution. See `rule-24-addendum-track-1c-close-out-corrections-2026-07-09.md` §2 for full correction record.

### 3.4 Template-recovery test added as pre-registered gate (Fable §B.1)

**Current Item 133 body:** silent on parametric functional form for Family II templates.

**Amendment proposal:** Add pre-registered **template-recovery test** to Item 133 harness:
- Generate trajectories from each of 6 Reagan templates + noise at H24-observed channel SNR
- Require matcher to recover generating template at ≥95% accuracy
- Require ≤5pp accuracy gap between smooth (cosine/Chebyshev 2-4 coefficients) vs piecewise-linear variants before either is frozen
- If piecewise-linear passes within 5pp of smooth, framework's simpler choice wins on evidence
- Estimated cost: ~150 lines, reuses `dtw.ts` (Track 1c artifact)

Pre-registration format: file this amendment body BEFORE running the test so outcome is falsifiable independent of framework's preference.

### 3.5 Null-distribution calibration amendment (Fable §C.1.2)

**Amendment proposal:** Item 133 harness gets pre-registered **null-distribution calibration**:
- Per (template, channel), build null DTW-distance distribution from phase-randomized surrogates of real plane time series (IAAFT surrogates preserve autocorrelation + amplitude spectrum)
- Set MATCH thresholds at fixed FPR (e.g., 1%) against null distribution
- Converts Family II from ranking device into detector with controllable FPR
- H3 ≥25% invisibility criterion (`S7:137`) silently requires this + Track 1c currently provides no calibration
- Estimated cost: ~120 lines reusing `dtw.ts`

## 4. Item 134 (Stage 6 Conversation Plane) — 3 amendments per Fable §B.5 + §C.2 + §D.7

### 4.1 Two-gate ship structure (Fable §D.7)

**Fable finding:** Framework's Cluster A2 Node.js algorithmic close conditions (`CRG:196`) are legitimate for determinism + scaling shape + budget arithmetic but do NOT extend to Stage 6/7 ship claims. JS-engine + GC behavior differs materially Node/V8 vs consumer devices (Safari/JavaScriptCore). Stage 6 allocation-heavy by design.

**Amendment proposal:** Item 134 prerequisites gain explicit two-gate structure:
- **Gate 1 (Node algorithmic):** A2 chassis harness + Fable C.2 extensions (concurrency axis + burst mode + spawn histogram + allocation metric) pass
- **Gate 2 (real-hardware ratification):** same harness scenario replayed in-browser on weakest supported device with conversation burst load; ship claims BLOCKED until Gate 2 reports ≥1.5× headroom AND allocation-rate within budget
- Framework has prior art at `path-a-cross-device-browser-testing-methodology-guide-v1.md` (per Fable audit note — UNVERIFIED at framework side but Fable inspected public methodology tree)

### 4.2 Harness generalization extensions (Fable §C.2)

**Fable finding:** A2 Phase B chassis carries as-is (4-tier + budget assertions + headroom + multi-seed + log-log slope) but load model does NOT carry to Stage 6.

**Amendment proposal:** Item 134 harness = A2 Phase B chassis + 4 concrete extensions:
1. **Concurrency axis:** conversations ∈ {0, 50, 250, 500} at fixed N=5000; per-conversation marginal cost report; 0-conversations row is hot-path-zero regression guard
2. **Burst-load generator:** 100 conversations spawned within 10-tick window; assert p99 tick cost (not just median) since A2 max spikes already occur at steady state
3. **Spawn-cost histogram:** `ConversationState.init` p50/p95/p99 as first-class metric with own budget line
4. **Allocation-rate metric:** bytes-allocated/tick + GC pause count; bridge to Gate 2 (allocation behavior is where Node vs device diverges first)

Pass criteria: budget compliance at 250 concurrent; p99 spawn < 1ms; zero idle cost; allocation rate within 2× of pre-Stage-6 baseline.

### 4.3 Cross-consumer discipline amendment (Fable §B.5)

**Current framework position (clean-room guide §6.5):** cross-consumer byte-identical composition wrappers.

**Fable finding:** PARTIAL. Byte-identity achievable one layer down from where framework proposed. Substrate MUST port byte-identical; wrappers legitimately differ.

**Amendment proposal:** Item 134 amendment specifies 3 enforcement artifacts:
1. **Substrate byte-identity check:** extend sha256 vendor manifest (Fable §C.5) to cover `conversationPlane.ts` + future `siftLayer/` files; CI test fails on drift
2. **Context-injection equivalence test:** same seeded conversation + participants + IDENTICAL context objects fed through each consumer's wrapper → must produce identical `DialogueActEvent` streams
3. **Divergence manifest:** per-consumer file enumerating every intentional wrapper divergence with one-line rationale (greppable per Section 6 convention pattern)

## 5. Item 137 (Segregated-press content-adjudication) — 1 amendment per Fable §B.4

### 5.1 Surfacing/voicing distinction (Fable §B.4)

**Current Item 137 body (`AGD:2982-2993`):** option (c) restricts diegetic surfacing to community-internal channels (newsletters, diaries) until consultation-gate resolves.

**Fable finding:** consultation gate covers HOW community-internal content is voiced, not only WHICH channels exist. Period voice for 1944 Black Philadelphia bundle involves register/dialect/content choices INSIDE option (c). Without explicit distinction, (c)-at-V1 becomes backdoor for shipping ungated period voice.

**Amendment proposal:** Item 137 body adds explicit clause:
> "**Option (c) removes the gate from the SURFACING decision; it does NOT remove it from the VOICING decision.** Community-internal channel content (newsletters, diaries) shipping at V1 under (c)-first posture remains consultation-gated at anchor-tier discipline (`fable-5-stage-6-conversation-plane-spec-2026-07-09.md` §4 + `fable-5-stage-7-sift-layer-spec-2026-07-09.md` §5) for register/dialect/content-voicing decisions. Named-reviewer sign-off remains prerequisite for voicing decisions; only the surfacing-channel decision is ratified via (c) at V1."

**Verification caveat:** `disclosure_rule.md` is local-only; its v1.0 alignment with (c)-first claim is UNVERIFIED-at-Fable-audit-time. Framework accepts Fable's YES-with-carve-out contingent on framework copying disclosure_rule.md operative clause into public methodology tree.

## 6. Item 139 (Belief store PROV-O extension) — 4 amendments per Fable §A.3 + §B.3

### 6.1 Provenance correction (Fable §A.3.1)

See `rule-24-addendum-a2-phase-c-occupational-asymmetry-provenance-2026-07-09.md`. Occupational asymmetry attributed to Fable 5 (not framework departure).

### 6.2 PRIVATE StoryInstance semantics preservation (Fable §B.3 Condition 1)

**Amendment proposal:** Item 139 body adds explicit condition:
> "PRIVATE visibility is evaluated on StoryInstance participants, INDEPENDENT of any participant's belief-store tier. Coarse-tier NPCs can anchor PRIVATE StoryInstances (Family II sifts plane time series with no belief-store dependency)."

### 6.3 Depth-of-provenance vs existence-of-belief distinction (Fable §B.3 Condition 2)

**Amendment proposal:** Item 139 body clarifies asymmetry semantics:
> "Coarse tier = belief exists with source-class aggregate (~5 bytes/known-instance: instance ref + confidence bucket + source-class enum). Rich tier = full PROV-O chain (wasDerivedFrom + hadPrimarySource + confidence). Reporters + police + detectives need provenance CHAIN for corroboration mechanics — not exclusive possession of beliefs."

### 6.4 Lazy promotion design addition (Fable §B.3 design addition)

**Amendment proposal:** Item 139 body adds design element:
> "**Lazy promotion:** any NPC becoming a participant in a StoryInstance matching designated pattern classes (crime/scandal/witness shapes) gets belief cluster promoted to fine-grained at promotion time. Bounded cost (promotions gated by story participation which sifter computes); preserves ~260 bytes/Sim budget in steady state; eliminates 'wrong NPC has coarse memory' failure mode."

Plus new H-test for Stage 7 H-battery: coarse-tier witness → pattern match → promotion → detective interview reads promoted provenance chain end-to-end.

## 7. Item 140 (Event-scope canonical registry Phase 8.x post-V1) — 1 amendment per Fable §D.3

### 7.1 Cross-product provenance pointer extension (Fable §D.3)

**Fable proposal:** Metadata-only middle path costing nothing at V1 while preserving Item 140's deferred option. Extend `canonicalRegistry.ts` (shipped 2026-07-04 per `AGD:3078`) with **provenance pointers** — per canonical entity append-only list of `(product_id, sim_run_id, seed, tick_range, pattern_id, substrate_version, pattern_pack_version)` tuples recording WHERE that entity's stories happened without moving event data cross-product.

**Amendment proposal:** File as amendment WITHIN Item 140 (trigger condition + review scope already cover this):
- ~40 lines schema extension + append API; no runtime reads at V1
- Writes fire only when StoryInstance completes (Stage 7) or lifeline compiles (Post 0189) — both off-hot-path
- **H29 test (Fable-designed):** cross-product resolution round-trip — write pointer in product A's run; from product B, resolve pointer → replay seed+tick_range → regenerate StoryInstance; assert regenerated instance matches original's pattern_id + participants. Pass: 100% on 20-instance battery. Kill: if replay-regeneration diverges (substrate version drift), pointer schema needs `substrate_version` pinning
- This is Layer 1 as ecosystem's long-term memory (not just entity directory): Rooms-product NPC can "remember" its Memory Lanes instance's man_in_a_hole arc via deterministic replay + framework's already-validated capability

## 8. UNVERIFIED disclosure

1. **Fable's live-agenda access verified byte-identical to framework HEAD.** Fable audit §"Preservation claim verified" states diff byte-identical against Fable originals + agenda line numbers match. VERIFIED by Fable audit (framework accepts on Fable's authority; direct re-verification via framework typecheck + git status this session).
2. **Fable's B.1 template-recovery test empirical calibration.** Fable proposes ≥95% recovery accuracy + ≤5pp gap between smooth vs piecewise-linear. Thresholds are Fable's proposal, not primary-source-derived. UNVERIFIED as canonical; adopted as pre-registered pass criterion via this amendment.
3. **Fable's C.2 harness extensions pass criteria** (budget compliance at 250 concurrent; p99 spawn < 1ms; zero idle cost; allocation rate ≤ 2× baseline): Fable proposals; not empirically-validated at framework side. Adopted as pre-registered gates.

## 9. Cross-references

- Fable 5 adversarial audit `fable-5-adversarial-audit-2026-07-09.md`
- Rule 24 addendums this session: `rule-24-addendum-track-1c-close-out-corrections-2026-07-09.md` + `rule-24-addendum-a2-phase-c-occupational-asymmetry-provenance-2026-07-09.md`
- Council #9 review agenda IMMUTABLE body: `council-9-review-agenda-draft-2026-07-05.md` (per Rule 24; amendment-body appended via this addendum)
- Section 6 UNVERIFIED convention: `section-6-unverified-disclosure-convention-2026-07-09.md`

## 10. Status

**Amendments FILED per Rule 24 addendum protocol.** Council #9 review at 2026-09-05 to 2026-10-05 window adjudicates whether to accept each amendment. Framework's prior-artifact immutability preserved.
