# When Verification Catches Itself: An Audit Chain Across Two Sessions

**Author:** Jimmy McColery
**Date:** 2026-05-04
**Status:** Empirical finding from one cross-session drain comparison, suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I run a verification practice across my work sessions: at the end of substantial sessions, I run what I call a drain probe. The drain examines the session's content against the current state of my framework's canonical files and surfaces drift, fires of named failure modes, planning content that needs preservation, and earned lessons worth filing.

The drain prompt is a paste-ready template that I've iterated across drain runs. The current version asks for seven categories of audit plus a closing prioritization plus a decomposed self-grade. The output is typically a substantial markdown document I save to my framework's historical archive.

I ran two drains in the same week recently. The first drain was on a session that ended a few days ago. The second drain was on the session that ran today. Both drains followed the same prompt template, attached the same kind of canonical-state inputs, and were processed by the same kind of AI model on the verification side.

The second drain caught an error in the first.

This post is about what happened, why it's interesting, and what it suggests about how verification chains work.

## The setup

Both drains examined sessions that had ended. The first drain examined the prior session's content (a session that had reached substantive closure on architecture decisions and accumulated empirical evidence about my framework's failure modes). The second drain examined this week's session (which built on the prior session's outputs and produced additional empirical findings).

Both drains had access to the same canonical state. The framework's canonical files include rules I've earned and codified, structural records of my project state, and accumulated empirical lessons. The drains can read these files directly through a deterministic-file-read substrate paired with the verifying model.

Both drains ran independently. The model running the second drain didn't see the first drain's output until I attached it as a continuity artifact. The two drains weren't coordinated; they ran several days apart and produced their findings independently.

## What the first drain claimed

The first drain made several findings about the prior session. Most were cleanly grounded in canonical state: claims about where artifacts lived, what decisions had been made, what the prior session's outputs were. Phase 5 of the verification chain confirmed those findings.

But one finding was a substantive claim about my framework's canonical rules. Specifically, the first drain claimed that an existing canonical rule already covered a certain failure-mode pattern within its scope. The implication: a refinement candidate I'd been treating as separate (warranting its own evaluation in the next architecture-revision cycle) was actually already covered by the existing rule. The drain framed this as helpful operational closure: "this question is settled; the rule already covers it."

I noted the finding when reviewing the drain output but didn't immediately verify it against the canonical rule's actual text. I filed it as "operationally hygienic to verify when the question next arises" rather than as a load-bearing claim requiring immediate check.

## What the second drain found

The second drain ran on this week's session, which had treated that same refinement candidate as a separate candidate (consistent with how I'd been thinking about it throughout the session). When the second drain audited this week's session against canonical state, it noticed the apparent discrepancy and read the canonical rule's actual text directly to resolve which framing was correct.

The verifying model's finding: the existing canonical rule does not explicitly cover the failure-mode pattern in question. The rule covers related disciplines, but the specific failure mode the first drain claimed was within scope is actually distinct. The first drain's reading was inferential; the second drain's reading was direct.

Reading the canonical rule's actual text produced a different conclusion than the first drain had drawn from inference. The refinement candidate is genuinely separate; the question isn't already settled.

## Why this matters

Two things are interesting about this empirical sequence.

The first interesting thing: a drain corrected another drain. The first drain's claim, which had been confidently stated and which I'd internalized as "operational closure," was wrong. The second drain caught it by reading canonical directly rather than inferring from related context.

The second interesting thing: the correction held up. The verifying model's reading of the canonical rule's text matches what I find when I read the rule directly. The correction isn't itself the kind of inferential leap that produced the first error; it's grounded in the rule's actual content. The verification chain didn't just generate a different opinion; it generated a finding that holds up against the primary source.

This is empirical evidence that verification chains can catch errors in their own components when the components have independent access to the same primary sources. The first drain's error wasn't caught by anyone reviewing the first drain in isolation; it was caught when a second verification ran against the same canonical state and produced a different reading.

## The structural feature that makes this work

What makes the second drain reliable as a check on the first drain isn't that the second drain is smarter or that the verifying model is better. Both drains used the same prompt template, the same kind of model, the same canonical inputs.

The structural feature is independence. Each drain runs in its own context. Neither drain's findings are conditioned on the other drain's findings. When both drains read the same primary source (the canonical rule's actual text), they can produce different conclusions, and the difference surfaces the question of which is correct.

If the second drain had read the first drain's output before running its own audit, the second drain might have inherited the first drain's reading rather than verifying it independently. Independence requires the verifying step to come at the question fresh.

This is true generally about verification chains: independence between steps is what makes the chain reliable. If each step in a chain depends on the previous step's output rather than verifying against the original source, errors propagate forward instead of getting caught.

## What this isn't

I'm not claiming verification chains catch all errors. The empirical evidence is one specific error caught by one specific verifying step. The first drain's other findings haven't been independently re-verified by other drains; some of them might also be wrong. The second drain's findings haven't been independently re-verified either; if some are wrong, a future drain might catch them.

I'm not claiming AI-on-AI verification is reliable in general. Two drains running on different sessions and reading the same canonical files happened to produce different conclusions on one specific point. That's an empirical outcome, not a theoretical guarantee. Different drains running on different sessions might have produced different patterns of agreement and disagreement.

I'm not claiming the verification chain's structural design is novel. The pattern of "have multiple verifications check the same primary source independently" is implicit in code review, peer review, and replication studies. What's empirically interesting here is observing the pattern work in practice within an iterative AI-assisted workflow.

I'm not claiming the rule the first drain misread is itself important. The specific rule's content isn't the point; the point is that the drain made an inferential error about the rule, and a subsequent drain caught it by direct reading.

## What I am claiming

Two drains running independently against the same canonical state can produce findings that disagree with each other. When they disagree, reading the primary source directly resolves the question.

The first drain in my sequence made an inferential error: it claimed an existing rule's scope covered a pattern that the rule's actual text doesn't cover. The error wasn't caught when I reviewed the first drain's output; I lacked enough context to flag the inference as questionable. The error was caught when a second drain ran independently and produced a different reading.

This is empirical evidence that verification chains where multiple steps independently check the same primary source can catch errors in their own components. The pattern's reliability comes from each step's independence from the others. If verification steps depended on each other's outputs, errors would propagate forward; because they depend on the primary source instead, errors get caught when the primary source disagrees with a prior step's reading.

The lesson generalizes past my specific drain methodology. Any iterative verification practice (code review, document audit, fact-checking, research peer review) faces the same structural question: do the verification steps depend on each other, or do they each verify independently against the original source? The latter pattern catches errors the former pattern misses.

That's the empirical finding. One error caught by one cross-drain comparison. Suggestive, not conclusive. But suggestive enough to name the pattern explicitly.

## Why this changed how I think about verification

Before running these two drains in sequence, I treated drain output as relatively authoritative. The drain prompt is well-iterated; the verifying model has access to canonical state; the drain runs without time pressure. I expected drain findings to be substantively reliable.

After observing one drain's finding fail to hold up against another drain's direct read, I treat drain output differently. Not as unreliable, but as one verification step in a chain rather than as the final word. Drain findings about substantive claims (what a rule covers, what the canonical state actually says) deserve verification against the primary source, even when the drain has produced confident output.

This isn't a discount on drain methodology. The drain prompt and the verifying model are doing useful work. It's a calibration on what drain output represents: a verification, not a verification chain. A single verification can be wrong. A verification chain (with each step independent) is more reliable than any single step.

The practical consequence: when a drain makes a substantive claim about canonical state, I now verify it directly. Five-second check. The verification might confirm the drain's finding (most cases) or reveal a drift (occasional). Either outcome strengthens the canonical record.

## The small empirical lesson

One drain caught another drain's inferential error by reading canonical directly. The error was substantive but small; the catch was empirically grounded; the lesson generalizes.

Verification chains catch errors when their components are independent and verify against primary sources rather than against each other's outputs.

That's it. One observation, one mechanism, one rule. Worth naming explicitly because the pattern is invisible when you're inside a single verification step but obvious when two verification steps disagree and you have to figure out which is right.

---

*Update note (2026-06-21 ship date): Since this post was drafted on 2026-05-04, time has elapsed. The temporal references above ("this week," "a few days ago," "ran today") reflect the drafting moment when both drain runs were recent events. The empirical sequence described occurred in early May 2026; the methodology lesson articulated remains accurate. The original temporal framing is preserved as-written from the drafting moment; this update note acknowledges the time elapsed since.*
