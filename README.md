# The Street Code

Methodology research on AI-assisted work: cross-substrate audit chains, canonical-state discipline, framework-encoded verification.

## Start here (plain English)

This repository is a public notebook. It records what I have learned from using AI tools to help build software and write, and the rules I use to catch AI mistakes such as making things up or skipping checks. Most posts were written with AI assistance, and each one says so. It is a personal project, separate from my career in customer success and training (see [jimmymccolery.com](https://jimmymccolery.com)).

If you only read three posts:

1. [How a Personal AI Discipline Framework Earns Its First Rules](posts/0005-how-a-personal-ai-discipline-framework-earns-its-first-rules.md): the core idea in short form.
2. [Cross-Substrate Triangulation as Solo-Indie Methodology](posts/0039-cross-substrate-triangulation-as-solo-indie-methodology.md): why checking one AI's work with a different AI catches more errors.
3. [What the Gang Actually Does and What's Theater](posts/0040-what-the-gang-actually-does-and-whats-theater.md): an honest look at which parts of the process add value.

Two terms you will see everywhere: a **substrate** is an AI tool or model (Claude, Gemini, Grok), and **CC** is Claude Code, the AI coding assistant.

## What this is

This repo collects substantive writing on a personal framework for AI-assisted methodology research work. The framework operates across multiple AI substrates (Claude Code, Claude on web, Gemini, Grok) with explicit verification phases (Phase 1 canonical content read, Phase 3 generation, Phase 5 byte-level verification). Posts here document patterns observed during framework operation, architecture decisions, and methodology research findings.

The work is operator-audit-shaped: writing serves as memory-keeping and audit trail for the operator's own methodology research arc. Public availability enables discoverability for others researching similar territory.

## Navigation

- posts/ - Substantive published methodology research writing
- methodology/ - Framework documentation and operational disclosure
- Work-in-progress drafts are kept private and are not part of this public repository

## Conventions

**Filename numbering prefix:** Four-digit zero-padded sequential number reflecting authoring order. Posts numbered 0001-NNNN by body Date ascending; same-day clusters ordered by methodology-arc sequence (the order in which the substantive work documented in posts was performed). Filenames sort by reading order. Slots may be retracted (with the slot-number gap preserved as visible audit record) when a duplicate or other auditable issue surfaces post-publication; see SUMMARY.md for the canonical record of any retracted slots.

**Body Date field:** The frontmatter `**Date:**` field reflects authoring Date: when the substantive work documented in the post was performed. Authoring Date is the basis for filename numbering order.

**Frontmatter structure:** Posts use Markdown frontmatter with `**Author:**`, `**Date:**`, and `**Status:**` fields, followed by an italic disclosure note acknowledging AI writing assistance. This convention was tightened partway through the corpus; posts 0026-0035 (10 files) carry partial frontmatter omissions that are preserved per the immutability convention rather than back-applied (parallel to the em-dash legacy gap documented in `methodology/post_audit_checklist.md`). The CI audit enforces frontmatter consistency from post 0036 onward.

**Post-naming pattern:** `NNNN-kebab-case-slug.md` where NNNN is four-digit zero-padded number reflecting authoring order convention above.

**CC-OPTIMIZED-SUMMARY blocks (post-2026-07-05 amendment):** Load-bearing methodology posts include an HTML-comment block immediately after the title with grep-consistent keyword `CC-OPTIMIZED-SUMMARY`. The block is reader-invisible on GitHub (HTML comments do not render in Markdown display) but grep-accessible from file scope. Purpose: distill the post's load-bearing framework knowledge into a structured 200-400 word summary (post_id + domain + canonical_rule + load_bearing_claims + applicability_triggers + mechanism_details + cross_refs) that AI-assistant sessions can consume without loading full 2000-2600 word post bodies. Retrofit applied to 16 load-bearing posts as of 2026-07-05 (posts 0090, 0111, 0112, 0115, 0116, 0118, 0120, 0125, 0127, 0128, 0136, 0143, 0146, 0163, 0167, 0168); ongoing retrofit + new-post template mandates the block for every post from 2026-07-05 onward. Immutability preserved: reader-facing content unchanged; metadata layer only. To consume the blocks: `grep -A 25 CC-OPTIMIZED-SUMMARY posts/NNNN*.md`. Format specification: `~/Projects/substack/post_template.md` v2.

## Author

Jimmy McColery: building methodology research tools for AI-assisted work.
