# Post Authorship Style Guide — the-street-code

**Version:** 1.0.0 · **Date:** 2026-07-14 · **Author:** derived from 10-post corpus sample + canonical template

**Purpose:** Consolidated style guide for framework post authorship at `~/Projects/the-street-code/posts/`. Distilled from canonical the private post template + the private disclosure rule v1.0 + corpus sampling (Posts 0011, 0044, 0129, 0143, 0146, 0163, 0175, 0178, 0194, 0197).

**When to consult:** Before authoring any post at `~/Projects/the-street-code/posts/`. Loads canonical voice + structural discipline + Rule 19 gates for citation verification.

---

## 1. Post title conventions

Pattern: `[When|As|At]` + `[specific empirical event | architectural decision | methodology finding]`

**Verbatim examples from corpus:**
- Post 0175: "Council #8 Canonized Five Rules Plus Policy Plus Split-Retire-Reduce Mechanism…"
- Post 0197: "When Four Stage 2 Empirical Hypotheses Passed and Corrected the Elevator Pitch…"
- Post 0146: "Ten Layers of Model, Not One Layer of Prompt…"
- Post 0194: "When the Vendor-Sync Reminder Hook Captured Safety Without Losing Control…"

**Discipline:** NEVER use em-dashes (—) in titles. Replace with periods, commas, or "Plus".

---

## 2. Voice specification (6 pillars)

1. **Technical professional, not expert.** Direct, opinionated, factual. First-person operative ("I noticed," "I ran," "I tested"). No performative humility. No "AI can/cannot" generalizations from single observations.

2. **Honest calibration on empirical confidence.** "Single run, n=1, suggestive not conclusive" (Post 0175 status language). State what counts as evidence and what does not. No hiding null results.

3. **Plain prose over academic phrasing.** Post 0146 example: "NPCs do not know how humans function. NPCs embody mathematical models" (not "epistemic substrates encapsulating behavioral dynamics"). Watch for academic slips in voice-fit pass.

4. **Jargon explained inline at first use.** From canonical template: "A 'drain probe' is my procedure for extracting accumulated learning from a chat before closing it." Framework-internal terms get 10-15 word plain-English unpacking.

5. **Occasional narrative confession.** Post 0163: "My initial pattern classification was Pattern A…the reasoning was defensible; the classification was wrong." Posts acknowledge reasoning errors caught by the framework's own discipline.

6. **Citations embedded, not footnoted.** "Zakharin and Bates 2023 (PLOS ONE 18(6):e0287391)" inline rather than [reference N] footnotes. Author-year + venue specificity per Post 0129 verification discipline.

---

## 3. Front-matter recipe

Mandatory structure:

```markdown
# [Post Title]

<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: [0XXX]
date_published: [YYYY-MM-DD]
domain: [methodology-discipline | framework-architecture | empirical-validation |...]
status: published
canonical_rule: [rule-name-or-pattern]
load_bearing_claims:
  - [claim 1]
  - [claim 2]
applicability_triggers:
  - [when to consult this post]
mechanism_details:
  - [constants, thresholds, specific mechanics]
cross_refs:
  - Post [XXXX] [relationship]
CC-OPTIMIZED-SUMMARY -->

**Author:** Jimmy McColery
**Date:** [YYYY-MM-DD]
**Status:** [specific phrasing]

*Note: I'm a tech professional documenting my work in personal AI infrastructure. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The framework, the experiments, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*
```

Soft-disclosure disclaimer is **mandatory at header**. No variation from canonical wording.

---

## 4. CC-OPTIMIZED-SUMMARY block spec

- **Format:** HTML comment `<!-- CC-OPTIMIZED-SUMMARY v2.0... -->` immediately after title
- **Length target:** 200-400 words (split post if approaching 500)
- **Required subsections:**
  - `post_id` — canonical post number
  - `domain` — from fixed vocabulary (methodology-discipline / framework-architecture / research-observation / product-feature / empirical-validation-harness)
  - `canonical_rule` — what rule/pattern the post canonizes or extends
  - `load_bearing_claims` — 2-4 bullets capturing substantive contribution
  - `applicability_triggers` — 3+ specific conditions when CC should consult
  - `mechanism_details` — specific constants + thresholds + decision criteria
  - `cross_refs` — Post [XXXX] + short description; canonical files; memory; literature

**Immutability discipline:** Can be added to previously-published posts without violating post immutability because reader-facing narrative unchanged.

---

## 5. Structural template (5 arc types)

**Pick one consciously per template §Post structure variations.**

**Type 1 — Single-Session Finding (1200-1800 words)**
Opening setup → substantive finding (3-5 sections) → what this produced → what I'm not claiming → what I am claiming

**Type 2 — Multi-Session Foundation (2500-3500 words)**
Opening (acknowledge prior post) → session-by-session arc → takeaways → what I'm not claiming → what I am claiming

**Type 3 — Diagnostic/Research Arc (2000-2500 words)**
Setup → observation → initial interpretation → literature reframe → implications → not-claiming / am-claiming

**Type 4 — Council Close (2500-4500 words)**
Council configuration → candidacies + verdicts → cross-cutting architectural questions → what changed → what did not change → bounds → closing statement

**Type 5 — Operational Discipline Single-Finding (1500-2000 words)**
Problem context → specific fire → why this matters → pattern analysis → applicability triggers → not-claiming / am-claiming

**Heading discipline:** H2 (`##`) for major sections. Title is H1. Subheadings rarely deeper than H3.

---

## 6. Em-dash discipline (CRITICAL)

**Rule:** Zero em-dashes (—, Unicode U+2014) anywhere in post including CC-optimization block.

**Replacements:**
- **Period** for hard breaks: "The rule worked. So did the recovery."
- **Semicolon** for related ideas: "The framework made the work look careful at the procedural layer; it didn't enforce empirical correctness at the verification layer."
- **Parentheses** for asides: "The operator-side procedural-moral-test discipline (Post 0125) separates trait dimensions from procedural moral frames."
- **Colon** for lists/elaboration: "The framework's discipline binds at one layer but not the other: knowing where it half-works is more useful."

**Pre-publication verification:** `grep -c '—' [post-file]` must return `0`.

---

## 7. Citation format (Rule 19 K=3 CONVERGENT discipline)

**Inline citations with author-year + venue specificity:**

✅ "Zakharin and Bates 2023 (PLOS ONE 18(6):e0287391) test the four-factor reduction…"
✅ "Russell 1980 *Journal of Personality and Social Psychology* 39(6):1161-1178 for valence-arousal…"

❌ "As the literature suggests…" (vague)
❌ "Research [1] shows…" (footnotes)
❌ "Recent work on personality…" (unspecific)

**Load-bearing external citations:** Independent verification per Rule 19 Marcus Reed Protocol before publishing.

**Framework-internal:** Post [XXXX] + brief description. Memory: `[filename.md]`. Canonical: `[filename.md]`.

---

## 8. Length target

| Arc type | Word count range |
|---|---|
| Single-finding | 1200-1800 |
| Single-session | 1500-2000 |
| Foundation/multi-session | 2500-3500 |
| Diagnostic/research-program | 2000-2500 |
| Council close | 2500-4500 |
| Validation arc | 1500-2000 |

Corpus modal range: **2000-3500 words**. Under 1500 = single-finding. Over 4000 = Council closes / multi-week execution arcs.

---

## 9. Table + code block usage

- **Tables:** When enumeration is load-bearing, comparison across rows matters, constants/thresholds need specificity (Post 0175 Rule 20 count-ledger)
- **Code blocks:** When formula is load-bearing, config structure matters, pseudocode illustrates mechanism (Post 0146 EFE formula)
- **Verbatim quotes:** When precision is load-bearing for the post's argument (Post 0163 spec-error quoting)

**Avoid:** Decorative tables or code. Every block should be essential to the argument.

---

## 10. Publication checklist

- [ ] Metadata block complete (title, author, date, status)
- [ ] CC-optimization block v2.0 per spec; `grep CC-OPTIMIZED-SUMMARY` returns exactly 2 matches
- [ ] CC-optimization block 200-400 words
- [ ] Soft-disclosure disclaimer present and unchanged
- [ ] "What I'm not claiming" section present (3-5 bounded statements)
- [ ] "What I am claiming" section present (1 calibrated claim)
- [ ] Voice-fit pass complete (no academic phrasing slips + unexplained jargon)
- [ ] Em-dash count zero: `grep -c '—' [post-file]` returns 0
- [ ] Disclosure check per the private disclosure rule
- [ ] Load-bearing citations independently verified (Rule 19 Marcus Reed Protocol)
- [ ] Word count noted for tracking
- [ ] Cross-substrate audit if high external-claim density
- [ ] Update `~/Projects/the-street-code/SUMMARY.md` index
- [ ] Update `~/Projects/the-street-code/framework-research-index.md` if load-bearing methodology
- [ ] Regen master-setup launcher via `regen_launcher_hashes.py` post-publish

---

## 11. Anti-patterns to avoid (from corpus failure analysis)

**Voice failures:**
1. Academic phrasing on substantive findings — "empirically demonstrated" instead of "the rule worked"
2. Framework-internal jargon without unpacking
3. Performative humility or expertise framing — "Leading researchers have shown…"
4. First-person hedging on load-bearing claims — "I think perhaps…"

**Structural failures:**
1. Missing "What I'm not claiming" section (Post 0146 shows value)
2. Verdict-token convergence without modal-status analysis (Post 0129 documents trap)
3. Unverified external citation under time pressure (Post 0163 documents fire; Rule 19 mandatory)
4. Regen-timing gaps and canonical-file staleness (Post 0143 documents 6 fires)

**Discourse failures:**
1. Fabrication risk from "comprehensive-delivery under deadline pressure" (Post 0163)
2. Count-ledger drift in Council proposals (Post 0175)
3. Unmarked schema-placeholders bleeding into game-logic assumptions (Post 0128)

---

## 12. Framework-specific conventions

**Rule 14 Six-Pattern Verdict Classification** (Council-close posts): Identify verdict pattern explicitly (A/B/C/D/E/F).

**Rule 19 Marcus Reed Protocol** (external attribution): Load-bearing operator-defined named entities require verification per 3-condition gate.

**Rule 20 Canonization-Propagation Gap** (Council + BUILD sync): Verify propagation across 6 layers before shipping — canonical / posts / memory / CW project knowledge / deploy kits / regen outputs.

**Rule 24 Post-Audit-Correction** (immutability + transparency): Previously-published posts remain immutable. Corrections ship as top-of-file notice or canonical-index entry if operationally load-bearing.

---

## Croydon-arc framework posts authorship plan (Posts 0176-0179+)

### Recommended authorship order

1. **Post 0177 (first)** — Q8 Player Role Architecture (3000-4500 words; Arc Type 2 Foundation)
2. **Post 0176 (second)** — Croydon Methodology Framework Contribution (3500-5000 words; Arc Type 2 Foundation)
3. **Post 0178+ (third)** — Council #11 K=3 Deployment Synthesis (2500-3500 words; Arc Type 4 Council Close)
4. **Post 0179+ (fourth)** — Rule 19 Corrections Roll-Up (2000-3000 words; Arc Type 5 Operational Discipline)

**Order rationale:** Architecture → methodology specialization → deployment synthesis → lessons extraction.

### Effort estimates

| Post | Estimated hours | Prerequisites |
|---|---|---|
| 0177 Q8 Player Role | 8-12 hrs | Q8 role spec + power-resource mapping + era-parametrization tables + 13-layer storage audit |
| 0176 Croydon Methodology | 10-14 hrs | Bakhtinian theory read + 6-voice examples + K=3 anchor examples + Trust Posterior Registry spec |
| 0178+ Council #11 Deployment | 12-16 hrs | Q8 Wave 1 completion + 14-ship validation data + 100+ candidacy enumeration + K=3 cross-substrate synthesis |
| 0179+ Rule 19 Roll-Up | 6-8 hrs | Corrections ledger with 63+ entries + categorization by fire-family + lessons enumerated |

**Total:** 36-50 hours across 4 posts.

---

## Sources

- Canonical template: the private post template
- Disclosure rule: the private disclosure rule (v1.0)
- Corpus samples: Posts 0011, 0044, 0129, 0143, 0146, 0163, 0175, 0178, 0194, 0197 at `~/Projects/the-street-code/posts/`
- Framework research index: `~/.claude/framework-research-index.md` (v2.14)
- Rules canonization: Council #8 close (Post 0175) — Rules 20-24
