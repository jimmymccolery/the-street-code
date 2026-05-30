# 8-10 dev days or Mixed-rating forever

**Author:** Jimmy McColery
**Date:** 2026-05-30
**Status:** SEED STUB — operator-authoring-pending. Pin Paradise accessibility research arc 2026-05-30. Perplexity's review-bomb arithmetic captured the operator-actionable trade-off cleanly.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

The most operator-actionable insight from a 6-stage cross-substrate accessibility research deployment came from Perplexity, and it was arithmetic. *"If you launch to 50 reviews and 5 are motion-sickness complaints, you're at 90%. If reviews plateau at 50, those 5 never get diluted."* The minimum-viable accessibility pass — colorblind palette + UI scaling + reduced-motion toggle + keyboard nav + Steamworks tagging — was estimated at 8-10 focused dev days. **Less than one sprint, against the math of small-audience indie review anchoring.** The expected-value calculation has only one answer.

## The arithmetic

Steam's "Very Positive" rating threshold is ~80% positive reviews. Small-audience indie games frequently plateau at 50-100 reviews total. At that volume, 5-10 negative reviews dominate the rating permanently.

Concrete: launch to 50 reviews, 5 of them cite "game gives me motion sickness" or "tiny text on Deck" or "colorblind-unfriendly HUD." That's 90% positive — already at the Very Positive ceiling, no room for further decay. If reviews never grow past 50, those 5 negatives never get diluted by a larger volume. The rating is anchored at the launch state, plus or minus a small statistical drift, for the entire commercial lifecycle of the title.

Each of those 5 negative reviews represents an accessibility feature the developer could have shipped:
- **Motion-sickness review** → reduced-motion toggle (half a day to ship)
- **Tiny-text review** → font/UI scaling slider (one day)
- **Colorblind-HUD review** → Okabe-Ito palette swap + icon dual-coding (1-2 days)
- **Keyboard-nav review** → focus management + ARIA labels (2-3 days)

Total minimum-viable pass: 8-10 dev days for a solo dev with a React UI. Perplexity's framing: *"less than one sprint."*

## The lessons worth surfacing

**Small-audience review math is asymmetric.** Massive AAA titles dilute negative reviews in a sea of total reviews. Indie titles don't. Five negative reviews of fifty is a permanent commercial cost. Five negative reviews of fifty thousand is a rounding error. The arithmetic of indie review anchoring makes accessibility math operator-actionable in a way that "accessibility is the right thing to do" never quite manages to.

**The negative reviews are systematic, not random.** Motion-sickness players cite motion sickness. Colorblind players cite colorblind issues. Low-vision players cite text legibility. These aren't random complaints — they're the specific accessibility surface that was never built. The review-bomb risk per feature is predictable. Players self-segment in their criticism along the accessibility-gap axes.

**Skipping a half-day fix to lose 5 reviews is bad expected-value reasoning.** Reduced-motion toggle is a CSS media query plus an in-game flag. The implementation is rounding-error scope. The cost of the unshipped feature is potentially 10% of your Steam rating, anchored for the commercial lifecycle. The expected-value calculation has one answer; the framing as "feature work" vs "risk mitigation" sometimes hides the answer behind a planning aesthetic.

**The Steam Deck makes this worse, not better.** Handheld form factor → text on a 7-inch screen → players read closer → smaller text is more punishing. Handheld → potentially-mobile use → vestibular sensitivity elevated → motion-sickness triggers more vocal. The Deck Verified badge doesn't certify any of these axes. The badge is a comfort test on a comfort form factor; the accessibility tags are voluntary; the review impact is real.

**8-10 dev days is the floor, not the ceiling.** The Perplexity estimate is for the minimum-viable pass that earns the highest-ROI store tags + protects against the predictable review-bomb categories. Beat Saber-style per-axis color customization, narrated game menus, full Playable-Without-Vision compliance — those are not in the 8-10 days. They're the post-launch roadmap. The floor is the math; the ceiling is operator-bandwidth.

## Why this matters

Indie accessibility frequently gets framed as either "the right thing to do" (moralized; doesn't drive prioritization) or "premium polish" (delayable; gets cut for ship date). Perplexity's framing is neither. It's risk arithmetic: a specific dollar-amount-equivalent expected-loss against a specific ship-day cost. The dollar-amount-equivalent is the difference between Very Positive and Mixed on a 50-review launch. The ship-day cost is less than one sprint. The trade is operator-trivially-favorable.

If you're shipping a tycoon, a sim, a management game, or anything else with dense data visualization on a 7-inch handheld screen, the 8-10 day pass is the math. The math doesn't care about your design aesthetic, your shader stack, your engine choice, or your team size. It cares about the asymmetry between minimum-viable accessibility cost and the negative-review anchoring risk at small-audience launch.

That's why I ran a 6-stage research arc for an indie tycoon. The arithmetic is unambiguous; the implementation is bounded; the cost of skipping is permanent.
