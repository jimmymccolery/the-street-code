# The span that looked like a link

**Author:** Jimmy McColery
**Date:** 2026-05-28
**Status:** SEED STUB — operator-authoring-pending. Small but generalizable bug class from sueyourkid.com casenotes.html 2026-05-28 evening: pattern divergence between sibling pages where the cleaner-template index page got the implementation wrong. Sibling to Post 44 "Bowler Bug Deep-Dive" in concrete-bug post-mortem register.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

The operator opened a live page on their satirical-legal-journal site and asked the kind of question that doesn't get asked often enough: "Are these 'Read the full digest →' links supposed to work and go somewhere?"

They weren't. The "Read the full digest →" elements on 16 case-entry articles were `<span class="read-more">` tags. They styled like links. They had no `href`. Clicking did nothing.

## The diagnostic arc to narrate

1. **What's there**: 16 case-entry articles on `casenotes.html`. Each has an `<h3><a href="case-X.html">Title</a></h3>` heading link (functional). Each has a `<p class="excerpt">…</p>` description. Each has, immediately after, `<span class="read-more">Read the full digest →</span>` styled to *look* like a link but with no href.
2. **What it should be**: anchor with `href` matching the heading link's destination. Two functional click targets per article (title + read-more), not one functional + one inert.
3. **Where the bug came from**: comparison with the homepage's Case Notes section reveals the pattern divergence. The homepage uses `<a class="read" href="case-X.html">Read full digest →</a>` (functional). The dedicated index page used `<span class="read-more">` (inert). The cleaner-template page got the implementation wrong; the homepage got it right.
4. **The fix**: one-pass Python regex transformation. Extract the `href` from each article's `<h3>` link; rewrite the trailing span as an anchor with that href. 16 spans → 16 anchors. Deterministic; reversible via git revert if anything looked off.

## The lessons worth surfacing

**Pattern divergence between sibling pages is a recurring bug class.** The site has working examples and broken examples of the same UI element. The working examples are visible. The broken examples are visible. Yet the bug persisted because nobody asked the right question until the operator clicked on the wrong page.

**Visual-style affordance and functional affordance diverge silently.** CSS styled the spans to look like links. The text said "Read the full digest →" — the arrow is the universal visual cue for "click for more." Everything about the design language said "click me." Nothing about the implementation backed it up.

**Operator-side observation catches what automated checks miss.** The site passes HTML validation. Link-checker tools wouldn't flag spans-without-hrefs as broken links (they're not links). The bug only surfaces from a human clicking the visual call-to-action and noticing nothing happens. This is the operator-side catch sub-surface that the framework's recovery mechanisms specifically reserve for — when the automated layers can't see the problem, the human has to.

## The meta-lesson on internal linking and AdSense

AdSense's automated review treats user-experience signals as part of the "content value" assessment. Broken visual call-to-action elements degrade the experience even when they don't register as broken links. Fixing 16 inert spans to functional anchors improved the site's internal-linking density and the user-flow continuity *during* the same review window where Tier 1 AdSense remediation was being evaluated. The bug wasn't filed as an AdSense fix; it became one anyway.

## Cross-references

- sueyourkid commit `92bc5bd` (16 spans → 16 anchors transformation; commit message includes the regex pattern + verification gates)
- sueyourkid `casenotes.html` (the page in question; now-functional)
- sueyourkid `index.html` (the page with the correct pattern that revealed the divergence)
- master-setup `research_queue.md` Topic 86 sub-pattern (operator-side catch sub-surface family extends to UI-affordance-vs-implementation divergence catches)
- master-setup `lessons-learned.md` 2026-05-28 evening CC-velocity extension entry (this catch is one of the heterogeneous work-type items)

## Voice notes

Match the concrete-bug post-mortem register of Post 44. The audience is solo-indie developers building content sites who haven't audited their internal-linking affordances since they shipped. Open with the operator's question (the right question; not asked often enough). Walk the diagnostic arc. Surface the three lessons (pattern divergence; visual-vs-functional affordance; operator-side catch). Close with the meta-lesson about how UI bugs that aren't caught by automated tools persist until a human clicks.

Short post; the bug is small. Don't pad. The value is in naming the pattern (cleaner-template-page-got-it-wrong) for operators who have similar bugs in their own sites.
