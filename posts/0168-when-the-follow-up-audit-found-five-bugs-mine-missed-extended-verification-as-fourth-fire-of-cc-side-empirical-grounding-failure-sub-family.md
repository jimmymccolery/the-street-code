# When the Follow-up Audit Found Five Bugs Mine Missed: Extended Verification as Fourth Fire of CC-Side Empirical Grounding Failure Sub-Family

<!-- CC-OPTIMIZED-SUMMARY v1.0
post_id: 0168
domain: methodology-discipline
canonical_rule: extended-verification-third-layer-discipline
load_bearing_claims:
  - CC-side-empirical-grounding-failure sub-family fires at n=4 within-arc across 4 architecturally-distinct layers (sub-shapes 19+20+21+22 in 2026-07-05 arc)
  - Rule 20 candidacy Family A empirical foundation at n=16 candidate sub-shapes approaching canonization threshold at Council #8 methodology deployment scope
  - Framework methodology extension proposal: extended-verification as third-layer discipline below post-synthesis audit (Post 0163 BUILD-time) and post-audit-correction (Post 0167 post-publication)
  - Extended-verification mechanism: delegate follow-up directed scan to agent with scope-widening prompt that specifies a dimension distinct from initial audit's framing
  - Sub-shape 22 split into 2 catch layers with 3 initial rubric catches + 5 extended agent catches totaling 8 catches of same architectural family across Phase 1 baseline + Phase 2.6.C + Phase 2.10 + Phase 3.0-E
applicability_triggers:
  - When applying rigorous 6-dimension grading rubric audit to shipped code and initial audit surfaces an architectural-family bug (e.g. perspective-swap gap, cross-cutting propagation gap)
  - When shipping new state fields to a framework with perspective-swap architecture (Phase 2.9-C simBView) — must extend both simBView construction (read side) AND tickSimB return propagation (write side)
  - When 6-dimension rubric audit completes and scope was framed at latest phase only — consider follow-up agent scan widening to earlier phases for pre-existing instances of same architectural family
  - When authoring closure claims in framework code — mandatory to add regression test covering the specific direction claimed; test suite passing on existing tests insufficient
mechanism_details:
  - 6-dimension grading rubric weights: 30% factual accuracy + 20% Rule 19 anti-fabrication + 15% internal consistency + 10% framework alignment + 15% actionability + 10% scope discipline
  - Extended-verification prompt template: enumerate 4-8 specific mechanics from prior phases; for each ask "does this field appear in simBView construction? in tickSimB return propagation? if READ but not WRITTEN back, gap-YES"
  - CC-side-empirical-grounding-failure sub-family fire layers: attribution overclaim (methodology posts) + operational-cost framing (strategic recommendations) + code closure bug (single-mechanism semantic-inversion) + architectural-extension-awareness (perspective-swap framework)
  - Post-immutability preserved via addendum posts not in-place edits per Post 0167 discipline
cross_refs:
  - Post 0143 (parent canonization-propagation gap discipline family Family A)
  - Post 0163 (post-synthesis audit at BUILD-time scope; first layer of audit discipline stack)
  - Post 0166 (narrow-ship methodology; contains attribution overclaim corrected by Post 0167)
  - Post 0167 (post-audit-correction at post-publication scope; second layer of audit discipline stack)
  - Memory: feedback_cc_authored_perspective_swap_gap_for_phase_3_mechanical_layer_candidate_22nd_sub_shape_2026-07-05.md
  - Memory: feedback_cc_authored_code_bug_in_closure_claim_without_regression_test_candidate_21st_sub_shape_2026-07-05.md (parent shape for CC-side-empirical-grounding-failure sub-family)
  - Council #8 proposal: ~/Projects/the-street-code/methodology/post-audit-discipline-consolidated-proposal-for-council-8-2026-07-05.md
CC-OPTIMIZED-SUMMARY -->

**Author:** Jimmy McColery
**Date:** 2026-07-05
**Status:** DRAFT CANDIDATE pending operator review before shipping. Single-finding arc documenting a specific fourth-fire event of the framework's CC-side-empirical-grounding-failure sub-family (sub-shapes 19, 20, 21, 22 shipping within a single 2026-07-05 arc); extends candidate 22nd sub-shape of Post 0143 canonization-propagation gap discipline family Family A from initial n=1 fire to include five pre-existing gaps caught by a follow-up agent-driven audit that my initial 6-dimension rubric audit missed; empirical foundation for framework methodology extension proposing extended-verification as third-layer discipline below post-synthesis audit (Post 0163) and post-audit-correction (Post 0167)

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I'm a solo indie developer building a procedural-character architecture for a multi-decade tycoon simulation. The framework's Sim AI substrate ships shared across multiple products in the ecosystem. This post documents a specific empirical finding from a 2026-07-05 late-morning session: after I shipped a substantial Phase 3 personality progression arc (nine commits, seventy new tests) and then applied a rigorous 6-dimension grading rubric audit per Post 0163 precedent, my audit found three architectural bugs. I fixed them. Operator then asked me to consult the framework's spatial-topology reference and address any remaining loose ends. I delegated the loose-end check to an Explore agent. The agent found five more bugs my audit had missed. All five were pre-existing gaps from earlier phases (Phase 1 baseline, Phase 2.6.C, Phase 2.10) plus one gap in the phase I had just shipped (Phase 3.0-E).

The initial audit's three bugs plus the follow-up agent's five additional bugs total eight bugs caught in a single afternoon. All seven hundred fifty six tests were passing at the end of Phase 3 arc before the audit began. The pattern that made all eight bugs invisible to the test suite is a systematic coverage gap: zero tests validated propagation of Sim B's state through the framework's perspective-swap architecture. Every Phase 3 test set state.simB to null or tested state-level fields, not the perspective-swapped Sim B path.

This is not the first CC-side-empirical-grounding-failure event in the framework's tracking. It is the fourth within a single arc. Sub-shape 19 (attribution overclaim in Post 0166, corrected via Post 0167). Sub-shape 20 (operational-cost framing without empirical grounding). Sub-shape 21 (Phase 2.9-C step 2 sentiment key derivation bug caught by rigorous audit). Sub-shape 22 (this event, split into two catch layers). Four architecturally-distinct failure modes stacking within one day.

## The initial rigorous audit

Operator asked me to apply a rigorous 6-dimension grading rubric to Phase 3 work. The rubric is the same one canonized at Post 0163: thirty percent factual accuracy, twenty percent Rule 19 anti-fabrication discipline, fifteen percent internal consistency, ten percent framework methodology alignment, fifteen percent actionability and completeness, ten percent scope discipline. Total one hundred.

Applying it to Phase 3 shipped code, I graded each phase artifact and looked for issues. Phase 3.0-A caching mechanics: A (92). Phase 3.0-C planning: A (93). Phase 3.0-E fire: A- (88). Phase 3.1-A HEXACO: initially I graded B (82) because I noticed Sim B's HEXACO Openness scaling wasn't wired through the perspective-swap architecture. Digging into the code confirmed: simBView construction spreads state.hexaco (Sim A's) into the tick context that Sim B's decideNextAction and completeAction see. Sim B's own HEXACO fields lived on state.simB.hexaco but were never read during Sim B's tick.

Same pattern for Phase 3.1-B attachment. Same pattern for Phase 3.0-D skills. Bug #1.

I also noticed that tickSimB (the function that ticks Sim B via the perspective-swap shim) returned a state that only propagated certain fields. Sim B's skill accumulations from actions, water storage from store_water, food cache from cache_food, held wood from gather_wood: all dropped by the return statement. Bug #2.

Bug #3 was that HEXACO Emotionality stress drift and biographical longing mechanics I had shipped earlier in the arc lived inside tickSingleSim (Sim A's tick function). tickSimB doesn't call tickSingleSim; it constructs simBView and dispatches to decideNextAction, completeAction, or navigateTowardAction. Sim B never received her HEXACO Emotionality's chronic stress baseline effect. Sim B's absent bonds in her biography never triggered longing events.

I fixed all three. I extracted the stress drift and longing block into a helper function called from both Sim A and Sim B ticks. I added Sim B's Phase 3 field overrides to simBView with fallback semantics that preserve pre-Phase-3 test behavior. I added Sim B's mutable Phase 3 state propagation to the tickSimB return statement. I added five regression tests validating Sim B's behavior on the fixed paths. Test count moved from 756 to 761. Sub-shape 22 memory entry filed. Council #8 proposal document updated. Cross-consumer verify clean.

I thought the audit was complete.

## The follow-up loose-end check

Operator then said: consult the framework's spatial-topology reference file and all related surfaces to address any loose ends that have now surfaced.

The spatial-topology file at `~/.claude/cc_nav_payload.md` provides a Depth-0 authority for the framework's project structure and recent commits. Consulting it, I confirmed the audit fix commits landed, vendor sync landed, regen sync landed. I also confirmed the framework's tracking surfaces (SUMMARY.md at the-street-code, tasks.md at sim-ai, ROADMAP.md at RoomToLife) were current.

Beyond confirming state, I spawned an Explore agent with a specific directed prompt: audit the tickSimB return propagation across ALL previously-shipped phases and check whether the same perspective-swap gap I just fixed for Phase 3 fields existed for earlier phases. The prompt enumerated six specific mechanics to check: Phase 2.6.C water memory, Phase 2.8 pair-history and sentiment, Phase 2.8 aggression state, Phase 2.10 hasCaughtFish transfer during share_food, Phase 3.0-E fires (just shipped), and Phase 1 baseline hasShelter.

The agent returned five additional gaps I had missed in my initial audit.

**Gap 1: hasShelter, shelterPosition, worldGrid (Phase 1 baseline).** When Sim A builds shelter, tickSingleSim mutates state.hasShelter, state.shelterPosition, and state.worldGrid (adds the shelter cell). Propagation to next state works because tickSingleSim returns the mutated state directly. When Sim B builds shelter via the perspective-swap shim, completeAction mutates simBResult.hasShelter, simBResult.shelterPosition, and simBResult.worldGrid. But tickSimB's return statement spreads `...state` for these fields (reading original state) and never propagates simBResult's mutations back. Sim B build_shelter has been effectively LOST since the perspective-swap architecture at Phase 2.9-C step 1 landed.

**Gap 2: knownWaterSources (Phase 2.6.C water memory).** Same pattern. Sim B water memory discoveries via drink_from_stream navigation update simBResult.knownWaterSources. tickSimB return doesn't propagate. Sim B's water memory has been LOST since Phase 2.6.C water-infrastructure integration.

**Gap 3: Sim A needs from Sim B share_food (Phase 2.10 kindness).** The share_food action's completion code mutates next.simB.needs (recipient hunger reduction). In the perspective-swap architecture, when Sim B shares food with Sim A, next.simB in simBView case is the Sim A representation. So the recipient's needs mutation IS Sim A's hunger reduction. tickSimB return propagates state.simB.needs from simBResult.needs (Sim B's own decayed needs), but does NOT propagate Sim A's top-level needs from simBResult.simB.needs (Sim A representation's post-fed needs). Sim A's hunger reduction from Sim B's share_food has been LOST since Phase 2.10 kindness mechanics shipped this morning.

**Gap 4: fires array (Phase 3.0-E fire mechanic, just shipped).** When Sim B builds fire or tends fire via the perspective-swap shim, simBResult.fires contains the new or updated fires array. tickSimB return spreads `...state` and never propagates fires. Sim B build_fire and tend_fire have been LOST since I shipped Phase 3.0-E four hours before the audit event.

**Gap 5: worldGrid mutation from Sim B build_shelter (already partially covered by Gap 1 above).** The worldGrid mutation is a distinct field to propagate; without it, even if hasShelter and shelterPosition were somehow propagated, the physical cell would still show as the pre-shelter place type.

Combined discovery: five bugs across four phase generations, one of which was in the phase I had shipped just hours earlier.

## Why the initial audit missed these

The initial audit applied the 6-dimension grading rubric to Phase 3 artifacts specifically. Its scope was Phase 3 fields (hexaco, attachment, biography, skills, waterStorageLevel, foodCacheLevel, heldWood). I looked at the simBView construction and the tickSimB return and I saw the Phase 3 gap. I did not extend the same check to earlier phase fields because the audit prompt (my own) was scoped to Phase 3.

The follow-up agent-driven audit applied a directed prompt asking specifically: check whether the same gap exists for earlier phase mechanics. Different scoping. Different surfaces. Different findings.

This is architecturally significant. My initial audit's scope-discipline (which is one of the six rubric dimensions weighted at ten percent) was set to Phase 3 because Phase 3 was what I had shipped. Applying scope-discipline correctly under that framing produced a Phase-3-scoped audit. The framing was inadequate to the actual bug distribution because the bug family (perspective-swap-propagation gap) spans phase generations, not one phase.

The Explore agent's directed prompt widened the scope to phase-generations-spanning. Under the widened scope, the same 6-dimension rubric would have caught the earlier gaps, but I would have needed to know to widen the scope. The gap in my initial audit was scope framing, not rubric application.

## Why 756 tests all passed anyway

The test suite grew from 686 to 756 during the Phase 3 arc. Every new test targeted Sim A behavior (via top-level state fields) or state-level fields (fires, worldGrid, pair). Zero tests targeted Sim B behavior via the perspective-swap shim.

The perspective-swap architecture is an implicit contract that no test enforces. There is no test named "verify all state fields propagate symmetrically through perspective-swap" because no such test exists. Individual mechanics get individual tests. The contract that says "when a new state field is added, both Sim A and Sim B must be able to accumulate it and propagate it" is not represented in the test suite.

This is a well-known class of bug in software with mirrored code paths. The gap between "each path individually works" and "both paths respect the same architectural contract" is a coverage gap that only architecture-aware tests can catch. Individual mechanic tests do not catch it.

The framework's test coverage systematic gap is now surfaced empirically. Every subsequent framework phase should include at least one Sim B behavior test for any new state field. Better: a lint or check that scans simBView and tickSimB return for coverage of every state field.

## The framework methodology observation

The CC-side-empirical-grounding-failure sub-family within Post 0143 canonization-propagation gap discipline family Family A now fires at n=4 within-arc across four architecturally-distinct layers:

- Sub-shape 19: attribution overclaim in published methodology post (Post 0166, interpretation-of-empirical-data layer)
- Sub-shape 20: operational-cost framing without empirical grounding (strategic-recommendation layer)
- Sub-shape 21: code bug in closure claim without regression test coverage (single-mechanism semantic-inversion layer)
- Sub-shape 22: perspective-swap-symmetric-propagation gap (architectural-extension-awareness layer with initial n=1 catch by my rubric audit plus n=5 extended catches by follow-up agent audit)

Four fires in one arc across four distinct layers. This is beyond the framework's usual multi-fire canonization threshold of three fires across distinct work classes. The sub-family may warrant its own canonization as a distinct rule at Council #8 methodology deployment scope, separate from Rule 20 candidacy Family A's broader canonization-propagation gap discipline.

The specific methodology discipline extension this fire proposes: **extended-verification as third-layer discipline**. The framework's canonized discipline stack currently has post-synthesis audit (Post 0163) at BUILD-time scope, catching artifact-consistency errors before ship. Post 0167 documented post-audit-correction discipline at post-publication scope, catching factual errors after ship. Extended-verification would sit below both: catching what the audit missed by widening scope via directed follow-up.

The specific mechanism: after applying the 6-dimension rubric, delegate a follow-up check to an agent with a directed prompt that widens scope beyond what the original audit framed. The follow-up prompt should be specific enough to catch what the original audit did not see. Generic "check for anything else" prompts do not work; the follow-up must specify a widened dimension (in this event, phase-generation-spanning rather than phase-3-scoped).

The failure mode this discipline extension addresses: my initial audit scoped correctly to Phase 3 but missed pre-existing gaps. The correction is not a better rubric. The correction is a broader follow-up scope after the initial rubric completes.

## What I'm not claiming

I'm not claiming the Explore-agent audit is architecturally superior to my rubric audit. Both apply the same underlying discipline (scan the code, check for gaps). The agent audit happened to have a wider scope. My rubric audit could have had the same wide scope if I had framed the prompt differently. The lesson is scope-framing, not agent-vs-human.

I'm not claiming every audit needs a follow-up agent scan. That would be process theater. What I am claiming is that when the audit surfaces architectural-family bugs (Bug #1 was already an architectural family, perspective-swap-propagation), a follow-up scan widened to earlier phases is a low-cost check for pre-existing instances of the same family.

I'm not claiming the five pre-existing bugs were undetectable before this event. Any of the five could have been caught if a test had validated Sim B's build_shelter, or if the operator had run a two-Sim seed=42 empirical session where Sim B was in position to build shelter first. The bugs were undetected because the specific test coverage and the specific empirical scenarios that would have surfaced them were never run.

I'm not claiming Rule 20 candidacy Family A is ready for canonization at n=16 candidate sub-shapes. Canonization is a Council methodology deployment adjudication. Sixteen sub-shapes is empirically strong but Council #8 must adjudicate whether the pattern generalizes across framework-methodology work or whether it stays within its current scope.

I'm not claiming the CC-side-empirical-grounding-failure sub-family will canonize as a distinct rule separate from Rule 20 Family A. The framework's adjudication of whether these should unify under one umbrella or split into separate rules is a Council-methodology-deployment matter beyond this post's scope.

I'm not claiming the extended-verification discipline extension applies to every post-audit session. It applies when the initial audit surfaces architectural-family bugs. When the initial audit surfaces isolated mechanic-level bugs, the extended-verification overhead may not pay for itself.

## What I am claiming

The 2026-07-05 late-morning audit event fired four architecturally-distinct instances of the framework's CC-side-empirical-grounding-failure pattern within a single arc: attribution overclaim, operational-cost framing, code closure bug, and perspective-swap-symmetric-propagation gap. Four fires in one arc across four distinct failure layers.

The perspective-swap-symmetric-propagation gap (sub-shape 22) split into two catch layers: initial rubric audit caught three Phase 3 fields; follow-up agent-driven audit caught five additional pre-existing fields from Phase 1 baseline through Phase 3.0-E just-shipped. Combined test count moved from 756 to 764 after both fix layers landed with regression tests locking in the fix contracts.

The proposed framework methodology extension: extended-verification as third-layer discipline below post-synthesis audit (Post 0163) and post-audit-correction (Post 0167). Mechanism: after the initial rubric audit completes, delegate a follow-up directed scan to an agent with a scope-widening prompt. The scope-widening prompt must specify a dimension distinct from the initial audit's framing.

Post 0143 Family A empirical foundation now sits at n=16 candidate sub-shapes across framework scope levels and mechanisms. CC-side-empirical-grounding-failure sub-family fires at n=4 within-arc across four architecturally-distinct layers, approaching canonization threshold as a candidate distinct rule at Council #8 methodology deployment scope.
