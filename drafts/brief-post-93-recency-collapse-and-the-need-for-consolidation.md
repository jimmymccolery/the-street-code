# Drafting brief — Post 93 "Recency Collapse and the Need for Consolidation"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 93 within Posts 89-95 retraction block. Per R5 design: justifies tiered storage via 0.995/game-hour decay anchor; links to hybrid path posts 97-99.
**Scope verdict:** SAFE — methodology + open-academic citations + technical analysis. No Memory Lanes protected scope (no NPC-roster naming, no save-format internals).
**Length target:** 3000-4000 words per R5 design.

## Thesis

Naive memory architectures for procedural characters operating over multi-decade timescales fail to one of two failure modes:
1. **Recency collapse:** raw event memory grows unbounded → save-file bloat + retrieval cost prohibitive → eventually some hard cap forces deletion → "the framework forgot the 1950s."
2. **Premature compression:** aggressive consolidation throws away the texture that makes characters feel like they've LIVED through time → "the framework remembers the 1950s but only as flat summary."

Modified-C-bis adopts a **tiered consolidation** model: raw events live in Layer 1 with bounded recency window; consolidation pass (yearly per CW R6 ratification 2026-06-10) promotes key events to Layer 2 encoded-and-reconstructed perspective; everyday events decay via 0.995/game-hour anchor. The 0.995 decay anchor is the load-bearing technical commitment that makes the architecture computationally tractable at multi-decade scale.

Post 93 explains the recency-collapse problem + the consolidation solution + the 0.995 anchor + why this links to the hybrid-path posts (97-99) that handle the runtime-cost trade-offs.

## Sections (outline)

1. **Hook:** "Modified-C-bis lets characters live through 30 game-years of bowling-alley regulars. Naively storing every interaction event would crash the save file. Naively summarizing them would flatten the texture. Here's how the framework threads the needle."

2. **The recency-collapse problem.** Walk through the arithmetic:
   - 88 NPCs × ~10 interactions/game-week × 52 weeks × 30 game-years = ~1.37M interaction events
   - Even at 100 bytes per event = 137MB raw — too large for save-state on iOS
   - Retrieval cost: O(N) over millions of events makes mood-congruent retrieval (Eich 1995) impractical
   - Naive growth makes the architecture fail to deliver the multi-decade promise

3. **The premature-compression failure mode.** What aggressive compression looks like:
   - Replace all 1950s interactions with "had X interactions; net sentiment Y"
   - Player observes character + finds them flat ("you remember me as a number?")
   - Loses the texture that distinguishes Modified-C-bis from Sims/RimWorld
   - The framework would be solving a problem at the cost of the feature

4. **The tiered consolidation model.** Three layers + consolidation pass:
   - **Layer 1 (raw):** recent events stored verbatim; bounded recency window (~last 6-12 game-months per character)
   - **Layer 2 (encoded-and-reconstructed):** consolidated events that promoted from Layer 1 during yearly consolidation pass
   - **Layer 3 (accumulator):** running (valence + arousal + stress) state per DC1 split; integrates Layer 1 + Layer 2 contributions
   - **Yearly consolidation pass:** triggered at game-year boundary; promotes core events (high-affect; high-pair-history-impact; high-trait-modulated-encoding-weight) to Layer 2 with summary form; decays everyday events via 0.995/game-hour anchor

5. **The 0.995/game-hour decay anchor.** Why this specific value:
   - Half-life of ~138 game-hours = ~6 game-days (assuming 24 game-hours/game-day)
   - In a typical bowling alley, that's enough to retain the texture of a busy game-week + softens by next game-week
   - Tuneable per character via trait modulation (high-stress characters retain longer; secure-attachment characters consolidate faster)
   - Empirically inspired by forgetting-curve literature (Ebbinghaus 1885; modern reanalyses) but not directly derived — operator's design choice based on game-feel + computational budget

6. **What gets consolidated vs decayed.** Decision rule for consolidation:
   - **Core events (promote to Layer 2):** affective spike events (high-arousal moments); pair-history-significant events (large sentiment shift); trait-modulated-significant events (e.g., for high-anxious-attachment characters, perceived-threat events); first-occurrence events ("the time the player first introduced themselves")
   - **Everyday events (decay):** routine interactions (regular tipping, regular ordering, regular small talk); events that don't shift any axis of (valence, arousal, stress, pair-sentiment) by threshold

7. **Why this links to the hybrid path (Posts 96-98).** Tiered consolidation is necessary but not sufficient for V1 performance:
   - Naive active inference scoring even on consolidated layers may still be too slow at 88 NPCs
   - Need cached policies + slow consolidation (Post 98 hybrid path: Project Zomboid offscreen storylet pattern)
   - Multi-graph memory (Post 97: MAGMA-style typed indexes) for fast retrieval within tiered storage
   - LLM-backed observation/reflection (Post 96: Park 2023 Generative Agents) only at consolidation-trigger boundaries, not per-interaction

8. **V1 implementation cost.** Schema: tiered storage + yearly-pass scheduler. ~20-36 hours BUILD-side per R5 ratification candidate table.

9. **Honest scope: what consolidation doesn't solve.** It doesn't solve:
   - The retraction-condition-Trigger-1 risk (state-space self-variable accidentally encoded via consolidated summary)
   - The cross-cultural-tags problem (consolidation may erase cultural-context tags if not preserved through the pass)
   - The save-load determinism (consolidation timing must be deterministic across save/load boundaries)

10. **Closing.** The 0.995 anchor is not derived; it's a designed choice that respects both empirical literature and computational budget. The framework's transparency about it (publishing the anchor + the trade-offs) is the discipline.

## Key citations

- **Ebbinghaus, H. (1885).** *Über das Gedächtnis: Untersuchungen zur experimentellen Psychologie*. (Forgetting-curve canonical anchor; secondary citation only — modern reanalyses preferred.)
- **Murre, J. M. J., & Dros, J. (2015).** Replication and analysis of Ebbinghaus' forgetting curve. *PLOS ONE* 10(7):e0120644. (Modern forgetting-curve reanalysis.)
- **Eich, E. (1995).** Searching for mood dependent memory. (Mood-congruent retrieval anchor; ties to Post 91.)
- **Sleep-dependent consolidation:** Walker 2017 *Why We Sleep* or Stickgold & Walker 2013 review.

## Cross-links

- LINKS BACK TO: Post 91 (sentiment override + pair-history accumulation)
- LINKS FORWARD TO: Posts 96 + 98 + 99 (hybrid path technical sequence — consolidation is necessary but not sufficient; need cached policies + multi-graph memory + LLM-at-consolidation-boundary)
- IMPLEMENTATION TIE: Round 9 generative-model formalization (Q3 belief-update + consolidation-phase filter)

## Drafting prerequisites

- Murre & Dros 2015 forgetting-curve replication (~1h).
- Sleep-dependent consolidation literature scan (~1h; Stickgold-Walker 2013 review).
- Operator-side benchmark of save-file size at varying consolidation thresholds (~2h technical exercise; informs the 0.995 anchor's empirical defense).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision + benchmark write-up. Target 3000-4000 words.
