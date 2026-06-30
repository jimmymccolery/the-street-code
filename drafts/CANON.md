# Canon-vs-Brief Boundary — Recommendation

**Filed:** 2026-06-29
**Scope:** Where canonical NPC-philosophy + architecture lives, and how publication briefs in `drafts/` should reference it.
**Companion to:** `drafts/INDEX.md`

---

## The problem

The 22 publication briefs in `drafts/` (see INDEX.md) embed substantive architectural commitments inside each post-shaped artifact:

- Three-layer memory architecture + DC1 valence/arousal/stress split
- HEXACO for cooperation/exploitation + attachment for relational encoding
- Pair-relational sentiment with sentiment-override (Hawkins-Carrère-Gottman 2002)
- 0.995/game-hour decay anchor + yearly consolidation pass
- Position-(a) structural-only sophisticated active inference + state-space-content boundary
- 4-audit mandatory test surface + 3 retraction-condition triggers
- 5-element cross-cultural disclosure discipline
- WEIRD-defaults schema placeholders + Cross/Crenshaw V1 scope-down

These are **load-bearing for Memory Lanes + Room To Life + future management sims + future city sims**. If they only live inside drafting briefs, two failure modes follow:

1. **Drift between briefs:** brief-post-90 says one thing about attachment encoding; brief-post-95 says something subtly different; the V1 implementation diverges from both. No single source of truth.
2. **Drift between products:** Memory Lanes implements one version; a future sim implements a slightly different version because the canon was scattered across briefs that no one re-read.

A brief is meant to source ONE blog post. A canon doc is meant to be referenced by N posts + N products. Different artifacts; different lifecycle.

---

## What canon currently looks like (empirical state, 2026-06-29)

**The de facto canon today lives in `~/Projects/Open Alley/architecture/`:**

| File | Lines | What it covers |
|---|---|---|
| `modified-c-bis-ratification-2026-06-09.md` | 315 | Modification 6 ratification; Episodic vs Diachronic axes; Wiredu personhood-as-achievement grounding |
| `modified-c-bis-canonical-citations-2026-06-09.md` | 450 | Canonical citation chain; primary-text verification; F-8 through F-18 flag history |
| `emotion-conditioned-encoding-three-layer-memory-2026-06-09.md` | 460 | Three-layer architecture; emotion-conditioning at encoding time; Layer 3 DC1 split |
| `sim-ai-phase-1-build-scope-2026-06-11.md` | 300 | Phase 1 empirical validation scope; cultural baseline test matrix |
| `round-9-r4-canonical-generative-model-spec-2026-06-11.md` | ~200 | Generative model formalization + active inference + striving targets |
| `cross-crenshaw-elevation-and-v1-scope-down-2026-06-09.md` | ? | Cross/Crenshaw V1 SCHEMA-PLACEHOLDER ratification |
| `wiredu-moral-danger-primary-text-defense-2026-06-09.md` | ? | Primary-text defense; Wiredu Ch 9 quote bank |

**Room To Life's sim-ai code references these Open Alley files as canonical** (verified in code comments at `~/Projects/roomtolife/src/lib/sim-ai/a7Memory.ts`, `layer3Accumulators.ts`, `culturalBaselines.ts`, `inferenceLoop.ts`, `strivingTargets.ts`).

**Open Alley's own `build-cycle-13-pinboy-subsystem-design-lock-cascade.md` declares Room To Life Universe as the intended canonical NPC philosophy home** for cross-product subsystems — but Room To Life doesn't have that home yet. There's an empty seat.

---

## The recommendation

**Short-term (NOW through V1 ship): keep canon in Open Alley/architecture/. Don't migrate.**

Reasoning:
- The work is already there. Migrating mid-arc costs days and creates risk (broken cross-refs in active code).
- Briefs already reference Open Alley paths. The pattern works.
- Memory Lanes V1 ships from Open Alley; the canon being co-located with the ship target is correct for V1.
- Migration cost > migration benefit until you start a SECOND product that needs to share the canon.

**Cross-link discipline to formalize:**
1. Every publication brief in `drafts/` cites the relevant Open Alley canonical file by path at the top of the brief's "Key citations" section
2. Every Open Alley canonical file lists the publication briefs that translate it (so drift in canon flags affected briefs)
3. Room To Life code comments continue to reference Open Alley canonical paths (already the case)
4. `the-street-code/research/citations/modified-c-bis-canonical-citations.md` stays as the cross-product citation index (already serves this role)

**Medium-term (Memory Lanes V1 ships → V1.x): consolidate citation index into Room To Life.**

When Memory Lanes V1 is shipped and a second sim/product enters scoping, MIGRATE per Open Alley's build-cycle-13 framing:

- Source: `~/Projects/Open Alley/architecture/*.md`
- Destination: `~/Projects/roomtolife/_workspace/architecture/*.md`
- Naming convention: `YYYY-MM-DD_topic-canonical.md` (matches Room To Life's existing `_workspace/design-notes/` pattern)
- Open Alley/architecture/ files become symlinks OR stubs pointing to Room To Life canonical home
- Memory Lanes-specific applications (e.g., Pin Paradise NPC roster, pinboy subsystem) stay in Open Alley
- General NPC-philosophy + memory architecture + cross-cultural discipline + active-inference spec moves to Room To Life

This makes Room To Life the ecosystem-canonical-home that Open Alley's build-cycle-13 envisioned. Avoid this migration until V1 ships — the cost of moving + the cost of broken cross-refs is real, and there is no benefit until product #2.

**Long-term (Steam V1.0 + new products): Room To Life owns canon; products consume.**

Once Room To Life is the ecosystem canonical home:
- New management sims spec by reading Room To Life canonical files
- City sims that need NPC philosophy reference the same canon
- Publication briefs in the-street-code continue translating canon → public posts
- Room To Life canon evolves with each product's empirical contact; canon updates trigger affected-brief re-verification

---

## Smallest concrete first step (today, no migration)

**Action 1: Add a "Canon source" line to every brief in `drafts/`.**

For each brief, add a single line near the top under "Status":

```markdown
**Canon source:** `~/Projects/Open Alley/architecture/modified-c-bis-ratification-2026-06-09.md` (for Modification N) + any other canonical files this brief depends on
```

This formalizes the brief-references-canon pattern. Takes ~30 min for all 22 briefs.

**Action 2: Add a reverse-index to the master citation file.**

In `~/Projects/the-street-code/research/citations/modified-c-bis-canonical-citations.md`, add a section "Briefs that translate this canon":

```markdown
## Brief translation index
- Modification 5 (cross-cultural disclosure): briefs 84, 92, 99, 100, 101, 102
- Modification 6 (Episodic vs Diachronic axes): briefs 83, 94, 95
- Three-layer memory architecture: briefs 90, 91, 93, 95, 97, 98
- ...
```

When canon updates, this index tells you which briefs need re-verification. Takes ~30 min.

**Action 3: Don't migrate. Don't restructure. Don't create a `roomtolife/foundations/` folder yet.**

Wait until V1 ships. The discipline cost of premature consolidation is higher than the friction of cross-project paths.

---

## What this recommendation does NOT do

- Doesn't lock in the Open Alley → Room To Life migration timing (operator decides post-V1 based on actual second-product scoping)
- Doesn't change the cross-cultural disclosure discipline (5-element commitment is canon-location-independent)
- Doesn't substitute for primary-text reads (canon depends on operator-side primary-source verification regardless of where the canon file lives)
- Doesn't preempt Room To Life's own canonical-naming convention if it differs (Room To Life uses `YYYY-MM-DD_topic-canonical.md` in `_workspace/design-notes/`; canon files would inherit that pattern on migration)

---

## Open question for operator

The implicit assumption above: **Memory Lanes V1 ships before any second product enters scope.** If that ordering changes (e.g., you decide to start a city sim BEFORE V1 ships), the migration moves up. Flag if the ordering assumption breaks; CANON.md gets revised.
