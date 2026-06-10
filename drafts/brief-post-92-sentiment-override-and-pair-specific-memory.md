# Drafting brief — Post 92 "Sentiment Override and Pair-Specific Memory"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 92 within Posts 89-96 retraction block. Per R5 design: bridge from literature to games using bowling-alley tipping scenario + commercial-precedent comparison.
**Scope verdict:** SAFE — methodology + open-academic citations + commercial-precedent discussion at META-rule level. No Memory Lanes protected-scope details (e.g., does NOT name specific NPC roster + does NOT enumerate pair-history accumulator weights).
**Length target:** 3500-5000 words per R5 design.

## Thesis

The pair-specific relational history mechanism in Modified-C-bis has a canonical psychological-literature anchor that Round 1 (Gemini DR) surfaced and the framework adopted: Gottman's **sentiment override** (Hawkins, Carrère & Gottman 2002 *Journal of Marriage and Family* 64(1):193-201). Sentiment override formalizes what was already intuitively obvious: pair-relational behavior is biased by an accumulated cumulative-affective sentiment toward the partner, not just by the current interaction's content. Once a positive sentiment-override regime engages, partners interpret ambiguous behavior charitably; once a negative regime engages, the same behavior is interpreted as confirmation of partner bad-intent. Post 92 walks through how this maps to game NPCs with the bowling-alley tipping scenario as the worked example + compares the framework's pair-history mechanic against the commercial precedents (Sims 4 Sentiments, RimWorld opinions, CK3 memories, Dwarf Fortress emotional memory tiers).

## Sections (outline)

1. **Hook:** "A regular bowler tips a pinboy a quarter. A different bowler tips the same pinboy a quarter. Five years later, the two regulars are very different to the pinboy. The framework's job is to make that legible mathematically."

2. **The bowling-alley tipping scenario.** Open with a concrete walkthrough:
   - Bowler A (regular; tips 25¢ for 10 game-years; pinboy now expects the quarter and feels mild gratitude weekly)
   - Bowler B (irregular; tipped once with a 50¢ tip during a busy night; pinboy retains the moment but it doesn't shape weekly expectations)
   - Bowler C (no-tip history; one-time-tip 50¢; pinboy is surprised; the moment is encoded but the sentiment-override regime is uncertain)
   - The same one-time-tip event becomes gratitude / reputation / pair trust / public norm signal / nothing depending on encoding conditions

3. **What sentiment override is.** Hawkins, Carrère & Gottman 2002: married couples' perception of partner behavior is biased by an accumulated positive-or-negative sentiment regime. The regime acts like a Bayesian prior over partner behavior interpretation. Discuss the empirical methodology + the cross-cultural caveat (sample WEIRD-derived; broader cross-cultural literature is mixed).

4. **How it maps to game NPCs.** Sentiment override implementation in Modified-C-bis:
   - Each ordered pair (A, B) has a sentiment scalar in [-1, +1]
   - Updates with each interaction event using a decay-toward-current + drift-from-history formula
   - Biases event-interpretation in pair-history-accumulator (positive sentiment → over-encode positive-tagged events; negative sentiment → over-encode threat-tagged events)
   - Cap on number of active pair-sentiments per character (Sims 4 cap of 4 sentiments per Sim-pair is the commercial precedent; framework adopts 3-5 active sentiments per ordered pair per R5 design)
   - Older sentiments either decay, merge into summaries, or promote to core pair events (consolidation per Post 94)

5. **Commercial precedent comparison.** Compare 4-5 systems honestly:
   - **Sims 4 Sentiments** (EA update notes November 2020 + The Sims Wiki): shared memorable experiences form sentiments; one-sided possible; max 4 active per Sim-pair; weakest-sentiment replacement. Closest commercial precedent for pair-specific affective memory at consumer scale.
   - **RimWorld opinions** (RimWorld Wiki Social): bounded mood/opinion modifiers per pair; decay; threshold-triggered behaviors. Simpler than sentiments but proven at scale.
   - **CK3 memories** (CK3 Wiki Patch 1.7): chronological event memories used by content (event triggers reference past pair history). Memory-as-content-trigger rather than memory-as-affective-substrate.
   - **Dwarf Fortress emotional memory tiers** (DF Wiki Memory thought): tiered memory storage from recent → consolidated → forgotten. Distinct from CK3's event-trigger model.

6. **What Modified-C-bis adds beyond the commercial precedents.**
   - Multi-decade NPC memory (precedent absence)
   - Emotion-conditioned encoding (precedent absence)
   - Retrieval-time affect modulation (precedent absence at the same depth)
   - Active-inference-inspired decision scoring under position-(a) discipline (precedent absence)
   - The combination, NOT any individual component, is the novelty claim per R5 "novel in combination, not in components" honesty (anchor for Posts 97-99 hybrid path)

7. **What Modified-C-bis does NOT do better than the commercial precedents.**
   - Production engineering — Sims/RimWorld/CK3/DF all ship at consumer scale; Modified-C-bis is a research framework spec, not yet production-tested
   - UI surfacing — the player-facing rendering of relationships is a separate problem the framework does not solve
   - Modding extensibility — Modified-C-bis is operator-internal; the commercial precedents have mod scenes

8. **Cross-cultural caveat for pair-sentiment.** Sentiment override empirical anchor is WEIRD-sample-derived; Hawkins-Carrère-Gottman 2002 is U.S. married-couple sample. For multi-decade multi-cultural NPC populations, the framework should NOT assume the same sentiment-override dynamics hold universally without cultural-context tags. Posts 100-104 cross-cultural sequence covers the broader handling.

9. **Closing.** The framework's pair-specific memory architecture is grounded in canonical psychological literature (Gottman) + commercial-precedent-validated (Sims) + extended (multi-decade + emotion-conditioned). Honest scope: novel in combination, not in components.

## Key citations

- **Hawkins, M. W., Carrère, S., & Gottman, J. M. (2002).** Sentiment override. *JMF* 64(1):193-201.
- **Sims 4 Sentiments:** EA update notes (Nov 10, 2020); The Sims Wiki Sentiment page.
- **RimWorld Social mechanics:** RimWorld Wiki.
- **CK3 memory:** Crusader Kings 3 Wiki Patch 1.7 + Memory pages.
- **Dwarf Fortress emotional memory:** DF Wiki Memory (thought) page.
- **Cross-cultural Gottman caveat:** various cross-cultural studies of marriage interaction; flag as area where Modified-C-bis defers to operator-side reading.

## Cross-links

- LINKS BACK TO: Post 89 (retraction table — pair-history is added commitment) + Post 90 (DC1 split — sentiment scalar is one dimension) + Post 91 (attachment style modulates pair-encoding)
- LINKS FORWARD TO: Posts 97-99 hybrid path (commercial-precedent honesty) + Post 100 (cross-cultural framing)
- IMPLEMENTATION TIE: Round 9 generative-model formalization (Q3 belief-update + Q4 EFE decomposition references pair-history scalars)

## Drafting prerequisites

- Hawkins, Carrère & Gottman 2002 primary text (~1h).
- Sims 4 Sentiments documentation review (EA notes + Wiki + community discussions; ~1h).
- RimWorld + CK3 + DF Wiki review for accurate commercial-precedent description (~1.5h).
- Cross-cultural marriage-research caveat literature scan (~1h).

## Hour estimate

At observed velocity: ~6-9 hours drafting + revision + commercial-precedent verification. Target 3500-5000 words.
