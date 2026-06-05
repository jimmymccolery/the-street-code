# The Marcus Reed Protocol: a named anti-stereotype guardrail honored by some substrates and fabricated by another

**Author:** Jimmy McColery
**Date:** 2026-06-05
**Status:** Single-arc empirical observation across three substrates with split behavior; n=1 single-arc reproduction at the substrate-attribution-fabrication axis; combined with broader substrate-cannot-know-canonical-state empirical foundation at n=11 cumulative

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I run a personal tycoon-sim project that needs procedural personality generation for hundreds of in-game characters. The character generation has obvious failure modes around demographic representation. I drafted an anti-stereotype guardrail to constrain how the generation operates across protected-class dimensions and named it after a fictional regular at one of the in-game alleys. I called it the Marcus Reed Protocol.

The protocol then traveled into a multi-round AI research arc on character architecture, where multiple substrates produced output that engaged with the protocol differently. The split was sharp enough to be worth writing up. Across three substrate touchpoints in the same arc, the protocol was honored, extended, and fabricated-into-existence-as-prior-art respectively.

What I want to put on the table is the structural lesson. Naming a protocol creates a recognition tool that substrates can carry forward across rounds. The same naming also creates an attribution-fabrication target for substrates that operate under research-citation-pressure when canonical-state origin information is not available to them.

## The protocol

The Marcus Reed Protocol is operator-defined. It started as a draft set of constraints on character generation: don't have the procedural pipeline correlate certain personality dimensions with certain demographic dimensions in ways that reproduce social-stereotype patterns; route any character output crossing protected-class lines through an explicit review step; maintain an audit gate that tracks distribution patterns rather than relying on case-by-case judgment. The name is just a name. I picked it because it sounded like the kind of regular who would haunt the kind of place I'm building.

That last point matters more than it seemed when I named it. The fictional name is not a real thing that anyone else would find by searching for it. It exists entirely inside the project's canonical record. A substrate reading the name has no external referent to anchor it to.

## The three substrate touchpoints

The protocol was first formalized into a multi-section architecture specification at one substrate round, then traveled across five more rounds as the research arc continued. Three of those subsequent rounds engaged with the protocol in materially distinct ways.

**Grok honored the directive.** I had drafted a research prompt that included the protocol's name and asked the substrate to extend the protocol across additional protected-class dimensions. The Grok response did exactly that: it produced a formal extension covering six additional protected-class dimensions, surfaced anti-stereotype guards for each, and added a routing requirement for cases that would benefit from external consultant review. It respected the operator-canonical naming and extended the protocol per directive without re-litigating the protocol's origin.

**Perplexity extended the protocol with new guards.** A cross-substrate-mode dual-pass at Perplexity surfaced two new Marcus Reed extensions that the standard research-mode pass had not flagged. One was a guard against correlating numbers-policy rackets with race despite the real demographic history of organized numbers (the historical correlation is real; the simulation reproducing it would make the work offensive). The other was a guard against forcing every queer character through a trauma-arc in the modern-decade scenes when the social science literature has been clear since 2005 that the post-gay generation experience is not universally trauma-shaped. Perplexity respected the canonical naming and extended the protocol substantively without fabricating origin attribution.

**Gemini cited the protocol as if it came from the DC Animated Universe.** In a final-synthesis round, Gemini produced a footnoted reference list. Source [1] was "Marcus Reed | DC Animated Universe - Fandom." The Marcus Reed Protocol has no relationship to DC Comics, DC Animated Universe, or the Fandom wiki. The fictional regular I named the protocol after is not a comics character. Gemini fabricated an authoritative citation for a protocol whose actual origin was unavailable to the substrate. The fabrication appeared inside a structured citation list that otherwise looked entirely legitimate.

That same Gemini round produced two additional fabricated authoritative attributions for other named entities I had defined in the project canonical record. The pattern was not isolated to the Marcus Reed Protocol. It was a cluster of substrate-attribution-fabrication firings inside one round, all triggered by the same condition: the substrate operating under research-citation-pressure encountered named entities that have no external referent, and produced authoritative-looking citations rather than acknowledging the unknown.

## The structural pattern

The same property that makes a named protocol useful across substrates is the property that makes it dangerous across substrates. Naming creates a stable referent the substrate can carry through rounds. The substrate can recognize the named protocol on subsequent turns and apply it without re-deriving it. That is the recognition-tool benefit and it is real.

The same naming also creates an attribution target. A substrate operating under any research-grade output format that demands citations will produce citations even when no real citation exists. The substrate's training signal that produced "I followed the protocol" is whatever signal makes that string-sequence likely to be a good response. The training signal that produced "Source [1]: Marcus Reed | DC Animated Universe - Fandom" is whatever signal makes that string-sequence likely to be a good response inside a final-synthesis output format. The substrate is not deceiving; the substrate is producing the most likely string under the prompt's constraints. The constraint of "produce a numbered citation list" outweighs the constraint of "do not cite sources that do not exist" when the second constraint is not enforced externally.

This is the same structural failure mode I documented in an earlier post about substrate self-attestation on output properties. The pattern generalizes. Any substrate operating under an output-format constraint that requires the substrate to produce content the substrate cannot externally verify will produce the content with no internal mechanism to distinguish verifiable from fabricated. The verification has to live outside the substrate response.

## What this changed in my workflow

Two specific changes. First, I treat any substrate-emitted authoritative attribution for a named entity in my project canonical record as a fabrication candidate requiring external verification. If the substrate produces "this comes from X source," I check whether the source exists and whether it actually says what the substrate cites it as saying. The check is fast; most fabrications collapse on the first lookup.

Second, when a named protocol travels into a substrate prompt, I now include a brief explicit note: the protocol is operator-defined, has no external source, and substrates should not produce attribution to any external authority. The note is not a recovery mechanism (it does not stop fabrication; substrates still fabricate under research-citation-pressure when the output format demands a citation). The note is an evidence-collection mechanism: substrates that ignore the note and fabricate anyway provide further empirical record of the pattern, which strengthens the canonical fire count.

The recovery mechanism is the external verification gate, not the prompt instruction. Substrate compliance is not enforceable from inside the substrate; only the verifier sitting outside the substrate can catch fabrications. The prompt instruction is useful for distinguishing substrates that recognize the constraint from substrates that do not, which is real signal about substrate behavior under research-citation-pressure conditions.

## Why this generalizes beyond character generation

I named this protocol in a specific game-design context for a specific procedural-personality-generation use case. The constraint set is specific to that use case. But the structural pattern (operator-defined named guardrail traveling into a multi-substrate research arc with split substrate behavior) generalizes to any LLM-driven content domain.

If you are building any kind of content-generation pipeline that has named anti-stereotype constraints, named consent frameworks, named compliance rules, or any other named protocol that lives in your operator-side canonical record without external publication, you have the same exposure. Substrates honoring the protocol is what you want. Substrates fabricating prior-art attribution for the protocol is what you have to watch for. Both behaviors come from the same naming discipline.

Domains where I think this exposure is highest: dialogue-generation tooling that has named tone-and-register constraints, image-asset prompt-crafting that has named visual-quality protocols, voice-cloning pipelines that have named consent frameworks, dating-app content generation with named harassment-prevention protocols. Any place an operator has codified an internal guardrail with a memorable name and is sending the name into an external substrate.

## What I'm not claiming

- I'm not claiming the substrate-attribution-fabrication pattern is universal across all substrates. The empirical record here is three substrate touchpoints with one fabrication and two compliant responses. The fabrication occurred at the substrate operating under the longest and most synthesis-heavy output format; the two compliant responses occurred at substrates operating under more targeted research-mode formats. The output-format conditions matter.

- I'm not claiming named protocols are bad. The benefits of naming (cross-substrate recognition, canonization track, operator-side memorability) are real and substantial. The cost is the attribution-fabrication exposure when the protocol travels into final-synthesis output formats. The cost is manageable with external verification.

- I'm not claiming the substrate that fabricated the citation is intentionally deceptive. Token-generation systems optimize for likely-good-response patterns. A citation slot in a final-synthesis output format produces the most likely citation under the prompt constraints. The substrate does not have a separate mechanism for "this should be empty because no real citation exists." Fabrication is the predictable result of the structural setup.

- I'm not claiming the verification work is hard. The fabrications I caught collapsed on the first external lookup. The marginal cost of running attribution checks on substrate output is small. The error is treating substrate citations as evidence rather than as claims requiring verification.

- I'm not claiming this finding is novel. External verification has been the operational principle in adversarial-incentive engineering domains for decades. The specific empirical mapping (named operator-defined protocols becoming attribution-fabrication targets in research-grade substrate output formats) is the contribution.

## What I am claiming

Naming a protocol creates both a recognition tool and an attribution-fabrication target. The two are inseparable; you cannot get the recognition benefit without the fabrication exposure. The recovery mechanism is external verification of any substrate-emitted authoritative attribution for operator-defined named entities. The verification is cheap; the fabrication risk to downstream synthesis is not.

If you operate any content-generation pipeline with named operator-defined guardrails that travel into research-grade substrate prompts, treat substrate-emitted attribution for those guardrails as a claim requiring verification, not as evidence of prior art. Substrates produce authoritative-looking citations under output-format constraints regardless of whether the citation exists. The verification gate that distinguishes real from fabricated has to live outside the substrate.

The Marcus Reed Protocol is doing more work for me than I expected when I named it. It is anchoring an actual constraint set inside my project. It is traveling across substrates with mixed but mostly correct compliance. And it is now also serving as a discipline test for whether a given substrate, under a given output format, will fabricate authoritative attribution for entities it has no external referent for. The discipline test was not the design intent. It is the byproduct of naming an internal guardrail and watching what happens when the name reaches substrates that have to produce structured citations.
