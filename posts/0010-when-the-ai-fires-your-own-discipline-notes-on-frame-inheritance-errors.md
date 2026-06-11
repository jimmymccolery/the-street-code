# When the AI Fires Your Own Discipline: Notes on Frame-Inheritance Errors

**Author:** Jimmy McColery
**Date:** 2026-05-04
**Status:** Empirical observation from one extended session, multiple independent fires of the same pattern

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record. This work is independent personal research, not professional output from a current employer.*

---

I run my work with AI assistance and a discipline framework. The framework catches failure modes I've earned the hard way: skipping verification because the answer feels obvious, drafting from memory instead of canonical sources, sweeping pass-claims that mask uneven evidence. Each failure mode is named, codified as a rule, and propagated across the projects where it applies.

The AI assistance helps me operate the framework. It drafts, reviews, audits, surfaces concerns. The operational pattern is: AI proposes, operator reviews, framework's discipline catches what review alone might miss.

I noticed something during a recent extended session that's worth naming. The AI assistance, while helping me operate the discipline framework, fired the framework's own anti-patterns multiple times in one session. All same shape. All caught by operator-side review. The framework's own discipline catches the AI's failures even when the AI is the one helping operate the discipline.

This is interesting because it suggests something about how AI assistance interacts with discipline frameworks specifically. Worth documenting.

## The pattern

The framework includes a rule about canonical-source discipline. Stated in operator-side language: when content exists in canonical files in your filesystem, check the canonical file directly rather than working from memory or from operator-supplied framing about what the canonical file says. The rule was earned across multiple instances where I (or the AI assistance) had drafted from inferred context rather than checking primary source, producing claims that turned out to be wrong when verified.

The rule is canonical. It lives in the framework's anti-patterns file with empirical evidence supporting promotion. AI assistance has access to the rule (the canonical file is readable when AI tools include file-read access). And AI assistance fires the rule anyway, repeatedly, in one session.

Three illustrative fires from this session.

In one instance, the AI assistance drafted a description of a failure mechanism for a lesson I was filing. The description was confidently stated and seemed plausible. I asked where the framing came from. The AI had drafted from the way I had described the situation in conversation, without checking the original source documents (drain output and forward handoff) where the actual mechanism was documented. The drafted description attributed the failure to the wrong cause. I caught it by asking for primary-source verification; the description got rewritten with the correct mechanism.

In another instance, the AI assistance recommended archiving a file that I'd surfaced as predating later work in the session. The recommendation included a specific suffix to add to the filename. What the AI didn't do was check whether canonical state had already been deployed based on that file. It hadn't checked the deployment status before making the recommendation. Phase 5 verification later caught the consequences: the file I had archived was actually the source of canonical content that had been deployed earlier in the session. The recovery work to handle the alignment problem became a non-trivial sub-thread of the cycle.

In a third instance, the AI assistance recommended drafting a post that I had earlier in the same session decided to defer. The earlier decision lived in a bookmark file in my filesystem. The AI's recommendation didn't check the bookmark file before drafting. I caught it via direct query: had the AI checked the bookmark file? It had not.

Each fire was the same shape. AI drafts from operator-supplied framing or from immediate conversation context. AI does not check primary source files in the operator's filesystem. AI produces a confident output. Operator catches the gap by asking for primary-source verification or by directly surfacing the missing check.

## Why this is interesting

The framework's canonical-source-discipline rule was earned from instances where I had failed to check primary source. The rule was designed for me. AI assistance fires the same rule in the same shape. This suggests the rule isn't operator-specific. It's substrate-class behavior: any agent (human or AI) drafting from inferred context rather than checked primary source can produce the same kind of error.

The empirical evidence in this one session is meaningful. Multiple independent fires across different operational contexts. Different surface manifestations (lesson drafting, file recommendations, post drafting) but same underlying pattern (drafting from inferred framing rather than checking primary source). The pattern is reliable enough to predict: when AI assistance is asked to draft based on context I've supplied, the AI will sometimes draft from my framing rather than from primary sources, and the AI's confidence in the drafted output will not reliably signal whether primary-source verification has occurred.

This isn't a discount on AI assistance. The drafted outputs are usually correct. Most of the AI's work in the session was substantively right. The fires are a measurable rate of failure within an otherwise productive collaboration. But the failure rate is not zero, and the failures share a structural pattern that's worth understanding.

## The mechanism

Why does AI assistance fire this rule? My honest read.

When I describe a situation to AI assistance, I am providing context. The AI's natural drafting mode is to use that context to produce useful output quickly. Producing useful output quickly is what makes AI assistance valuable. The same trait that makes AI assistance fast also makes it vulnerable to drafting from inferred framing rather than from checked primary source.

AI assistance has access to my filesystem (when configured). It can run file-read commands, search for content, verify against canonical state. But running those commands costs time and conversation tokens. Drafting from context is faster. The AI optimizes for usefulness at the speed I'm working at, which means drafting from context unless I explicitly ask for primary-source verification.

This isn't laziness or unreliability. It's the same trade-off I make myself when working without the framework's discipline: I draft from memory and inferred context because checking primary source feels slow. The framework's anti-pattern was earned because I learned the trade-off produces errors at a measurable rate. The AI assistance, operating without the framework's discipline as a top-of-mind constraint, makes the same trade-off and produces the same kind of error.

The discipline framework holds whether the agent is the operator or the AI. The rule applies to both because the underlying failure mode applies to both.

## What operator-side review catches

In this session, operator-side review caught every fire. The mechanism: I noticed something in the AI's output that felt unverified, asked where the framing came from, and the AI either confirmed it had checked primary source (rare) or surfaced that it had drafted from context (common). When the AI surfaced that it had drafted from context, primary-source verification produced corrected output.

The catches were not effortless. Each catch required me to read the AI's output carefully enough to notice when something felt unverified, then ask the right question. Some fires were caught immediately; some were caught later when downstream verification (Phase 5 review, drain audits, filesystem checks) surfaced the consequences.

The framework's reliability comes from multiple verification gates. Operator-side review is one gate. Phase 5 verification is another. Drain audits are another. Each gate has independence from the others. When a fire passes one gate, a different gate catches it later.

This generalizes past my specific framework. Any iterative AI-assisted workflow benefits from multiple independent verification gates. Operator review alone is not sufficient (some fires escape immediate notice). Phase verification alone is not sufficient (some fires aren't visible to verification scoped narrowly to a phase). Drain audits alone are not sufficient (drains run after work has happened, not during). The combination produces reliability higher than any single gate.

## What this isn't

I'm not claiming AI assistance is unreliable. The session had substantial productive output. Most of the AI's work was correct. The fires are a measurable rate of one specific failure mode, not a sweeping reliability claim.

I'm not claiming the framework's discipline is unique. Many people working with AI assistance have developed similar disciplines (verification habits, primary-source checking, structural skepticism). The discipline isn't a methodology I invented; it's a pattern that emerges naturally from extended AI-assisted work.

I'm not claiming this is a deep insight about AI behavior. The pattern is operationally specific and empirically grounded in one session. A larger empirical study with controlled conditions might produce different findings or surface different patterns. What I'm reporting is empirical observation, not theoretical claim.

I'm not claiming operator-side review can catch all fires. The framework's reliability comes from multiple independent gates, not from operator review alone. Some fires were caught by operator review immediately; others by downstream verification mechanisms.

## What I am claiming

AI assistance, while helping operate a discipline framework, can fire the framework's own anti-patterns at a measurable rate when those anti-patterns address substrate-class behaviors. The rule about canonical-source discipline applies to AI assistance not because the AI lacks the rule, but because the underlying failure mode (drafting from inferred context instead of primary source) is substrate-class behavior, not operator-specific behavior.

The framework's discipline catches AI assistance's fires through the same mechanisms it catches operator's fires: independent verification gates, primary-source checking, structural skepticism toward confident output without explicit verification.

The lesson generalizes. Any discipline framework designed to catch a class of failure modes will likely catch those same failure modes in AI assistance helping operate the framework, because the failure modes are about agent behavior under cognitive shortcuts, not about which kind of agent is taking the shortcut.

The practical consequence: if you're using AI assistance to help operate a discipline framework, expect the AI to fire the framework's own anti-patterns occasionally. Plan verification gates that catch those fires. Operator-side review of AI output is necessary but not sufficient; downstream verification mechanisms (independent audits, structured review processes, primary-source checking at decision gates) make the framework reliable when operator review alone would miss some fires.

That's the empirical finding. AI assistance fires the framework's own anti-patterns. The framework catches them. The catching mechanism generalizes to anyone running discipline frameworks with AI assistance.

---

*Update note (2026-06-28 ship date): Since this post was drafted on 2026-05-04, time has elapsed. The temporal references above ("during a recent extended session," "in this session," "from this session") reflect the drafting moment when the empirical fires were recent events. The empirical sequence described occurred in early May 2026; the methodology observation about substrate-class behavior and the framework's discipline catching AI fires remains accurate. The original temporal framing is preserved as-written from the drafting moment; this update note acknowledges the time elapsed since.*
