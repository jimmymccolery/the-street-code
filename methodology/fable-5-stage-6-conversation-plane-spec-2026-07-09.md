# Stage 6 Proposal — Conversation Plane (Computed Projection)

**Status:** PROPOSAL — pre-research-arc sketch, authored outside the framework (external substrate: Perplexity Computer). Not canonical. Subject to multi-substrate review, Rule 24 discipline on adoption.
**Date:** 2026-07-09
**Format lineage:** Stages 2–5 (Posts 0197–0200) — research grounding by parallel agents, plane module + typed-event-bus integration, numbered hypothesis harness with quantitative pass criteria, architectural-fix-not-test-criteria discipline, cultural-bundle extension, deterministic seeded replay, performance tier gates, premortem, Council items filed.
**Scope amendment required:** Post 0146 explicitly disclaims dialogue systems as out of scope. This Stage brings conversation **mechanics** (act selection, flow dynamics, relational consequence) into scope. **Surface realization (the actual words) remains out of scope** — it is a separate authoring workstream (utterance banks), gated behind this Stage passing.

---

## 1. Position in the Architecture

### 1.1 What the conversation plane is
A **computed projection, not a persistent plane** — per the Post 0198 precedent, where the operator's original persistent-Cartesian-plane proposal for first impressions was revised into a deterministic function of (perceiver, target, context, seed). Same move here:

- `ConversationState` is **ephemeral**: instantiated at conversation start as a deterministic function of (participants, context, seed), evolved per turn, discarded at conversation end.
- Only **typed events persist**: `DialogueActEvent`s on the event bus, consumed by GAMYGDALA appraisal → PAD, pair-relational plane (trust/investment/commitment), attachment-modulated memory encoding, habitus plane.
- The 2-D "Cartesian plane" the operator envisioned survives as a **diagnostic surface** (intimacy × tension trajectory plot in the operator-facing UI), never as a decision surface — consistent with the canonized single-observation-surface failure pattern (Layer 3 alone was the wrong surface; Post 0182 lineage).

### 1.2 What it is not
- Not a generator of words. No LLM in the runtime loop (unchanged).
- Not new relational bookkeeping. Trust, sentiment, investment, commitment stay owned by the pair-relational plane (Post 0199). The conversation plane **reads** them at spawn and **writes** to them only via typed events — no duplicated state to drift.
- Not a topic/knowledge system. `topicRef` pointers resolve against existing memory traces and Schema v0.2 runtime tables; conversation does not carry world knowledge of its own.

### 1.3 Why this junction matters (M10 lesson)
Post 0201 found the M10 cultural modulator architecturally inert (≤4% contribution). Conversation is the highest-visibility junction where cultural bundle content can become behavioral: directness norms, silence tolerance, turn-taking rhythm, register, honorifics are all *audible* culture. H6 below is an explicit non-inertness gate with a quantitative floor, so this Stage cannot ship a second inert cultural mechanism.

---

## 2. Research Grounding — Four Agent Briefs

Per Stage 4 convention (four research agents, named literature per mechanism). All citations below are real published work; per R19, every citation must survive a verification round (Perplexity/GPT-5.5 byte-level pass, as run in Post 0198's late-evening addenda) before canonization.

**Agent 1 — Conversation structure and turn-taking (Conversation Analysis).**
- Sacks, Schegloff & Jefferson 1974, "A Simplest Systematics for the Organization of Turn-Taking for Conversation," *Language* 50(4): adjacency pairs, turn-allocation, repair organization.
- Stivers et al. 2009, "Universals and cultural variation in turn-taking in conversation," *PNAS* 106(26): all 10 sampled languages minimize gap and overlap, but mean response offsets vary by culture (~±250 ms band) — this is the empirical warrant for **bundle-scoped turn-gap norms** rather than universal constants.
- Clark & Brennan 1991, "Grounding in Communication" (in *Perspectives on Socially Shared Cognition*): common ground as jointly accumulated stock — basis for the `groundingStock` state dimension and its role in the 0.78 sentiment-plateau question (§8.4).

**Agent 2 — Relational communication dynamics.**
- Reis & Shaver 1988 intimacy spiral (already canonical, Post 0199): disclosure → perceived partner responsiveness → intimacy.
- Altman & Taylor 1973, *Social Penetration*: disclosure depth/breadth escalation is reciprocal; one-sided disclosure does not deepen intimacy.
- Gottman 1994 (*What Predicts Divorce*): four horsemen as dialogue acts; ~5:1 positive-to-negative interaction ratio distinguishing stable dyads; repair attempts and their conditional success. Wired to existing Post 0199 mechanics (trust erosion ~3 units/horseman-event; Hawkins, Carrère & Gottman 2002 sentiment override already canonical).
- Berger & Calabrese 1975, uncertainty reduction theory, *Human Communication Research* 1: question-density decays as familiarity rises — testable act-mix prediction.

**Agent 3 — Accommodation and alignment.**
- Giles, Coupland & Coupland 1991, Communication Accommodation Theory: convergence signals affinity, divergence signals distance/identity assertion.
- Pickering & Garrod 2004, "Toward a mechanistic psychology of dialogue," *BBS* 27(2): interactive alignment as an automatic priming mechanism — supports cheap, deterministic style-match computation.
- Ireland et al. 2011, "Language Style Matching Predicts Relationship Initiation and Stability," *Psychological Science* 22(1): LSM quantitatively predicts relationship outcomes — warrant for `styleMatch` as a scalar with relational consequence.

**Agent 4 — Sociolinguistics, politeness, and linguistic capital.**
- Brown & Levinson 1987, *Politeness*: face-threatening acts; indirectness scales with power distance + social distance + imposition — the act-selection cost function.
- Labov 1966/1972: register stratification and style-shifting by class and attention — grounds code-switching costs.
- Bourdieu 1991, *Language and Symbolic Power*: linguistic capital as embodied cultural capital; ties conversation directly into the Stage 5 habitus plane (field-dependent legitimacy of speech styles; habitus-field mismatch is *heard*).
- Dunbar 1996, *Grooming, Gossip and the Evolution of Language*: gossip as social-bonding and reputation-transmission mechanism — grounds the gossip act type and §9.2.

**Annex A — Dialogue-act taxonomy standards:** SWBD-DAMSL (Jurafsky, Shriberg & Biasca 1997) and ISO 24617-2 (dialogue act annotation) as naming/structure references — adapt, don't adopt wholesale (42-tag SWBD granularity is oversized for runtime).
**Annex B — Games precedent:** Façade drama/beat management (Mateas & Stern 2003), Versu social practices (Evans & Short 2014, *IEEE TCIAIG* 6(2)), Talk of the Town knowledge/rumor propagation (Ryan et al., AIIDE Experimental AI in Games workshop 2015), Dwarf Fortress topic system. Precedent confirms: act-level selection + templated surface is the shipped-game granularity; POS-level assembly has no successful precedent.
**Annex C — Corpora for the later utterance-bank workstream (NOT this Stage):** COHA, DARE, Switchboard, CANDOR (Reece et al. 2023, *Science Advances*), period newspapers, oral-history transcripts. Policy: AI as extractor-under-attestation with per-term provenance, never generator (R19).

---

## 3. Module Design — `conversationPlane.ts`

### 3.1 Data structures

```
DialogueActEvent (typed event bus)
  actType: DialogueActType        // §3.2 taxonomy
  speaker: NPCRef
  target: NPCRef | GroupRef
  topicRef?: MemoryTraceRef | SchemaRowRef   // resolves against existing stores only
  register: RegisterTag           // bundle-scoped
  faceThreat: number [0..1]       // computed, Brown-Levinson weighting
  intensity: number [0..1]
  seedPath: DeterministicSeedRef  // replay guarantee

ConversationState (ephemeral, per active conversation)
  participants: NPCRef[]
  context: { sceneId, privacy, audienceSize, bundleNormsInEffect }
  // five state dimensions (the "plane," properly 5-D with 2-D diagnostic projections):
  intimacyDepth: number           // Reis-Shaver / Altman-Taylor
  tension: number                 // face-threat stock, homeostatic (repair = restoring force)
  groundingStock: number          // Clark-Brennan common ground accumulated this conversation
  turnBalance: number             // signed; who is holding the floor
  styleMatch: number              // CAT/LSM convergence index

CulturalConversationExpectations (per CulturalContextBundle)
  directnessNorm, silenceTolerance, turnGapNorm (per Stivers 2009 variation),
  honorificRegisterRules, disclosureDepthNorms, repairStyleNorms,
  personhoodSpeechNorms   // Baselines A/B/C hooks; Wireduan communal-speech norms
                          // → consumer wiring for the communal_standing_b generosity-ledger scaffold
```

Initialization is the Post 0198 move: `ConversationState.init(participants, context, seed)` reads HEXACO, PAD, attachment, pair-relational state (trust, sentiment, investment), habitus/field positions, and bundle norms — computes starting values deterministically. Nothing persisted.

### 3.2 Dialogue-act taxonomy (16 acts, literature-grounded per type)

Mirrors the 14-event pair-relational taxonomy discipline (Post 0199): every act type carries a named-literature grounding and typed consequences.

| # | Act | Grounding | Primary consequences (via bus) |
|---|-----|-----------|-------------------------------|
| 1 | small_talk | Eggins & Slade 1997 | low-stakes grounding +, PAD micro-positive |
| 2 | question | Berger & Calabrese 1975 | grounding +, uncertainty − |
| 3 | disclosure (leveled 1–3) | Altman & Taylor 1973 | intimacy candidate (reciprocity-gated), attachment-modulated encoding |
| 4 | responsiveness_display | Reis & Shaver 1988 | validates pending disclosure → intimacy + |
| 5 | compliment | Gottman positive stock | sentiment +, face + |
| 6 | humor_bid | Martin et al. 2003 (HSQ styles) | style-conditional: valence + or trust − (§H7) |
| 7 | gossip | Dunbar 1996 | third-party sentiment transfer, reputation propagation |
| 8 | request | Brown & Levinson 1987 | face-threat, indirectness-scaled |
| 9 | refusal | Brown & Levinson 1987 | face-threat to requester, politeness-mitigated |
| 10 | advice | (face-threat variant of 8) | competence-face threat, habitus-gap-scaled |
| 11 | criticism | Gottman horseman 1 | trust −, tension + |
| 12 | contempt | Gottman horseman 2 | trust − (strongest), styleMatch divergence |
| 13 | defensiveness | Gottman horseman 3 | repair-blocking, tension + |
| 14 | stonewalling | Gottman horseman 4 | active turning-away (per Post 0199 fix #2), trust − |
| 15 | repair_attempt | Gottman 1994 | tension restoring force; success gated by sentiment override |
| 16 | apology / topic_shift (paired closers) | CA repair organization (SSJ 1974) | tension −, grounding reset |

Acts 11–14 are **not new mechanics** — they are the existing Post 0199 four-horsemen events, now emitted by a selection mechanism instead of scenario scripts. This is the plane's cheapest integration win: Stage 4 already built the consequence side.

### 3.3 Act selection (no LLM, cached, deterministic)
Softmax over candidate acts consistent with the existing EFE/cached-policy decision layer (Layer 5):
- **Priors** from HEXACO (e.g., eXtraversion → floor-holding and act rate; Agreeableness → repair propensity; Honesty-Humility → disclosure honesty) — wiring beyond Agreeableness is deliberate, addressing Council #9 Item 106's broader-HEXACO-wiring candidacy.
- **Modulators**: PAD state (arousal → intensity; low dominance suppresses face-threatening acts), attachment (avoidance suppresses disclosure depth; anxiety raises reassurance-seeking question rate), pair-relational trust/sentiment (Gottman override gates horseman emission), habitus/field (power-distance term in the Brown-Levinson cost), bundle norms (directness, silence, turn-gap).
- **Cost function**: face-threat weighting per Brown & Levinson (power distance from field position gap + social distance from relationship + imposition from act type).
- Per-tick cost must fit the cached-policy budget; sophisticated inference only at consolidation (unchanged).

### 3.4 Coupling matrix additions (sparse)
New couplings: conversation→PAD (via GAMYGDALA appraisal of received acts), conversation→pair-relational (existing event types), conversation→memory (disclosure content becomes trace with prediction-error-gated encoding), habitus→conversation (register cost), bundle→conversation (norms). No conversation→HEXACO direct coupling (personality drifts only via the existing cross-plane forcing path — preserves Stage 2 H2 semantics).

---

## 4. Cultural Layer and Consultation Gate

- `CulturalConversationExpectations` extends bundles A/D/E first (matching Post 0199's `PairRelationalCulturalExpectations` precedent), grounded per bundle: e.g., Anchor E's gaman profile predicts elevated silence tolerance and suppressed negative-affect disclosure; Anchor D's 1946 Tejano context requires code-switching cost modeling (Spanish/English register by scene: school HIGH-cost, home LOW — reusing Post 0192's scene-salience weighting).
- **HIGH-RISK representation flag:** dialect and register for Anchor A (1944 Black Philadelphia) and Anchor E (Japanese-American resettlement) fall squarely under the consultation-gate policy (CARE/OCAP/TK Labels). Named-reviewer sign-off remains unresolved ecosystem-wide; therefore **bundle speech norms block at anchor tier and do not ship to procedural tier until the gate resolves** — same posture as intersection nodes.
- **Dialogue-Surface Lint gate** (5 rules, Post 0179 lineage) extends to any future utterance-bank workstream; this Stage emits no surface text, so lint applies only to act-name and register-tag vocabulary.

---

## 5. Hypothesis Harness (H1–H8)

Headless Vitest, `--no-file-parallelism`, deterministic seeds. Baseline protocol: 5 seeds × 2 scenarios (per Post 0197), **100-seed sweep required before any meta-claim** (Post 0182 discipline; single-seed claims unreliable). Scenarios: (S1) canonical Anchor A betrayal scenario (reuse from Stage 1 integration harness, Post 0196); (S2) new "league night" scenario — 8 NPCs, repeated weekly co-location over 100k ticks, mixed-bundle dyads.

| H | Claim | Grounding | Pass criterion |
|---|-------|-----------|----------------|
| **H1** | Adjacency structure emerges from selection, not scripting: act-conditional response distributions honor pair constraints (question→answer/refusal dominant; repair_attempt→de-escalation) | SSJ 1974 | Conditional-probability table matches predicted dominance ordering in ≥90% of pairs, all 5 seeds; byte-identical replay per seed |
| **H2** | Intimacy requires reciprocity: matched disclosure-responsiveness loops raise intimacyDepth; one-sided disclosure plateaus or reverses | Reis-Shaver 1988; Altman-Taylor 1973 | Reciprocal dyads > one-sided dyads on ending intimacy, effect d ≥ 0.5, 100-seed sweep |
| **H3** | Gottman dynamics reproduce through selection: dyads whose emitted positive:negative act ratio ≥5:1 remain stable; horseman-dominant dyads show trust collapse; repair success is sentiment-override-gated | Gottman 1994; Post 0199 mechanics | Stable/distressed classification by ratio ≥80% accurate at 100k ticks; repair success rate significantly higher above sentiment threshold |
| **H4** | Accommodation: styleMatch converges in high-affinity dyads, diverges under contempt; attachment avoidance attenuates convergence | Giles CAT; Pickering-Garrod 2004; Ireland 2011 | Convergence slope sign correct in ≥3 of 4 conditions per seed; avoidance attenuation d ≥ 0.3 |
| **H5** | Politeness scales with position: indirectness ratio (indirect:direct request forms) increases monotonically with field-position power gap | Brown-Levinson 1987; Stage 5 habitus plane | Monotonic trend across ≥4 power-gap buckets, Spearman ρ ≥ 0.6 |
| **H6** | **Cultural non-inertness gate:** bundle conversation norms produce measurable cross-bundle behavioral divergence (act mix, silence, turn-gap, disclosure depth) between A/D/E dyads | Stivers 2009; bundle scholarship | Bundle assignment explains **≥15% of variance** in act-mix profile (vs. M10's ≤4%); if <15%, the Stage FAILS its own reason for existing — redesign junction, do not ship |
| **H7** | Humor is style-conditional: affiliative bids raise dyad valence broadly; aggressive bids erode trust in low-trust dyads but bond high-trust dyads | Martin et al. 2003 | Interaction effect (humor style × trust level) significant, direction correct, 100-seed sweep |
| **H8** | **Offscreen equivalence (scale gate):** summarized conversations (aggregate typed events, no act sequence) yield long-run sentiment/trust trajectories statistically indistinguishable from full act-level simulation | Project Zomboid offscreen pattern | KS test on 100k-tick ending sentiment distributions, p > 0.05 across 100 seeds; validates LOD switching for 1,000–5,000 NPCs |

**Architectural-fix discipline:** Stage 4 needed 3 architectural fixes to reach 7/7; expect the same here. Predicted fix sites (premortem, §7): reciprocity gating (H2), repair gating (H3), variance floor (H6). Fixes must change architecture, never pass criteria.

**Anchor-integrity side gates (every run):** HEXACO displacement < 2.0 under conversational forcing (Stage 1 threshold); PAD returns within tolerance post-conversation; no anchor-pair encoding collisions (Post 0196 UMAP diagnostic re-run with conversation-derived features added).

---

## 6. Performance and Scale Gates

- **Tick budget:** N=5,000 baseline is 0.896 ms/tick with ~260 bytes/Sim. Conversation plane budget: ≤ +0.15 ms/tick at N=5,000 with 250 concurrent active conversations (act selection O(1) from cached priors; ConversationState only allocated for player-adjacent/onscreen conversations per H8 LOD).
- **Memory:** ephemeral ConversationState ≤ 200 bytes/active conversation; zero persistent per-Sim overhead beyond existing planes (events flow through the existing bus and stores).
- **Determinism:** byte-identical replay to 10,000 ticks including active conversations; seed threading through act selection and topic resolution.
- **Device tier:** iPad Mini baseline must retain ≥1.5x headroom with conversation plane enabled (current floor 1.9x — budget consumes no more than ~0.4x of it).

---

## 7. Premortem (named failure modes)

1. **Double-bookkeeping drift** — conversation plane accumulates persistent relational state parallel to pair-relational plane. *Mitigation:* architectural — ConversationState is ephemeral by type; persistence only via bus events.
2. **Second inert mechanism (M10 repeat)** — norms wired as a weak scalar modulator that HEXACO/attachment swamp. *Mitigation:* H6 hard gate at ≥15% variance; norms enter act selection as priors and costs (structural), not as a multiplier.
3. **Single-surface verdicts** — reading the 2-D intimacy×tension plot as truth. *Mitigation:* plot is diagnostic-only; verdicts require the harness (Post 0197 discipline: empirical harness parallel to any UI).
4. **Fabricated grounding** — the act taxonomy or bundle norms citing invented scholarship. *Mitigation:* scheduled R19 citation-verification round before canonization (Post 0198 precedent found 3 fabrications in one evening).
5. **Representation harm at procedural tier** — dialect/register norms auto-applied to 100 procedural NPCs per bundle without review. *Mitigation:* consultation-gate block (§4) until named-reviewer sign-off resolves.
6. **Termination unawareness** — harness passes 7/8 and pressure builds to ship anyway. *Mitigation:* H6 and H8 are designated non-negotiable gates in advance.

---

## 8. Interactions with Open Questions

- **8.1 Sentiment 0.78 plateau (undeliberated):** `groundingStock` offers the missing decay path — sentiment maintenance gated on periodic grounding refresh; stale common ground → slow decay; re-contact with high stored investment → rapid recovery ("old friends pick up where they left off," Rusbult floor). This converts an undeliberated constant into a deliberated mechanism. File as a linked hypothesis for Stage 6.1.
- **8.2 Wireduan generosity ledger (communal_standing_b):** gossip and communal-speech acts are the natural consumer — public generosity acknowledgment propagates standing through third-party talk. First concrete consumer wiring for the Steam V1.0 scaffold.
- **8.3 Fiske relationship_mode ablation (un-run 4-condition gate):** conversation act-mix profiles give that ablation a much richer observable than Layer 3 accumulators — consider running it inside the Stage 6 harness.
- **8.4 Negative event types (deferred Phase 2.5+):** envy/betrayal/resource-conflict get their delivery mechanism (gossip, refusal, contempt) without new plumbing when un-deferred.

---

## 9. Council #9 Items to File

1. Scope amendment to Post 0146's dialogue-systems disclaimer (mechanics in, surface out).
2. H6 variance floor (≥15%) as the general non-inertness standard for any future cultural mechanism (generalizes the M10 finding into a rule candidate).
3. Consultation-gate dependency: conversation norms join intersection nodes as blocked-at-procedural-tier pending named-reviewer resolution.
4. Utterance-bank workstream charter (corpus extraction under R19 attestation; COHA/DARE/Switchboard/CANDOR; provenance-per-term).
5. Deterministic-projection pattern (Post 0198 first-impressions + Stage 6 conversation, n=2) as a named architectural pattern candidate: "ephemeral computed interaction-state, persistent typed events."

---

## 10. Elevator Pitch (empirically honest, per Post 0197 discipline)

> **NPCs whose relationships are built one conversation at a time — with no scripts and no AI text generator.** Every exchange is a sequence of typed conversational moves — disclosures, jokes, requests, criticisms, repairs — chosen by each character's personality, mood, attachment style, cultural upbringing, and social position, and every move leaves a permanent mark on trust, intimacy, and reputation. Two strangers become friends because their disclosures were reciprocated; a marriage erodes because contempt outran repair; a pinboy hears the manager differently than the manager hears him, because class position is audible. It runs deterministically at thousands of NPCs on an iPad, every conversation replayable byte-for-byte — and it is the first mechanism where a character's cultural world measurably changes how they behave, not just what the wiki says about them.

*(Pitch claims map to gates: "no scripts" → H1; "reciprocated" → H2; "contempt outran repair" → H3; "class is audible" → H5; "cultural world measurably changes behavior" → H6; "thousands on an iPad" → H8 + §6. Per Post 0197, if a gate fails, the corresponding pitch sentence is deleted, not softened.)*

---

## 11. What This Enables In-Game

- **Legible relationship causality:** players can trace *why* two NPCs drifted apart to specific observable exchanges — the alley regular who stopped joking with the manager after the refused raise.
- **Culture and era you can hear:** 1946 San Antonio and 1944 Philadelphia dyads *converse differently* by measurable act-mix, silence, and register — the Chronological Challenge mode gains a per-decade social texture channel.
- **Bark/subtitle layer for free:** each DialogueActEvent is already a UI-ready caption ("Rosa opens up to Marcus about her brother") without writing a single line of dialogue — the Simlish/Dwarf Fortress solution, shippable before any utterance bank exists.
- **Gossip-driven reputation:** communal standing, rumors about the alley, league-night social politics — all propagate through the same act system.

## 12. Beyond Conversation — Same Machinery, Other Systems

The reusable pattern is: **ephemeral computed interaction-state + typed move selection + persistent relational consequence.** Everything below is the same module shape with a different move taxonomy:

1. **Negotiation & commerce:** the 1952 AMF lease-vs-1956 Brunswick-purchase decision as an interactive negotiation — offers, concessions, face-threats, walk-aways — with the salesman's HEXACO and the operator's capital position driving the same Brown-Levinson cost function. Haggling, hiring interviews, supplier relationships.
2. **Labor relations:** pinboy strikes, no-shows, ball-trick retaliation (your documented failure modes) become emergent outcomes of accumulated unrepaired horseman exchanges with management rather than scripted events — Phase 2.5's negative event types get their causal substrate.
3. **Competition psychology:** a bowling match as a pressure×flow interaction plane — trash talk (face-threat acts), choking under an audience (arousal forcing), rivalry formation from repeated matches. Era-conditional federation NPCs gain competitive personalities.
4. **Mentorship & skill transmission:** pit-work coworker mentorship (already in your bowling Scene) as disclosure/advice/responsiveness loops that gate skill-learning rates — apprenticeship on Wacquant's 6–24-month habituation timescale, linking directly into the Stage 5 habitus plane.
5. **Group dynamics:** league teams as multi-party conversation state (turnBalance generalizes to floor-dominance; cohesion as group-level groundingStock) — team chemistry that predicts league retention through the 8.4M→1.8M historical arc.
6. **Venue atmosphere as emergent aggregate:** mean valence/tension of active conversations per venue = an "alley vibe" metric patrons perceive and respond to — a tycoon-loop signal (vibe → patronage) that is fully emergent rather than authored.
7. **Family & cozy systems (RoomToLife):** the 90s-bedroom product's emotional register is family conversations through a wall — dinner-table dynamics, sibling repair cycles, a parent's stonewalling — all on the same 16-act taxonomy with a domestic-field politeness profile.
8. **Cross-product memory ("memory and place"):** conversation events written into biographical records via the entity registry mean a RoomToLife character can *remember a specific 1962 alley conversation* — provenance-tracked, replayable, true.

---

## 13. Out of Scope (explicit)

Surface text generation and utterance banks; voice/audio; player-NPC free-text dialogue; any runtime LLM; multi-party conversations beyond the league-night scenario's dyadic decomposition (full n-party floor management deferred to Stage 6.2); non-verbal channel integration with the Stage 3 first-impressions plane (natural follow-on, deferred).
