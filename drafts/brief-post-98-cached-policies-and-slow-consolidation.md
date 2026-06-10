# Drafting brief — Post 98 "Cached Policies and Slow Consolidation"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 98 — CLOSER of the Posts 96-98 hybrid-path block. Per R5 design: Project Zomboid offscreen storylet architecture + visible-behavior separation = production analogy for cheap runtime + slow simulation layers.
**Scope verdict:** SAFE — methodology + commercial-precedent META-level discussion. No protected scope.
**Length target:** 3000-4500 words.

## Thesis

Project Zomboid's offscreen storylet architecture (Indie Stone blog 2022 "the zuckerverse") demonstrated a production-ready pattern for procedural-character behavior at multi-decade scale: cheap CACHED POLICIES drive per-frame visible behavior; slow OFFSCREEN STORYLET SIMULATION runs at lower cadence (typically once per game-day or game-week) to update the deeper state that cached policies depend on. Modified-C-bis adopts this two-tier pattern. Cached policies (decision rules baked from sophisticated active inference at yearly consolidation boundaries) drive per-frame NPC behavior at iOS V1 framerate budgets. Slow consolidation (yearly per Post 93) updates the cached policies based on the year's accumulated experience. Post 98 closes the hybrid-path block by tying together: cached policies (cheap runtime) + multi-graph memory (Post 97 typed indexes) + Park 2023 backbone (Post 96 three-process decomposition) + audit-first sequencing (Post 94).

## Sections (outline)

1. **Hook:** "Project Zomboid shipped a multi-decade simulation game on indie budget by separating cheap-runtime from slow-simulation. Modified-C-bis adopts that exact pattern with active-inference machinery in the slow layer."

2. **What Project Zomboid showed.** Brief recap of the 2022 Indie Stone blog post:
   - Per-frame visible behavior: cheap state-machine policies + cached lookups
   - Offscreen storylet simulation: characters off-camera continue to exist + accumulate state via lower-cadence simulation passes
   - When player enters area, cached state is loaded + visible behavior resumes
   - Multi-zone game maps + dozens of NPCs + multi-day simulation at indie production quality

3. **The two-tier pattern formalized for Modified-C-bis.**
   - **Tier 1 (runtime; cheap; per-frame):** cached active-inference policies + sentiment-override lookups + trait-modulated heuristics. NPCs visible to player respond at ~30fps target without LLM calls or deep policy search.
   - **Tier 2 (consolidation; slow; per-game-year):** sophisticated active inference (under Path A operator ratification 2026-06-10 PM) evaluates the past year's accumulated experience; updates cached policies for the upcoming game-year; runs at consolidation-pass boundary (per Post 93)
   - **Audit-layer use of sophisticated inference (per Post 94):** runs at Tier 2 cadence; verifies cached policies still align with framework's structural-only-position-(a) discipline
   - **Cross-references:** Park 2023 three-process decomposition (Post 96) handled at Tier 2; multi-graph memory typed indexes (Post 97) at Tier 1 + Tier 2

4. **Per-frame computational budget walkthrough.**
   - iOS V1 framerate target: 30 fps (33ms per frame)
   - 88 NPCs × per-decision per-frame? No — most NPCs at any moment are stationary or in cheap-cached-policy mode
   - Active NPCs (in player's perceptual window): ~8-12 maximum
   - Per active NPC per frame: cached-policy lookup (~10-100 microseconds) + sentiment-override apply (~similar) + render — fits comfortably in framerate budget

5. **The 0.995/game-hour decay anchor's interaction with cached-policy invalidation.**
   - When does a cached policy need invalidation? When the underlying state (accumulator + trait + pair-history) has drifted beyond a threshold from when the cached policy was baked
   - Drift detection: cheap per-frame check on a few key state-scalars; if threshold exceeded, mark cached policy for re-bake at next consolidation
   - Most cached policies last most of a game-year unchanged; this is the cost-saving the hybrid path delivers

6. **Comparison: full per-frame sophisticated inference vs cached-policies-with-slow-bake.**
   - Full per-frame sophisticated inference: 88 NPCs × deep policy search × per-frame = breaks budget
   - Cached policies + slow-bake: 88 NPCs × cheap lookup × per-frame + ~1 deep policy search per character per game-year at consolidation = fits budget
   - Quality trade-off: cached policies are static within a game-year; characters won't surprise the player mid-year. Acceptable for cozy sim; would be a problem for combat-driven gameplay.

7. **Audit-layer integration with cached policies.**
   - At consolidation-pass boundary, sophisticated active inference runs in audit-layer mode (per Post 94)
   - Audit verifies: does the cached policy align with position-(a)-compatible EFE-minimization under updated state? does any cached policy now require sophisticated-inference-style metacognitive recursion that the cached form doesn't support?
   - Failed audit → cached policy regenerated with sophisticated-inference apparatus; characters whose cached policies needed updating get fresh policies starting next game-year
   - Audit logs: operator can review which cached policies needed regeneration as a debugging + quality-monitoring channel

8. **V1 implementation cost.** Two tiers + drift detection + audit-pass integration. ~30-50 hours BUILD-side estimated.

9. **Honest scope: where cached-policy + slow-consolidation fails.**
   - Doesn't handle rare-event-driven cached-policy invalidation gracefully (player can mid-year trigger a cached-policy mismatch by doing something extraordinary; cached policy won't re-evaluate until consolidation)
   - Doesn't address cross-NPC interaction depth (cached policies are per-NPC; multi-NPC interaction surprises need additional handling)
   - Doesn't scale beyond cozy-sim cadence (combat or fast-paced gameplay would invalidate the cached-policy assumption)

10. **Closing.** "The hybrid path is three borrowings + one combination: Park 2023 backbone + MAGMA typed indexes + Project Zomboid offscreen storylet pattern + active-inference state-space-content discipline. Novel in combination, not in components. Honest enough to ship."

## Key citations

- **Project Zomboid Indie Stone blog 2022 "the zuckerverse":** https://projectzomboid.com/blog/news/2022/03/the-zuckerverse/ (commercial-precedent reference; verify URL still active at drafting time).
- **Park 2023 Generative Agents** (cross-referenced from Post 96).
- **MAGMA arXiv:2601.03236** (cross-referenced from Post 97).

## Cross-links

- LINKS BACK TO: Post 94 (audit-first sequencing) + Post 93 (consolidation pass) + Posts 96-97 (Park 2023 + MAGMA backbones)
- LINKS FORWARD TO: Post 95 retroactively (V1 spec includes hybrid-path commitments)
- IMPLEMENTATION TIE: Round 9 Q4 EFE decomposition specifies the audit-layer vs runtime-layer apparatus + the per-frame budget constraint

## Drafting prerequisites

- Project Zomboid Indie Stone 2022 blog post primary-text read + verify URL active (~30 min).
- Operator-side cached-policy invalidation logic sketch (~1-2h technical exercise).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision + cross-link verification. Target 3000-4500 words.
