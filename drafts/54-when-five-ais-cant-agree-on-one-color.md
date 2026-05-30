# When five AIs can't agree on one color

**Author:** Jimmy McColery
**Date:** 2026-05-30
**Status:** SEED STUB — operator-authoring-pending. Pin Paradise accessibility cross-substrate disagreement on Okabe-Ito palette-to-axis mapping. 5-of-5 substrate-disagreement; 2 limited coincidences across 25 cells.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## The seed: what to write about

I have 5 soul-axes that need colors. The Okabe-Ito colorblind-safe palette has 8 colors. Hundreds of valid mappings exist. I asked 4 different AI substrates plus an orchestrator-class for a recommendation. I got 5 different mappings. 3 of the 5 axes received fully distinct color assignments across all 5 sources. The only 2 coincidences were a single hex value matching for 2 axes between 2 specific pairs of substrates.

## The data

The 5 axes: Authenticity + Vibe/Nostalgia + Community + Operations + Customer Satisfaction. The 5 substrate outputs:

| Soul Axis | Gemini Deep | Perplexity | CW computed | Gemini Pro Extended |
|-----------|-------------|------------|-------------|---------------------|
| Authenticity | Vermillion | Blue | **Amber #E69F00** | **Orange #E69F00** ← match |
| Vibe/Nostalgia | Reddish Purple | Orange | Slate | Sky Blue |
| Community | Sky Blue | Bluish Green | Teal | Vermillion |
| Operations | Orange | Vermillion | Blue | Bluish Green |
| Customer Sat | Bluish Green | **Reddish Purple #CC79A7** | Yellow | **Reddish Purple #CC79A7** ← match |

That's it. Two cells out of twenty.

## The lessons worth surfacing

**Substrate consensus is a coverage illusion.** When 3 of 5 sources call something "the obvious choice," I tend to trust it. The Okabe-Ito palette is "the obvious starting point" because it's the scientifically-engineered colorblind-safe palette every accessibility primer cites. So 5 sources agreed on the palette. But mapping 5 axes to 5 of 8 colors is a thematic + perceptual + emotional + brand decision — and on that decision, there is no substrate consensus. Each substrate generated a plausible mapping; no two converged.

**Computed evidence beats thematic assertion.** Only one of the 5 sources actually ran the CVD math. CW's mapping was produced by Machado-matrix CVD transforms in linearRGB color-interpolation domain + CIEDE2000 perceptual distance + brute-force optimizer over hue + lightness candidates. It guarantees a minimum ΔE of 10.7 across normal vision + deuteranopia + protanopia + tritanopia + grayscale. The other 4 mappings asserted "this is colorblind-safe" without computation. Two of those 4 used ΔE values that were estimates, not computations — one source explicitly self-disclosed it couldn't execute the matrix math, then gave estimated numbers anyway.

**The computed mapping has its own weakness, honestly flagged.** CW's optimizer pushed Vibe/Nostalgia to a slate gray (#495057) as the grayscale lightness-anchor — the one color that gives the palette its monochromacy safety. Slate is thematically weak for a "vibe and nostalgia" axis. The optimizer doesn't know about thematics; it knows about ΔE. The honest disclosure of the trade-off is more valuable than any of the 4 thematic mappings that hid the trade-off behind un-justified assertion.

**No five-hue palette survives grayscale on color alone.** The killer finding from the computed math. Grayscale collapses everything to lightness; you can't separate 5 categories by lightness alone without pushing some near-black and some near-white, which wrecks a HUD. So secondary encoding (icons + text + letter grades) is mandatory, not a nicety. This isn't a palette failure; it's an information-theoretic limit. The mapping disagreement above is partly a distraction — the real V1 decision is making sure color is never the sole channel.

**Five distinct expert opinions ≠ five wrong answers.** Each mapping is internally defensible. Each is colorblind-safe at the dichromacy level (the standard tests). The decision isn't "find the right one"; it's "the substrate consensus doesn't exist, so this is operator-judgment territory, and I need to make the call." Treating substrate-disagreement as a flag for delegation back to the operator is more useful than treating it as a sign of substrate failure.

## Why this matters

When AI consensus exists, lean into it. When AI consensus doesn't exist, the absence is itself a signal: this decision lives outside what cross-substrate triangulation can resolve. Brand-color decisions, thematic mappings, operator-aesthetic — these are not things the substrates can vote on. Five different mappings doesn't mean the substrates are bad. It means the question doesn't have a substrate-resolvable answer.

The next time I see five experts give me four different answers, I'll stop hoping for the fifth to break the tie. That's not how this works.
