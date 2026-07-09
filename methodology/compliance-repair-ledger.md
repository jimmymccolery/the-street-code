# Compliance Repair Ledger

Append-only ledger of MECHANICAL compliance-repair edits per Rule 24 amendment
candidate Item 142 (Fable 5 adversarial audit §D.8). Each entry records the
mechanical fix + the invariant-diff test result + the responsible commit.

Rules:
1. Only mechanical fixes (normalization-invariant diff test PASSES) go in this ledger.
2. Semantic edits go through Rule 24 addendum protocol (dated addendum file).
3. Entries are append-only; do NOT edit prior entries.
4. Commit must be tagged `mechanical-fix` in message.
5. `verify-mechanical-fix.py` must be re-runnable against the recorded refs.

## Ledger

### Entry 1 — Em-dash + frontmatter compliance repair (posts 0198-0201)

- **Date:** 2026-07-09 late
- **Triggering lint rule:** em-dash discipline (posts 0036+ zero U+2014 per methodology/post_audit_checklist.md) + frontmatter completeness (Author + Date + Status + AI-assistance disclosure)
- **Normalization:** `em-dash+frontmatter` (replace U+2014 with `--` + strip inserted 6-line frontmatter block)
- **Pre-fix ref:** `3204ac9` (HEAD before em-dash regression)
- **Post-fix ref:** `8df57fb` (audit fix commit)
- **Files affected:** `posts/0198-*.md`, `posts/0199-*.md`, `posts/0200-*.md`, `posts/0201-*.md`
- **H33 test result:** PASS at n=4 (verified 2026-07-09 late; see `scripts/verify-mechanical-fix.py` for reproduction command)
- **Test invocation:**
  ```
  python3 scripts/verify-mechanical-fix.py \
    --pre-ref 3204ac9 --post-ref 8df57fb \
    --normalization em-dash+frontmatter \
    --paths posts/0198-when-a-late-night-operator-inquiry-about-physical-characteristics-produced-a-cross-cultural-attractiveness-and-first-impression-architecture-with-a-seven-hypothesis-harness.md \
      posts/0199-when-stage-four-pair-relational-plane-migrated-fire-i-bond-history-from-hexaco-scalar-to-derived-property-while-preserving-production-discipline.md \
      posts/0200-when-stage-five-bourdieu-habitus-plane-completed-the-cognitive-architecture-with-symbolic-capital-as-nonlinear-emergent-property.md \
      posts/0201-when-a1-external-empirical-anchoring-displaced-architectural-derivation-and-showed-the-m10-fold-was-inert.md
  ```
- **Council #9 status:** Item 142 candidacy n=1 anchor (H33 PASS).
