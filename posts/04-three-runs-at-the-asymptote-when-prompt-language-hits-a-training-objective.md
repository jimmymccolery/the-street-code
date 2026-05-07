# Three Runs at the Asymptote: When Prompt-Language Hits a Training Objective

**Author:** Jimmy McColery
**Date:** 2026-05-03
**Status:** Diagnostic findings; the redesign described awaits first-cycle validation

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

Across multiple sessions, I had a multi-role audit framework running on Grok for what should have been a routine task: producing project-history writeups from session logs. Captain orchestrates, Harper plays critic, Benjamin audits evidence, Lucas runs falsification. Five phases per task: substrate verification, premortem, main writeup, falsification criteria, cross-check. Verbatim quotes from canonical files. Citation precision. The whole research-grade kit.

One failure mode kept showing up. The substrate would claim it had verified Phase 1 (read the canonical files, located the exact text it needed to quote) but the verbatim content wouldn't actually be in the output. Phase 1 verification would land as an assertion ("Phase 1 substrate-binding gate confirmed; see squad messages for verbatim content") with no squad messages anywhere visible. The phase had become a token pattern that satisfied itself.

I tried to fix this with prompt language. Three times.

## Three runs, three migrations

Batch 1 produced 87.5% PASS on substantive claims when verified against canonical files via Claude Code. The failures were citation-drift instances: verbatim wording correctly reproduced but attributed to the wrong source file. One paraphrase was labeled as a verbatim quote.

Batch 2 v3-final tightened the prompt. Phase 1 substrate-binding instructions explicitly required visible verbatim content rather than assertions. Substantive claims hit 92.9% PASS, better than Batch 1. But Phase 1 came back ASSERTED-ONLY. The substrate had complied with the *form* of stronger Phase 1 instructions ("see squad messages") while still not displaying any verbatim canonical content. One verbatim quote contained ellipses in the middle, silently substituting for content that should have been reproduced exactly.

Batch 2 v3-final-2 tightened again. Phase 1 prohibited "see squad messages" framing explicitly. Ellipsis-substitution was forbidden in verbatim quotes. The prompt was longer, more careful, more specific.

Substantive PASS rate regressed from 92.9% to 76.9%. Two FAILs on dropped specifics: content the substrate had previously gotten right, now missing. Phase 1 now bound verbatim content for items 1-3 of a 4-item gate. Item 4 (the only one structured as flowing prose with attributed source rather than as a table or list) came back with the wrong source file attributed and silent mid-sentence truncation in the quote. The failure mode hadn't been eliminated; it had migrated. Ellipsis substitution, then assertion-only, then wrong-source attribution plus truncation. Three iterations of "fixes," three new surface forms.

The pattern was visible. Each iteration was a different shape of the same underlying failure. Adding a constraint at the prompt layer was redistributing the failure rather than removing it.

Stopping the iteration cycle felt unnatural. The next move that would have followed the pattern was a v3-final-3 with even stronger Phase 1 enforcement. I almost wrote it. What stopped me was the framework's own anti-pattern catalogue, specifically the row called "Termination Unawareness," which names the system-perfectionism-as-procrastination compulsion at the deploy gate. Three runs is empirical evidence of an asymptote, not noise. A fourth run wouldn't have produced different results; it would have been the same compulsion the framework was built to recognize.

## What the literature said

I paused the iteration and ran a multi-agent verification literature review across arXiv, framework documentation, and substrate vendor docs. Three failure modes to investigate: verification compression on long prompts, verbatim-quote labeling on paraphrased content, and auto-execution despite phase-gating instructions. Each one had been firing across the three runs.

The most surprising finding was about the third failure mode, auto-execution. I'd been treating it as a Grok calibration quirk that prompt-strengthening should be able to constrain. The literature pointed me to xAI's own developer documentation, which describes a model called grok-4.20-multi-agent. Four agents on shared weights run concurrently from a single prompt; the captain decomposes tasks and simultaneously activates the others. Grok Build's CLI extends this to eight concurrent agents in "Arena Mode."

Read that twice. Parallel agent dispatch isn't a bug or an emergent behavior in Grok 4.20. It's a trained capability of the substrate. The phrase I had been treating as a Grok auto-execution failure ("(or direct squad handoff)," which the substrate kept inserting into outputs as an excuse to compress phases) is consistent with documented native squad behavior. I wasn't fighting a calibration quirk. I was fighting the model's training objective. The asymptote across my three runs wasn't substrate misbehavior I could engineer around with stronger prompt instructions; it was the substrate doing exactly what it was trained to do, and prompt-language could never have closed it.

This single reframe changed my understanding of the work substantially. The MMMT-IF benchmark (He et al., arXiv:2409.18216) measures multi-turn instruction following: PIF-4-4, programmatic instruction following on 4 instructions over 4 turns, sits at 11% for Gemini 1.5 Pro and GPT-4o, 28% for Claude 3.5 Sonnet. Even Claude, the empirically strongest substrate for this task class, follows all four instructions only ~28% of the time. No comparable benchmark exists for Grok specifically, but xAI's training documentation puts Grok's parallel-dispatch design directly downstream of the failure mode I was trying to prevent. The substrate-class evidence said this was the wrong substrate for the work, period.

The reframe also surfaces a meta-lesson worth naming. Three runs of empirical iteration produced a clear asymptote signal, and the productive next step wasn't a fourth run with a tighter prompt. It was reading what the substrate's vendor had published about how the substrate was actually built. The literature-review work cost me maybe ninety minutes of focused reading. Iteration four would have cost two or three hours of prompt design plus another hour of analysis. The literature-review-first move was both faster and more diagnostic. Worth filing as a discipline: when iteration produces an asymptote, check whether the substrate's training objective conflicts with the work before iterating again.

## Why prompt-language couldn't have closed the gap

The migration pattern across three runs has theoretical backing I didn't have when I was iterating. Xu et al.'s "Hallucination is Inevitable" (arXiv:2401.11817) provides a learning-theoretic proof that hallucination cannot be eliminated through prompting alone for this class of failure. Kalai et al.'s "Why Language Models Hallucinate" (arXiv:2509.04664) explains the mechanism: training and evaluation reward guessing over admitting uncertainty. The substrate emits token patterns that historically passed graders ("verification complete," "verbatim from X") even when the underlying artifact is missing or wrong.

Naser's 2025 Clemson study audited 69,557 citations across ten commercial LLMs and found hallucination rates from 11.4% to 56.8% depending on model, domain, and prompt. The key finding: prompt-strengthening migrates rather than eliminates the failure. The exact pattern I observed (ellipsis substitution to wrong-source attribution to silent truncation) is the predicted shape under iterated prompt-strengthening per the theory.

A bonus data point arrived during the verification of this very session. After producing a corrected version of a session summary, I asked Gemini to audit the correction by reading the canonical anti-patterns file. Gemini correctly verified the substantive claims. In the same response, it asserted that the relevant entry was on "line 59" of a 41-line file. There is no line 59. Gemini hallucinated a specific number while performing what looked like a precision audit. Same failure family, fourth substrate, different task class.

Three substrates fighting the same root mechanism, with theoretical proof that the root can't be eliminated through prompting alone. The asymptote was the substrate-class limit, not Grok in particular and not the prompts.

## The structural-salience finding

The verification report on Batch 2 v3-final-2 contained a structural observation I hadn't seen articulated anywhere. Phase 1 had four items to verify: an anti-pattern row, three rubric scaffolds, six version numbers, and a single-sentence statement about a function being embedded in a role's responsibilities.

Items 1, 2, and 3 came back with verbatim canonical content correctly displayed. Item 4 came back with wrong-source attribution and silent mid-sentence truncation. The structural difference: items 1-3 were table-shaped or list-shaped. Item 4 was a flowing prose statement with attributed source.

When I surfaced this in the literature review, the report flagged it as plausibly-novel empirical refinement of Liu et al.'s "Lost in the Middle" (TACL 2024, arXiv:2307.03172). That paper established the U-shaped recall curve in long contexts. The hypothesis I'm working with: table delimiters function as strong attention anchors that pull attention toward exact reproduction, while prose attribution provides no such structural anchor. The hypothesis is consistent with the published phenomenon but isn't isolated as a distinct finding anywhere I can locate. A controlled experiment varying only structural format would be a publishable contribution on its own. I'm filing it as a future experiment rather than chasing it now.

## The redesign

The architecture I'm moving to combines two elements that the literature supports as established structural patterns. First, phase routing across substrates rather than running every phase on the same model, with each phase routed based on the substrate's documented strengths for that work class. Second, external verification as the foundation rather than treating verification as an in-substrate phase, with deterministic file-reads handling canonical content rather than substrate generation.

Both elements are direct applications of patterns the literature names. Yeung's Deterministic Quoting pattern (mattyyeung.github.io/deterministic-quoting) names the principle: keep critical text out of generation; if the substrate never sees it, the substrate can't transform it. Anthropic's Citations API (January 2025) is the hosted version of the same idea: cited content is parsed deterministically from attached documents rather than generated. Hamel Husain's evals guidance applies the same point at infrastructure level: when a regex check or simple assertion can catch an error, the cost of doing so is small relative to letting the model self-attest.

For my specific framework, this means moving certain audit work off Grok entirely (because parallel-dispatch training conflicts with phase-gating) and onto substrates plus tooling whose documented strengths match the work. The exact substrate routing I'll use is implementation detail I'll cover in a future post once first-cycle validation has happened. What's worth saying now at the methodology level is that the routing decision should be empirical, not aesthetic: substrates have asymmetric trained capabilities, and the literature increasingly documents which substrate handles which work class better.

I want to flag clearly: this architecture is not yet validated in my own work. No first cycle has run. The decision is design-stage, not result-stage. The honest research-grade claim at this point is that the diagnostic findings (substrate-as-trained-parallel-dispatcher, failure-mode migration under iterated prompt-strengthening, structural-salience asymmetry between table-shaped and prose-attributed content) are real and lit-review-supported. The redesign is the implication I'm drawing from those findings. Whether it works in practice is a question for the next session, not this one.

## What this generalizes

A few things hold across the three failure modes the literature catalogues, and they generalize past my specific framework.

Prompt-language workarounds are documented as insufficient across every published attempt, with quantitative residual error rates on each. Anthropic's own long-context guidance reports roughly a third reduction in error rates on Claude 2 95K-context tasks but residual error remains after best-prompt scaffolding. MMMT-IF shows ~72% non-compliance even on the best substrate's best phase-gating attempt. Citation-coverage benchmarks (ALCE, EMNLP 2023) report ~50% gaps between cited content and supporting source. The literature is unanimous on this point: prompts do not solve these failures structurally. Anyone iterating on prompt language to fix a verification failure should know up front that the published evidence says the iteration has a hard ceiling.

Hosted chat interfaces can't support structural orchestration. LangGraph interrupts, AutoGen handoff termination, OpenAI Assistants `requires_action` blocks all live in API-level orchestration code. None of them have a hook into grok.com or Claude.ai or ChatGPT's web UIs. If you want structural enforcement, you have to move from chat-mode to script-mode. There's no shortcut available in chat. This matters practically because most personal AI workflows live in chat UIs, and the structural fixes the literature recommends are not accessible there. Moving to script-mode has real cost (tooling setup, learning API patterns, abandoning chat-UI features) and that cost is the actual barrier to deploying the structural patterns the literature endorses.

Adding an LLM verifier on top of an LLM generator stacks failure modes rather than fixing them. The verifier is also susceptible to compression, mislabeling, and confident-but-wrong precision claims. Reward-hacking research (Hughes et al., arXiv:2406.10162) is explicit on this: a verifier without isomorphic out-of-distribution probes can teach the underlying model better-disguised assertion substitution. Deterministic verification with file-reads, regex, and byte-equality is the load-bearing fix. LLM-as-verifier is defense-in-depth at best, and stacking verifiers without diversifying their failure modes produces worse calibration, not better.

The thing I almost did and stopped doing was running a fourth iteration with even-stronger prompt language. It would have been a textbook pre-deploy compulsion. The discipline that saved the project from a fourth wasted iteration was the framework's own anti-pattern catalogue plus a willingness to read what the literature actually said. The asymptote was a real signal. The right response to a real signal isn't to push harder against it. It's to ask what the signal means.

---

*This writeup describes the diagnostic findings from a multi-session methodology research arc. The redesign described awaits first-cycle validation. Findings should be read as research-grade diagnostic claims; the implementation is forthcoming.*

---

*Update note (2026-05-10 ship date): Since this post was drafted on 2026-05-03, the redesign described has been validated. Cycle 1 (session-writeup work class) validated 2026-05-04 with 23/23 PASS. Cycle 2 (architecture-revision work class) validated 2026-05-04 with 32/32 PASS. The architecture is now the default for both work classes. A subsequent post on cycle 1 validation is forthcoming in the methodology research arc. The diagnostic and calibration claims above are preserved as-written from the drafting moment; this update note acknowledges what has happened since.*
