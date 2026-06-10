# Drafting brief — Post 81 "Cite the Process Theory Not the Principle"

**Status:** Brief only; not yet drafted. Per CW R6 Tier 5 item 19.
**Target slot:** Post 81 (lead philosophical post; T-4 months to ship).
**Scope verdict (per closure memo):** SAFE — pure methodology + public-domain academic philosophy (Friston / Colombo & Wright). No Memory Lanes protected scope.

## Thesis

The Free Energy Principle (FEP) has been criticized as untestable metaphysics. The Friston 2017 active-inference paper itself disclaims the principle's prescriptive force in §4.4 and §5. The framework Modified-C-bis adopts cites the process theory — the mathematical machinery of POMDP active inference — and explicitly does not adopt the principle's metaphysical commitments. This sidesteps the Colombo & Wright 2021 falsifiability critique by accepting its premise (the FEP-as-principle is not falsifiable) and routing around it (the process theory IS empirically tractable).

## Key citations (all locked at `architecture/modified-c-bis-canonical-citations-2026-06-09.md`)

- **Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017).** Active inference: A process theory. ***Neural Computation*** 29(1):1-49. doi:10.1162/NECO_a_00912. §4.4 + §5 metatheoretical disclaimer; Appendix F naive/sophisticated distinction.
- **Colombo, M., & Wright, C. (2021).** First principles in the life sciences: the free-energy principle, organicism, and mechanism. ***Synthese*** 198 (Suppl 14):3463-3488. §4.1 (preprint p.28) concedes FEP "defines a class of process models."
- **Bowers, J. S., & Davis, C. J. (2012).** Bayesian just-so stories in psychology and neuroscience. ***Psychological Bulletin*** 138(3):389-414. Falsifiability criterion citation.
- **Williams, D. (2021).** Predictive coding and thought. ***Philosophical Studies*** 179:1693-1714. Most precise recent FEP critique; cite for reviewer-anticipation.

## Structural outline

1. **Hook:** The recurring objection to using Friston's framework for NPC design is that the FEP is metaphysics, not science. State the objection cleanly. Don't strawman it.
2. **The objection's accurate part:** Colombo & Wright are right that the FEP-as-principle has the structural shape of a metaphysical claim. Quote §4.1 directly. Acknowledge the critics' point.
3. **The 2017 paper's own disclaimer:** §4.4 + §5 disclaim the principle's prescriptive force. Friston himself separates the principle from the process theory. Quote.
4. **The move that exits the critique:** Modified-C-bis cites the PROCESS THEORY (the POMDP mathematical machinery) not the FEP-as-principle. The process theory has empirical traction; the principle does not need to.
5. **What this costs:** The framework gives up the metaphysical-foundation claim. It gains operational testability. The trade is worth it for procedural-generation design where you need running code, not a theory-of-everything.
6. **What I am claiming + what I am not claiming.**

## Voice spec adherence

- Zero em-dash characters (— character). Use periods, semicolons, parentheses, colons.
- No emojis.
- "What I am not claiming" + "What I am claiming" both as H2 headers (per the operator's catch on Posts 71-80 sections being too short; expand each to ~313+ words per older-post density target).
- First-person reflective stance. The post is methodology, not academic argument — it documents the operator's framework decision rather than arguing for it as philosophy.

## Disclosure-discipline notes

- No cross-cultural framing in this post. Pure philosophy-of-science methodology.
- No Memory Lanes protected-scope references — talk about NPC design in directional terms only.
- Mention the framework's existence (Modified-C-bis) without enumerating all six modifications. The full framework lives in the architecture/ folder; this post discusses one move.

## Drafting prerequisites

- Modified-C-bis ratification complete (DONE).
- Canonical citations document complete (DONE).
- Terminology discipline document complete (DONE). Use "present-state-anchored active inference" if mentioning V1 mechanism.

## Estimated word count

~3,500-4,500 words (matches Post 71-80 density target post-catch).

## Drafting session notes

- This is the lead philosophical post. Read the Friston 2017 page bank in `project_friston_2017_primary_source_ingested_2026-06-09.md` before drafting.
- Use the §4.4 + §5 + Appendix F page citations directly from the primary source.
- Quote Colombo & Wright §4.1 verbatim (preprint p.28) — the concession is the load-bearing element of the post.
- This post explicitly does NOT discuss Wiredu, PersonaWeaver, or the cryptographic puzzle. Save those for Posts 83-85. Post 81's scope is the process-theory-vs-principle move only.
