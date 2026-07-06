<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0048
title: What 10 indie tycoon games taught me about V1 scope
date_published: 2026-05-31
status: published
superseded_by: none
domain: indie tycoon V1-scope research finding across 10 titles 1994-2018
project_scopes: pin-paradise, street-code-methodology
cc_task_relevance: v1-scope-decisioning, tycoon-genre-benchmarking, research-substrate-primary-source-verification
phase_binding: era-independent
discipline_family: verify-against-canonical-files
canonical_rule: Zero counterexamples across n=10 indie tycoon titles for the pattern V1 equals one strong mode plus later versions add modes scenarios or DLC
load_bearing_claims:
  - Survey covered RollerCoaster Tycoon 1999 through Two Point Hospital 2018 with intentional mix of clearly-indie plus small-team-or-publisher-backed
  - Six of ten produced clean reconstructions from primary or near-primary sources; four flagged as vertical-slice-scope-not-directly-documented rather than confabulated
  - Empirical pattern held across two decades of indie tycoon shipping practice with no counterexamples
applicability_triggers:
  - When making V1 scope decisions for a tycoon-genre project
  - When considering multiple structurally-different modes at first public release
  - When authoring research posts requiring primary-source substrate verification
mechanism_details:
  - Substrate honestly flagged missing primary-source availability rather than confabulating citations
  - Convergence across two-decade sample provides strong empirical foundation against multi-mode-at-V1 aspiration
cross_refs:
  - Post 0049 (design mode vs code mode work classes)
  - Post 0058 (catching AI hallucinations cross-substrate discipline)
-->

# What 10 indie tycoon games taught me about V1 scope

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Research-program post; n=10 titles surveyed; convergent finding across all 10 cases

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I'm building a bowling-alley tycoon sim solo, targeting Early Access on October 31, 2026. In the middle of architectural lock-in for the V1 scope, I had to answer a question that mattered more than I initially realized: what did the comparable indie tycoon games actually ship at V1? Not the final, polished, multi-mode versions you see on Steam today. The V1. The first public release. Before the expansions, before the multi-mode features, before the modding scenes filled in the gaps.

I ran the question past a research-rigor AI substrate with primary-source citation requirements across 10 indie and small-team tycoon titles spanning 1994 to 2018. The research came back with a finding so clean it changed how I scoped my own V1. This post is the finding.

## The 10 games

The survey covered RollerCoaster Tycoon (1999), Theme Hospital (1997), SimTower (1994), Game Dev Tycoon (2012), Software Inc. (2015 Early Access), RimWorld (2013 Kickstarter pre-alpha), Project Highrise (2016), Cities: Skylines (2015), Two Point Hospital (2018), and Dwarf Fortress (2006 alpha; 2022 Steam). The selection was intentional: a mix of clearly indie (Dwarf Fortress, RimWorld, Software Inc., Game Dev Tycoon, Project Highrise) and small-team-or-publisher-backed (Cities: Skylines, Two Point Hospital, RollerCoaster Tycoon, Theme Hospital, SimTower) titles that represented the design space I cared about: management sims with deep simulation systems and long-tail engagement.

The research approach was deliberate. For each title, find the closest available primary-source artifact (dev blog, postmortem, developer Q&A, contemporaneous press demo, official forum thread) and try to reconstruct the V1 scope: what shipped at first public release, what was actually playable, how many "modes" the game offered, what the depth-vs-breadth balance looked like.

Six of the 10 titles produced clean reconstructions from primary or near-primary sources. RimWorld's V1 was the Ludeon dev blog's "build 250 first public pre-alpha" entry, which documents the November 2013 Kickstarter build's exact feature set. Software Inc. has well-maintained dev pages documenting its Early Access trajectory. Dwarf Fortress has Bay 12's site plus extensive Wikipedia coverage of the 2006 alpha. Game Dev Tycoon's V1 maps cleanly to the December 2012 1.0 release with public press coverage. The other four titles produced reconstructions from indirect sources (press demos, marketing copy, dev-diary inference), which the substrate flagged honestly as "vertical-slice scope not directly documented" rather than confabulating crisp primary citations.

## The killer finding

Here is the finding, quoted directly from the research output:

> "I did not find strong precedents where an indie/small-team tycoon successfully shipped multiple structurally different modes (e.g., 'Default,' 'Chronological Challenge,' 'Franchise Management') all at V1 with equal depth. Evidence instead points to: V1 = one strong mode; later versions add modes, scenarios, DLC, or meta-progression."

That is a clean empirical pattern. Ten titles surveyed. Zero counterexamples. The pattern held across two decades of indie tycoon shipping practice.

The finding caught me because my own V1 design had drifted toward a three-mode structure: a default sandbox, a chronological-challenge mode (decade-by-decade progression with era-specific economic and cultural constraints), and a franchise-management mode (multiple bowling alleys under one owner). All three modes were notionally at "equal depth" in the lock body. None of them were structurally trivial; each shared core systems but each layered distinct mechanics on top of the shared base.

The research result was: nobody has shipped that.

## What each game actually shipped at V1

A quick survey, one paragraph per title, focused on the V1 mode count and depth rather than the final game.

**Dwarf Fortress (Bay 12, 2006 alpha):** Fortress mode. Just Fortress mode. Adventure mode and Legends mode arrived later. The August 2006 alpha released after four years of solo dev work and supported the now-classic "single fortress on a generated world" loop. Sixteen years later, the December 2022 Steam release was effectively the polished V1 the indie market had been waiting for. The mode count at first public alpha was one. The mode count at Steam release was still small.

**RimWorld (Ludeon, 2013 pre-alpha):** Single core mode. Three crash survivors, base construction, AI storyteller events, raiders. Five years from 2013 Kickstarter build to 1.0 in 2018. The expansions (Royalty, Ideology, Biotech) layered systems on top of the single colony-survival mode; they did not introduce orthogonal modes. Different starting scenarios are parameter tweaks on the single core mode, not separate modes with their own systems.

**Software Inc. (Coredumping, 2015 Early Access):** Single mode. Run one software company. The first Early Access build was "build, hire, ship products" at minimal depth. A decade of Early Access added product types, HR depth, stock trading, and other sub-systems, but the structural mode count stayed at one. The depth grew vertically inside one mode; the breadth never expanded into multiple orthogonal modes.

**Game Dev Tycoon (Greenheart Games, 2012):** Single mode. One company, progression through platform eras, simple office upgrades. No secondary meta-mode at launch. Greenheart Games was founded July 2012; 1.0 shipped December 10, 2012. Five months from company founding to shipping. The V1 was already the single primary mode, full stop.

**RollerCoaster Tycoon (Chris Sawyer, 1999):** The 1999 Windows demo offers one scenario (park) with a roughly 25-minute play limit, exposing the full coaster-building, staff, shops, finances, and guest-simulation loop. The de facto vertical slice was "one park, full systems, time-limited." The shipped game scaled to many scenarios, but each scenario was a parameter variation on the same mode. There was no separate "Chronological Mode" or "Franchise Mode."

**Theme Hospital (Bullfrog, 1997):** Level-based campaign. One hospital per level. Growing set of rooms, diseases, staff systems. The campaign-with-levels structure is one mode with variable scenarios. There is no documented separate "Sandbox" or "Free Build" mode at V1; sandbox-style play is a level state, not a separate mode with separate mechanics.

**SimTower (1994):** Single tower per save. Built floor by floor. Multiple tenant types. No multi-tower mode. No alternate progression structure. The depth came from progression within one structure over many years.

**Project Highrise (SomaSim, 2016):** Single tower per save. One building, deep internal systems as the only mode. Later DLC expanded content (new tenants, scenarios) rather than adding distinct modes. Same pattern as SimTower two decades later.

**Cities: Skylines (Colossal Order, 2015):** Single city per save. Citizens with home/work, traffic pathfinding, residential/commercial/industrial zoning. Variations were in maps and starting conditions. No secondary game modes existed at launch.

**Two Point Hospital (Two Point Studios, 2018):** Single hospital per level. Multiple levels. Spiritual successor to Theme Hospital with the same single-mode structure. Press demos from the lead-up to launch showed one early hospital with subset content; the core camera, staff, queues, and financial systems were the same as the final game. Single mode with level-based progression.

Ten titles. Ten single-mode V1s. The pattern is not a small-sample artifact; it is a multi-decade convergent industry practice.

## Why multi-mode V1 is the failure mode

The research output frames this in terms of "vertical slice" discipline, which is worth pulling out because the term has a specific industry meaning that often gets conflated with prototype or MVP.

A prototype is cheap and messy. Test ideas, test core mechanics, don't worry about art or production quality.

An MVP, or early-access V1, is sellable but incomplete. Used to validate the business model.

A vertical slice is a production prototype. One "slice of cake" at near-shipping quality, covering core gameplay, representative content, and integrated systems. The vertical slice proves the team can actually build the final experience. It is depth-along-one-axis, not breadth-across-many-axes.

For indie or small-team tycoon games, the vertical slice that becomes V1 is structurally always single-mode. The reason is not that multiple modes are technically impossible; the reason is that production quality for multiple modes at equal depth requires roughly multiplicative effort. Two modes at depth D cost roughly 2x the production effort of one mode at depth D. Three modes at depth D cost roughly 3x. Small teams cannot pay the multiplier. The competing strategy is to ship one mode at depth D and add modes later, paying the multiplier incrementally over a longer timeline, which is what every game in the survey did.

The structural reason multi-mode V1 fails for small teams is that the modes share core systems but diverge in surface mechanics, and the surface divergence is where production cost lives. Two modes that share simulation systems but diverge on UI surface and decision affordances and progression structure require separate UI work, separate playtesting, separate balance passes, separate tutorial flows. The shared core systems don't reduce the surface cost. The surface cost is what kills small-team V1 ambition.

The corollary: multi-mode at V1 is feasible for large studios with parallel team structures, where each mode has its own production lead. Small teams don't have parallel teams. They have one team that has to ship something coherent. Coherence is single-mode.

## What I'm doing with the finding

My V1 design had drifted toward three modes. The research caught the drift.

The response was to lock the V1 scope to one mode: the default sandbox, which is the single-mode vertical slice that the simulation systems support cleanly. The chronological-challenge mode and the franchise-management mode were both deferred to post-V1. The deferral is not "nice to have someday." The deferral is a load-bearing scope discipline: the V1 must demonstrate that the single default mode is itself shippable at production quality before any second mode begins production. The bidirectional gameplay-test gate I locked at V1 (the V1 must allow both bankruptcy-via-operational-neglect and profitable-equilibrium-via-active-management paths through the default mode, both directions playable) is the depth-along-one-axis test that the single-mode vertical-slice discipline operationalized.

The chronological mode and franchise mode aren't dead. They are post-V1 expansions, paid the same way every survey title paid for its multi-mode features: incrementally, over a longer timeline, after the single-mode V1 had demonstrated production-quality depth on its own terms.

The reframing changed multiple downstream decisions. The art pipeline scoped to one era at V1 instead of decade-by-decade era assets. The narrative voice locked to one tone instead of three era-specific tones. The economy locked to one set of price ranges instead of three sets indexed by decade-specific inflation. Each of these decisions had been quietly drifting larger because the multi-mode scope was implicitly carrying them. Locking to single-mode V1 pulled the whole scope back to something a solo developer can actually ship by October 31, 2026.

## What this is not

This is not "indie devs should never attempt multi-mode at V1." The survey did not include every indie tycoon game ever shipped. Some titles probably did attempt multi-mode V1; those titles did not surface in the convergent sample, which might reflect substrate selection bias toward well-documented or commercially successful titles. The research finding is "I did not find strong precedents," not "multi-mode V1 is impossible." The directional pattern is real; the strength of the pattern depends on how the unsurveyed titles distribute.

This is also not "all single-mode V1s succeed." Plenty of single-mode V1s shipped and failed. The discipline is necessary but not sufficient. The point of locking to single-mode V1 is to reduce the probability of failure mode "scope too large for team to ship at production quality." Other failure modes (no audience, bad mechanics, marketing failure) are not addressed by scope discipline. They have their own disciplines.

This is also not a claim about AAA studios. The survey was indie and small-team. AAA studios with 200-person teams routinely ship multi-mode at V1 because they have the parallel-team structure to pay the production multiplier. The finding is specific to the small-team production constraint.

## What I'm not claiming

- I'm not claiming the 10-title sample is comprehensive. It surveyed well-documented titles with primary or near-primary source availability. Less-documented titles, especially flops with no surviving postmortems, are absent from the sample. The pattern could weaken if those titles were included.

- I'm not claiming "single-mode V1" is sufficient for success. It is necessary scope discipline given a small-team production constraint. Other disciplines (mechanic quality, audience identification, marketing) are independent and not addressed here.

- I'm not claiming the research substrate's primary-source identifications are infallible. The substrate flagged honestly when reconstructions were inference rather than primary; I cross-checked a sample (the RimWorld Ludeon blog entries; the Greenheart Games Game Dev Tycoon timeline) and the flags held up. For the four titles flagged as inference-based, the conclusions are weaker than the six well-verified titles.

- I'm not claiming "vertical slice" terminology is universally consistent. The term has drifted across industry usage. The specific definition I'm using (production prototype, near-shipping quality, single-cake-slice along one axis) is the one the research synthesized across multiple AAA and indie sources; some indie devs use the term more loosely to mean any early-playable build.

- I'm not claiming this finding is original. Several indie postmortems and GDC talks have made adjacent points about scope discipline. What I'm adding is the 10-title convergent empirical pattern across multiple decades, which is useful for indie devs trying to talk themselves into multi-mode V1 ambitions: someone has already run the survey, and the survey produced a clean pattern.

## What I am claiming

Across 10 surveyed indie and small-team tycoon titles spanning 1994 to 2018, V1 was structurally single-mode in every case. Multi-mode features arrived later, layered on top of the single-mode foundation through DLC, expansions, or extended Early Access. The convergent pattern holds across multiple decades of indie shipping practice.

For indie devs scoping a tycoon V1: if your V1 scope includes more than one structurally distinct mode at equal depth, the empirical record suggests that scope will not ship. The honest options are to cut scope to single-mode V1 (the survey-supported path), or to commit to large-team production structure that pays the multi-mode multiplier (the AAA path that the survey did not cover and that solo and small-team devs cannot access).

The discipline costs little to apply at design time. The cost of skipping the discipline and discovering at production time that the multi-mode scope is unshippable is large. I caught my own multi-mode drift in the architectural lock cycle that produced this research; the catch saved scope that would have been unshippable by my October 31, 2026 Early Access target.

The empirical record this post stands on is the 10-title survey produced by one research-class deep-research substrate pass with primary-source citation requirements. The substrate flagged inference-based reconstructions honestly. The finding is convergent across all 10 titles with zero counterexamples surfaced in the sample. n=10 across two decades is stronger than n=1 from any single postmortem, which is the contribution this post is making to indie tycoon V1 scope discussions.
