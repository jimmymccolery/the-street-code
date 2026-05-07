# When Deployment Outpaces Decisions: A Mid-Iteration Alignment Problem

**Author:** Jimmy McColery
**Date:** 2026-05-04
**Status:** Empirical lesson from one cycle, generalization to anyone running iterative work

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I ran an architecture-revision session this week that surfaced a session-management problem I hadn't seen named before. The problem isn't deep, but it has consequences, and it generalizes past my specific framework to anyone running iterative work where outputs drive state changes. Worth naming explicitly.

Here's the shape of it.

## The setup

I run an architecture-revision cycle in three phases. Phase 1 produces a verified-content document containing every canonical claim the cycle's writeup will need. Phase 3 synthesizes the writeup, making decisions about anti-pattern promotions, refinement evaluations, and version bumps. Phase 5 verifies Phase 3's output against canonical files independently.

The cycle's contract: Phase 3 produces proposed bytes for canonical changes. Phase 5 verifies those proposed bytes against scope plan and Phase 1 ground truth. If Phase 5 passes, an operator-side step deploys the proposed bytes to canonical files (anti-pattern rows, session log entries, earned lessons).

This sequence works cleanly when the scope plan is stable before Phase 3 runs. The architecture's failure mode prevention assumes Phase 3 has settled inputs.

## What actually happened

In the cycle I ran this week, I deployed canonical state from an intermediate Phase 3 output. The Phase 3 was real work, produced against the scope plan as it existed at that moment. I deployed the changes (anti-pattern rows added, version bumped, session log row written, earned lessons appended to the lessons file). Cycle felt like it had reached closure.

Then the session continued. The scope plan got corrected: two new earned lessons surfaced and were added; an existing earned lesson's mechanism description was rewritten as I noticed I had attributed the failure to the wrong cause; an additional refinement candidate was added. By the time the scope plan stabilized, it had three substantive changes from the version Phase 3 had run against.

I produced a second Phase 3 output, this time against the corrected scope plan. The second output reflected the additional changes: more earned lessons, more refinement decisions, slightly different reasoning chains.

Phase 5 verification ran on the second output. It passed all the architectural tests cleanly. Zero substance-fabrication fires, zero verbatim-mislabeling fires, clean self-attestation.

But Phase 5 also caught something else: the second Phase 3's proposed bytes diverge from the canonical bytes I had already deployed earlier in the session. Because deployment had happened from the first Phase 3, the canonical state reflected an earlier version of the work than the rewritten Phase 3 was now proposing.

The architecture's contract was honored on both Phase 3 outputs. Each output was internally consistent with the scope plan it ran against. The alignment problem isn't an architecture defect. It's a session-management lesson.

## The mechanism

Mid-session canonical deployment optimizes for closure on what's been decided so far. When you've finished work that feels complete, deploying it to canonical state feels like the right next move. The work moves from "in progress" to "done."

But iterative sessions sometimes accumulate corrections after intermediate outputs are produced. A scope plan you thought was stable turns out to need a correction. A lesson you thought was finalized gets rewritten when you notice an attribution error. An additional candidate surfaces that wasn't in the scope plan when Phase 3 ran.

Once canonical is deployed from intermediate output, subsequent corrections cannot retroactively update the deployed state without rollback work. The deployed canonical record reflects an earlier-state version of the work. Phase 5 verification on the rewritten output catches the alignment problem but cannot resolve it. Resolution requires operator-side decisions about which version of the artifact to keep.

## Three operator-side recovery options

When the alignment problem surfaces, three reasonable paths exist.

**Path A: Accept the deployed state.** The earlier-version canonical record stands. Subsequent corrections that were applied to the scope plan and rewritten output get either applied as separate additions or filed as documentation rather than deployed. Lower disruption to deployed canonical state. Cost: the canonical record reflects an earlier version of the work; the additional content from corrections lives elsewhere.

**Path B: Roll back and redeploy.** Edit canonical files to remove the earlier-version deployment, then redeploy from the rewritten output. Cleaner record. Cost: substantial editing work; risk of introducing new errors during rollback-and-redeploy; canonical history shows a deployment-rollback-redeployment pattern that may be confusing to future readers.

**Path C: Treat the rewritten output as superseded.** The earlier deployment stands; the rewritten output gets archived as a draft that didn't deploy. Cost: loses the additional content the rewritten output contained; creates a precedent of intermediate-output-as-canonical that may bias future cycles toward early deployment.

I chose Path A in this case. The deployed canonical state is real production record. Disrupting it to match a draft document feels backwards. The two earned lessons that were added to the corrected scope plan got appended to the lessons-learned file as separate entries. The additional refinement decision got recorded in the verification report and scope plan rather than in deployed session log text. Path A minimized disruption to deployed canonical state while preserving the additional empirical content.

The choice is operator-side judgment. Path A is the lower-friction option. Path B produces a cleaner record at higher cost. Path C minimizes work at higher information loss. None is strictly correct; the right choice depends on which trade-offs matter for your specific work.

## The rule

Architecture-revision cycles deploy canonical state only after the full scope plan is stable AND verification is complete on the final output. Intermediate outputs produced before scope plan stabilization should not drive canonical deployment.

If intermediate deployment has already happened, the recovery is operator-side decision per artifact. The framework can flag the alignment problem (verification caught it cleanly) but cannot resolve it. Resolution is operator judgment.

The rule generalizes past my specific cycle structure. Any iterative work where outputs drive state changes can hit this:

- A Git workflow where branches get merged before review comments resolve.
- A document workflow where shared edits propagate before all reviewers respond.
- A code-review workflow where a feature ships before all tests pass.
- A research workflow where conclusions get cited before the underlying analysis is finalized.

In each case, the same shape: state changes that propagate from work that wasn't fully settled, then the work continues to evolve, then the propagated state is misaligned with the now-current work. Recovery requires operator-side decisions about which version is canonical.

## What this isn't

I'm not claiming this is a deep architectural insight. The lesson is operational discipline rather than design wisdom. Anyone running iterative work has probably hit similar problems and developed similar discipline; this post just names the pattern explicitly.

I'm not claiming the recovery options are exhaustive. There are likely intermediate paths beyond the three I named (partial rollback, paired-deployment, deferred deployment with explicit reversion plan). The three I described are the ones I considered for my specific situation.

I'm not claiming Path A is universally correct. I chose it because the deployed canonical state was real production record I didn't want to disrupt. A different operator with different stakes might reasonably choose Path B (cleaner record worth the disruption cost) or even Path C (minimize work, accept information loss). The right path depends on which costs matter for your work.

## What I am claiming

Architecture-revision cycles deploy canonical state only after the full scope plan is stable and verification is complete on the final output. Intermediate-output-as-canonical creates alignment problems that subsequent corrections expose. The verification chain can catch these problems but cannot resolve them. Recovery requires operator-side decisions weighing disruption against record-cleanliness against information loss.

The lesson is small. The empirical evidence is one explicit fire from one cycle. But the pattern generalizes, and naming the pattern explicitly may save someone else the recovery work I did this week.

That's the lesson. One fire, one recovery, one named rule.
