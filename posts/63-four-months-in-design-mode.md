# I spent four months in design mode. Then I shipped 40 commits in a day.

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** Single-finding arc on the design-mode-to-code-mode transition for solo dev with cascading architectural decisions; n=1 transition

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

The standard indie-dev advice is to ship fast and iterate. Don't over-design. The code teaches you what the design should be. Get something playable and let the playtests drive the rest.

I spent four months ignoring that advice.

From late January through late May 2026, I built almost no game code. What I built instead was a design document. By the time the design document closed, it ran to roughly thirty-five thousand words of canonical architectural decisions across thirteen major sub-systems for the bowling-alley tycoon sim I'm shipping as Early Access on October 31, 2026. Then on the day after the design closed, I shipped 40 commits implementing the first major refactor it had been blocking. Zero broken-main commits across the day. Operator-side visual test between each commit. The longest single bug-fix iteration was three commits, which contained the bug to its own phase rather than letting it compound across other phases.

This post is about the transition. About what changes between design mode and code mode. About why for some projects the four-month design intensive is not the failure I was told to avoid; it's the precondition for the kind of code-mode execution that doesn't break.

## The indie-dev wisdom and what's true about it

The "ship fast, iterate" advice is correct for a wide class of projects. Specifically: projects whose architectural decisions are local (one feature at a time, no cascading invariants), or projects whose iteration cycle is cheap (small codebase, fast tests, easy rollback). For a simple Steam-deck-friendly puzzle game or a single-screen prototype that fits in your head, ship-fast wins because the cost of architectural rework is bounded and the cost of getting playtest signal is high.

The advice breaks down for projects whose architectural decisions cascade.

A bowling-alley tycoon sim has cascading decisions. How time ticks in the simulation affects how state serializes affects how citizens persist across save/load affects how the pricing sub-system reads its inputs affects how marketing inherits price elasticity from pricing affects how lane oil simulation reaches into pricing for capital-expenditure tiers and into environment entropy for degradation timing and into citizen reaction sensitivity for the deeper "every league bowler reacts differently" simulation layer.

Decide the time-tick spec wrong on day one and you eat the cascade cost across every downstream system every time you touch a downstream system. The cost compounds. Eight downstream systems each touching the wrong time-tick spec in different ways means eight separate places that need to be unwound when the spec turns out to need revision. Refactoring that out at month nine of development is more expensive than locking the spec at month one and having every downstream system inherit cleanly from the locked spec from the start.

The honest version of the wisdom is "ship fast where ship-fast works." The version most indie-dev posts deliver is the unqualified version: "ship fast, always; designing too much wastes time." That version is wrong for cascading-architecture projects, and the cost of believing it gets revealed at month nine when the refactor cost is what stops you from shipping at all.

## What design mode produces that ship-fast doesn't

Four months of design mode produced thirteen architectural-lock cycles. Each cycle was a structured deliberation session whose output was one locked answer to one architectural question. The output was a section of canonical design content, not source code. The deliberation involved multi-substrate AI cross-substrate triangulation: the same architectural question went to two to four different AI substrates in parallel, each with the same context, then I'd synthesize the responses, identify convergence and divergence, run an orchestrator pass that produced a resolution verdict on the divergent items, and ratify the items the substrates couldn't unilaterally resolve.

The pattern earned a name across the arc. Council-of-Four-architectural-deliberation-class methodology. Four perspectives in parallel, orchestrator synthesis, Madisonian-rule resolution on divergence (one substrate produces, another verifies; structural independence enforces honesty about disagreement rather than synthesis-as-compromise). The methodology is substrate-agnostic; the discipline lives in the orchestration layer, not in any specific AI tool.

What the cycles produced was not source code. It was decision locks. Each lock-body section captured: the decision itself, the reasoning chain that produced it, the inheritance topology to other locked decisions, the constraints it imposed on V1-critical-path work, and the explicit deferrals (what was excluded from V1 scope and parked for post-V1 follow-up). The lock-body sections accumulated into a single canonical artifact that the codebase would later inherit from.

Around the seventh cycle a structural pattern emerged that I hadn't planned for: the new lock-body sections composed on top of older lock-body sections without modifying them. Marketing locked on top of citizens locked on top of entropy locked on top of the early sketches. Lane oil locked on top of marketing on top of citizens on top of entropy. Each new lock-body owned the composition layer; the older sections stayed textually immutable. By the end of the arc the cross-Q-lock cascade composition-layer pattern was an empirically-validated architectural-design discipline, not a stylistic choice. The pattern matters because newer architectural decisions compose on top of older ones, which is the same pattern the source-code architecture will need to mirror at runtime.

The cycle work also surfaced trade-offs the substrates couldn't unilaterally resolve. Operator-judgment items showed up at every cycle: scope-creep risks, brand or commercialization implications, V1-vs-post-V1 deferral decisions, anything where my judgment was the load-bearing input. I'd ratify each item explicitly, then the cycle would close. The substrates were the deliberation layer; the ratification was mine.

None of this work produced shippable game code. All of it produced the architectural ground that shippable game code could later commit to without breaking.

## The code mode that opens after lock-in

Day after the design intensive closed, I shipped 40 commits implementing the first refactor.

The refactor took the codebase from rendering one interactive bowling lane to four simultaneous lanes (two with full physics including interactive bowlers, two with statistical resolution running at one-Hertz background simulation). Single shared physics world. Per-lane collision groups preventing cross-lane interaction. Per-lane state management. Statistical lane visual representation. Test scaffolding covering atomicity invariants on the per-lane state transition functions.

40 commits across the day. Each commit a discrete phase from the build-decomposition spec. Operator-side visual test between each phase. When the visual test caught a bug, bug-fix iteration before moving to the next phase. The most invasive bug was a three-system interaction between React JSX prop diffing, RigidBody position re-application, and Zustand subscribe semantics; it took three fixes to fully resolve, and each fix lived in its own commit because the phase-decomposition discipline contained the bug to its own phase rather than letting it compound across phases.

Zero broken-main commits across the day.

The execution worked because the architectural questions were already settled. Each commit could focus on its own scope without re-litigating an architectural decision that should have been settled. Time-tick spec was locked at cycle two; the multi-lane refactor inherited it cleanly. Persistence schema was locked at cycle four; the new per-lane state shape inherited the persistence inventory cleanly. The cross-lane collision-group decision was the only architecturally novel question the refactor itself surfaced, and it was a local question with no cascading implications because the broader physics-world decisions were already locked.

This is the part the "designing too much wastes time" advice misses. The cost of design mode is real. Four months is four months. Nothing visible to a player. Nothing shippable. Nothing demoable beyond what was already shippable before the intensive started. From the outside, four months of design mode looks like four months of nothing happening.

What was actually happening was the cascading-cost accounting that the codebase would otherwise have eaten during BUILD. The cycles paid the cascade cost in design time so the source code wouldn't have to pay it in implementation time. The 40-commit day on day one of BUILD execution caught the value: every commit landed cleanly because no commit was a surprise to any other commit, because every architectural decision had already been settled before any source-code commit committed to it.

## The honest emotional arc

The four months were hard.

Other indie devs were shipping. My demo build hadn't changed in weeks. Friends were asking when I'd have something playable. The Steam Wishlist target I'd committed to for October 31 felt simultaneously distant and impossibly close. Every week I spent in design mode was a week I wasn't getting playtest signal, wasn't building audience, wasn't accumulating the demos and screenshots and gifs that would eventually drive the Wishlist conversion.

The countervailing pressure was knowing that the code I'd ship without the design work wouldn't survive contact with the downstream sub-systems. I'd built enough cascading-architecture projects to know what the failure mode looked like: ship fast, get to month six, hit the wall where every change touches three sub-systems, slow to a crawl, abandon. The wall was the failure mode the design intensive was structured to avoid.

The single hardest moment was around cycle nine, three months in, when I had to extend the intensive past the original two-month estimate to handle the cycle eleven and twelve and thirteen sub-systems that the earlier cycles had surfaced as load-bearing. The extension felt like failure. It also turned out to be the cycles that produced the cross-Q-lock cascade composition-layer pattern, which made the whole cycle arc retroactively more valuable than the original two-month estimate had projected.

What the intensive cost was four months. What it bought was 40-commit BUILD execution with zero broken-main and operator-side bug catches between commits. The trade was worth it for this project. Whether it's worth it for any specific other project depends on whether that project's architectural decisions cascade.

## What I'm not claiming

- I'm not claiming pre-BUILD design discipline always beats ship-fast for every refactor scope. Some refactors don't need this overhead. Pre-BUILD lock-in pays compounding interest specifically when architectural decisions cascade across downstream systems. For projects without cascading decisions, ship-fast is the right discipline.

- I'm not claiming four months is a universal target. The cycle count was load-bearing; the calendar time was a byproduct. Different project complexity classes will produce different cycle counts. Mine produced thirteen because the sub-system count plus the cascading-dependency density required thirteen lock-bodies. Other projects would produce three, or twenty.

- I'm not claiming Council-of-Four-architectural-deliberation-class methodology is novel. The methodology is a directional pattern with prior art in multi-perspective-review systems (peer review, judicial panels, design crit). What's specific to the AI variant is the cross-substrate triangulation discipline and the structural-independence-enforces-honesty mechanism applied to divergence.

- I'm not claiming this pace is sustainable. Four months of intensive design work is not a maintainable cadence. It's an arc-close window with a specific shape: architectural-lock candidacy accumulation triggers an intensive, the intensive closes the accumulation, the next intensive opens months later when the candidacy backlog crosses threshold again. The 40-commit BUILD execution that followed is also not maintainable as a daily cadence; both are arc-shaped, not steady-state.

- I'm not claiming "design more" is the right advice for every indie dev who tells me their refactor isn't shipping. Sometimes their refactor isn't shipping because they're avoiding the hard work of writing the code, not because the architectural ground is unsettled. The diagnostic question is whether the refactor would compose cleanly on top of the existing architecture if the architecture were the right shape; if yes, the issue is execution discipline, not design discipline.

## What I am claiming

Four months of pre-BUILD architectural lock discipline produced 40-commit BUILD execution in one day with zero broken-main commits and operator-side bug catches between commits. The pre-BUILD investment compounded measurably at BUILD time. For projects whose architectural decisions cascade across downstream systems, this kind of pre-BUILD discipline pays the cascade cost up front and the BUILD execution catches the benefit.

The counter-narrative to ship-fast is not "always design first." The counter-narrative is "for projects with cascading architectural decisions, pre-BUILD lock-in pays compounding interest at BUILD time, and the right time to pay it is before any source-code commit locks in a wrong-shaped decision that will need to be unwound." The discipline is not a substitute for ship-fast where ship-fast works. It is the right discipline for the project class where ship-fast doesn't.

The transition itself was the part I wasn't prepared for. Four months of design mode is mostly invisible. The BUILD execution that opens after lock-in is mostly visible. The asymmetry produces a specific feeling: that the design-mode months were "nothing happening" and the BUILD-mode day was "everything happening at once," when in fact the BUILD-mode day was a direct readout of the design-mode months. Both modes were the same work. One looked like dev work to the outside; the other looked like staring at design documents. Both modes were what shipping a cascading-architecture project actually required.

I'm in code mode now. I get to write code. That alone makes the four months worth the trade.
