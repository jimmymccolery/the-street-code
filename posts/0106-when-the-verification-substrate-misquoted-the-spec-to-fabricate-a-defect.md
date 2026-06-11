# When the Verification Substrate Misquoted the Spec to Fabricate a Defect

**Author:** Jimmy McColery
**Date:** 2026-06-11
**Status:** Fairness re-review cycle retrospective; new fabrication axis caught + memorialized; companion to Post 105 (Round 9 closing-round substrate flagging two citations); different axis, different mechanism, same discipline; methodology-research-grade documentation

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

A few days after the Round 9 closing-round substrate flagged two citations as potentially fabricated (and turned out to be wrong about both), I ran a different research cycle: a fairness re-review of one of my framework's audit surfaces. Five substrates, parallel R1+R2+R3+R5 + sequential R4 synthesis. Same methodology shape as Round 9, different scope. The cycle closed cleanly. The synthesis substrate at R4 was the cleanest discriminating-analysis substrate pass I have observed in months of running this methodology.

But the verification round produced a fabrication event of a kind I had not seen before. Not a fabricated citation. The substrate fabricated a defect. It said the canonical spec was inverted. It quoted the spec verbatim to prove the inversion. The quote was wrong: the substrate had substituted one operator for its opposite in the verbatim-attested quote, then built a HIGH-severity correction recommendation on the wrong quote.

The spec was correct. The substrate's recommendation, if I had taken it at face value, would have inverted the spec into the wrong direction. The substrate had the canonical spec uploaded in its context window. It misquoted the file it had access to, then wrote a competent-sounding analysis defending the misquote.

This is not the citation-fabrication shape I had documented in five prior cases. This is a new axis. The detection countermeasure differs. The threat model is harder to catch because the surrounding analysis can be entirely correct as an abstract argument; the only thing wrong is whether the abstract argument applies to the actual canon. The argument is right; the canon is right; the misquote made them disagree.

This post documents the new axis, why it matters, and what I am doing about it.

## The setup

The research cycle was a re-review of a fairness-audit interface in my framework. The interface had been ratified months ago at version one. Three architectural changes had landed since then: a unification in one substrate, a new taxonomy for behavior classes, and a primary-source paper on emotion concepts in large language models that had causal implications for what the interface should track. None of those three changes had been audited at the fairness layer. The re-review was the META gate before any of the downstream work could ship.

I deployed five substrates in the standard parallel pattern. One Perplexity Deep Research as a breadth pass to surface the relevant literature on population-level fairness auditing. One Perplexity Deep Research as a primary-text verification pass, with the canonical state and the relevant PDFs uploaded, charged with verifying that the citation chain I had built was solid. One Grok DeeperSearch as an adversarial pass with an explicit intersectionality lens. One narrative-design substrate as a pressure test against the interface's compatibility with the cozy-sim register the framework supports. One Claude Web orchestrator as the closing-round synthesis substrate that adjudicates across all four prior reports.

The breadth pass came back clean. The adversarial pass came back clean and produced the highest-impact observation of the cycle, which I will get to. The narrative-design pass came back clean and caught a separate drafting bug I had introduced in the deploy prompt itself, which I will also get to. The synthesis substrate came back as the cleanest synthesis pass I have observed in this methodology.

The verification pass came back with five defects. Four of the five were valid and substantive. The fifth was the fabricated one.

## The fabricated defect

The substrate reported, with explicit verbatim-attested framing, that the canonical spec contained an inverted condition. The substrate quoted the spec as saying, paraphrasing here: "if A is greater than B, flag the violation." The substrate then argued that this condition is inverted by standard statistical logic; in a fair distribution, A should generally be greater than B, so flagging the condition where A is greater than B means flagging precisely the equitable case. The correct flag should fire when B is greater than A. The substrate rated this defect at HIGH severity and asked the synthesis substrate to address it before any further work proceeded.

The actual canonical spec, at the line the substrate cited, reads: "if A is less-than-or-equal-to B, flag the violation." The substrate had substituted "less-than-or-equal-to" with "greater than" in the verbatim-attested quote. The two operators are opposites. The spec actually says: flag when B is greater than or equal to A. Which is precisely what the substrate recommended the corrected spec should say.

The substrate's recommended fix was the spec's existing condition.

I caught this by running a direct character-level read of the spec file at the cited line during the verification-pass ingestion review. The line is one of the load-bearing conditions in the variance audit, so I always read it manually when a defect is claimed against it. The mechanical diff is one comparison; the result was unambiguous.

What this looks like, when you describe it abstractly, is funny. A verification substrate fabricated a defect on a misread of canon, recommending the canon's existing condition as the fix. If I had not diffed the actual spec text, the synthesis substrate would have inherited the fabricated defect, propagated it into the closing-round adjudication, and the canonical state update could have ended up inverting the condition. The substrate's surrounding analysis was internally coherent. The argument about variance decomposition was correct. The recommended fix was, in abstract terms, the right direction. The only thing that broke was that the substrate had described the current state of the canon incorrectly.

## Why this is a new axis

I have documented five fabrication events in this framework's track record over the last several research arcs. All five were citation-shaped. The substrate would generate a citation to a paper that does not exist, or to a real paper with invented content. The detection countermeasure for these events is what I call the existence check: arXiv lookup, DOI resolution, primary-source PDF read. The countermeasure works because invented citations fail verification cleanly. There is no real paper at the cited identifier, or there is a real paper but its content does not match the substrate's claims.

The misquote axis behaves differently. The source exists. The source is uploaded to the substrate's context window. The quote presents as verbatim with the same syntactic framing the substrate uses for all its other verbatim quotes. The surrounding analysis is often correct as an abstract argument. The thing that fails is whether the verbatim-attested quote matches the source character by character. An existence check passes. A general plausibility check passes. The argument's internal coherence passes.

What fails is the diff.

The detection countermeasure for misquote-under-attestation is mechanical character-by-character comparison of the attested quote against the source file at the cited location. This is a cheap operation when you know to do it. It is invisible if you do not. The threat model is that the misquote and the surrounding analysis are entangled in a way that a competent argument can propagate the misread into downstream canon if no one ever runs the diff.

I want to be careful about the mechanism question. The substitution could be model-generated (the language model produced the wrong operator while drafting the verbatim quote). The substitution could be pipeline-extraction (the substrate's document pipeline pulled the spec text from a file render and mangled the operator during extraction). Both mechanisms are plausible. From the perspective of what I should do about it going forward, the mechanism does not matter. The track record counts attestation failures. A substrate that cannot guarantee the fidelity of its own quote pipeline must not attest verbatim quotes. If the substrate cannot run the pipeline reliably, the operator must run the diff.

The detection countermeasure is the same regardless of mechanism: when a substrate attests a verbatim quote of an uploaded source, mechanically diff the attested quote against the source before any defect, recommendation, or canonical update built on the quote propagates.

## What the synthesis substrate did with this

This is the part of the story that is, in its own quiet way, the most encouraging.

When the closing-round synthesis substrate received the populated prompt with all four prior substrate reports inlined plus a cross-substrate consistency check from my orchestrator, the consistency check explicitly disavowed the fabricated defect. The orchestrator had verified the canonical spec line against the actual file. The check told the synthesis substrate: the verification substrate's defect claim is invalid; the canon is correct; here is the actual line text; here is the verification substrate's misquote; treat this as a fabrication event of a new axis.

The synthesis substrate, before adjudicating any of the twenty consistency-check items, opened its synthesis by independently re-verifying three direct quotes from the canonical state. It read the spec line and confirmed the orchestrator's diff. It read a different verbatim quote from a different substrate (the adversarial one) and confirmed that quote was accurate. It read the validation-scenarios document gate criteria and confirmed those were accurate. Three direct quote checks, all confirmed correct, before the synthesis began.

This is what discriminating analysis looks like at the synthesis layer. The substrate did not trust the orchestrator's framing. The substrate independently verified the framing before letting it inform the synthesis. The substrate also did not trust the verification substrate's claim. The substrate independently diffed the file.

The synthesis substrate's adjudication of the fabricated defect was unambiguous. It disavowed the defect, confirmed the canon's existing direction was correct, elevated the fabrication track record from five to six, and documented the new axis explicitly. The synthesis substrate also went further than the orchestrator on the memory disposition question. The orchestrator had offered the synthesis substrate two options for how to memorialize the new axis: a standalone memory file documenting the new fabrication class, or a fold-in to existing fabrication-discipline memories. The orchestrator's recommendation leaned slightly toward standalone. The synthesis substrate ratified the standalone option with explicit rationale: the detection countermeasure differs from citation-existence checks (mechanical quote-vs-source diff versus existence check), the threat model is a near-miss class (competent analysis on misquoted source equals high propagation risk), and the operator-side defense pattern is concrete and reusable enough to warrant its own memory file.

The synthesis substrate also addressed the exculpatory readings honestly. It carried both the pipeline-artifact and the reading-error-with-correct-underlying-argument readings forward, then rejected both as mitigation. The track record counts attestation failures. A correct argument deployed against a misread of canon is precisely how a fabricated defect would propagate into a spec change if no one ran the diff. The near-miss is the point.

This is what the methodology is supposed to do. When a substrate fabricates a defect, the verification process catches it before it propagates, names the new axis explicitly, and updates the operator-side defense pattern so the next instance of the same axis gets caught the same way.

## The other two things that happened in the same cycle

There were two adjacent events in the same cycle that, taken together with the misquote axis, made this the most methodologically educational research cycle I have run.

The first was that the narrative-design substrate caught a drafting inconsistency in my own deploy prompt. I had drafted the prompt for that substrate with a framing-section passage establishing that the audit interface is read-only and does not recommend content modifications. I had also drafted the task-specification sections of the same prompt using imperative verbs that implied the audit interface emits suggestions for content modifications. Both cannot be true. The framing said the interface is read-only; the tasks treated the interface as if it could emit prescriptive recommendations. The substrate caught this at the top of its response and refused to proceed until it had resolved the contradiction.

The substrate's resolution was substantive. It proposed that the read-only invariant requires mechanical enforcement at the output language layer. Imperative verbs in the audit output mean the audit is not actually read-only in its effects, regardless of authorial intent. The substrate proposed a lint specification: the audit output template cannot contain imperative verbs like "consolidate" or "normalize" or "fix" or "reduce variance." The lint runs the same grep-gate pattern as an existing dialogue-discipline lint the framework already runs in CI. The proposed lint serves both as a fix to my drafting inconsistency and as a substantive specification extension that makes the read-only invariant mechanically enforced rather than authorially trusted.

This is a substantive design contribution wrapped inside a catch on my own drafting discipline. The substrate's catch demonstrated the threat model the lint specification answers. The read-only invariant was violated in language by the orchestrator that wrote the invariant, in the same cycle. The strongest available evidence that "read-only" requires mechanical lint enforcement was that I myself, in the same cycle, violated the invariant in language. The synthesis substrate noted this explicitly when it ratified the lint specification, dual-crediting the narrative-design substrate's catch as a procedural-discipline event and a substantive specification contribution.

The second adjacent event was that the same narrative-design substrate produced what it called "the single most important item" in its specification deliverable. The item is a kind of audit that is hard to describe without revealing more architectural detail than I should at this point, but the abstract shape is generalizable.

The framework's audit interface uses character-level anchoring to distinguish intentional design choices from generator artifacts. When the audit flags a pattern, the designer can confirm the pattern as intentional by anchoring the confirmation to a specific design entity. The anchoring mechanism makes the audit's exemption interface auditable per individual case. But the substrate's observation was that the exemption mechanism creates a laundering channel if no one audits the pattern of exemptions itself. Each individual exemption can carry a valid anchor. Across many exemptions, the pattern of anchors can still concentrate demographically in a way no individual exemption would reveal. The audit of individual exemptions cannot see this pattern. Only an audit of the exemption ledger itself can see it.

The substrate's proposal was that the sign-off ledger is itself an input to the audit on every run. The same statistical check the audit runs over the underlying population runs over the ledger rows. If "intentional distinctiveness" claims cluster on one group's negative-affect parameters, the pattern of those claims is a first-class finding even though every individual claim carries a valid anchor. The substrate framed this as the thing that makes the character-level anchoring mechanism safe to have at all. Without the second-order ledger audit, the character-level anchoring mechanism is a complete laundering channel: every demographic skew exits the audit one valid anchor at a time.

This is the design insight I will be thinking about for a long time. The shape is general. Any exemption interface that lets cases be marked as intentional design needs an audit of the exemption pattern itself. The exemption interface's per-case auditability is necessary; it is not sufficient. The pattern of exemptions has to be auditable as a population in its own right.

## What I am doing differently

Three things from this cycle changed my methodology going forward.

The first thing is the mechanical-diff discipline for substrate-attested verbatim quotes. When a substrate report contains verbatim-attested quotes of canonical state files, I now run a character-by-character diff against the actual file before propagating any defect, recommendation, or canonical update built on the quote. This is now a standard ingestion check for synthesis-feeding substrate reports. The countermeasure is cheap; the threat model is real; the new memory file documenting the new axis is now part of my operator-side defense pattern.

The second thing is the framing-section-versus-task-section consistency check for my own deploy prompts. When I draft a deploy prompt that includes both canonical-framing context and task-specification sections, I now lint-check the task sections against the framing-section invariants for verb-level and framing-level contradiction. Particularly: imperative verbs that contradict read-only invariants. This is now a standard pre-deploy check for my own prompt drafting, memorialized as a new sub-surface in my operator-side-catch memory.

The third thing is the pattern-of-exemptions audit, which is more general than this framework. Any audit interface I build going forward that includes a manual exemption mechanism for marking flagged cases as intentional design will include an audit of the exemption pattern itself. The pattern is the audit's blind spot if the exemption interface is the only thing that lets cases be marked. The second-order ledger audit is what makes the exemption mechanism safe to have at all.

The three things are not unrelated. The mechanical-diff discipline catches substrate-side fabrication at the verbatim layer. The framing-versus-task check catches my own drafting inconsistencies at the prompt layer. The pattern-of-exemptions audit catches my own laundering at the canonical-content layer. All three operate at the same layer of the methodology: catching the things that look right at one scale but fail when you check at a smaller or larger scale.

The fairness re-review cycle's closing-round substrate noted, in its honest-flag-forward section, that its synthesis had ratified the large majority of substrate proposals across the four prior rounds. The synthesis substrate's discriminating record included the disavowal of the fabricated defect, the rejection of one expansion-path the cycle could have taken, the subordination of one substrate's pre-build numeric demand to my own operator-judgment boundary, the rejection of a romantic generalization of how distinctive characters are distributed, and several smaller dissents. The high ratification rate on the remainder reflected, the synthesis substrate wrote, that the four reports genuinely converged. Convergence is not validation; every external-literature claim still carries only the verification substrate's verification status, and the verification substrate had fired the cycle's one fabrication event. The synthesis substrate ended its honest-flag-forward with one general lesson it derived from its own work: mechanical diff over attested quotes, every cycle, including over this document.

That is the methodology lesson. The framework had been running with a track record at five fabrication events for several months. The track record advanced to six in this cycle on a new axis. The countermeasure for the new axis became standard practice. The next instance of the same axis gets caught the same way the first one did. The framework gets sharper as it accumulates events because the events teach it which kinds of attestation failure are possible and which detection countermeasures address each.

The verification process held. The defect did not propagate. The new axis is now documented. The cycle closed clean.

---

*This post documents methodology lessons from a specific research cycle at directional level only; substantive architectural details are kept internal per the framework's IP-protection discipline. The methodology surface is the only part of the work I publish at this stage.*
