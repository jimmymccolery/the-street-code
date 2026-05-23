# The Street Code — Post Ideas Queue

**Purpose:** Capture methodology research observations + patterns surfaced during framework operation that warrant potential publication. Each entry includes empirical foundation, leverage rating, and writing-readiness notes.

**Convention:** When an entry becomes ready for drafting, move it (or its drafting workspace) to `drafts/`. When draft is ready for publication, move to `posts/` with sequential numbering per README naming convention.

**Status field values:** `idea` (initial capture) / `drafting` (active writing in `drafts/`) / `published` (in `posts/` with NN-prefix) / `retired` (no longer worth pursuing)

---

## Idea 1 — Rubric Scaffold 4 false-flag pattern: when output-format scaffolding introduces verification regression

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** HIGH (most novel + immediately useful to multi-substrate-audit practitioners)

**Empirical observation:** At Q11 close substrate audit, same Gemini substrate ran twice on identical audit target:
- RUN 1 (Audit Report): sequential prose Hall Monitor format. Zero false-flag claims. Per-dimension grades B / A− / C+ / B− / A. 16 named-anchor citations with specific URLs.
- RUN 2 (Audit Findings): formal Verification Report + Evidence Audit table format per `role_output_schemas.md` v1.3 Rubric Scaffold 4. **3 false-flag catches** (§13 Q9 "wholly absent from literal file attachments" + population scale "unresolved" + Axis G "unbounded") — all 3 literally present in uploaded canonical content per CC literal-state verification. Per-dimension grades B+ / A− / B / B− / A.

**Hypothesis:** Formal verified/unverifiable/contested status field pressures substrate to assign verification verdict WITHOUT genuine literal-file verification, increasing false-negative-existence claim probability. Counterintuitive: structured rubric designed to enforce verification rigor empirically introduces verification regression.

**Empirical foundation:** n=1 at Gemini RUN 2 (Q11 close). Banked at master-setup `lessons-learned.md` Q11 close entry as candidate canonical-artifact refinement observation; architecture-revision-session deliberation territory if n=2+ accumulates at future architectural-lock audits.

**Writing-readiness:** Concrete empirical observation; specific framing; counterintuitive finding. Could write now with explicit "n=1 currently; future deployment validates" framing. Methodology research interest: how structured output rubrics interact with substrate verification discipline.

**Cross-references:** master-setup `lessons-learned.md` Q11 close banking entry at `801752b`; `role_output_schemas.md` v1.3 Rubric Scaffold 4 source; Open Alley `_archive/phase-6-0-session-2-Q11-town-as-sim-audit-response-gemini-run2_2026-05-22.md` (canonical-source-of-verbatim per anti-pattern #10).

---

## Idea 2 — Madisonian rule as substantive discipline: anti-pattern #6 enforcement at cross-substrate audit verdict divergence

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** HIGH (n=2 empirical reproduction; methodology generalizes beyond Open Alley)

**Empirical pattern:** Q14 + Q11 architectural-lock closes BOTH produced maximum-scale cross-substrate verdict divergence (one substrate stricter requiring iteration cycle; one substrate softer ready-to-commit). Operator/orchestrator did NOT majority-vote (which would have produced wrong verdict at Q14 close given 1-strict vs 1-soft = no majority). Instead applied anti-pattern #6 silent-compliance prevention: adopted stricter-substrate reasoning-chain integrity over softer-substrate hand-waving.

**Empirical foundation:** n=2 cumulative architectural-lock close reproduction (Q14 + Q11). Substrate-style-differential candidate empirical foundation n=6 cumulative (Q1+Q2+Q3+Q9+Q14+Q11) underwrites the substrate-default-softer-critique-pattern-at-Grok-side empirical reliability that motivates Madisonian-rule discipline.

**Writing-readiness:** Concrete methodology with reproducible empirical foundation. Useful framing for any multi-substrate audit workflow. Could include canonical anti-pattern #6 reference + concrete worked example from Q11 close adjudication.

**Cross-references:** master-setup `lessons-learned.md` Q14 close banking entry at `0d49d0b` + Q11 close banking entry at `801752b`; `_anti_patterns.canonical.md` v1.8 #6 Madisonian rule canonical lineage; Open Alley `_archive/` Q11 substrate audit response archives demonstrate divergent verdicts.

---

## Idea 3 — Substrate-style-differential pattern at n=6 cumulative: cross-substrate audit reliability in architectural-lock decisions

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** HIGH (substantial empirical foundation; serves as canonical methodology reference)

**Empirical pattern at n=6 cumulative (Q1+Q2+Q3+Q9+Q14+Q11):**
- **Gemini side:** stricter critique calibration + deeper architectural-pattern research extraction (e.g., RimWorld Flyweight Pattern + Cities:Skylines Death Wave + CK3 character culling extracted from named-anchor games)
- **Grok side:** softer critique calibration (verdict-shape regression: maximum-scale verdict divergence with Gemini at Q14 + Q11 close empirically reliable) + shallower architectural-pattern extraction from same named-anchor games BUT unique-coverage value (Songs of Syx + Dwarf Fortress as PL-4 + PL-6 named-anchor precedents at Q11 that Gemini didn't surface)

**Multi-dimensional pattern:** Depth-vs-coverage trade-off. Substrate-style-differential is not "one substrate strictly better"; it's complementary contribution that emerges from cross-substrate audit pattern.

**Writing-readiness:** Substantial empirical foundation enables full methodology post. Could include: when to use cross-substrate vs single-substrate audits; cost-benefit framing; canonical-methodology framing for Council-of-Three architecture.

**Cross-references:** master-setup substrate-style-differential candidate lineage: `76a89c8` (parent) + `3b03c87` + `9670f3c` + `34996f5` + `c8e71d6` + `4e791cb` + Q14 at `0d49d0b` + substrate-deployment-discipline at `1120e83` + Q11 at `801752b`. Existing the-street-code post `06-what-auditing-the-audit-taught-me-about-substrate-routing.md` + `11-what-cross-substrate-audit-surfaced-that-same-substrate-verification-missed.md` are antecedent posts; this would extend with n=6 cumulative + multi-dimensional framing.

---

## Idea 4 — Fix-cycle-surface drift variant: when amendment cycles introduce new drift while attempting drift fixes

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** MEDIUM (n=2 empirical foundation; counterintuitive finding worth surfacing)

**Empirical observation:** Cross-section reference drift discipline pattern operates at 4 workflow surfaces (post-landing + pre-deployment-self-audit + pre-deployment-canonical-verification + fix-cycle-surface). The fix-cycle-surface variant is empirically reproducible at n=2 cumulative:
- Q14 close: orchestrator amended iteration 3 to fix prior drift; amendment introduced new drift (`tycoon_tick_count` substitution for `current_tick` — both equally non-canonical)
- Q11 close: iteration 3 §16.11 framing introduced 2 drift items while fixing prior framing (`schema_version` SemVer assumption + §12 Q3 vs §13 Q9 mandatory-persistence-list location confusion)

**Counterintuitive finding:** Drift-fix attempts themselves drift. Methodology implication: verification gate at amendment-cycle output is load-bearing, not just at original-draft output. CC pre-commit verification catches the fix-cycle-surface variant.

**Empirical foundation:** n=2 cumulative. Banked at master-setup `lessons-learned.md` Q11 close entry as fix-cycle-surface variant reproduction.

**Writing-readiness:** Sufficient empirical foundation. Could include both Q14 + Q11 worked examples + methodology framing about discipline-cycle reproduction at amendment surfaces.

**Cross-references:** master-setup `lessons-learned.md` Q14 close banking entry at `0d49d0b` (fix-cycle-surface variant introduction; `tycoon_tick_count` substitution example) + Q11 close banking entry at `801752b` (n=2 reproduction; schema_version + §12 Q3 vs §13 Q9 examples). Anti-pattern #25b partial-absorption lineage.

---

## Idea 5 — Path C Q-audit-local symbol declaration pattern: scoped canonical-extension at format-flexible scope-limit

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** MEDIUM (n=2 empirical foundation; methodology useful for any canonical-state extension work)

**Empirical pattern:** Pattern for adding scoped symbols to architectural lock content without permanent canonical-lexicon extension. n=2 cumulative reproduction:
- Q14 §15.12: single-symbol sentence-prose format (`current_tick` declared as Q14-local with explicit scope-limit disclaimer + future-Q-audit-adoption-or-extension language)
- Q11 §16.3: multi-symbol pseudocode-block-variant format (3 symbols declared as Q11-local with scope-limit disclaimer + Path C lineage reference)

**Format-flexible at canonical-compliance level:** Both formats valid; canonical-compliance criterion is scope-limit disclaimer + Q-audit-local declaration + future-Q-audit-extension language (NOT specific syntactic format). Functional motivation determines format (single symbol → sentence-prose; multiple coordinated symbols → pseudocode-block).

**Empirical foundation:** n=2 cumulative.

**Writing-readiness:** Sufficient empirical foundation. Could include methodology framing about canonical-state-extension discipline: how to add scoped state without polluting canonical lexicon; format flexibility at scope-limit; downstream Q-audit adoption-or-extension semantics.

**Cross-references:** master-setup `lessons-learned.md` Q14 close banking entry at `0d49d0b` + Q11 close banking entry at `801752b`. Open Alley `tycoon-design.md` §15.12 + §16.3 literal Path C declarations.

---

## Idea 6 — Substrate-deployment phasing + canonical file slicing: operational discipline for substrates with input-size constraints

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** LOWER (operationally useful but more workflow-mechanics than methodology research)

**Empirical pattern:** Practical operational discipline for cross-substrate audits hitting Grok's input limits. Banked at master-setup `lessons-learned.md` at commit `1120e83` (Q14 close follow-up). n=2 cumulative reproduction (Q14 + Q11 both deployed phased Grok prompts):
- **Phased Grok prompt:** Phase 1 (Nerd + Hall Monitor research grounding + 5-dim grading) + Phase 2 (Stoner premortem + Teacher's Pet self-grade + Quarterback synthesis + Dissent Log). Same-chat-thread continuation; Phase 2 references Phase 1 outputs from memory.
- **Q-audit-relevant slice extraction:** master-setup `lessons-learned.md` 634KB → 70-94KB; master-setup `research_queue.md` 445KB → 32-39KB. Slice includes Q-audit-relevant entries only; full canonical file remains at parent path for non-sliced reference.
- **§-content extraction to separate upload file:** Proposed §15/§16 lock content extracted to dedicated `proposed-section-NN-iteration2.md` file rather than embedded inline in prompt body. Reduces prompt body size; substrates read audit-target as canonical-style upload.

**Writing-readiness:** Sufficient empirical foundation. More practical workflow methodology than novel research observation. Could write as practical-operational-discipline post for anyone running cross-substrate audits.

**Cross-references:** master-setup `lessons-learned.md` follow-up banking entry at `1120e83`; Q14 deployment package at `~/Desktop/Q14-audit-upload_2026-05-22/`; Q11 deployment package at `~/Desktop/Q11-audit-upload_2026-05-22/`.

---

## Idea 7 — Intra-substrate-consistency variance at Gemini side: dual-run deployment empirical observation

**Filed:** 2026-05-22 (Q11 close session)
**Status:** idea
**Leverage:** LOWER (n=2 cumulative across Q3 + Q11; novel surface but observationally lighter)

**Empirical observation:** When dual-Gemini-run deployment fires (Q3 multi-alley state architecture audit + Q11 town-as-sim audit), the two RUNs produce DIFFERENT specific findings + DIFFERENT grade distributions but CONVERGE on the same verdict-shape. At Q11 specifically:
- RUN 1: (ii) Adjust + 5 mandatory mods + 16 named-anchor citations + sequential prose format
- RUN 2: (ii) Adjust + 2 explicit mods + 3 false-flag catches + Rubric Scaffold 4 table format

**Implication:** Verdict convergence is reliable signal; specific-finding variance is informational (each RUN contributes different gap-detection). 3-archive substrate response archival convention emerges naturally (2 Gemini + 1 Grok = 3 archives at Q11 close).

**Writing-readiness:** Lighter empirical foundation than n=2-cumulative observations above. Could write as shorter observation post or fold into Substrate-style-differential post (Idea 3).

**Cross-references:** master-setup `lessons-learned.md` Q11 close banking entry at `801752b` + Q3 master-setup precedent (cross-reference in Q11 entry).

---

## Idea 8 — Why the Nine Sigils aesthetic: marketing-aesthetic-for-AI-methodology-frameworks as substrate-style-differential observation

**Filed:** 2026-05-23
**Status:** idea
**Leverage:** MEDIUM (novel framing surface; n=1 empirical observation at Nine Sigils poster filing; methodology research interest at intersection of brand-identity + system-mythos + AI-methodology-discoverability)

**Empirical observation:** Operator authored a vintage pulp-cinema-poster aesthetic promotional image for The Nine Sigils canonical artifact (filed at `brand-assets/the-nine-sigils-poster.jpg` 2026-05-23). Aesthetic register: mythic + culturally-embedded + quasi-religious (James Madison as central figure + 9 symbolic sigils in halo + obelisk-monument + classical Greco-Roman + Gothic cathedral architectural backdrop + Eye-of-Providence iconography + 1930s-40s pulp-poster typography). Deliberately differentiates from generic corporate-flat / startup-minimal / generic-techie AI methodology marketing aesthetics dominant in the broader AI tooling space.

**Hypothesis:** Marketing aesthetic for AI methodology frameworks is itself a substrate-style-differential surface. Generic-techie aesthetic (clean sans-serif + abstract geometric logos + gradient backgrounds + minimal color) reads as commodity tech-tooling discourse + low-mythic-weight. Mythic + culturally-embedded aesthetic (pulp-cinema + classical-architecture + symbolic-sigils + quasi-religious framing register) reads as embodied-methodology-tradition + high-mythic-weight. The aesthetic choice signals operator's claim about what KIND of artifact the framework is: commodity tooling vs cultural artifact vs intellectual tradition.

**Counterintuitive framing:** AI methodology frameworks are typically marketed with techie aesthetic that undersells their actual cultural ambition. The Nine Sigils poster deliberately inverts: high-mythic-weight aesthetic claims framework operates at cultural-artifact register rather than tooling register. Whether that claim is earned is reader-judgment; the aesthetic positioning is the substantive marketing move.

**Methodology research angles to explore:**
- Marketing aesthetic as signaling: what does aesthetic choice claim about framework's intended cultural register?
- Mythic register fit: when does mythic framing serve the framework (matches existing system's quasi-religious framing language: Sigils + Gates + anti-patterns as moral discipline) vs when does it overreach (audience reads as conspiracy-theory-adjacent or pretentious)?
- Cultural awareness tradeoffs: Masonic / Illuminati / Eye-of-Providence visual register carries baggage; operator-aware aesthetic embrace vs accidental association
- Madison-centric composition as Madisonian Gate personification: visual encoding of canonical relationship per anti-pattern #6 silent-compliance prevention canonical lineage
- Cross-tradition iconography (crescent moon, celtic cross, sun symbols) as cross-tradition-discipline framing vs tradition-specific endorsement

**Empirical foundation:** n=1 at Nine Sigils poster filing 2026-05-23. Future brand-asset filings at `brand-assets/` (companion posters for "The Madisonian Gate" + "The SuperGrok Gang" + "Anti-Patterns Canonical" per Nine Sigils poster README companion content candidates list) would extend empirical foundation. Sibling pattern: substrate-style-differential candidate at master-setup `76a89c8` lineage operates at audit-task surface; marketing-aesthetic-for-AI-methodology-frameworks observation may extend the candidate's surface coverage to brand-identity surface.

**Writing-readiness:** Sufficient empirical foundation for initial post. Could include:
- Concrete worked example (Nine Sigils poster as case study; visual composition analysis; canonical relationship encoded visually)
- Contrast with dominant generic-techie aesthetic in AI methodology space
- Aesthetic-as-positioning-claim methodology research framing
- Cultural awareness tradeoffs (mythic register baggage; intentional vs accidental association)
- Forward-looking discipline: brand-asset folder convention + canonical-content cross-reference discipline + companion-content-candidates pattern

**Cross-references:** the-street-code `brand-assets/the-nine-sigils-poster.jpg` + `brand-assets/README.md` (canonical asset annotation; companion content candidates list filed there); master-setup `the_nine_sigils.canonical.md` v1.0 (canonical content the marketing promotes); master-setup `_anti_patterns.canonical.md` v1.8 anti-pattern #6 Madisonian rule canonical lineage (visual relationship Madison-as-central-figure encodes); substrate-style-differential candidate at master-setup `76a89c8` lineage (sibling pattern at audit-task surface).

---

*End of post-ideas queue. Move entries to `drafts/` when active writing begins; move to `posts/` with NN-prefix when ready for publication.*
