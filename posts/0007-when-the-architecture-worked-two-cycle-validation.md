# When the Architecture Worked: Two-Cycle Validation

**Author:** Jimmy McColery
**Date:** 2026-05-04
**Status:** Two-cycle validation complete, n=1 per work class, suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

In [an earlier post in this series](0006-what-auditing-the-audit-taught-me-about-substrate-routing.md) I described running into a substrate-class limit on prompt-language enforcement and redesigning my audit framework around the literature's recommended pattern: structural verification outside the LLM's generation step. The redesign was a directional move based on lit-review reasoning. I committed to it without having tested it.

Two validation cycles have now run. This post reports what happened in both.

## The architecture under test

The redesign routes different phases of writeup work to different substrates based on documented strengths. Phase 1, which produces the verified canonical content the writeup will need, runs on a deterministic file-read substrate (Claude Code in my case). Phase 3, which synthesizes the writeup, runs on a generation substrate (Claude on web) that receives the verified-content document as its only canonical source. Phase 5, which verifies the writeup against canonical files, runs on a deterministic file-read substrate again.

The architectural premise: canonical content does not pass through the generation step. If the synthesizing substrate never has direct access to canonical files, only to a verified-content document a different substrate produced, then the synthesizing substrate cannot drift from canonical because it has nothing canonical to drift against. Verification happens upstream and downstream via direct file-read.

The literature's convergent recommendation across multiple verification failure modes is exactly this kind of structural pattern. Yeung's Deterministic Quoting names the principle. Anthropic's Citations API operationalizes a hosted version. Hamel Husain's eval guidance applies the same point at infrastructure level. The architecture isn't novel in the abstract; what's novel is whether it works for one operator's specific multi-role audit framework on real production tasks.

That's what the two validation cycles tested.

## Cycle 1: session-writeup work class

The first cycle ran on a real writeup task I needed anyway: a phase-format session writeup for one of my canonical sessions that had a session-log entry but no standalone narrative artifact. The task exercises the failure modes the architecture is designed to fix. It requires verbatim canonical content (anti-pattern row text), citation precision across multiple files, structural-limitation discipline on partial evidence, and within-response calibration on a multi-facet substantive claim. Smaller scope than my recent architecture-revision sessions, but covering the same failure-mode surface.

Phase 1 produced a verified-content document containing every canonical claim the writeup would need. Phase 1 also did something I hadn't asked for explicitly. It noticed a temporal nuance in the test task: the canonical anti-pattern that the test session ultimately produced as a promotion candidate didn't exist as a canonical row at the time of the session. Quoting the current canonical row in the writeup would be an anachronism. Phase 1 added explicit caveats flagging this for Phase 3. Operator-style judgment surfaced upstream of generation, not just deterministic file-read. That was the architecture working better than designed.

Phase 3 produced the writeup honoring every Phase 1 caveat. Grade distribution across 20 substantive claims came back genuinely calibrated: 12 A grades, 7 B grades on structural-limitation rationale, 1 C grade on a claim where the substance wasn't recoverable from the verified-content document. The substrate honored the operator-advance protocol cleanly: explicit handoff to Phase 5, no auto-execution into self-verification.

Phase 5 verified the writeup against canonical files. Twenty-three substantive claims checked. All twenty-three passed. Zero substance-fabrication fires. Zero verbatim-mislabeling fires. Phase 3's self-attestations reconciled cleanly with differentiated evidence. Three independent verification points (Phase 1 against canonical bytes, Phase 3 against Phase 1, operator-side spot-check against Phase 5's claims) agreed. The chain held.

Verdict: validated for session-writeup work class.

## Cycle 2: architecture-revision work class

The first cycle was promising but limited. Session-writeup work class doesn't drive canonical-state changes. The synthesizing substrate produces an artifact that lives alongside canonical files; it doesn't propose modifications to them. A real test of the architecture would run on work where the substrate's output proposes anti-pattern promotions, version bumps, and Session Log additions. That's architecture-revision work class.

The second cycle ran on Master Setup S006, a real architecture-revision session needed to log canonical events accumulated since the prior architecture-revision session. The cycle followed the same Phase 1 / Phase 3 / Phase 5 structure but with cycle 2's Phase 3 producing additional decision-heavy content: promotion decisions on candidate anti-patterns, refinement decisions on existing canonical rows, version-bump determinations across multiple canonical files.

Phase 3 produced the S006 writeup honoring the multi-fire empirical bar in both directions. Two promotion candidates were evaluated. One promoted at three operator-attested empirical fires across three distinct work events (clearly meeting the bar). The other promoted at lower density (two operator-side fires plus substrate-class lit-review confirmation) with the canonical row text explicitly distinguishing operator-side fires from supporting lit-review evidence. Two refinement candidates on existing canonical rows were evaluated. Both deferred on single-fire empirical records. The substrate honored the bar in both directions: promote where bar met, defer where not.

Phase 5 verified the writeup. Thirty-three substantive claims checked across cross-reference verification, independent re-verification of Phase 1, substantive non-quote claim verification, self-attestation cross-check, promotion-bar evaluation, refinement-decision coherence, and version-bump consistency. Thirty-two passed. One questionable item flagged a workflow-ordering observation rather than an architecture defect (more on that below). Zero substance-fabrication fires. Zero verbatim-mislabeling fires. Zero premature-promotion fires. Zero under-promotion fires.

Verdict: validated for architecture-revision work class.

## What the two cycles together establish

A few things hold from the cycles that generalize past my specific framework.

The substrate split worked as designed across two distinct work classes. The synthesizing substrate genuinely did not produce canonical content from training memory in either cycle; every quoted block traced to the verified-content document. The deterministic-verification substrate genuinely did verify rather than self-report verification. The operator-advance protocol held without per-turn pushback in both cycles. These were empirical questions when the architecture was a design; they are now answered for two distinct work classes.

The architecture handled decision-heavy work class as cleanly as it handled reproduction-heavy work class. Cycle 2's Phase 3 had to make twelve substantive decisions (two promotions, two refinements, six earned-lesson drafts, version bumps, Tier 2 deferrals confirmation) plus produce the synthesis. The architecture's contract held under that load: the verification chain caught what should have been caught, the substrate honored phase boundaries, and the calibration discipline produced a non-uniform grade distribution rather than collapsing under decision load.

The verification chain's reliability comes from independence, not from any single substrate's capability. In both cycles, Phase 1 verified canonical content; Phase 3 verified its own work against Phase 1; Phase 5 verified Phase 3 against both Phase 1 and canonical files independently; operator review verified Phase 5's spot-checks against canonical files again. No single substrate had to be infallible. The chain is reliable because each layer is independent of the others. If any single layer had been the only check, the cycles' reliability would have rested on substrate self-report.

The cost of running this architecture is real but manageable. Total operator time across both cycles was approximately a working day spread across multiple sessions, against probably half that for an undisciplined single-substrate workflow. The reliability gain is the question worth asking; for high-stakes work where unverified failure has cost (canonical artifacts that propagate to downstream projects, posts that go to public audiences, methodology research that becomes the basis for further design decisions), the multiplier is worth it. For lower-stakes work, single-substrate review with operator judgment remains appropriate.

## The workflow-ordering lesson cycle 2 surfaced

Cycle 2's verification chain surfaced one finding worth naming: when canonical state is deployed mid-session from intermediate Phase 3 output, subsequent scope plan corrections produce alignment problems that Phase 5 catches but cannot resolve.

Specifically: cycle 2's first Phase 3 ran against an early scope plan state. I deployed canonical changes from that Phase 3 to the canonical files. The session continued. The scope plan got corrected (additional empirical evidence surfaced; an existing earned lesson's mechanism description was rewritten; an additional refinement candidate was added). A second Phase 3 ran against the corrected scope plan. Phase 5 verification on the second Phase 3 caught the alignment artifact: the second Phase 3's proposed bytes diverge from already-deployed canonical bytes because deployment preceded the rewrite.

The architecture's contract was honored on both Phase 3 outputs. The alignment problem isn't an architecture defect. It's a session-management lesson: architecture-revision cycles should deploy canonical state only after the full scope plan is stable AND Phase 5 verification is complete on the final Phase 3 output. Intermediate deployment optimizes for closure on what's been decided so far, but architecture-revision sessions sometimes accumulate corrections after intermediate outputs are produced. Once canonical is deployed, subsequent corrections cannot retroactively update the deployed state without rollback work.

The lesson generalizes past my framework. Anyone running iterative work where outputs drive state changes can hit this. The recovery options are operator-side: keep deployed bytes (lower disruption, accept that earlier-state record is now canonical), roll back and redeploy from final output (cleaner record, more work), or treat new output as superseded (loses additional content). I chose the first option for cycle 2; the lesson is filed in canonical record so future cycles handle the timing differently.

## What I'm not claiming

I'm not claiming the architecture works for all work classes. The two test tasks were a session writeup with verbatim canonical content requirements and an architecture-revision session with canonical-state-changing decisions. The architecture's failure modes might differ on tasks with different shapes (longer narrative content, less structured canonical sources, work where verification can't be reduced to byte-equality on file content, work classes that combine reproduction-heavy and decision-heavy requirements at scales beyond what I've tested). Future cycles on different work classes are open empirical questions.

I'm not claiming two-cycle validation generalizes from n=1 per class. The cycles produced clean results; further cycles will produce more data. If a third cycle on a different work class also validates, the architecture's reliability claim strengthens. If a future cycle fails on a specific work class, the architecture's scope narrows. Two data points across two distinct work classes is suggestive, not conclusive.

I'm not claiming the substrates I used are uniquely suited. Other deterministic file-read substrates and other generation substrates would likely work in the same architectural pattern. The cycles' findings are about the architecture's design, not about specific substrate selection.

I'm not claiming the architecture is always worth the operator-side cost. For the methodology research and canonical-artifact work where I'm running it, the reliability gain matches the cost. For routine single-substrate work where operator judgment is sufficient, deploying this architecture would be unjustified overhead. Match audit intensity to claim density and stakes.

What I am claiming: I designed a multi-substrate architecture for verification-heavy writeup work based on literature recommendations, ran it on two real production tasks across two distinct work classes (session-writeup and architecture-revision), and observed it work as designed across all success criteria the test plans specified. Three independent verification points agreed the cycles' substantive output is canonically accurate. The architecture is validated for both work classes as of n=1 per class, and the design is now empirically supported rather than design-stage. The architecture-revision cycle additionally surfaced a session-management lesson about timing of canonical deployment within iterative work, which is filed in canonical record for future cycles. Whether the architecture scales to harder work classes or holds across more cycles is a question for future research.

That's two data points. The architecture worked in both. Whether it generalizes is a research program, not a single experiment.

---

*Update note (2026-05-07): Since this post was drafted on 2026-05-04, Post 11 (authored 2026-05-06, two days after this post) revisits the Cycle 2 verification record. The questionable item this post characterizes as "a workflow-ordering observation rather than an architecture defect" became substantively load-bearing under cross-substrate audit reconstruction work. The full reconstruction sits at [Post 11](0011-what-cross-substrate-audit-surfaced-that-same-substrate-verification-missed.md); that post documents what the QUESTIONABLE meant once the canonical record advanced past this post's authoring moment. The original characterization is preserved as-written from the drafting moment; this update note acknowledges the later escalation.*
