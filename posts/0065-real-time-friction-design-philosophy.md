<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0065
title: Real-time friction as design philosophy: when game cost is your actual attention
date_published: 2026-06-01
status: published
superseded_by: none
domain: tycoon design real-wall-clock time as cost vector for manual-task mechanics
project_scopes: pin-paradise
cc_task_relevance: tycoon-cost-vector-design, real-time-friction-mechanic, attention-as-currency
phase_binding: era-independent
discipline_family: none-applicable
canonical_rule: Manual maintenance and cleaning task mechanic uses real wall-clock time as cost so player attention is on the same ledger as in-game financial cost
load_bearing_claims:
  - Standard tycoon cost vectors are abstractions (money energy AP time-of-day)
  - Design breaks pattern by making task duration real wall-clock time not in-game time
  - Player trades real attention for in-game wage savings legibly at experience level
  - Bounded honest discussion of when the design would not work
applicability_triggers:
  - When designing tycoon cost vectors around player attention rather than abstractions
  - When mechanic exposes wall-clock friction to player as legible trade-off
  - When authoring game-design philosophy posts
mechanism_details:
  - Real-time task duration makes the cost ledger unified with player experience
  - Player can choose manual work (save wages, spend attention) or delegate (pay wages, save attention)
cross_refs:
  - Post 0056 (mechanic as new friction class)
  - Post 0068 (composition over modification architectural pattern)
-->

# Real-time friction as design philosophy: when game cost is your actual attention

**Author:** Jimmy McColery
**Date:** 2026-06-01
**Status:** Game-design philosophy post; one specific design choice with structural argument for why it works in the tycoon genre and bounded honest discussion of when it would not work

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The standard cost vectors in tycoon-genre games are abstractions: money, energy, action points, time-of-day, resource buckets that fill and drain at game-pace. The player makes decisions against the abstract costs; the game models the consequences; the loop repeats. The abstractions work because they are bounded (the cost is a number on a UI; the bound is legible; the decision space is tractable) and because they preserve the player's real-world experience as something distinct from the game's modeled experience.

This post is about a design choice that breaks the standard pattern in a specific way. The tycoon sim I'm building solo includes a mechanic where the player can choose to manually perform maintenance and cleaning tasks before or after the alley's operating hours, saving the staff wages those tasks would otherwise cost. The catch is that the manual tasks take real-world time. Taking out the trash takes ten minutes of real wall-clock time. Cleaning the bathrooms takes twenty minutes. Restocking the bar shelves takes fifteen minutes. The player's real attention budget is the cost vector; the game's modeled consequences flow from how the player chooses to spend that real attention.

This is unusual in tycoon-genre design. Most tycoon sims that include "player does tasks personally" mechanics treat the task duration as in-game time (the in-game clock advances; the player watches a progress bar; the player's real attention is preserved for the next decision). The design choice in this sim is to make the task duration real wall-clock time, which puts the player's actual attention on the same cost ledger as the in-game financial costs. The decision space changes structurally because the player is now trading real attention for in-game wage savings, and the trade-off is legible at the player's actual experience level rather than at the game's modeled level.

This post documents the design philosophy behind the choice, the structural argument for why it produces a specific kind of gameplay arc, and the bounded honest discussion of when this design would not work.

## The scrappy-owner arc

The structural arc the mechanic produces has a specific shape. New players entering the game's early stages with limited capital will choose to do maintenance tasks personally to save staff wages. The early-game financial pressure is real (the alley has to cover rent, equipment leases, utility costs; staff wages are a substantial line item; reducing staff hours by doing tasks personally moves the alley from net-negative to net-positive faster).

The early-game scrappy-owner mode produces a specific gameplay feel: the player is invested in the alley at the level of physical labor, not just at the level of capital and management decisions. The player who has spent forty minutes of real wall-clock time across an in-game day cleaning bathrooms and restocking shelves has a different relationship to the alley than the player who has spent the same in-game day clicking through resource-buffer decisions on the management UI. The physical-labor mode produces emotional buy-in that pure management UI does not.

The arc continues into mid-game. As the alley's financial position improves, the player's opportunity cost on the manual labor increases. The forty minutes spent cleaning bathrooms could instead be spent reviewing marketing decisions that produce larger revenue increases, or evaluating event-card decisions that affect customer-base composition, or planning capital expenditures that affect long-term operational capacity. The player gradually transitions from "I save money by doing this myself" to "I save money by hiring someone to do this and spending my attention on higher-value decisions."

The transition is the design's intentional output. The mechanic is not designed for players to do manual labor through the whole game; it is designed for players to feel the transition from scrappy-owner physical engagement to executive-level strategic engagement. The transition is what most tycoon games' standard cost-vector designs do not produce, because the standard cost vectors do not include the player's real attention as a cost.

By late-game, the player has a fully staffed alley operating without player intervention on routine tasks. The player's attention is on the executive layer: capital expansion decisions, brand-positioning choices, multi-alley scaling questions, the long-term strategic moves that define late-game tycoon decision space. The early-game manual-labor mode is now a memory; the alley operates without the player's physical engagement; the player's relationship to the alley has matured from physical to strategic.

This is the scrappy-owner-to-executive arc that the design is reaching for. The arc is one of the most satisfying gameplay patterns in tycoon-genre design when it works; the standard cost-vector designs do not produce it cleanly because the standard cost vectors do not put the player's real attention on the cost ledger.

## Why this works in the tycoon genre specifically

The tycoon genre has specific structural properties that make real-time friction work as a design choice. The properties do not generalize to all game genres; the design works here in a way it would not work in other genres.

The first property is the time-scale match. Tycoon games are typically played in extended sessions (one to three hours per session) with substantive operational arcs within each session. The session length is long enough to accommodate ten-minute or twenty-minute real-time tasks without those tasks consuming a disproportionate fraction of the play session. A ten-minute trash-takeout task is meaningful but bounded; the player can still complete substantive in-game progress within the same session.

The second property is the decision density. Tycoon games typically present many small decisions per minute during active play (which customer to serve next, which menu option to expand, which staff position to fill, which marketing channel to spend on). The decision density is high enough that a ten-minute pause for manual labor is felt as a deliberate reduction in decision intensity rather than as a forced stop. The pause is the design's intentional input; the player who chooses manual labor is choosing reduced decision intensity for that period.

The third property is the strategic-vs-operational distinction. Tycoon games make a clear distinction between strategic decisions (which products to offer, which markets to enter, which capital investments to make) and operational decisions (which customer to serve next, which menu option to expand). The manual-labor mechanic targets the operational layer specifically; the player who is doing trash takeout is reducing the operational layer's load on staff hours, not reducing strategic attention. The two layers remain distinct.

The fourth property is the emotional register. Tycoon games invite emotional investment in the simulated business. The player cares about the alley because the alley's success is the game's success metric; the alley's failure modes (insolvency, customer attrition, staff dissatisfaction) feel like personal failures to the player. The emotional investment makes the manual-labor mechanic resonate: the player who is physically engaged with the alley's operations feels the alley's success more viscerally than the player who manages it from an executive UI.

These four properties are tycoon-genre-specific. Action games have different time-scale dynamics (sessions are typically shorter and more intense; a ten-minute real-time task would consume the session). Strategy games have different decision-density dynamics (decisions are typically lower-frequency and higher-weight; a ten-minute pause would feel like a forced interruption). RPGs have different strategic-vs-operational distinctions (the operational layer is typically combat-driven rather than maintenance-driven; manual labor would not map cleanly to existing mechanics). The design choice works in tycoon-genre specifically because tycoon-genre structural properties align with the choice's structural requirements.

## The opportunity-cost realization

The mechanic's most distinctive moment is the opportunity-cost realization. The player has been doing manual labor through several in-game days. The early-game finances are now positive; the alley is running profitably. The player notices, mid-task, that the forty minutes spent cleaning could instead be spent on marketing decisions that would produce substantially larger revenue increases.

This is the moment the design is reaching for. The player has internalized the trade-off without the game prompting it. The trade-off is not "you should hire staff for these tasks" appearing as a tutorial popup; the trade-off is the player's own calculation of where their attention produces more value. The realization is structurally important because it produces the transition from scrappy-owner to executive mode at the player's own initiative.

The post-realization behavior is the design's intended output. The player hires staff for the routine tasks; the staff wages eat into the alley's profitability but free the player's attention; the player redirects attention to higher-value strategic decisions; the alley's financial performance improves because strategic attention compounds harder than manual-labor attention does at this stage of the game.

The realization is also the mechanism that resolves a structural risk in the design. If the player did not realize the opportunity cost, the player would continue doing manual labor indefinitely, the alley would be net-profitable but underperforming, and the player would be doing labor that staff would do for an affordable cost. The design depends on the player's realization to drive the transition; the realization depends on the player's actual attention being on the cost ledger. The cycle is self-reinforcing only if the real-time friction is genuinely felt; abstracting the friction away would break the cycle.

## When this design would not work

The design is genre-specific and player-specific. Several conditions need to hold for the mechanic to produce the intended arc rather than a frustrating experience.

The player's session length needs to support the real-time tasks. Players who can play in two-hour blocks can absorb ten-minute manual tasks without losing session momentum; players who can only play in fifteen-minute blocks cannot. The design penalizes short-session play patterns; players whose lives only support short sessions will find the mechanic frustrating rather than engaging.

The player needs to engage with the strategic-operational distinction the design relies on. Players who treat tycoon games as casual idle clickers will not engage with the opportunity-cost realization that the design depends on; they will continue doing manual labor because the labor is salient and the alternative strategic-attention moves are less salient. The design works best for players who are deliberately engaging with the strategic layer.

The player's emotional register needs to align with the design. Players who want pure escapism from real-world labor will find the real-time manual-labor mechanic actively unwelcome; the game is asking them to do labor in the leisure activity they came to the game to escape into. The design works for players who find the physical engagement with the alley emotionally meaningful; it fails for players who want pure abstraction.

The session length, strategic engagement, and emotional register conditions are not universal. The design will divide the player base into players who love the mechanic and players who dislike it. The dividing line is the player's own approach to the game; no amount of design tuning can convert players who want pure abstraction into players who want physical engagement. The design accepts the split.

The split is part of the design's intentional positioning. The bowling-alley tycoon sim is not designed to appeal to all tycoon-genre players; it is designed to appeal specifically to players who want the scrappy-owner-to-executive arc that real-time friction produces. The portion of the tycoon-genre player base who wants this arc is large enough to support the design's commercial target (the Early Access window opens October 31, 2026); the portion who wants pure abstraction will not be the target market for this specific game.

## What I'm not claiming

- I'm not claiming real-time friction is universally applicable to tycoon-genre design. The four structural properties documented above (time-scale match, decision density, strategic-vs-operational distinction, emotional register) need to hold for the mechanic to work. Tycoon sub-genres that violate any of those properties would not benefit from the mechanic.

- I'm not claiming the scrappy-owner-to-executive arc is the only good gameplay arc in tycoon-genre design. Many other arcs work; the standard cost-vector designs produce many of them. The real-time friction mechanic produces this specific arc cleanly; the design is for projects targeting this arc, not for projects targeting other arcs.

- I'm not claiming the design has been empirically validated through playtesting. The bowling-alley tycoon sim is in Early Access development; the mechanic's behavior under real player conditions is not yet measured. The structural argument is theoretical; the empirical validation will come during the Early Access window and may surface refinements to the design.

- I'm not claiming the design rejects accessibility considerations. Players whose health conditions, disability statuses, or life circumstances do not support the session-length and engagement-pattern conditions the design depends on are correctly served by accessibility options that abstract the real-time friction into in-game-time friction. The accessibility path is part of the design's planned implementation; the post focuses on the default-mode design philosophy.

- I'm not claiming this design pattern is novel. Real-time-cost design patterns appear in several other games (cookie-clicker variants where idle time produces resources; live-service games where session frequency matters more than session intensity; some classic management sims that included real-time-paced maintenance). What this post adds is the specific tycoon-genre application of real-time friction as a strategic-operational distinction driver and the scrappy-owner-to-executive arc framing as the intended gameplay output.

## What I am claiming

For tycoon-genre games whose structural properties match four specific conditions (extended-session play patterns; high decision density; clear strategic-vs-operational distinction; emotional register supporting physical engagement with the simulated business), making routine maintenance and cleaning tasks consume real wall-clock player time rather than abstract in-game time produces a specific gameplay arc that standard cost-vector designs do not produce.

The arc runs from scrappy-owner mode (early-game player chooses manual labor to save staff wages; physical engagement with the alley produces emotional buy-in) through opportunity-cost realization (mid-game player notices that manual-labor time could produce larger revenue increases if redirected to strategic decisions) to executive mode (late-game player has fully staffed alley operating without player intervention on routine tasks; player's attention is on strategic and capital decisions). The transition between modes is the design's intended output; the transition is what most standard cost-vector designs do not produce because they do not put player's real attention on the cost ledger.

The design is genre-specific and player-specific. Tycoon-genre structural properties make the mechanic work; other genres' structural properties would not support it. Players who want extended sessions with strategic engagement and physical-investment emotional register will find the mechanic produces the intended arc; players who want pure abstraction or short-session play will find the mechanic frustrating. The design accepts the split because the targeted player base is large enough to support the commercial position.

The empirical record this post stands on is the design philosophy for a bowling-alley tycoon sim in pre-launch development. The mechanic's behavior under real player conditions will be measured during the Early Access window opening October 31, 2026. The structural argument for why the mechanic should produce the intended arc is theoretical; the empirical validation is the work the Early Access window will do.

For game designers reading this who are considering similar mechanics in their own tycoon-genre projects: the design choice is high-leverage when the tycoon-genre structural properties hold and high-risk when they do not. The four-property check (session length; decision density; strategic-operational distinction; emotional register) is the diagnostic for whether the mechanic will work in any specific tycoon sub-genre. Designs that pass the check have access to a specific gameplay arc that standard cost-vector designs cannot easily produce; designs that fail any of the four properties should use abstract cost vectors and accept the standard gameplay arcs those produce.
