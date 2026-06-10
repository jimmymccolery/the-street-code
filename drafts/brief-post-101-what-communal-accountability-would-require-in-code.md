# Drafting brief — Post 101 "What Communal Accountability Would Require in Code"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 101 within Posts 99-103 cross-cultural sequence. Per R5 design: shows the generosity ledger + community accountability mechanics that Option (a) from R7 R6 Section 3 would have required.
**Scope verdict:** SAFE-METHODOLOGICALLY but HIGH cross-cultural exposure. Full 5-element disclosure discipline (humility brackets; primary-text-only citation; retraction condition).
**Length target:** 3500-5000 words.

## Thesis

The Wiredu mapping was dropped from V1 mechanics (Post 92; Posts 100) because the procedural-test → trait-slider mapping is a category error. But the more interesting question is: WHAT WOULD IT TAKE to actually implement Wireduan communal accountability in code? Post 101 specs out the Option (a) build (from R7 R6 Section 3): a generosity ledger that tracks accumulated relational obligations + a community accountability mechanic that surfaces obligations when characters interact + decision-scoring that consults obligations alongside individual preferences. Cost estimate: 8-18 hours design + 25-70 hours code. Why this is a Steam V1.0 candidate (~Oct 2027) not iOS V1: the mechanic is genuinely Wireduan rather than ornamental; it adds real game-design complexity (player interactions become consequence-laden in a way that goes beyond reputation); and the 1950s pinboy V1 baseline doesn't require it (Wiredu's universal first principle of morals can stay at the framework-paper layer for V1). Post 101 is a "what would it actually cost" post for the cross-cultural community.

## Sections (outline)

1. **Opening humility paragraph (5-element discipline).** Standard humility framing.

2. **Hook:** "I dropped the Wiredu mapping from V1 mechanics. This post specs what it would take to put it back — in real code, with real player consequences."

3. **What Option (a) from R7 R6 Section 3 was.** Recap:
   - Option (a): retain Wiredu as load-bearing AND build a real communal-accountability mechanic
   - Option (b): decouple HEXACO H from Wiredu philosophical grounding (banned per R7 R6: would discard defensible philosophical framing)
   - Option (c): DROP the Wiredu mapping as load-bearing V1 mechanics; retain only as philosophical framing in Post 84 + framework paper + self-correction post (Post 92). **OPERATOR CHOICE.**
   - Cost: Option (a) was 8-18h design + 25-70h code = 33-88 total hours. Path A operator ratification 2026-06-10 PM ("most comprehensive solution") makes Option (a) reconsider-able for Steam V1.0 + 143-day-runway accommodates re-add candidacy for V1 if operator decides — but Post 101 documents what it would COST, not what's been re-ratified.

4. **The generosity-ledger mechanic.** Spec walkthrough:
   - Each character maintains an outgoing-ledger + incoming-ledger
   - Outgoing-ledger: events where this character gave generosity to another character
   - Incoming-ledger: events where this character received generosity from another character
   - Ledger entries are tagged with: pair (giver, receiver), event-time, generosity-type (tip, favor, defense, time, attention), magnitude
   - Ledgers persist via Layer 2 consolidation pass (per Post 93) + entity-index typed-index lookup (per Post 97)

5. **The community-accountability mechanic.** Spec walkthrough:
   - At decision-scoring time, an active-inference evaluation reads the character's outgoing-ledger + incoming-ledger
   - Decisions are scored against TWO criteria:
     - Individual preference (the HEXACO + accumulator + pair-history form per V1 spec)
     - **Communal accountability adjustment:** does the candidate action MAINTAIN or VIOLATE the character's accumulated relational obligations? A character with high incoming generosity has obligations; refusing to reciprocate damages the communal-accountability score
   - The adjustment is a SECOND TERM in the EFE decomposition (per Round 9 generative-model formalization Q4)
   - Implementation: ~25-50 hours code (ledger storage + maintenance + decision-scoring integration)

6. **Walk through a bowling-alley scenario.** Pinboy + bowler regular tipping:
   - Without communal-accountability: bowler regular tips quarterly per HEXACO H + accumulator + sentiment override; pinboy responds per his own state
   - With communal-accountability: when bowler stops tipping after 5 years of habit, pinboy's incoming-ledger registers loss of accumulated incoming generosity; decision-scoring for pinboy's interaction with bowler now factors the obligation-shift; pinboy's responses become more pointedly cool until reciprocity resumes or relationship resets
   - Player observation: characters feel like they remember favors + slights at a deeper level than sentiment-override alone provides
   - This IS Wiredu's relational personhood operationalized: action evaluated in the context of accumulated relational obligations

7. **Why this is a Steam V1.0 candidate, not iOS V1.**
   - Cost: 33-88 hours total = substantial fraction of LEAN V1 budget (190-260h LEAN; even Path A's 270-410h ratification doesn't fit comfortably)
   - Marketing-copy discipline: communal accountability raises the cross-cultural exposure of the player-facing experience; full Marcus Reed Surface 8 re-review needed (more substrate-triangulation work)
   - Multi-decade payoff: communal-accountability ledgers payoff is most visible at Steam V1.0 Chronological Challenge mode (cross-era arcs where ledgers accumulate over decades)
   - 1950s pinboy V1 baseline doesn't strictly need it (Wiredu inspiration at framework-paper layer is sufficient for V1; mechanic at Steam V1.0 is the natural slot)

8. **Honest scope: what this spec doesn't solve.**
   - Doesn't solve cross-cultural breadth — the Wiredu-derived ledger mechanic respects Wiredu's framework but doesn't automatically respect other communal-ethics traditions (Confucian role ethics; Ubuntu; etc.)
   - Doesn't solve performance scaling — adding ledger lookups per decision increases per-frame budget
   - Doesn't replace cached-policies + slow-consolidation pattern (Post 98) — the ledger mechanic is an additional input to cached-policy regeneration at consolidation boundaries
   - Doesn't substitute for Cross/Crenshaw V1 SCHEMA-PLACEHOLDER discipline (Post 99's cross-cultural sequence is multi-traditional; no one mechanic addresses all)

9. **What this post is + what it is NOT.**
   - IS: a what-would-it-cost post for the cross-cultural-philosophy + game-design community
   - IS: documentation of Option (a) as a banked Steam V1.0 candidate
   - IS NOT: a commitment to ship Option (a) (operator may still choose to ship Option (c) DROP indefinitely)
   - IS NOT: a claim of Wireduan authenticity (the mechanic is INSPIRED BY Wireduan philosophy; structural-borrowing-only per 5-element discipline)

10. **Closing humility paragraph (5-element discipline).** Standard close. Retraction condition applies; primary-text-defensibility judgment standard; 14-day response timeline.

## Key citations

- **Wiredu, K. (1992).** Ch 9 *Person and Community*. CRVP.
- **R7 R6 Section 3 (item-1582) Option (a) cost estimates.** Reference: `~/.claude/projects/-Users-jimmy/memory/project_philosophical_research_arc_round_6_close_2026-06-09.md` (arc-close memory).
- **R5 generosity accountability spec (item-1581) Action 4 row.** Reference: `~/Projects/Open Alley/_archive/2026-06-10-round-7-r5-perplexity-computer-chatgpt-5-5-operationalization-npc-memory-architecture-arc.md`.
- **Modified-C-bis canonical citations** for HEXACO + active-inference references.

## Cross-links

- LINKS BACK TO: Post 99 (5-element discipline) + Post 100 (why Wiredu cannot be a trait slider — sets up "but what if you actually wanted to operationalize it") + Post 92 (Wiredu DROP self-correction with comprehensive context)
- LINKS FORWARD TO: Post 102 (intra-African dispute disclosure — communal accountability is contested within Akan philosophy) + Post 103 (WEIRD-defaults — communal accountability mechanic requires cultural-context tags)
- IMPLEMENTATION TIE: Round 9 Q4 EFE decomposition could integrate communal-accountability adjustment; conditional on operator Steam V1.0 scope decision

## Drafting prerequisites

- Wiredu Ch 9 + relevant Gyekye/Dzobo chapters primary-text read (~5-8h; cross-cultural-sequence prereq)
- Operator-side ledger schema sketch (~2-3h technical exercise)
- Marcus Reed Surface 8 implications for communal-accountability mechanic (~2-4h thinking)

## Hour estimate

At observed velocity: ~7-10 hours drafting + revision + 5-element discipline review + technical-spec verification. Target 3500-5000 words.
