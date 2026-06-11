# 13 architectural-lock cycles in 7 days: the Phase 6.0 design arc closes

**Author:** Jimmy McColery
**Date:** 2026-05-27
**Status:** Multi-session arc retrospective from a 7-day pre-BUILD design intensive; n=1, descriptive not prescriptive on the broader methodology claim

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Between May 20 and May 27, I closed 13 architectural-lock cycles for a bowling-alley tycoon sim I've been building solo. Each cycle resolved one major V1 design question that had been blocking BUILD-stage work. The cycles ran across three working sessions, produced thirteen lock-body sections at the design document, and consumed roughly seven full days of focused operator time.

Then on the eighth day I shipped Phase 6.1 BUILD execution. Multi-lane refactor. Single shared Rapier physics world, per-lane collision groups, four active lanes rendering simultaneously, full test scaffolding. 40 commits across the day. Zero broken-main commits. Operator-side visual test cycle between each phase, bug-fix iteration when the visual test caught something, then the next phase.

The thirteen cycles and the forty commits are the same story. The seven days of pre-BUILD architectural lock-in are what made the 40-commit BUILD day possible. This post is the retrospective on the cycle arc. A companion post will cover the BUILD day. Both are framed around a counterintuitive claim that I want to put on the table early: pre-BUILD architectural lock-in discipline is the opposite of "ship fast" indie-dev advice, and that's why it works.

## What an architectural-lock cycle is

An architectural-lock cycle is a structured deliberation session whose only output is a locked answer to one architectural question that the codebase needs answered before BUILD-stage work can proceed. The output is a section of canonical design content in `tycoon-design.md` (the project's design canonical artifact), not source code. The deliberation involves multi-substrate AI cross-substrate triangulation: I run the same architectural question past two to four different AI systems in parallel, each receiving the same context, then synthesize the responses, identify cross-substrate convergence and divergence, run an orchestrator pass that produces a Madisonian-rule resolution verdict on the divergent items, and ratify operator-judgment items the substrates couldn't resolve. The lock-body section that emerges captures the decision, the reasoning, the inheritance topology to other architectural decisions, and the V1-critical-path implications.

The pattern has evolved over the project. Early cycles ran with two substrates. Recent cycles have stabilized at four substrates in parallel. The four-substrate pattern earned a name: Council-of-Four-architectural-deliberation-class methodology. Council-of-Four is a directional name for a structural pattern (four perspectives, orchestrator synthesis, Madisonian-rule resolution on divergence) rather than a specific tool wiring. Different operators could fire the same pattern with different substrate selections; the methodology lives in the discipline layer, not in any specific substrate's continued availability.

## The thirteen cycles

Here's the ledger. One sentence per cycle.

**Q1 (May 21):** Soul-axis set lock. Four input axes for the tycoon sim: Operations, Community, Vibe/Nostalgia, Authenticity. The axis set was the foundation everything downstream had to inherit.

**Q2 (May 21):** Time-tick spec under Option B. How time advances in the sim, what triggers tick events, how player actions interleave with simulation passes.

**Q3 (May 21):** Multi-alley state architecture. The persistence-requirements list (what must serialize across save/load) and the message-bus event-type list. Q3 owns the requirements; Q9 owns the serialization format.

**Q9 (May 21):** Save schema design v1. Serialization format specifics including schema versioning (monotonic-integer convention, not SemVer), save format portability, and the worker-thread streaming serialization mandate.

**Q14 (May 22):** Environment Entropy. How Operations, Community, and Vibe/Nostalgia decay in absence of player input. Authenticity does not decay; it's a state-of-being binary per the Q2 ratification. Q14 closed before Q11 because Q14's environment-decay baseline became the ground state Q11 (citizens) had to build against.

**Q11 (May 22):** Town-as-Sim / Persistent Citizens. The citizen capsule schema, social-edges table, archived-citizens field, per-citizen deviation vector layered on pool-baseline. Q11 also surfaced the split that produced Q18 as a follow-up architectural-lock candidate.

**Q18 (May 25):** Character-generation pipeline architecture. The split from Q11 per operator-judgment item ratification. Consumes Q11's citizen capsule schema as ground state. Q18 closed with three-of-three substrate axis-level convergence on ten architectural decisions and substantive enhancement divergences on three axes.

**Q7 (May 25):** Asset authoring approach. All environment, lane, and equipment 3D assets across the project. Q7 registered at Q14 close as Medium scope per a Finding 6 ratification. The lock body excluded animation library architecture, which deferred to a future Q-candidate.

**Q12 (May 25):** Pricing sub-system. The first cycle in the arc that achieved full three-of-three option-level convergence across all eleven axes. Substantive refinement folds applied at seven axes; eight substrate-surfaced new tensions integrated. Q12 also restored full Council-of-Three cross-substrate triangulation after the prior Q7 cycle ran degraded.

**Q13 (May 26):** Marketing sub-system. Inherited the Phase 6.1 playtest-calibration V1-critical-path gate from Q12, Q11, and Q14. Q13 was the cycle where §20 cross-Q-lock cascade composition-layer pattern first emerged at n=1. The new lock-body section composes on top of older lock-body sections without modifying them.

**Q17 (May 26):** Lane oil pattern simulation. V1-required. The Q17 lock body produced §21 cross-Q-lock composition layer at n=2 cumulative empirical fire. Lane oil simulation reaches into Q12 (pricing for oil-machine CapEx tier), Q14 (oil pattern degrades over time as environmental entropy sub-stat), and Q11 (per-citizen ball reaction sensitivity).

**Q5 (May 26):** Architectural correctness. The cycle that produced §22 composition layer at n=3 cumulative. Q5 also locked the Q5 §22.10 bidirectional gameplay test gate: a falsifiable shipping gate where the V1 must allow both bankruptcy-via-operational-neglect AND profitable-equilibrium-via-active-management paths. Both directions playable; if only one direction is reachable, the V1 isn't shippable.

**Q19 (May 27):** Card-layer integration. The cycle that produced §23 composition layer at n=4 cumulative empirical fire. Q19 closed the meta-mechanic / card-layer architectural surface that composes on top of every prior Q-lock without invalidating any of them.

## How the cycles ran

Each cycle followed the same shape. I'd draft an audit prompt that loaded the architectural question, the relevant existing canonical content, and the deliberation surface. The prompt would go to two to four AI substrates in parallel, each in its own session with its own attached files. Substrates returned audit reports with verdicts (clean, adjust, iteration-N required) and substantive findings.

I'd run a first-pass synthesis to identify the convergence and divergence across substrate responses. Convergence points became candidate locks. Divergence points needed Madisonian-rule resolution: when substrates disagree, the divergence itself is the signal that the question hasn't actually been resolved, and an orchestrator pass has to either reconcile the disagreement (sometimes by adopting a hybrid that neither substrate proposed) or apply a Madisonian-rule decision rule (separation-of-powers analog: one substrate produces, another verifies; structural independence enforces honesty about disagreement rather than synthesis-as-compromise).

The orchestrator pass produced a resolution verdict. The verdict went back to me for operator-judgment items that needed human ratification: trade-offs the substrates surfaced but couldn't unilaterally decide, scope-creep risks, brand or commercialization implications, anything where my judgment was the load-bearing input. I'd ratify each item explicitly, then the cycle would close with a lock-body section written into `tycoon-design.md` plus updates to companion canonical artifacts (the ROADMAP entry, message-bus event lists, persistence inventory, V1-critical-path register).

The cycle shape stayed constant across the seven days. What varied was the depth. Q1, Q2, Q3, Q9 (the first four cycles, all closed on day one) ran two-substrate. Most of the middle cycles ran three-substrate. The late cycles (Q5, Q19) ran four-substrate with full Council-of-Four-architectural-deliberation-class methodology. The methodology earned its name across the arc; the early cycles were the warm-up that produced the empirical evidence that more substrates surfaced more catches.

## The cross-Q-lock cascade composition-layer pattern

Around Q13 a structural pattern emerged that I hadn't planned for. The §20 lock-body section (Q13 marketing sub-system) had to compose on top of §16 (Q11 citizens), §15 (Q14 entropy), and §14 (the Sessions 1 sketches). The composition didn't invalidate any prior lock-body section. The newer lock-body owned the composition layer; the older lock-body sections stayed textually immutable.

§21 (Q17 lane oil) hit the same pattern at n=2 cumulative. §22 (Q5 architectural correctness) at n=3. §23 (Q19 card-layer integration) at n=4. By the end of the arc the cross-Q-lock cascade composition-layer pattern was an empirically-validated architectural-design pattern, not a stylistic choice. Newer architectural decisions compose on top of older ones; older lock-body content stays immutable; composition discipline lives in the newer lock-body.

The pattern matters for two reasons. First, it lets the design document grow without rewriting earlier sections, which means earlier locks stay as canonical reference rather than getting silently superseded. Second, it makes the architectural decisions composable in a way that the source-code architecture will need to mirror. The Q19 card-layer integration §23 lock specifies that meta-mechanic effects (card-layer mechanics that modify how the sim behaves) compose on top of base-game mechanics without invalidating them, which is the same pattern at the runtime layer that the lock-body sections instantiated at the design-document layer.

## Why pre-BUILD lock-in beats ship-fast for invasive architecture

The standard indie-dev advice is to ship fast and iterate. Don't over-design; design as you go; the code teaches you what the design should be. The advice is correct for a wide class of projects, especially projects whose architectural decisions are local (one feature at a time, no cascading invariants) or projects whose iteration cycle is cheap (small codebase, fast test suite, easy rollback).

The advice breaks down for projects whose architectural decisions cascade. A bowling-alley tycoon sim has cascading decisions: how time ticks affects how state serializes affects how citizens persist affects how pricing works affects how marketing inherits from pricing affects how lane oil simulation reaches into pricing and environment entropy and citizen reaction sensitivity. Decide time ticks wrong on day one and you eat the cascade cost across every downstream system every time you change a downstream system.

Pre-BUILD architectural lock-in is the way to pay the cascade cost up front, before any source code commits to a decision that will need to be undone. The seven days of cycle work locked the cascades. The 40-commit BUILD day on day eight was possible because none of the BUILD commits were eating a cascade-cost surprise. Each commit could focus on its own scope without re-litigating an architectural decision that should have been settled.

The counter-narrative is not "always design first" or "always avoid ship-fast." The counter-narrative is "for projects with cascading architectural decisions, pre-BUILD lock-in pays compounding interest at BUILD time, and the right time to pay it is before any source-code commit locks in a wrong-shaped decision that will need to be unwound."

## The payoff

Day eight was Phase 6.1 BUILD execution. The refactor took the codebase from rendering one interactive bowling lane to four simultaneous lanes (two with full Rapier physics including interactive bowlers, two with statistical resolution running at one-Hertz background simulation). Single shared Rapier physics world. Per-lane collision groups preventing cross-lane ball/pin interaction. Per-lane RigidBody management. Statistical lane visual representation. Vitest test scaffolding covering atomicity invariants on the per-lane state transition functions.

40 commits across the day. Each commit a discrete phase from the BUILD-decomposition spec. Operator-side visual test between each phase. When the visual test caught a bug, bug-fix iteration before moving to the next phase. The most invasive bug was a three-system interaction between React JSX prop diffing, Rapier RigidBody position re-application, and Zustand subscribe semantics; it took three fixes to fully resolve, and each fix lived in its own commit because the phase-decomposition discipline contained the bug to its own phase rather than letting it compound across phases.

Zero broken-main commits across the BUILD arc. The BUILD execution worked because the architectural questions were already settled. I'll cover the BUILD day in a companion post; this one is about the seven days that preceded it.

## Personal reflection

I'm a solo developer. My quality-over-speed preference is canonized as a user memory at this point because I stated it explicitly enough that it shaped subsequent collaboration. The seven-day intensive arc is not sustainable as an ongoing pace; it's an arc-close window with a specific shape (architectural-lock candidacy accumulation triggers a session, the session closes the accumulation, and the next arc opens). I close arcs when the candidacy backlog crosses a threshold that signals BUILD-stage work would otherwise eat cascading cost.

The multi-substrate AI orchestration is the load-bearing input that lets a solo developer run cycles at this depth. Council-of-Four-architectural-deliberation-class methodology is what makes pre-BUILD design discipline a viable solo-dev practice. The methodology doesn't depend on which specific AI substrates are running which specific phase; the discipline layer is substrate-agnostic. Different operators could fire the same pattern with different substrate selections.

I'm not claiming this pace is healthy. I'm not claiming pre-BUILD lock-in always beats ship-fast. I'm not claiming Council-of-Four-architectural-deliberation-class methodology is novel. What I'm claiming is concrete: seven days of pre-BUILD architectural lock discipline produced 40-commit BUILD execution in one day with zero broken-main commits and operator-side bug catches between commits. The pre-BUILD investment compounded measurably at BUILD time, and the compounding was the point.

## What's next

Phase 6.2 is the next architectural cycle. The candidacy backlog includes worker-thread streaming serialization (the Q9 V1-critical-path implication), a perf-test sandbox for the Q5 §22 lane oil computational budget gate, and Float32 BVH macro-precision empirical validation at the cross-bank distances that the multi-lane physics world now needs to handle. The 5-month V1 Early Access target sits at October 31, 2026. The architectural-lock arc that just closed was the work that the EA target compounds against.

## What I'm not claiming

- I'm not claiming 13 cycles in 7 days is sustainable or healthy as an ongoing pace. This was an intensive arc-close window with a specific trigger (candidacy accumulation crossing a threshold) and a specific end state (the accumulation closed; the next arc opens later).
- I'm not claiming pre-BUILD design discipline always beats ship-fast for every refactor scope. Some refactors don't need this overhead. Pre-BUILD lock-in pays compounding interest specifically when architectural decisions cascade across downstream systems.
- I'm not claiming Council-of-Four-architectural-deliberation-class methodology is novel. The methodology is a directional pattern with prior art in multi-perspective-review systems (peer review, judicial panels, design crit). What's specific to the AI variant is the cross-substrate triangulation discipline and the Madisonian-rule resolution applied to divergence.
- I'm not claiming all 13 cycles produced equal-quality locks. Some Q-cycles were lighter than others; some required iteration-3 cycles to converge; the cumulative arc was the value, not any single cycle taken in isolation.
- I'm not claiming solo dev plus AI collaboration is faster than a senior-engineer team for this kind of pre-BUILD design discipline. This isn't a comparative study. It's a description of what one solo developer with multi-substrate AI orchestration produced over seven days.

## What I am claiming

7 days of intensive pre-BUILD architectural lock discipline produced 40-commit Phase 6.1 BUILD execution in one day with zero broken-main commits plus operator-side bug catches between commits. The pre-BUILD investment compounded measurably at BUILD time. For projects whose architectural decisions cascade across downstream systems, this kind of pre-BUILD discipline pays the cascade cost up front and the BUILD execution catches the benefit.

The counter-narrative is not "always design first" or "always avoid ship-fast." The counter-narrative is "for projects with cascading architectural decisions, pre-BUILD lock-in pays compounding interest at BUILD time, and the right time to pay it is before any source-code commit locks in a wrong-shaped decision that will need to be unwound." The discipline is not a substitute for ship-fast where ship-fast works; it is the right discipline for the project class where ship-fast doesn't.

The empirical record this post stands on is one 7-day arc closing one 13-cycle Phase 6.0 design intensive, producing one 40-commit Phase 6.1 BUILD day. n=1 on the arc. The pattern's broader generalization is the standing question; whether other operators running other project classes under similar pre-BUILD discipline produce similar BUILD-time compounding is the empirical extension I'd want to see.
