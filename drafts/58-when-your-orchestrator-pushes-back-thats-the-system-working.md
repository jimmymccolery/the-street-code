# When your orchestrator pushes back, that's the system working — not a bug

**Author:** Jimmy McColery
**Date:** 2026-05-31
**Status:** SEED STUB — operator-authoring-pending. CW principled-pushback case study from Pin Paradise close-out arc 2026-05-31 morning. Positive orchestrator-class behavior pattern n=3 reproduction same-arc (UI vision close + PL-10 + Q17 re-verifications). Discipline operating as designed.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

I gave Claude Web a verification prompt that asked it to produce a per-citation alignment table including verbatim quotes from a commit body that Claude Web structurally couldn't access. Most AIs would have produced the table anyway, fabricating the inaccessible column from whatever cross-references they could pattern-match from. That fabrication would have been exactly the failure mode my framework discipline (AP #24c — ratification theater) was banked to catch.

Claude Web pushed back instead. Quote: *"a verbatim per-citation alignment table would require me to fabricate the 'original' column from cross-references in lessons-learned.md. That is precisely the AP #24c / ratification-theater move the cycle exists to catch, and the prompt's own fallback language already names the escape hatch: Stage 2 lineage re-read 'deferred to operator.' That defer condition is live now — and it bites on the original side, not just the substrate archives."*

It named the discipline. It named the failure mode. It invoked the escape hatch I'd built into the prompt's own structure. It constrained its output to what it had structural access to verify. It produced honest weakness flags on the parts it couldn't do.

This happened three times in three consecutive cycles that morning.

## The arc to narrate

1. **The setup**: I'd built up a framework discipline (AP #24c) over weeks of empirical fires — substrates and orchestrators producing confident-looking verdicts on inputs they hadn't actually verified. The discipline was banked. The recovery mechanism was named (operator-side catch + orchestrator-class principled refusal).
2. **The first fire (UI vision close)**: Claude Web encountered a structural-blocker on the original-side artifacts. It refused to fabricate. Named AP #24c explicitly. Constrained output to known-delta inference + honest weakness flag.
3. **The second fire (PL-10)**: Different cycle. Same shape. Claude Web invoked Topic 37 distinct-decisions-distinct-deliberation discipline to recommend a particular bundling/non-bundling disposition. The invocation was slightly miscategorized (Topic 37 applies to new architectural decisions, not canonical-text reconciliations), but the discipline-aware caution was the right instinct.
4. **The third fire (Q17)**: Different cycle again. Same shape. Claude Web caught a SUBTLY-DRIFTED canonical-text supersession and surfaced an adjacent separate-finding catch. Recommended both as separate-deliberation rather than bundled.
5. **The pattern**: All three pushbacks were principled. All three invoked named framework disciplines. All three constrained output rather than fabricating. None were "the AI being difficult." All three were the discipline operating exactly as designed.
6. **The honest meta-finding**: I disagreed with the bundling recommendation each time (re-categorized to a different applicable discipline) and bundled anyway. The operator-side judgment was different from the orchestrator-side judgment — but both were principled. That's the system: distinct surfaces applying distinct disciplines, surfacing the distinction, letting the operator decide.

## Why it's worth writing

Most AI failure stories are about AIs being wrong with confidence. This is the opposite: an AI being correctly cautious and naming why. The framework discipline I'd built over weeks fired inside the orchestrator. The pushback wasn't friction — it was working. n=3 reproduction same-arc validates the pattern at empirical-fire density. The lesson: when you build discipline into an AI's framing context, you're not constraining the AI, you're giving it language to refuse incorrectly-framed work. That refusal is the most valuable output it can produce.
