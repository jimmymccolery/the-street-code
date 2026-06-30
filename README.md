# The Street Code

Methodology research on AI-assisted work: cross-substrate audit chains, canonical-state discipline, framework-encoded verification.

## What this is

This repo collects substantive writing on a personal framework for AI-assisted methodology research work. The framework operates across multiple AI substrates (Claude Code, Claude on web, Gemini, Grok) with explicit verification phases (Phase 1 canonical content read, Phase 3 generation, Phase 5 byte-level verification). Posts here document patterns observed during framework operation, architecture decisions, and methodology research findings.

The work is operator-audit-shaped: writing serves as memory-keeping and audit trail for the operator's own methodology research arc. Public availability enables discoverability for others researching similar territory.

## Navigation

- posts/ - Substantive published methodology research writing
- methodology/ - Framework documentation and operational disclosure
- drafts/ - Work-in-progress posts not yet ready for publication

## Conventions

**Filename numbering prefix:** Four-digit zero-padded sequential number reflecting authoring order. Posts numbered 0001-NNNN by body Date ascending; same-day clusters ordered by methodology-arc sequence (the order in which the substantive work documented in posts was performed). Filenames sort by reading order. Slots may be retracted (with the slot-number gap preserved as visible audit record) when a duplicate or other auditable issue surfaces post-publication; see SUMMARY.md for the canonical record of any retracted slots.

**Body Date field:** The frontmatter `**Date:**` field reflects authoring Date: when the substantive work documented in the post was performed. Authoring Date is the basis for filename numbering order.

**Frontmatter structure:** Posts use Markdown frontmatter with `**Author:**`, `**Date:**`, and `**Status:**` fields, followed by an italic disclosure note acknowledging AI writing assistance. This convention was tightened partway through the corpus; posts 0026-0035 (10 files) carry partial frontmatter omissions that are preserved per the immutability convention rather than back-applied (parallel to the em-dash legacy gap documented in `methodology/post_audit_checklist.md`). The CI audit enforces frontmatter consistency from post 0036 onward.

**Post-naming pattern:** `NNNN-kebab-case-slug.md` where NNNN is four-digit zero-padded number reflecting authoring order convention above.

## Author

Jimmy McColery: building methodology research tools for AI-assisted work.
