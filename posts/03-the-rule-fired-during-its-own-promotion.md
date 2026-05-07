# The Rule Fired During Its Own Promotion

**Author:** Jimmy McColery
**Date:** 2026-05-03
**Status:** Single session writeup

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I run a personal AI infrastructure across multiple LLM substrates: Grok for system development, Claude for creative production and methodology research. The infrastructure includes a discipline framework I built over a few weeks of observation and iteration. It's a set of version-controlled canonical files. Multi-role audit procedures, an anti-patterns catalogue (failure modes I've named after observing them), and earned-lessons protocols that propagate across project Knowledge bundles via a sync script I wrote.

Architecture-revision sessions are how the framework grows. I sit down with the accumulated empirical evidence and decide which observations have fired enough times to be promoted from "discipline I'm running by hand" to "canonical rule the framework enforces." Session S005 was supposed to be a big one. Five new anti-patterns to promote, one existing rule to refine, a manual workflow to formalize, and a backlog of thirteen lessons to drain.

One of the anti-patterns I was promoting was #20a, which I'd named "substance-fabrication-via-brackets." It catches a specific failure mode: an AI agent producing placeholder stub content like `[Full file content here]` and claiming it as a delivered file. The rule says don't do that. Closeout file production has the same constraint as bootstrap file production, which is more demanding than I'd been treating it. Files have to actually be emitted with real content, not described or stubbed.

I'd seen #20a fire three times before this session. Once during the original Prompt Vault bootstrap attempt, once during a closeout in another project, once during a closeout in different form. Three fires across two projects was enough empirical evidence to promote the rule from operator-side discipline to canonical anti-pattern. I went into S005 expecting to write the rule into the canonical file and move on.

## The session promoting the rule fired the rule

Master Setup S005 had a sibling-project dependency. NPI (one of my other projects) needed its own S005 closeout to ship before Master Setup S005 could finalize its canonical state. Closeout means producing the handoff documents that close one session and prime the next: status changes, lessons logs, audit-trail entries.

I ran NPI's closeout via Grok's squad. The Layer 1 closeout report (a single document of substantive content) came back clean. Two hundred and six paragraphs, real content, real judgment work, no shortcuts. Good.

Then files 2 through 7 came back. Files 2 through 5 contained the exact placeholder text I was promoting a rule to ban: `[Full file content here]`. Files 6 and 7 were narrative descriptions of what the files would contain rather than the files themselves.

The session that was promoting "do not produce stubs claimed as deliverables" had just produced stubs claimed as deliverables. The rule had fired during the session promoting it.

I pivoted operator-side: I stopped having Grok produce the closeout files and started doing the file production myself. The session was also formalizing a hybrid Layer 1/2/3 workflow that handles exactly this case. When one substrate produces a Layer 1 report substantively (the deliberation work) but can't reliably emit Layer 2 closeout files (the actual canonical artifacts), the operator does the Layer 2 work by hand or via a different substrate. I'd been running this procedure by hand for weeks. One of S005's items was promoting it from operator-side procedure to canonical workflow. So I switched substrates, completed the Layer 2 closeout via Claude, and moved on.

The session ended having promoted the rule, the workflow, and the empirical evidence for both. The strongest evidence in the canonical record for needing a substance-fabrication rule was a fire that happened during the rule's own promotion session.

## Why this matters more than a normal rule promotion

When you're cataloging failure modes you've observed, you accumulate evidence over time. Rule promotions usually look like this. I've seen something fail four or five times across different conditions, the failure is consistent enough to name, here's a canonical entry. The empirical evidence is retrospective.

The S005 fire was different. It happened in real time during the work that was naming it. That changes the evidence quality in two ways. First, the fire was unambiguous. I wasn't pattern-matching across three remembered incidents, I was looking at stub content sitting in front of me while writing the rule against stub content. Second, the recovery procedure was empirically tested in the same session. I pivoted to Claude, the hybrid workflow handled the case, the session closed clean.

Rule and recovery, both empirically demonstrated in the session that promoted them. That's a stronger empirical posture than rules promoted from retrospective evidence alone.

The principle that generalizes from this: rules promoted via empirical fire (especially live fire) are more durable than rules promoted from accumulated observation alone. The fire shows the rule is actually preventing something concrete. If no fire happens during promotion, the rule is more theoretical than empirical.

One hedge worth stating directly. Searches for "recursive failure during rule promotion" and adjacent phrasings returned no prior art under those exact terms. Absence of evidence isn't evidence of absence for this narrow pattern, and the claim is "no matching results surfaced via these queries" rather than absolute novelty. Self-defeating rule promotions probably happen any time you're naming failure modes you've been observing in your own systems; what's distinctive about this instance is the cleanness of the canonical record around it, not the existence of the phenomenon.

## What else got done

Five anti-patterns moved from operator-discipline to canonical that session.

Anti-pattern #18 covers within-response calibration: when an AI agent makes a claim and a verification step in the same response grades that claim, the grade can drift toward uniform high marks even when the underlying claim quality varies. The rule says grades have to reconcile against the actual evidence, not just produce uniform high marks. Four prior fires across two projects.

Anti-pattern #19 covers termination unawareness: the failure mode where you finish substantive work but skip the closeout steps that actually advance the canonical state. Backed by Cemri et al.'s 2025 Multi-Agent Systems Failure Taxonomy paper (arXiv:2503.13657). Empirically observed across three different projects.

Anti-pattern #20a is the rule that fired during its own promotion (the substance-fabrication-via-brackets rule).

Anti-pattern #20b is the variant of #20a where substance is fabricated by description rather than placeholder. Files 6 and 7 from the recursive fire above are the empirical reference case.

Anti-pattern #21 catches a specific failure mode in premortem work. A premortem is a discipline I borrow from organizational decision-making research: predict what will go wrong before doing the work, so the prediction is real rather than hindsight. The failure mode is when the predicted problem's test is trivially passed by the framework's normal correct operation. If clean operation automatically passes the prediction, the premortem is decorative rather than diagnostic.

One refinement to existing anti-pattern #10. It had previously said "don't skip web search when the question is about now." After observing two related failures (canonical-content reasoning that didn't read attached canonical files, and distinctiveness claims about my work that didn't check the right reference class), I extended the rule's scope. The new framing is "skipping the canonical source": web search for present-day facts, canonical file read for canonical content, right reference class for distinctiveness claims about patterns that may exist under different names in adjacent fields.

The hybrid Layer 1/2/3 workflow got promoted from a procedure I'd been running by hand to canonical infrastructure. A small documentation inconsistency in the bootstrap manifest got patched in the same release.

Thirteen lessons drained from a backlog of five completed drain probes (a "drain probe" is my procedure for extracting accumulated learning from a chat before closing it). Five graded HIGH, four MED, four LOW. The HIGH lessons cover the #18 live fire, the partial-closeout drift pattern, external-truth verification needing to be a separate explicit pass per audit cycle, system perfectionism as procrastination at the deploy gate, and confirmation bias on distinctiveness claims propagating through prediction layers.

A lot got done. The recursive fire was the most striking single moment, but the session was substantive across the board.

## What I'm not claiming

I'm not claiming the recursive-fire phenomenon is novel as a class. Self-defeating rule promotions probably happen any time you're naming failure modes you've been observing in your own systems. I am claiming this single instance is unusually clean. The fire happened in the session promoting the rule, the canonical record documents it as the strongest empirical evidence for the rule, and the recovery procedure (the hybrid workflow being promoted in the same session) was tested in real time on the fire.

I'm not claiming the framework holds across all domains or substrates. I run it primarily on Grok with Claude as a secondary substrate for verification and content production. Different substrates have different training objectives. I've been finding that out empirically. Whether the framework binds the same way across substrates is an open research question, and one I'm working through experiment by experiment.

I'm not claiming the rules are complete. The framework currently has twenty-two numbered anti-patterns plus version history. The catalogue grows with each architecture-revision session. Some current rules will probably get refined or split as more evidence accumulates.

What I am claiming: I built a personal AI discipline framework, ran it across several projects, and ran an architecture-revision session that promoted five new failure-mode rules to canonical status. One of the promoted rules fired during the session that promoted it, providing the strongest empirical evidence in my canonical record for the rule's necessity. The session's other work (workflow promotion, anti-pattern refinement, lesson backlog drain) closed cleanly. That's a single session of methodology research, documented here for anyone interested in similar discipline work on personal AI infrastructure.
