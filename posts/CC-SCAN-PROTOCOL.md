# The Street Code — CC-SCAN-PROTOCOL.md

**Purpose:** Documents how CC should navigate the 4-layer scan pyramid for post consultation. Optimized for minimum token cost + maximum relevance identification.

**Filed:** 2026-07-05 evening
**Applies to:** All CC sessions consulting `~/Projects/the-street-code/posts/`

---

## The 4-Layer Scan Pyramid

```
Layer 1: POSTS-INDEX.md                    (~50KB flat greppable index)
         │
         ↓ filter by project/task/phase/discipline
         │
Layer 2: POSTS-BY-{VIEW}.md                (~20KB specialized views)
         │
         ↓ identify specific relevant posts
         │
Layer 3: CC-OPTIMIZED-SUMMARY blocks       (200-400 word distillations at top of each post)
         │
         ↓ fetch full body only if summary insufficient
         │
Layer 4: Full post bodies                  (2000-2600 words each; final fallback)
```

**Rule of thumb:** Never open Layer 4 (full post body) without first consulting Layer 3 (summary block). Never open a post at random without first checking Layer 1 (flat index) or Layer 2 (specialized view).

---

## Layer 1: POSTS-INDEX.md (master flat index)

**When to consult:**
- Any post-scoped work session
- Verifying whether a specific post exists
- Checking post metadata (date + status + supersession)
- Discovering posts by any combination of tags

**How to use:**
```bash
# Filter by project
grep "proj:sim-ai" ~/Projects/the-street-code/posts/POSTS-INDEX.md

# Filter by CC task
grep "task:character-authoring" ~/Projects/the-street-code/posts/POSTS-INDEX.md

# Filter by phase
grep "phase:Phase-3" ~/Projects/the-street-code/posts/POSTS-INDEX.md

# Filter by discipline
grep "discipline:Rule-20" ~/Projects/the-street-code/posts/POSTS-INDEX.md

# Filter by multiple criteria (AND)
grep "proj:sim-ai" ~/Projects/the-street-code/posts/POSTS-INDEX.md | grep "phase:Phase-3"

# Filter to posts with v1.0 summary block
grep "v1-block:yes" ~/Projects/the-street-code/posts/POSTS-INDEX.md

# Filter to superseded posts (check for supersession-by or supersedes)
grep "supersed" ~/Projects/the-street-code/posts/POSTS-INDEX.md
```

**Output format:** One line per post: `{post_id} | {date} | {title} | proj:X | task:Y | phase:Z | discipline:D | status:S`

---

## Layer 2: POSTS-BY-{VIEW}.md (specialized views)

**Available views:**
- `POSTS-BY-PROJECT.md` — grouped by sim-ai + pin-paradise + open-alley + roomtolife + 90s-life-builder + street-code + cross-cutting
- `POSTS-BY-CC-TASK.md` — grouped by character-authoring + empirical-BUILD + methodology-research + multi-substrate-audit + Marcus-Reed-audit + anti-fabrication + operator-realism-check + canonization-propagation + deployment-verification + council-methodology + personality-architecture + memory-architecture + cross-cultural-personhood + framework-research + substrate-methodology + discipline-enforcement + verification-validation
- `POSTS-BY-PHASE.md` — grouped by era-independent + Phase-1 + Phase-2 + Phase-3 + Phase-4+
- `POSTS-BY-DISCIPLINE.md` — grouped by Rule-14-Madisonian + Rule-19-anti-fabrication + Rule-20-Family-A + Rule-11-substrate-specialization + operator-realism-check + verify-against-canonical-files + post-audit-correction
- `POSTS-SUPERSESSION-CHAIN.md` — tracks 4 active supersession chains + meta-discipline

**When to consult:**
- Working within a specific project scope → `POSTS-BY-PROJECT.md`
- Enforcing or extending a discipline → `POSTS-BY-DISCIPLINE.md`
- Executing a task class → `POSTS-BY-CC-TASK.md`
- Phase-specific empirical BUILD work → `POSTS-BY-PHASE.md`
- Following supersession chains → `POSTS-SUPERSESSION-CHAIN.md`

**How to use:**
```bash
# Read specific view file
cat ~/Projects/the-street-code/posts/POSTS-BY-PROJECT.md

# Or grep across all views
grep "Fires A-F" ~/Projects/the-street-code/posts/POSTS-BY-*.md
```

---

## Layer 3: CC-OPTIMIZED-SUMMARY blocks (in-post distillations)

**When to consult:**
- After identifying specific relevant posts via Layer 1 or Layer 2
- Before opening full post body
- Verifying post is applicable to current work

**How to use:**
```bash
# Grep summary blocks across all posts (finds keyword within blocks)
grep -A30 "CC-OPTIMIZED-SUMMARY" ~/Projects/the-street-code/posts/*.md | grep "your keyword"

# Extract just the summary block from a specific post
sed -n '/CC-OPTIMIZED-SUMMARY/,/-->/p' ~/Projects/the-street-code/posts/0170-*.md
```

**Summary block format (v1.0):**
```
<!-- CC-OPTIMIZED-SUMMARY v1.0
post_id: NNNN
domain: 1-line description
canonical_rule: canonical rule this post establishes or references
load_bearing_claims:
  - claim 1
  - claim 2
applicability_triggers:
  - trigger 1
mechanism_details:
  - mechanism 1
cross_refs:
  - reference 1
-->
```

**Status:** 41 posts have v1.0 blocks as of 2026-07-05 evening. Retrofit of 128 posts to v1.0+ blocks scheduled.

---

## Layer 4: Full post bodies (2000-2600 words each)

**When to consult:**
- Layer 3 summary insufficient for current work
- Need direct quote for citation
- Verifying summary block accuracy
- Discovering nuance not captured in summary

**How to use:**
```bash
cat ~/Projects/the-street-code/posts/0170-*.md
```

**Cost:** Highest token cost (2000-2600 words). Avoid unless Layer 3 explicitly insufficient.

---

## Search patterns by task class

### Task: "Working on Sim AI Fire A/B/C reshape"
```bash
# Layer 1: filter to sim-ai + empirical-BUILD
grep "proj:sim-ai" POSTS-INDEX.md | grep "task:empirical-BUILD"

# Layer 2: consult sim-ai section of POSTS-BY-PROJECT.md
# Layer 3: read summary blocks of Posts 0170, 0171 (Fires A-F narrative)
# Layer 4: fetch full body only if operator-realism-check details insufficient
```

### Task: "Character-authoring new PROPER_ANCHOR"
```bash
# Layer 1: filter to character-authoring task
grep "task:character-authoring" POSTS-INDEX.md

# Layer 2: consult character-authoring section of POSTS-BY-CC-TASK.md
# Layer 3: read summary blocks of Posts 0070 (Marcus Reed), 0146 (Ten Layers), 0169 (sub-shape 23), 0172 (Item 0334 retirement)
# Additional: consult ~/Projects/sim-ai/framework-research-index.md Character Generation Methodology section
```

### Task: "Council #8 methodology deployment preparation"
```bash
# Layer 1: filter to council-methodology + canonization-propagation
grep "task:canonization-propagation" POSTS-INDEX.md
grep "task:council-methodology" POSTS-INDEX.md

# Layer 2: consult POSTS-BY-DISCIPLINE.md for Rule 20 Family A + operator-realism-check + verify-against-canonical-files sections
# Layer 3: read summary blocks of Posts 0143, 0163, 0164, 0167, 0168, 0170, 0171, 0172
# Also: read methodology proposal at ~/Projects/the-street-code/methodology/post-audit-discipline-consolidated-proposal-for-council-8-2026-07-05.md
```

### Task: "Deploying framework changes to Vercel"
```bash
# Layer 1: filter to deployment-verification
grep "task:deployment-verification" POSTS-INDEX.md

# Layer 3: read summary blocks of Posts 0157 (tsconfig alias), 0158 (Rule 19 operational), 0165 (5 seconds late)
```

### Task: "Understanding cross-substrate methodology"
```bash
# Layer 1: filter to multi-substrate-audit
grep "task:multi-substrate-audit" POSTS-INDEX.md

# Layer 2: consult multi-substrate-audit section of POSTS-BY-CC-TASK.md
# Layer 3: read summary blocks of Posts 0039, 0040, 0061, 0087, 0090, 0110
```

---

## Multi-view intersection patterns

**Finding posts that match multiple criteria:**

```bash
# Sim AI + character-authoring + Phase-3
grep "proj:sim-ai" POSTS-INDEX.md | grep "task:character-authoring" | grep "phase:Phase-3"

# All operator-realism-check discipline posts
grep "discipline:operator-realism-check" POSTS-INDEX.md

# Cross-cutting posts about verification
grep "proj:cross-cutting" POSTS-INDEX.md | grep -E "task:(anti-fabrication|verification-validation|operator-realism)"
```

---

## Supersession-aware scanning

**When encountering a post reference in memory / framework-research-index / other posts, check supersession status:**

```bash
# Check if post is superseded at any scope
grep "^{post_id}" POSTS-INDEX.md | grep -E "supersess|supersedes"

# Or consult POSTS-SUPERSESSION-CHAIN.md directly
grep -A5 "Chain.*{post_id}" POSTS-SUPERSESSION-CHAIN.md
```

**Current supersession chains (as of 2026-07-05 evening):**
- Post 0146 → 0150 (HEXACO citation)
- Post 0166 → 0167 (attribution overclaim)
- Post 0170 → 0171 (Fire E cooldown mechanic)
- Post 0169 → 0172 (Item 0334 retirement)

---

## Maintenance protocol

**Adding a new post:**
1. Add v1.0 or v2.0 CC-OPTIMIZED-SUMMARY block at top (Layer 3)
2. Add entry to POSTS-INDEX.md master flat index (Layer 1)
3. Add entry to relevant POSTS-BY-{VIEW}.md files (Layer 2)
4. If post supersedes a prior post at some scope, update POSTS-SUPERSESSION-CHAIN.md

**Retiring a canonical concept referenced across posts:**
1. Do NOT edit historical posts (per addendum-preserves-immutability)
2. Ship correction post following one of 4 supersession patterns
3. Update POSTS-SUPERSESSION-CHAIN.md with new chain
4. Update discipline family memory entries + Council #N proposal as applicable

**Regen sync:**
- POSTS-INDEX.md + view files are canonical; regen pipeline picks up on next sync
- Framework-research-index (both sim-ai project scope and global CLAUDE scope) should reference this file structure

---

## Token efficiency comparison

**Before scan protocol (worst case):**
- Read all 169 posts × ~2500 words = 422,500 words = ~625KB
- Realistic CC scan cost: ~500,000 tokens per session for full corpus consultation

**After scan protocol (typical case):**
- Read POSTS-INDEX.md (~50KB) + relevant Layer 2 file (~20KB) + 3-5 summary blocks (~2KB) = ~72KB
- Realistic CC scan cost: ~15,000 tokens per session

**Efficiency ratio: 33× token cost reduction for typical scan patterns.**

---

## Cross-references

- Master flat index: `POSTS-INDEX.md`
- Specialized views: `POSTS-BY-PROJECT.md`, `POSTS-BY-CC-TASK.md`, `POSTS-BY-PHASE.md`, `POSTS-BY-DISCIPLINE.md`
- Supersession tracking: `POSTS-SUPERSESSION-CHAIN.md`
- Framework research indexes: `~/Projects/sim-ai/framework-research-index.md` + `~/.claude/framework-research-index.md`
- Treasure Map: `~/.claude/cc_nav_payload.md`
- Council #8 methodology deployment proposal: `~/Projects/the-street-code/methodology/post-audit-discipline-consolidated-proposal-for-council-8-2026-07-05.md`
