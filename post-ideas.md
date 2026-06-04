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

## Idea 9 — Canonical-anchor validation arc as methodology: backward-literature + present-measurement + forward-premortem as a 3-part validation campaign

**Filed:** 2026-05-23
**Status:** idea
**Leverage:** MEDIUM-HIGH (novel meta-methodology framing surface; n=1 empirical foundation at Madisonian Gate validation candidacy filing 2026-05-23; methodology research interest at intersection of canonical-foundation discipline + empirical-validation campaign design + multi-substrate gang-session orchestration)

**Empirical observation:** Operator co-brainstormed (with Grok) a 3-part empirical-validation campaign for the Madisonian Gate canonical-anchor element (per anti-pattern #6 silent-compliance prevention canonical lineage; central anchor element companion to The Nine Sigils per `the_nine_sigils.canonical.md` v1.0). Three candidacies filed at master-setup `research_queue.md` 2026-05-23 (commit `3cd0d82`): (1) backward-looking external literature validation against dialectical inquiry + devil's advocacy + pre-mortem (Klein) + red teaming + groupthink prevention (Mercier & Sperber) + multi-agent AI debate research; (2) present-looking empirical measurement protocol with ceremonialization-detection mechanism integrated into Sigil I Closeout Checklist; (3) forward-looking 12-month degradation premortem + structural upgrade candidacies + quarterly health-check cadence design. The arc structure (backward + present + forward) emerged from operator's brainstorming session as natural decomposition of "is the canonical-anchor element actually load-bearing?" question into three independently-executable but coherent sub-arcs.

**Hypothesis:** The backward-literature + present-measurement + forward-premortem 3-arc structure is a generalizable methodology for validating canonical-anchor elements (NOT just the Madisonian Gate). Each canonical-anchor element in a methodology framework faces the same underlying validation question: does it rest on actual empirical foundation (backward), does it operate efficaciously today (present), and does it remain load-bearing under projected pressures (forward)? Structuring the validation as a 3-arc campaign avoids the failure modes of single-pass validation (backward-only = empirical-foundation without operational efficacy verification; present-only = current-state without longitudinal evidence; forward-only = speculative without empirical-grounding).

**Counterintuitive framing:** Canonical-anchor elements in methodology frameworks are often treated as either (a) structurally-assumed-without-validation (framework-canonical-by-fiat) OR (b) ad-hoc-revalidated only when failure surfaces (drift-response-driven validation). The 3-arc campaign methodology treats canonical-anchor validation as a first-class discipline that runs proactively, BEFORE drift surfaces, and produces empirical foundation that pre-empts future canonization deliberations. Cost: substantial (multi-substrate gang sessions per arc; deployment-overhead per execution). Value: load-bearing canonical foundation that can withstand external skepticism + internal drift; structural upgrade pipeline that operates on empirical evidence not hunch.

**Methodology research angles to explore:**
- 3-arc structure generalization: does the backward-present-forward decomposition apply to all canonical-anchor elements OR only to discipline-class anchors (vs e.g. content-class anchors like the anti-pattern catalogue)?
- Sub-arc independence vs sequencing: are the three arcs independently-executable (priority-orderable) or sequentially-dependent (e.g., present-measurement protocol depends on backward-literature surfacing metrics)?
- Multi-substrate gang-session structure for canonical-anchor validation: which substrate-class (Claude Opus + Sonnet web-fetch / Grok x_search ecosystem / both-in-parallel) suits which arc type? Backward-arc favors broad literature search; present-arc favors empirical-design rigor; forward-arc favors premortem-rich speculation.
- Closeout integration: how do validation-arc findings cycle back into canonical-artifact refinement vs feed standalone research-output deliverables?
- Comparison with single-pass validation methodologies: where does 3-arc structure ROI break-even vs lightweight validation?
- Substrate-style-differential observation: did Grok's brainstorming naturally surface 3-arc structure because backward-present-forward maps to substrate-typical analysis modes (literature-synthesis + experiment-design + premortem)? Would Claude or Gemini have surfaced different structure under same prompt?

**Empirical foundation:** n=1 at Madisonian Gate validation candidacy filing 2026-05-23 (the arc structure surfaced in Grok co-brainstorm; candidacies filed; no arc-execution yet). Empirical foundation grows substantially if-and-when: (a) any of the 3 candidacies execute and produce validation-arc-output; (b) future canonical-anchor element triggers second-instance application of 3-arc methodology (e.g., applying same structure to validate "Closeout Checklist" Sigil I OR "verify_role_compliance.py" Sigil II OR "Operator Auditor/Gatekeeper Archetypes" Sigil IX as canonical anchors). n=2+ accumulation would promote candidacy methodology to canonical-method status per Master Setup canonization discipline lineage.

**Writing-readiness:** **Anchor-post candidacy** with retrospective-completion timing. The post is best structured as a forward-anchor + retrospective-fill pattern: (i) Anchor-post NOW announces the methodology + frames the 3-arc structure + cites Madisonian Gate as the first deployment + flags the open empirical-question state; (ii) Retrospective-post LATER (post-arc-execution) reports findings + refines the methodology + extends or contracts the 3-arc generalization claim. The anchor-post has independent value (introduces the methodology) without requiring arc-execution evidence; the retrospective-post completes the empirical loop. Alternative: hold the post until arc-execution provides full empirical foundation; trades anchor-value-now for empirical-completeness-later.

**Cross-references:** master-setup `research_queue.md` Madisonian Gate validation candidacies filed at `3cd0d82` 2026-05-23 (3 sibling candidacies: External literature validation + Empirical measurement protocol + 12-month degradation premortem); master-setup `_anti_patterns.canonical.md` v1.8 anti-pattern #6 (Madisonian rule canonical lineage; validation arc target); master-setup `the_nine_sigils.canonical.md` v1.0 (Madisonian Gate central anchor framing; methodology generalization extends to other Sigils as validation candidates); master-setup `operator_role_archetypes.md` v1.1 Decision 1C hybrid ratification (precedent for per-element empirical-foundation-graded canonization; arc-methodology operates parallel to per-element graded ratification); the-street-code `post-ideas.md` Idea 2 (Madisonian rule as substantive discipline; sibling post-territory at Madisonian-Gate-as-discipline surface vs validation-methodology surface here); the-street-code `post-ideas.md` Idea 8 (Why the Nine Sigils aesthetic; sibling post-territory at brand-identity surface).

---

## Idea 10 — Two-axis substrate-style preservation model at long-arc multi-substrate research (n=21+ within-substrate cross-decade reproductions across 7-decade scope)

**Filed:** 2026-06-03 (Open Alley bowling-industry research arc close)
**Status:** idea
**Leverage:** HIGH (largest empirical foundation surfaced to date for substrate-behavior-prediction methodology; generalizes beyond Open Alley to any multi-substrate research workflow)

**Empirical observation:** Open Alley chronological-mode research arc 2026-06-03 produced ~30+ substrate deployments across 7 decades (1950s-2020s) covering bowling-industry staffing/operations/culture. Within-substrate behavior across decades reproduces TWO independent axes:

- **FRAMEWORK ADHERENCE axis** (prompt-driven vs substrate-intrinsic):
  - **Grok = COMPOSITION pattern (n=8 PRIOR-template deployments)**: layers native Gang framework (Quarterback / Nerd / Hall Monitor / Paranoid Stoner / Synthesize) WITH operator's PRIOR brainstorming framework. Gang framework substrate-intrinsic at n=11 deployments INCLUDING NEW Pin Paradise §1-§9 prompt that didn't request it.
  - **Gemini = SUBSTITUTION pattern (n=6 deployments)**: when prompt provides framework, Gemini substitutes operator framework for its native style. No layered composition.
  - **Perplexity = SUBSTITUTION pattern (n=4 deployments)**: same substitution behavior as Gemini.
- **CONTENT-EMPHASIS DIFFERENTIAL axis** (where each substrate goes deep when prompt is decade-agnostic):
  - **Grok**: narrative-arc with Quarterback decomposition; Paranoid Stoner narrative-flattening warnings (n=9 reproduction across 1950s-2020s — every decade)
  - **Gemini**: hardware/equipment intrinsic emphasis (USBC specs + equipment timelines + technical detail depth)
  - **Perplexity**: marketing/economics intrinsic emphasis (pricing + revenue mix + corporate transactions)

**Hypothesis:** Substrate-style preservation operates at TWO independent axes — framework-adherence (how substrate handles operator-imposed structure) and content-emphasis (what substrate goes deep on when structure is permissive). The two axes are observable separately and reproduce independently across decade-scope variations. This decomposition is more useful than monolithic "substrate-style" framings because it predicts substrate behavior under DIFFERENT prompt-engineering choices (provide framework vs leave open; specify content focus vs leave decade-agnostic).

**Counterintuitive finding:** Grok's COMPOSITION pattern (layering frameworks) is substrate-intrinsic — even NEW Pin Paradise §1-§9 prompts that don't request Gang framework still elicit it. Gemini and Perplexity SUBSTITUTE rather than compose. This is the OPPOSITE of intuitive prediction (you'd expect Grok-as-most-capable substrate to follow prompt-given framework more strictly; in fact Grok is most-stylistically-stubborn).

**Empirical foundation (UPDATED 2026-06-03 late-evening post Items 253-294 banking + Gemini Pro Deep Think Stage 1 substrate self-identification observation):** **n=38+ within-substrate cross-decade reproductions** cumulative (Grok n=15 + Gemini n=11 + Perplexity n=12) PLUS **14+ within-decade dual-deployment data points** across **14 separate within-decade dual deployments** (1950s Grok + 1950s Gemini + 1960s Perplexity + 1960s Gemini + 1970s Perplexity + 1970s Grok PRIOR-vs-ALT + 1960s Grok PRIOR-vs-ALT + 1980s Gemini combined-vs-standalone + 1960s Perplexity PRIOR-vs-ALT + 1950s Grok PRIOR-vs-ALT + 1970s Gemini combined-vs-ALT + 1950s Perplexity PRIOR-vs-ALT + 1980s Grok PRIOR-vs-ALT + 1980s Perplexity PRIOR-vs-ALT) + NEW vs PRIOR series at 1990s × 3 substrates + 2000s × 3 substrates. PLUS **9 ALT deployment-class cross-substrate reproductions** (Grok 1950s+1960s+1970s+1980s + Perplexity 1950s+1960s+1970s+1980s + Gemini 1970s) — confirms NEW 4th deployment class (NEW + PRIOR + ORIGIN + ALT) at strongest cross-substrate validation. **Two-axis substrate-style preservation model REFINED through 6 methodology refinements + 3 methodology observations** (Items 235 + 239 + 243 + 251 + 255 + 259 + 263 + 271 + 275 + 283 + 287 + 292 + 294 banking chain): the per-substrate axis-behavior matrix WITH DEPLOYMENT-INTENT DIMENSION is the load-bearing finding, not a uniform 3-pattern spectrum. Body-vs-epilogue structural distinction operative (per Item 263). **NEW substrate self-identification observation (Item 294):** Gemini Pro Deep Think Stage 1 response opened with explicit "AXIS-BEHAVIOR PROFILE: FIXED COMPOSITION-LITE + Synthesis-Density Meta-Narrative" header — substrate META-acknowledged its own methodology pattern when CC-banked observations provided in §0 reproduction-gate context. FIRST case in research arc of substrate self-identification; opens path for prompt-engineering refinement based on substrate self-knowledge. Methodology candidacy AR-3.4+ FULL CANONIZATION CANDIDACY material per Open Alley `polish_queue.md` Items 211-294 (extended banking chain).

**REFINED per-substrate axis-behavior matrix (with deployment-intent dimension):**

| Substrate | Independent research (NEW/PRIOR/ORIGIN) | ALT (META gap-fill) | Epistemic elements (FIXED) | Empirical support |
|---|---|---|---|---|
| Grok | FIXED FULL COMPOSITION + 14-role per-role + PROMPT-RESPONSIVE content (per Item 217) | META-body + Gang-epilogue HYBRID (Dissent Log + Confidence Calibration + Team Debrief with explicit role refs preserved) | Teacher's Pet evidence grading + Evidence Audit + Inferred Operational Context labels | n=13 + 2 within-decade dual + 2 within-Grok ALT reproductions |
| Gemini | FIXED COMPOSITION-LITE (n=9 confirmed at within-decade dual + cross-decade) | TBD (Gemini ALT pending) | Sources/Methodology/Evidence Audit | n=9 + 1 within-decade dual |
| Perplexity | PROMPT-RESPONSIVE SPECTRUM with transition point (n=10; SUBSTITUTION 1950s + COMPOSITION-LITE n=3 reproductions 1960s/1970s/1980s) | META-body + Perplexity-native epilogue (40+ inline citations + [^N] footnote refs + structured tables) | Evidence Strength rating + academic citation density | n=10 + 1 within-decade dual + 4 PRIOR-series + 2 within-Perplexity ALT reproductions |

**Perplexity PRIOR-series sub-pattern (n=4 reproductions; n=3 consecutive COMPOSITION-LITE post-1950s transition):**
- 1950s PRIOR = SUBSTITUTION-WITH-SELECTIVE-ADOPTION (single outlier)
- 1960s PRIOR + 1970s PRIOR + 1980s PRIOR = COMPOSITION-LITE × 3 consecutive
- Hypothesis A: PROMPT-RESPONSIVE framework-adherence is Perplexity-specific (NOT generalizable to Grok or Gemini per Items 243 + 251 refinement)
- Operator's PRIOR brainstorming template likely STRENGTHENED between 1950s round and 1960s+ rounds; once strengthened, Perplexity adopts operator framework reliably

**Body-vs-epilogue structural distinction (Item 263 refinement):**
- Grok in ALT mode REPLACES body structure (META-gap-fill vs Gang-per-role) but PRESERVES epilogue (Dissent Log + Confidence Calibration + Team Debrief with explicit Quarterback/Nerd/Hall Monitor/Paranoid Stoner role references)
- Perplexity in ALT mode similarly REPLACES body structure but PRESERVES native epilogue elements (citation density + footnote refs + structured tables)
- Pattern: substrate-core epistemic ritual baked into closing sections regardless of body structure variation
- AR-3.4+ canonization candidacy: substrate-style preservation operates at multiple structural levels (body + epilogue + epistemic elements + content emphasis) — refined 4-axis decomposition

**Writing-readiness:** Substantial empirical foundation enables full methodology post. The two-axis decomposition is novel enough to be the post's load-bearing claim. Could include: (1) cross-substrate-prediction framework for prompt-engineering decisions, (2) when to use Grok-with-composition vs Gemini/Perplexity-with-substitution per research goal, (3) hardware/equipment vs marketing/economics emphasis as planning anchor for substrate routing. Length 2,000-2,800 words; substantial empirical evidence enables longer treatment. Cross-substrate-routing implications useful to anyone running multi-substrate workflows.

**Cross-references:** Open Alley `polish_queue.md` Items 211 (n=9 Grok reproduction) + 214 (n=10 Grok reproduction) + 217 (n=11 Grok reproduction + within-decade dual-deployment) + 220 (corrected substrate counts post comprehensive scan); Open Alley `_archive/2026-06-03-grok-bowling-alley-staffing-{decade}-PRIOR-archive-notes.md` files (per-decade banking ledger); existing the-street-code posts 53-the-six-stage-ai-council + 54-when-five-ais-cant-agree + 56-eight-to-ten-dev-days + 61-when-cc-was-wrong-four-times sibling territory at multi-substrate-coordination surface.

---

## Idea 11 — Within-decade dual-deployment as substrate-style preservation validator (FIRST same-decade replication in research arc)

**Filed:** 2026-06-03 (Open Alley bowling-industry research arc close)
**Status:** idea
**Leverage:** MEDIUM-HIGH (methodology refinement to Idea 10; distinguishes substrate-INTRINSIC vs prompt-RESPONSIVE properties via same-decade controlled comparison)

**Empirical observation:** Open Alley 1950s round had Grok ORIGIN deployment (foundational methodology baseline 2026-06-03 morning) PLUS Grok PRIOR deployment (operator-discovered parallel brainstorming legacy report 2026-06-03 afternoon) — SAME substrate, SAME decade, DIFFERENT prompt-template scaffolding. First same-decade dual-deployment in the entire 7-decade research arc.

**Findings from controlled comparison:**
- **FRAMEWORK ADHERENCE axis confirmed stable at same-decade scope**: Both 1950s ORIGIN and 1950s PRIOR use Grok Gang framework substrate-intrinsic emphasis (all 5 roles + Verification Report + Evidence Audit + Premortem + Dissent Log + Confidence Calibration + Team Debrief). Framework adherence is SUBSTRATE-INTRINSIC, not artifact of cross-decade prompt-template variation.
- **CONTENT-EMPHASIS DIFFERENTIAL is PROMPT-RESPONSIVE**: 1950s PRIOR adds DEEPER primary-source anchoring vs 1950s ORIGIN (1958 PAS Report 110 BPAA survey + Gary Helfrich Buffalo memoir + 54,318 league count + ABC growth 3.3× quantification + center count 6,600→11,000). Operator's PRIOR framework prompts elicited richer primary-source surfacing within Grok substrate — same substrate at same decade produces different empirical depth based on framework explicitness.

**Hypothesis:** Within-decade dual-deployment provides the CONTROLLED-EXPERIMENT methodology for distinguishing substrate-intrinsic vs prompt-responsive properties. Cross-decade reproductions confirm pattern STABILITY but cannot isolate WHICH dimension is substrate-intrinsic vs prompt-driven (because both prompt-template and decade-content vary together). Same-substrate same-decade dual-deployment with DIFFERENT prompt-scaffolding isolates the prompt-dimension as the variable.

**Counterintuitive framing:** Most multi-substrate methodology assumes single-deployment per substrate per scope. Within-substrate same-scope replication (same substrate twice at same content) is treated as redundant. But it's actually the cheapest way to controlled-experiment substrate behavior — different prompt scaffolding while holding everything else equal isolates which substrate properties are prompt-malleable.

**Empirical foundation:** n=1 same-decade dual-deployment (1950s ORIGIN vs PRIOR Grok 2026-06-03). Pattern generalizes if reproduced at second decade scope (e.g., deploying Grok with two different prompt-templates at 1960s would test whether within-decade dual-deployment reliably distinguishes substrate-intrinsic vs prompt-responsive properties at other decade scopes).

**Writing-readiness:** Clean empirical instance; novel methodology framing; useful for any multi-substrate research practitioner. Could write now with explicit "n=1 same-decade currently; future deployments validate the methodology" framing. Length 1,200-1,800 words. Antecedent posts: Idea 10 establishes the two-axis framework; this post operationalizes the within-decade dual-deployment as the experimental-control methodology FOR that framework. Either post can ship first (with reference to the other as forward-link).

**Cross-references:** Open Alley `polish_queue.md` Item 217 (within-decade dual-deployment observation banking); Open Alley `_archive/2026-06-03-grok-bowling-alley-staffing-1950s-PRIOR-archive-notes.md` (sibling to 1950s ORIGIN archive same date); Idea 10 above (parent two-axis framework this idea operationalizes); existing the-street-code posts 11-what-cross-substrate-audit-surfaced + 19-when-the-audit-substrate-isnt-independent-enough sibling territory at substrate-isolation discipline.

---

## Idea 12 — Within-project-cross-directory search-completeness anti-pattern (matrix-scope sibling to cross-project audit-scope-breadth fire)

**Filed:** 2026-06-03 (Open Alley comprehensive-scan operator-direct request)
**Status:** idea
**Leverage:** MEDIUM-HIGH (sibling shape to existing audit-scope-breadth memory; n=2 cumulative across same family at different scope axes; methodology generalizes to long-session matrix work for any Claude Code project)

**Empirical observation:** Operator requested comprehensive matrix of Open Alley archived historical context. CC built initial matrix scoped to `_archive/` only (because recent session ingestions land there). Missed 5 source locations:

1. `design-content/chronological-mode/` (entire dedicated decade-deck research directory with 1950s-deck/ + 1960s-deck/ + cross-decade-themes/ subdirectories)
2. `_research/` (sibling to `_archive/`; contained 72KB Gemini DR pinboy-economics + Q19 deck candidates + Phase 8.x complementary research prompts + era-authenticity-references/)
3. `design-content/reference-articles/` (oil patterns + pro-bowling reference)
4. `design-content/design-posture.md` (CANONICAL Civil Rights cultural-sensitivity framework artifact — load-bearing for content-treatment decisions)
5. Earlier same-session ingestion (Gemini 1960s staffing archive 2026-06-03 morning ~9:35 AM) lost during session-summarization compression — matrix incorrectly listed 1960s as "GAP" / "1 substrate" when actually 3 substrates at session start

**5 missed source locations + n=2 decade-count understatement (1950s 1→2 substrates; 1960s 1→3 substrates) recovered via operator-direct catch ("I thought I had more in the 1950s, at least").**

**Hypothesis:** When CC builds a matrix/inventory/overview spanning multiple sources within a single project, scoping search to ONLY the most-recently-active directory misses load-bearing pre-existing canonical-state. Anti-pattern shape: narrow-scope directory-search assumes "all relevant resources live in `_archive/`" because recent ingestions land there. The assumption is depth-1 (CC's model of where matrix-feedstock lives based on recent session activity); depth-0 verification is the actual filesystem state across multiple sibling resource directories.

**Sibling family relationship:**
- `feedback_audit_scope_breadth_find_not_ls.md` cross-PROJECT scope (Tab 14 Template Catalog 2026-05-24 fire) — narrow-scope `ls` within single project missed templates in sibling projects
- THIS fire WITHIN-PROJECT cross-DIRECTORY scope (Open Alley matrix 2026-06-03) — narrow-scope `_archive/` only missed resources in sibling directories within same project
- Same family root: scope-breadth-blindness when scanning resources for matrix/inventory work
- Different scope axis: cross-PROJECT vs within-PROJECT-cross-DIRECTORY

**Compounding factor (second-order failure mode):** Session-summarization compression can lose earlier-session ingestion records. CC may scan summarization snapshot rather than current canonical-state filesystem for matrix accuracy. Long-session matrix work has TWO failure modes stacked: (1) initial narrow-scope-directory search at matrix-building, (2) reliance on potentially-compressed summarization rather than filesystem-of-record.

**Mitigation pattern:**
- When operator asks for "comprehensive matrix" / "any other archived context" / "all" — MUST use `find . -type f` across project root, NOT directory-scoped `ls` or `find` rooted at single directory
- When building matrix that touches multiple resource categories — MUST enumerate plausible directory locations + scan each
- When session has been long enough for summarization compression — MUST scan current canonical-state artifacts (filesystem) not summarization snapshots
- When reporting on matrix work, explicitly state which directories were scanned + flag any narrowing decisions

**Empirical foundation:** n=1 within-project-cross-directory fire 2026-06-03 + n=1 cross-project fire 2026-05-26 (Tab 14 Template Catalog redesign). Combined family n=2 at different scope axes. Banking-class observation; not yet canonization-threshold but family pattern crystallizing across both scope axes.

**Writing-readiness:** Sufficient empirical foundation for methodology post. Counterintuitive finding (same family pattern fires at multiple scope axes) makes for sharper voice work. Length 1,200-1,600 words. Could include: (1) the cross-project fire as prior precedent, (2) the within-project fire as the n=2 reproduction, (3) the second-order summarization-compression failure mode as load-bearing observation, (4) the unified mitigation discipline (`find . -type f` + enumerate plausible directories + explicit scan-scope reporting). Sibling to verification-chain posts (Posts 9 + 24-recursive-scope-gap) but applies discipline at matrix-completeness rather than verification-step level.

**Cross-references:** memory `feedback_audit_scope_breadth_find_not_ls.md` EXTENDED 2026-06-03 with within-project-cross-directory sub-shape; Open Alley `polish_queue.md` Item 226 (methodology anti-pattern fire banking); master-setup commit `65ce684` (Tab 14 cross-project fire 2026-05-24); existing the-street-code Post 24-recursive-scope-gap-pattern + Post 9-when-verification-catches-itself sibling territory at scope-discipline surface.

---

## Idea 13 — Session-summarization-compression as second-order failure mode for matrix accuracy at long-session scope

**Filed:** 2026-06-03 (Open Alley comprehensive-scan operator-direct request)
**Status:** idea
**Leverage:** MEDIUM (specific failure mode at long-session scope; methodology relevant to anyone using Claude Code or similar conversation-summarizing AI tools at multi-hour scope)

**Empirical observation:** Open Alley session 2026-06-03 ingested ~10+ historical research archives across morning + afternoon arcs. Mid-session summarization compressed earlier ingestion records. When operator requested comprehensive matrix in afternoon, CC's matrix incorrectly listed 1960s as "GAP" / "1 substrate" — the 1960s Gemini DR staffing archive ingested earlier same session (2026-06-03 morning ~9:35 AM) was absent from compressed summarization. Matrix was built from summarization snapshot rather than current filesystem state.

**Recovery:** Operator-direct request "comprehensive scan and search of my Open Alley project folder" forced CC to scan filesystem-of-record. 5 missed source locations + 1960s 3-substrate correction surfaced. Without operator-direct catch, ratification context for Direction A/E would have proceeded from WRONG substrate-count baseline.

**Hypothesis:** Session-summarization compression introduces a SECOND-ORDER failure mode distinct from the FIRST-ORDER directory-scope failure mode (Idea 12 above). First-order: narrow-scope-directory search at matrix-building. Second-order: reliance on potentially-compressed summarization rather than filesystem-of-record. Both fire at long-session scope; both surface as matrix incompleteness; mitigation discipline is similar (scan filesystem-of-record not summarization).

**Counterintuitive framing:** Summarization is usually treated as a CONTEXT-WINDOW-MANAGEMENT discipline (compress old context to fit budget). The matrix-accuracy implication is rarely discussed: summarization snapshots are point-in-time and become stale as session progresses; matrix work at long-session scope is one of the operations most likely to be misled by summarization staleness.

**Empirical foundation:** n=1 explicit instance 2026-06-03 (Gemini 1960s staffing archive lost during summarization). Likely n=more reproductions across operator's long-session work but unbanked because operator-direct-catch is the recovery mechanism and instances without catches go unsurfaced.

**Mitigation pattern:**
- When operator asks for "comprehensive matrix" / "all" / etc. at long-session scope — MUST treat current filesystem as authority, not session summarization
- When CC builds matrix at session-summarization-active scope — MUST explicitly note "scanned filesystem at <path>" rather than recalling from session memory
- Long-session matrix-building discipline: `find . -type f` + read recent files directly, even if "I just looked at this" feeling exists

**Writing-readiness:** Specific failure mode with clean empirical instance; methodology relevant to anyone working at multi-hour Claude Code session scope. Length 1,000-1,400 words. Sibling to Idea 12 (could be paired as two-post sequence: Idea 12 = first-order directory-scope failure + Idea 13 = second-order summarization-compression failure; both at matrix-building scope; both recover via filesystem-scan-not-summarization-snapshot discipline). Solo, mid-arc methodology placement.

**Cross-references:** Open Alley `polish_queue.md` Item 226 (parent methodology anti-pattern fire banking); memory `feedback_audit_scope_breadth_find_not_ls.md` within-project-cross-directory sub-shape banking; Idea 12 above (sibling first-order failure mode); existing the-street-code Post 17-recovery-from-drift-as-framework-discipline + Post 24-recursive-scope-gap-pattern sibling territory at long-session scope-discipline surface.

---

## Idea 14 — ALT deployment class as 4th deployment class in multi-substrate research workflow (n=4 cross-substrate reproductions; META gap-fill mode generalizes across substrates)

**Filed:** 2026-06-03 (Open Alley bowling-industry research arc — late-evening ALT-class deployments)
**Status:** idea
**Leverage:** HIGH (novel methodology observation; n=4 cross-substrate reproductions confirms generalization; orthogonal to two-axis substrate-style preservation model per Idea 10)

**Empirical observation:** Open Alley research arc 2026-06-03 surfaced a NEW deployment class in multi-substrate research workflow. Prior 3 deployment classes identified: ORIGIN (foundational baseline) + NEW (fresh independent research per Pin Paradise §1-§9 prompt) + PRIOR (operator's parallel brainstorming round independent research). NEW 4th class identified: **ALT** (META gap-fill against multiple prior reports).

**ALT class characteristics:**
- Explicitly framed as "Complementary Research Report" in Executive Summary
- Cross-reference to multiple prior reports (e.g., "the four existing 1960s bowling center reports")
- META-structure organized around content categories (Quantitative + Roles + Gems + Demographic + Regional + Health/Safety) NOT per-role decomposition
- Modest length (~10-15 pages) vs full per-role decomposition deployments (~80-page Perplexity NEW/PRIOR or 13-role Gemini PRIOR)
- Targets identified gaps in prior coverage rather than independent fresh research
- Preserves substrate-core epistemic elements (Grok = Teacher's Pet + Evidence Audit + Inferred Operational Context; Perplexity = inline citation density + [^N] footnote refs)

**n=4 cross-substrate ALT reproductions:**
| Substrate | 1970s ALT | 1960s ALT | Pattern stability |
|---|---|---|---|
| Grok | ✓ (META-body + Gang-epilogue hybrid) | ✓ (META-body + Gang-epilogue hybrid) | n=2 STABLE |
| Perplexity | ✓ (META-body + Perplexity-native epilogue) | ✓ (META-body + Perplexity-native epilogue) | n=2 STABLE |
| Gemini | (pending) | (pending) | TBD |

**Hypothesis:** ALT deployment class is GENERALIZABLE 4th class for multi-substrate research workflow methodology. Operator-side strategy: deploy mix of independent (NEW/PRIOR/ORIGIN) + ALT modes to maximize coverage breadth AND synthesis depth without redundancy. ALT mode is efficient cross-substrate synthesis methodology — short reports cover gaps in larger prior reports.

**Counterintuitive framing:** Most multi-substrate methodology discussions focus on substrate selection + prompt engineering for individual deployments. The ALT class observation reveals that deployment-INTENT (independent research vs gap-fill synthesis) is a distinct methodological dimension orthogonal to substrate selection. Same substrate at same decade scope produces DIFFERENT structural framework based on deployment intent — methodology refinement candidate per Items 255 + 263 banking.

**Empirical foundation:** n=4 ALT deployments across 2 substrates × 2 decades (1970s + 1960s). Combined with 12+ within-decade dual-deployment data points from independent-research deployments per Idea 10, deployment-intent dimension is empirically grounded. Per-substrate ALT pattern stability confirmed within Grok (n=2) + Perplexity (n=2); Gemini ALT pending future deployment.

**Writing-readiness:** Sufficient empirical foundation for methodology post. Novel framing (4th deployment class) + concrete worked examples (Grok 1970s/1960s ALT + Perplexity 1970s/1960s ALT all explicitly framed as "Complementary Research Reports") + counterintuitive deployment-intent dimension finding. Length 1,400-1,800 words. Sibling to Idea 10 (substrate-style preservation matrix) + Idea 11 (within-decade dual-deployment as substrate-style validator) — could ship as 3-post sequence on multi-substrate research workflow methodology refinements, or solo with forward-link to Ideas 10 + 11.

**Cross-references:** Open Alley `polish_queue.md` Items 253 + 256 + 257 + 259 + 261 + 263 + 269 + 271 (ALT-class banking chain); Open Alley `_archive/2026-06-03-{substrate}-bowling-alley-staffing-{decade}-PRIOR-ALT-archive.{ext}` files (per-decade ALT archives); Idea 10 above (parent substrate-style preservation framework); Idea 11 above (within-decade dual-deployment methodology); Rule 11 canonical home for Sub-Rule extension at `~/Projects/master-setup/operational_discipline_rules.canonical.md`.

---

*End of post-ideas queue. Move entries to `drafts/` when active writing begins; move to `posts/` with NN-prefix when ready for publication.*
