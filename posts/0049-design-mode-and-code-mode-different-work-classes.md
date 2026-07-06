<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0049
title: Design mode and code mode are different work classes
date_published: 2026-05-31
status: published
superseded_by: none
domain: solo AI-assisted indie dev work-class taxonomy design-mode vs code-mode
project_scopes: street-code-methodology, pin-paradise
cc_task_relevance: architectural-lock-cycle-methodology, build-phase-transition, solo-dev-workflow-design
phase_binding: era-independent
discipline_family: none-applicable
canonical_rule: Design mode and code mode are not phases of the same work; they are structurally different work classes with their own transitions
load_bearing_claims:
  - 13 architectural-lock cycles closed against 13 V1 design questions between May 20 and May 27 2026
  - First BUILD day shipped 40 commits with zero broken-main commits after lock arc closed
  - Cross-Q-lock composition-layer pattern emerged unplanned across cycles preserving textual immutability of prior locks
applicability_triggers:
  - When transitioning from architectural-design phase to BUILD execution phase
  - When accounting for cognitive costs of switching between work classes on solo indie projects
  - When designing methodology posts on solo AI-assisted dev workflow
mechanism_details:
  - Composition discipline held across arc so no prior lock body needed modification
  - Design mode and code mode differ in cognitive shape, feedback loops, and validation criteria
cross_refs:
  - Post 0041 (methodology arc on architectural-lock cycles)
  - Post 0068 (composition over modification architectural pattern)
-->

# Design mode and code mode are different work classes

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Single-finding arc on the structural distinction between two work classes for solo AI-assisted indie dev; n=1 transition closing one architectural-lock arc to one BUILD-execution day

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I've been running AI-assisted indie dev work for about four weeks across multiple projects (the earliest repo timestamp in my project tree is May 4, 2026; the bowling-alley tycoon sim I'm building solo as Early Access for October 31, 2026 started its repo on May 20). Within that four-week window, a specific seven-day arc consumed almost all of my focused attention: thirteen architectural-lock cycles closed against thirteen V1 design questions for the tycoon sim, run between May 20 and May 27. On May 28 the lock arc closed and the BUILD execution opened. The first BUILD day shipped 40 commits with zero broken-main commits across the day.

Post 41 covered the methodology arc: what an architectural-lock cycle is, how the cycles ran, why pre-BUILD design pays compound interest at BUILD time, the cross-Q-lock cascade composition-layer pattern that emerged. That post made the methodology argument. This post is about a different observation that surfaced as the cycles closed and the BUILD opened: design mode and code mode are not phases of the same work. They are different work classes. The transition between them has its own shape.

This post is the reflection on that distinction.

## The moment cycle 13 closed

Cycle 13 closed on May 27 with the Q19 card-layer integration architecture lock body landed at the design document. The lock body was the fourth section in a cross-Q-lock composition layer that had emerged unplanned across the preceding three cycles. Each new lock body in the composition layer integrated cleanly against the prior locks without modifying them. By the end of cycle 13, the design document held thirteen lock bodies, each owning one architectural question, none of them at risk of mutual contradiction because the composition discipline had held across the arc.

What happened immediately after was strange. Closing a deliberation cycle is normally a small thing: write up the verdict, ratify the operator-judgment items, commit the markdown update, move on. Closing the thirteenth cycle in a seven-day stack felt different. The design document was textually complete. The next move was BUILD. I closed my laptop briefly and went outside.

The next day was forty commits. The BUILD execution that the seven days of design-mode work had been settling against. Each commit landed cleanly because no commit was eating a cascade-cost surprise. Each commit could focus on its own scope without re-litigating an architectural decision that should have been settled. Zero broken-main commits across the day. Operator-side visual test between each commit. When a bug surfaced, the bug-fix iteration committed independently rather than compounding across commits.

The transition between the two days is what I want to put on the table.

## Two work classes, not two phases of one class

The framing I'd been carrying into the arc was that design and code are phases of the same work. You design first, then you code. Each phase produces an artifact that feeds the next. The artifact handoff is what connects them.

That framing was wrong, or at least incomplete. Design mode and code mode are different work classes. The framing matters because the work involved in each is structurally different, and a solo dev who treats them as the same kind of work (with different surface details) ends up using the wrong tools and the wrong attention pattern for one of them.

Design mode produces decisions. The output isn't a document; the document is a record of the output. The actual output is a settled answer to a structural question about the system. The question takes hours of sustained attention to surface, more hours of deliberation to interrogate, and a final ratification step where the answer either commits to canonical state or doesn't. The hourly velocity is low. The decision density per hour is what matters.

Code mode produces commits. The output is source-code changes that move the running system from one state to another. Each commit either compiles and passes its tests or it doesn't. The feedback loop is immediate: write the change, run the test, observe the result. The decision density per hour is much higher than design mode because each commit is a small decision that resolves immediately, not a large decision that takes hours to interrogate.

Both modes are full work. Neither is preparation for the other. Calling design mode "preparation" demotes it; calling code mode "execution" demotes it. Both modes have their own success criteria. Design mode's success criterion is whether the decision holds under downstream pressure. Code mode's success criterion is whether the commit lands without breaking main. The two criteria measure different things and require different work shapes to achieve.

## What design mode actually is

The seven-day arc that produced the thirteen architectural locks was design mode at its most concentrated. The work shape across the seven days had a specific structure.

Each cycle began with framing the architectural question precisely. Not "how should we do citizens"; rather, "what is the canonical schema for per-citizen state given that downstream marketing wants per-citizen elasticity vectors and downstream simulation wants per-citizen deviation from pool baseline, and what is the persistence shape that lets both downstream surfaces inherit without modification." The framing took anywhere from twenty minutes to two hours depending on how much architectural surface the question touched.

Each cycle then deployed the question through a multi-substrate AI orchestration: two to four substrates in parallel, each receiving the same context, each producing an audit-class response. The orchestration consumed roughly two to six hours of operator attention across receipt, synthesis, cross-substrate convergence-and-divergence analysis, orchestrator-pass resolution, and operator-judgment ratification of items the substrates couldn't unilaterally resolve.

The lock body that emerged was a record of the cycle's output. The deliverable wasn't the markdown text. The deliverable was the decision encoded in the text. The text was the persistence layer for the decision; the decision was the actual thing produced.

Across seven days, thirteen cycles closed. Each cycle's lock body composed with the others. Some cycles ran two-substrate (the earlier cycles when the methodology was warming up). Some ran three-substrate. The late cycles ran four-substrate with full Council-of-Four-architectural-deliberation-class orchestration. The substrate count varied with the cycle's architectural surface; the deliberation discipline was constant.

What design mode is, structurally, is sustained attention applied to architectural questions through multi-substrate deliberation, with each cycle producing a decision encoded in canonical state. The visible artifacts are markdown files. The actual work is decision production.

## What code mode actually is

The 40-commit BUILD day on May 28 was code mode at its most concentrated. The work shape was structurally different from design mode.

Each commit was a discrete phase from a build-decomposition spec that I'd written before the BUILD day opened. The spec partitioned the multi-lane refactor into ordered phases, each with a specific scope (rename per-lane state fields, add new per-lane state shape, wire up the new pinsetter type discriminant, et cetera). Each phase committed independently with its own tests. The spec's ordering was load-bearing: a phase that committed out of order would break main because downstream phases depended on upstream phases' output.

Each commit produced immediate visible feedback. Run the dev server, click through the lane interactions, watch the visual test catch what the type checker didn't. When the visual test caught a bug, the next commit was the bug fix. The bug-fix commit didn't compound into the next phase because the phase-decomposition discipline contained each bug to its own commit boundary.

The hourly decision velocity was higher than design mode by an order of magnitude. Each commit was a small decision (this is the change for this phase) that resolved against the test loop in minutes. Each architectural surface decision (the load-bearing kind) was already settled because design mode had settled it. Code mode wasn't deliberating; it was executing.

Forty commits across a day is not exceptional output per se. What was unusual was that the forty commits landed against a settled architectural ground, so the execution discipline held without internal re-litigation. The cost of getting that ground settled was the seven days of design mode. The benefit was the day of code mode execution that didn't have to absorb design-mode work as it went.

## The visibility asymmetry

Design mode is mostly invisible to anyone outside the operator's head. Across seven days the visible artifacts were thirteen markdown sections in a design document, plus some commits to a research-queue file, plus orchestrator-pass synthesis files. None of those artifacts is a thing a user can interact with. None of them visibly moves the project toward shipping. Someone watching from outside, seeing only the commits, sees seven days of "design document grew" interspersed with no user-visible product change.

Code mode is loudly visible. Each commit is a visible change. The BUILD day produces forty commits, an updated demo, screenshots that look different from yesterday, gifs that show new behavior. Someone watching from outside sees the BUILD day as the day "the work happened."

The asymmetry is structural, not perceptual. Design mode genuinely produces less visible output per unit of operator attention than code mode does. The visible-output rate is not what design mode optimizes for. Design mode optimizes for the decision density per cycle. Visible output is downstream of that, in the BUILD execution that the design mode enables.

A solo dev who tries to maintain visible-output momentum across design mode breaks the discipline. The visible-output rate during design mode is supposed to be low. Forcing it up means cutting corners on the decisions that design mode is producing, which means BUILD mode then has to absorb the unsettled decisions and the visible-output rate during BUILD goes down as the BUILD work eats the cascade-cost surprise that design mode should have absorbed.

The asymmetry has implications for how solo devs explain their work to themselves and to others. "What did you do this week" answers differently in each mode. In design mode the answer is "I locked four architectural questions that the next BUILD arc compounds against." In code mode the answer is "I shipped a multi-lane refactor." Both answers describe work. The work classes are different.

## The transition itself

The moment between cycle 13 closing and commit 1 of the BUILD landing was its own thing. Not a smooth gradient. A discrete transition.

What made the transition land was that the design document was already textually complete and the build-decomposition spec was already drafted. Closing the design arc didn't require any additional design work; the spec for the next mode was ready to consume. Opening the BUILD arc didn't require any additional design retrieval; the canonical document was ready to inherit from.

What could have made the transition fail was either of two things. First, opening BUILD before the design was actually settled would have meant BUILD commits absorbing design work, which would have broken the work-class separation. Second, closing design without the BUILD-decomposition spec ready would have meant a discontinuity between modes where neither the prior nor the next work shape was available; the solo dev sits in the middle with no productive work to do.

The discipline that connected the two modes was the build-decomposition spec. The spec lived at the boundary between modes. It was drafted late in the design arc, partially as a forcing function to verify the design was actually settled enough to produce a decomposition. If the spec couldn't be cleanly written, the design wasn't done; the cycle wasn't closeable. The spec became the falsification test for the design arc's completeness.

The transition succeeded because the artifacts at the boundary were ready when the boundary arrived. Design mode produced the canonical document plus the build-decomposition spec. Code mode opened against the spec. The interface between modes was the spec. Without it, the transition would have produced the gap between modes that solo devs sometimes describe as "I finished planning but I don't know what to do next."

## How solo plus AI changes the work shape

A solo dev without AI orchestration can run code mode at full effectiveness. The compiler, the test loop, the visual test, the version control system, and the deploy pipeline are all the infrastructure code mode needs. None of that infrastructure depends on AI.

A solo dev without AI orchestration cannot run design mode at the depth this arc ran it. Multi-substrate deliberation requires multiple substrates running in parallel against the same architectural question with independent reasoning paths. Solo deliberation produces the same kind of output a single substrate produces: one perspective, one reasoning chain, one set of blind spots. The multi-substrate triangulation that catches divergence and forces resolution is what the substrates collectively enable that a solo dev alone cannot.

This means AI orchestration is load-bearing for design mode in a way it isn't for code mode. Different solo devs reach different conclusions about how much AI assistance to use in code mode. The variance is real and the trade-offs are real. Design mode at this depth doesn't admit the same variance: without multi-substrate deliberation, the cycles run shallower, and the cascade-cost surprises that design mode is supposed to absorb get pushed into BUILD where they cost much more.

The work shape that produced the seven-day arc plus the 40-commit BUILD day is a specific solo-plus-AI configuration. It is not a substitute for a team. It is not a substitute for solo dev without AI. It is a third thing: a work shape that has different production characteristics from either of the comparison points. The seven-day arc is what design mode looks like under this configuration. The BUILD day is what code mode looks like under this configuration. Both modes are full work, neither is preparation for the other, and the transition between them is its own discrete operation.

## What I'm not claiming

- I'm not claiming the design-mode / code-mode distinction is novel. The framing has analogs in classical software engineering (design phase versus implementation phase), in writing practice (planning versus drafting), and in many craft disciplines. What's specific to this post is the framing as different work classes (not phases) with different attention shapes and different success criteria, observed in solo AI-assisted indie dev specifically.

- I'm not claiming all solo dev should run a seven-day design intensive before any BUILD work. The intensive shape suited a specific project class (the bowling-alley tycoon sim's cascading-architecture decisions). Different project classes don't need this shape. Simple-architecture projects ship faster under ship-fast discipline.

- I'm not claiming AI orchestration is the only path to design-mode depth. Teams of engineers running design review can produce comparable depth through different mechanisms. The post's framing is specific to solo dev with AI orchestration, not a universal claim about how design mode has to run.

- I'm not claiming the transition itself is hard to navigate. For this specific arc, the build-decomposition spec at the boundary made the transition land cleanly. Other transitions could be harder if the boundary artifacts are not ready. The post's claim isn't that the transition is always smooth; it's that the transition is a discrete operation with its own shape.

- I'm not claiming the seven-day intensive is sustainable as ongoing cadence. It was an arc-close window with a specific shape (architectural-lock candidacy accumulation triggers an intensive, the intensive closes the accumulation, the next intensive opens later when the candidacy backlog crosses threshold again). The 40-commit BUILD execution that followed is also not maintainable as steady-state. Both modes are arc-shaped.

## What I am claiming

Design mode and code mode are different work classes, not phases of the same work. Design mode produces decisions encoded in canonical state; code mode produces commits against settled architectural ground. The hourly velocity differs by an order of magnitude. The success criteria differ. The visibility profiles differ. Treating them as the same work with different surface details breaks the discipline of both.

The transition between modes is a discrete operation, not a smooth gradient. The artifacts that live at the boundary (a complete canonical document, a ready build-decomposition spec) are what make the transition land cleanly. Without those boundary artifacts, the transition produces the gap that solo devs sometimes describe as "I finished planning but I don't know what to do next."

Solo dev with AI orchestration enables a specific work shape where design mode runs at multi-substrate-deliberation depth and code mode runs at conventional execution velocity. The configuration is not a substitute for a team and not a substitute for solo dev without AI; it's a third thing with its own production characteristics. The seven-day architectural-lock arc this post draws from is one empirical anchor for what this work shape produces; whether other operators running other project classes under similar configurations produce similar arcs is the empirical extension worth watching.

The first four weeks of my AI-assisted indie dev work produced one full Council-class architectural-lock arc plus the BUILD execution that compounded against it. The seven-day intensive plus the 40-commit BUILD day plus the transition between them are what I'm describing here. Whether the work classes named in this post survive further reproduction across other project arcs, and whether the transition-as-discrete-operation framing holds, are the load-bearing extensions of this post's empirical claim.
