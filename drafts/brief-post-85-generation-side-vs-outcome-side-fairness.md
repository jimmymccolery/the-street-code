# Drafting brief — Post 85 "Generation-Side vs Outcome-Side Fairness"

**Status:** Brief only; not yet drafted. Per CW R6 Tier 5 item 19.
**Target slot:** Post 85 (PersonaWeaver / Marcus Reed Protocol layers).
**Scope verdict (per closure memo):** SAFE if Marcus Reed described generically as "outcome-distribution audit" without naming Surface 8 enumeration or §39 specifics. Protected-scope strict.

## Round 7 framing note

PersonaWeaver paper framing is character expressiveness + dramatic tension addressing assistant alignment biases — NOT a fairness safeguard or bias-mitigation safety mechanism. The words "fairness" and "marginalized" do NOT appear in the paper. PersonaWeaver operates at the GENERATION/EXPRESSIVENESS layer; the outcome-distribution audit operates at the POST-GENERATION DISTRIBUTION layer; they are independent interventions at different layers, NOT two halves of one intervention. Citation chain must match `~/Projects/the-street-code/research/citations/modified-c-bis-canonical-citations.md` Modification 3 anchor section.

## Thesis

Fairness in procedural-character generation operates at two distinct layers that are often conflated. PersonaWeaver (Qraitem, Saenko, Plummer 2026) addresses GENERATION-SIDE bias by disentangling world-building from behavioral-building — producing characters with dramatic tension and behavioral diversity. The paper makes no fairness claim; the words "fairness" and "marginalized" do not appear in it. The Marcus Reed Protocol is an OPERATOR-NOVEL OUTCOME-SIDE intervention: a post-generation distribution audit that checks whether the population the system actually produces meets fairness criteria. The two interventions operate at different layers, and conflating them weakens both.

## Key citations (all locked at `architecture/modified-c-bis-canonical-citations-2026-06-09.md`)

- **Qraitem, M., Saenko, K., & Plummer, B. A. (2026).** Breaking the Assistant Mold: Modeling Behavioral Variation in LLM Based Procedural Character Generation. **arXiv:2601.03396** (v3 4 May 2026). Cite as arXiv until FAccT 2026 status verifiable post-28-June.
- **Mökander, J., Schuett, J., Kirk, H. R., & Floridi, L. (2024).** Auditing large language models: a three-layered approach. ***AI and Ethics*** 4:1085-1115. doi:10.1007/s43681-023-00289-2. CANONICAL three-layer audit framework anchor.
- **Sheng, E., Chang, K.-W., Natarajan, P., & Peng, N. (2019).** The Woman Worked as a Babysitter. ***EMNLP-IJCNLP 2019***, pp. 3407-3412. Regard-metric origin; cite with vintage caveat.
- **BiAxisAudit:** Gan, R., Dong, K., & Li, Q. (2026). arXiv:2605.09041. UNREVIEWED PREPRINT — cite with preprint-status caveat.

## Structural outline

1. **Hook:** "When PersonaWeaver got cited in my framework as a fairness safeguard, I started to wonder whether the paper actually claimed that. I went to read it."
2. **The PersonaWeaver framing as actually written.** The paper addresses positive moral bias and helpful-assistant bias — assistant-alignment biases that suppress dramatic tension. The disentanglement architecture is a character-expressiveness intervention. Read directly: the words "fairness" and "marginalized" do not appear in the paper. The framing is dramatic tension and behavioral diversity.
3. **The misframing surface.** When upstream substrate research framed PersonaWeaver as a fairness safeguard, it imported a claim the paper does not make. The correction (caught by current-arc Perplexity DR R2 + triply confirmed by Opus R4 primary-text read) is the kind of cross-substrate adjudication that resolves attribution drift before it ratifies into the framework.
4. **The two-layer distinction.** Generation-side fairness would be: producing characters whose distributional properties are inherently bias-free. Outcome-side fairness is: auditing the population the system actually produces and intervening at the distribution level. PersonaWeaver is GENERATION-SIDE in scope (and expressiveness, not fairness, in objective). The Marcus Reed Protocol is OUTCOME-SIDE.
5. **What Mökander 2024 grounds.** The three-layered audit framework — governance + model + application — situates outcome-side audits at the application layer. The Marcus Reed Protocol is positioned at that layer.
6. **The Marcus Reed Protocol described generically.** Outcome-distribution audit. Demographic parity of positive regard outcome across groups, with era-constraint disclosure. Multi-prompt OAT design to disentangle prompt effects from model effects (BiAxisAudit-informed). Do NOT name the 8-surface implementation; describe at the META-rule level only.
7. **Why the relational claim matters.** PersonaWeaver and Marcus Reed are independent interventions at different layers, NOT "complementary at the same layer." Calling them complementary imports a unified-fairness-pipeline framing that neither paper actually makes. The framework adopts both interventions but does not collapse them.
8. **What I am not claiming + what I am claiming.**

## Voice spec adherence

- Zero em-dash characters. No emojis.
- "What I am not claiming" + "What I am claiming" H2; ~313+ words each.
- The phrase "operator-novel" should be used carefully — assert it for the Marcus Reed Protocol specifically; acknowledge the lineage anchors (Mökander, Sheng, BiAxisAudit).

## Disclosure-discipline notes

- Marcus Reed Protocol described at META-RULE LEVEL ONLY ("named anti-stereotype guardrail," "outcome-distribution audit"). PROTECTED: 8-surface implementation, gate-engine specifics, demographic-coding policy, mitigation framework.
- PersonaWeaver discussion is fully public-domain academic content; no protection issues there.
- All preprint citations carry explicit preprint-status caveat (PersonaWeaver + BiAxisAudit).
- Add the current-bias-metric companion citation alongside Sheng 2019 (vintage caveat).

## Drafting prerequisites

- Modified-C-bis ratification complete (DONE) — Modification 3 reworded language is the load-bearing relational claim.
- Canonical citations document complete (DONE).
- **MANDATORY before drafting:** Re-read modification 3 final wording in `architecture/modified-c-bis-ratification-2026-06-09.md`.
- **RECOMMENDED before drafting:** Read Mökander 2024 in full (operator-side pre-publication reading queue).

## Estimated word count

~3,500-4,500 words.

## Drafting session notes

- This post is the conceptual foundation for the MRP FAccT 2027 paper. Drafting it well makes the paper drafting easier.
- The narrative beat that earns the post is the "I went to read the paper and the framing wasn't what the research had assumed" moment — it makes the post about the methodology of catching misframings, not just about fairness theory.
- DO NOT mention specific protected-scope architecture elements (Marcus Reed META-ARCH 8-surface gate; Surface 8 civil rights consultant review; specific NPC roster). These are protected scope.
- After publication, this post pairs naturally with the next published post (Post 70 already discussed Marcus Reed Protocol at the named-guardrail level; Post 85 deepens by adding the PersonaWeaver layer distinction).
