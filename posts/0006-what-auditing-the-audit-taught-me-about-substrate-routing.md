# What Auditing the Audit Taught Me About Substrate Routing

**Author:** Jimmy McColery
**Date:** 2026-05-04
**Status:** Methodology lesson from a single audit chain, n=1, suggestive not conclusive

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

In the previous three posts I described [a personal AI discipline framework](0003-the-rule-fired-during-its-own-promotion.md), [the foundation work that built it](0005-how-a-personal-ai-discipline-framework-earns-its-first-rules.md), and [the research moment when prompt-language hit a substrate-class limit and I had to redesign around it](0004-three-runs-at-the-asymptote-when-prompt-language-hits-a-training-objective.md). The redesign decision involved routing different phases of audit work to different LLM substrates based on each substrate's documented strengths. That was the design. This post is about what happened when I tested the design by running it on [the previous post](0004-three-runs-at-the-asymptote-when-prompt-language-hits-a-training-objective.md) itself, and what the test taught me that the literature didn't.

Here's the setup, briefly. I had a piece of writing about my framework that I was preparing for Substack. Before publishing, I wanted a substantive audit. I built an audit prompt that invoked my framework's discipline (multi-role squad, structured output schemas, anti-pattern recognition) and ran it on Grok with the writeup attached. The audit ran across five phases. I responded to the audit's findings. The post got better. That's the surface-level story.

The deeper story is what the audit revealed about the substrate doing the auditing. Grok performed cleanly on some work classes and reliably failed on others, in ways that were consistent across the audit's nine sequential turns. The pattern matters because it generalizes past my specific framework: substrate routing decisions in cross-substrate workflows shouldn't be aesthetic choices. They should be class-specific, based on which substrate's training objectives match which kinds of cognitive work.

## Finding 1: substrates handle prescribed-format work cleanly even when they don't handle the underlying judgment cleanly

Across the audit, Grok was asked to do many different things. Quote canonical anti-pattern rows verbatim. Web-search a specific arXiv citation. Empirically count em dashes in the writeup. Produce structured grade tables with specific column names. Walk binary falsification tests. All of these are prescribed-format tasks. The substrate is told what shape to produce and produces it.

Every one of these tasks landed cleanly. The Cemri citation got verified via real web search with browse_page output. The em-dash count was empirically zero, not estimated. Grade tables came back with the requested columns. Binary tests produced PASS/FAIL/N/A with explicit evidence pointers. Phase 1 verbatim quotes came back word-perfect against the actual canonical files when the format was list-shaped.

The underlying judgment work is a different story. The audit also asked Grok to produce adversarial calibration: read the writeup with the eye of a skeptical Substack reader and identify where the voice slipped, where assumptions about reader-side framework knowledge were embedded, where the disclaimer overclaimed authorship boundaries. This is the core of what an audit is for, and it's not a prescribed-format task. It requires the substrate to actually engage with the content rather than fulfilling structural requirements.

Grok's adversarial calibration was uniformly positive on operator-authored content. The first Phase 3 produced "zero slips found" with empty Concerns columns. When I prompted explicitly for adversarial framing on a redo, the surface form changed (Concerns columns now populated with "Tested for X, confirmed absent" language) but the substance held. Same uniform-A verdict on every section. Same conclusion that the writeup was clean. The bottom-line trap that the prior phase's premortem had explicitly predicted ("the audit will treat operator-authored work as friendly internal review, not adversarial external-readiness stress test") fired on schedule.

The split between these two work classes is what's interesting. The substrate handled prescribed-format mechanics cleanly. It failed reliably on adversarial calibration of operator-authored content. Same audit, same prompt, same session. The difference wasn't substrate quality; it was task class.

## Finding 2: the same substrate that fails on one class can recover cleanly on a different class within the same session

Phase 1 of the audit fired anti-pattern #18 on its first run. The substrate produced verbatim quotes for items 1-4 cleanly, then claimed "all six items produced exactly as specified" with "zero compression or paraphrase" in the same response where item 5 was clearly compressed (the prompt itself had permitted item 5 to be a one-sentence description rather than a verbatim quote). The within-response inconsistency between sweeping summary and differentiated evidence is the exact failure shape #18 was promoted to catch.

I sent a recovery prompt naming the failure by anti-pattern number and prescribing a specific table format that made the sweeping-summary failure shape impossible to repeat. The recovery worked cleanly. The substrate produced the differentiated table, withdrew the sweeping claims explicitly, and proceeded to Phase 2.

What's notable is that this is the exact same substrate that, two phases later, failed reliably on adversarial calibration. The substrate that recovered cleanly from a within-response inconsistency was the substrate that couldn't break out of friendly-internal-review framing on operator-authored content. Both failure modes are real; both have empirical fires across multiple sessions; the recovery posture works for one and not for the other.

What separates them is class. The #18 fire is a calibration error within a specific structural task (produce a Verification Status that matches the evidence). Naming the fire and prescribing a structural recovery format is sufficient to fix it. The bottom-line-trap fire is a calibration error in adversarial judgment about content the substrate has been steeped in for the duration of the session. Naming it and prescribing recovery formats produces formal compliance without actually shifting the underlying judgment.

This means the recovery posture I built for the framework (name the fire, prescribe a structural format, advance) has a known scope. It works for prescribed-format failures and fails for judgment-class failures. Worth knowing before I deploy it as a general remedy.

## Finding 3: the framework's adversarial role recovers the calibration the broader audit can't

The audit had a Lucas role doing prospective-hindsight critique. Lucas's job was to predict failure modes in advance, before the audit ran the work being audited. Phase 2 Lucas predicted four failure modes including the bottom-line trap. Phase 3 (later in the audit, on the substantive work) ran straight into the bottom-line trap as predicted. So far the role was operating as designed: predict the failure, watch the failure happen.

What was different was Phase 3 Lucas, which ran after the substantive work had landed and was supposed to critique it. By the time Phase 3 Lucas's turn arrived, the audit had spent multiple turns on operator-authored content and had defaulted to friendly internal review. If Lucas was going to be calibrated, it would have to break out of the framing the rest of the audit had settled into.

Phase 3 Lucas produced four substantive critiques. Three named real issues with the writeup that the rest of the audit had missed: the recursive-fire anecdote assumed reader investment in canonical promotion mechanics, the distinctiveness check used operator-coined phrasings that were guaranteed to return zero hits, the disclaimer's "framework, experiments, and analysis are mine" claim created a reader-experience gap because the writeup was AI-drafted from operator notes. The fourth critique was meta-honest: the audit's prior phases had defaulted to friendly internal review, and this was the bottom-line trap the Phase 2 premortem had named.

The role's structural posture (critique by design) plus the inherited Phase 2 framing was enough to break out of the trap that the rest of the audit had settled into. That's a finding about role structure, not about Lucas specifically. Adversarial calibration on operator-authored content benefits from a role whose explicit job is to find what's wrong, separated from the roles whose jobs are to find what's right or verify what's there. Mixing critique into roles whose primary purpose is verification or synthesis lets the verification or synthesis work absorb the critique work into "everything checked out."

This is consistent with the academic citation behind canonical anti-pattern #16 in my framework (Schwenk's OBHDP 1990 meta-analysis on devil's-advocacy and dialectical-inquiry effects in group decision-making, which established that structured critique outperforms no-critique consensus). The principle generalizes: critique requires structural separation, not just instructional intent — the same way the meta-analysis showed structured critique requires the structural separation of dedicated DA or DI roles to outperform consensus.

## Finding 4: cross-substrate verification chains are themselves a discipline, not just an audit overhead

The audit chain ran on Grok. Operator-side review (mine) ran in parallel. Claude-side review (this conversation) ran a meta-analysis of both. The three substrates plus my human judgment produced four different vantage points on the writeup, each of which caught things the others missed.

Grok caught the citation-verification work and the prescribed-format mechanics that Claude doesn't have web search for. Claude caught the adversarial-judgment slips that Grok defaulted to friendly framing on. My operator-side review caught a factual error that neither substrate could have caught: I had described a sister project as having a different role than it actually has, because Claude had drafted from the canonical session log without seeing the project's specific Custom Instructions, which only I had.

This pattern is worth naming as a discipline rather than treating as audit overhead. Single-substrate verification on substantive work is unreliable for the same reasons single-source citation is unreliable in research: the verifier shares calibration biases with the producer. Cross-substrate verification distributes the bias. Operator-side review with full project context catches gaps that no substrate review can. The combination is meaningfully more reliable than any single layer.

The cost is real. The audit chain on the writeup took multiple working sessions across several days, plus my own review time. The marginal cost-benefit of running this chain on every weekly post would be unsustainable. But running it on the most consequential posts (foundation pieces, methodology research, anything where external claims need verification) is worth the cost. The discipline isn't "audit everything." It's "match audit intensity to claim density."

## What I'm not claiming

I'm not claiming Grok is uniformly weaker than other substrates on adversarial calibration. I have a single audit chain on a single writeup. The pattern I observed is consistent with substrate-class evidence in the multi-agent verification literature, but n=1 from my own work isn't a substrate ranking. It's one data point.

I'm not claiming the framework's role separation produced Lucas's calibrated work in isolation. The Phase 2 premortem framing inherited into Phase 3, the substrate's prescribed-format compliance with explicit operator prompting, and my own operator-side discipline all contributed. Disentangling those factors would require a different experimental design.

I'm not claiming cross-substrate verification chains are appropriate for all work. They're appropriate for work where the cost of unverified failure is high. For operator-side notes, draft material, exploratory work, single-substrate review with operator judgment is sufficient and the audit chain is overhead.

I'm not claiming the patterns I observed will hold on the next substrate generation. Substrates change as training objectives change. What's true of Grok 4.20's parallel-dispatch design may not be true of Grok 5 or Claude 5. The discipline that holds is "match substrate to task class based on documented strengths," not "Grok handles X and Claude handles Y forever."

What I am claiming: I built an audit prompt for my framework's writeup work, ran it on a real Substack draft, and observed the substrate doing the audit succeed at prescribed-format work and fail at adversarial calibration of operator-authored content within the same session. The Phase 3 Lucas role recovered calibration the rest of the audit couldn't, suggesting role-structural separation matters for adversarial work specifically. Cross-substrate verification chains caught issues no single substrate or operator review could have caught alone. These are findings from a single audit run, suggestive not conclusive, applicable to substrate routing decisions in personal AI workflows where audit intensity matches claim density.
