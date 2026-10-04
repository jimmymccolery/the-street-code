# Phase 3.8.1 Ship 6 — UI Extensions — SHIPPED
## Council #11 Candidacy Artifact

**Filed:** 2026-07-12
**Status:** RATIFY-PROVISIONAL
**Ship commits:** roomtolife pushed

---

## §1 Scope

Post-substrate cascade UI extensions per Phase 3.8.1 v.next. Zero substrate mutations; UI only.

## §2 Extensions

### 1. IslandSimulation N-tab switcher at K>2
Replaces `CharacterViewersRow` flex row when `effectiveSimCount > 2`. Horizontal tab-strip at K=3..8 (~90 px/tab; 800 px fits 8). K=2 preserves side-by-side row bit-identical. K>8 dropdown deferred to Phase 3.8.2.
- `activeSimTab: SimId` useState<SimId>('a') at line 205
- Conditional render dispatch at `effectiveSimCount > 2 ? NSimTabSwitcher : CharacterViewersRow` at ~line 2311
- `NSimTabSwitcher` helper component at bottom of file

### 2. CharacterViewer 8-color SIM_AURA_PALETTE
`SIM_AURA_PALETTE: Record<string, string>` const map:
- `a`: `#ff3a4a` red (preserved bit-identical)
- `b`: `#4dd4ff` cyan (preserved bit-identical)
- `c`: `#fbbf24` yellow
- `d`: `#22c55e` green
- `e`: `#ec4899` magenta
- `f`: `#f97316` orange
- `g`: `#3b82f6` blue
- `h`: `#f472b6` pink

`getSimAuraColor(simId)` helper with djb2-hash-mod fallback across `FALLBACK_AURA_PALETTE` for out-of-canonical SimIds beyond 'h'.

### 3. CrossPlaneCouplingMatrix aggregate-over-N (Option A)
- Optional `simCount?: number` prop on §13 CrossPlaneCouplingMatrix
- Renders `N=K` badge in panel header when `simCount > 2`
- Tooltip surfaces pair-count = K*(K-1)/2 for aggregation semantics discoverability
- K=2 or omitted → no badge (bit-identical UI)

### 4. buildSimExtraContent factory dispatch
`buildSimExtraContent(simId)` factory dispatching:
- `'a'` → existing `simAExtraContent` (bit-identical)
- `'b'` → existing `simBExtraContent` (bit-identical)
- `'c'`-`'h'` → minimal N-Sim placeholder rendering per-Sim Needs/Layer3/Status/SimIntentPanel/ExtendedStatePanel from `state.sims[simId]`

## §3 Ship Verification

- roomtolife `npm run precheck`: GREEN (Next.js 16.2.6 Turbopack build + TypeScript typecheck pass clean)
- Lint errors present but all pre-existing (`useItemDrag.ts` + `.current` reads in `IslandSimulation.tsx` lines 1784-2912; none introduced by Ship 6)

### K=2 preservation verified
At `effectiveSimCount === 2` (or 1), the ternary at IslandSimulation:2311 falls through to original `CharacterViewersRow` block unchanged. `simCount={effectiveSimCount}` passed to CPCM causes N=K badge to render only at `simCount > 2` (identical UI at K=2). `simAExtraContent`/`simBExtraContent` blocks LITERALLY unchanged.

## §4 LOC Breakdown

| File | Added | Removed | Net |
|------|-------|---------|-----|
| `CharacterViewer.tsx` | 58 | 0 | +58 |
| `IslandSimulation.tsx` | 325 | 13 | +312 |
| `IslandStage345Panels.tsx` | 34 | 1 | +33 |
| **Total** | **417** | **14** | **+403** |

Target was ~690 LOC. Actual +403 net (below estimate).

## §5 Framework Methodology Firsts

- FIRST N-tab UI switcher for N-Sim viewer selection
- FIRST 8-color SIM_AURA_PALETTE with djb2-hash-mod fallback
- FIRST aggregate-over-N CrossPlaneCouplingMatrix with N=K badge + pair-count tooltip
- FIRST dispatch-wrapper preservation of existing 2-Sim blocks (bit-identical guarantee via literal code path preservation)

## §6 Deviations from Spec

**`buildSimExtraContent` factory shape:** Design called for full factory extraction. Ship implements dispatch wrapper preserving `simAExtraContent`/`simBExtraContent` as-is for 'a'/'b' branches. Rationale: the two existing blocks reference many outer-closure refs (`memoryGateHistoryARef`, `hexacoSnapshotRef`, `latestBiasForA`, `phase15Enabled`, `sessionLogRef.current.entries`, etc.) that are 2-Sim-shaped hard-coded — a true parameter-generic extraction would require substantial ref refactoring, which is out of the UI-only Ship 6 scope and touches K=2 preservation surface unnecessarily.

The dispatch pattern satisfies the load-bearing "K=2 preservation" requirement mechanically (a/b branches are literally the same code path), and K > 2 SimIds get a minimal but functional per-Sim panel matching what group substrate `SimStateSnapshot` universally exposes.

**Deep observability panels for K > 2 SimIds** (memory / approach-bias / rescue-choice / diagnostic sidebar) documented as deferred to Phase 3.8.2, matching Tier 8.1 §7 per-Sim panel-symmetry discipline precedent.

**LOC below estimate (~403 net vs ~690 target)** due to dispatch pattern avoiding duplication of ~250-line existing 'a'/'b' blocks.

## §7 Council #11 Candidacy

**Item 237 filed:** Phase 3.8.1 Ship 6 UI extensions ratification.

Sub-items:
- 237.1 N-tab switcher discipline (K=2 preservation + K>2 activation)
- 237.2 SIM_AURA_PALETTE 8-color + djb2 hash-mod fallback
- 237.3 CrossPlaneCouplingMatrix aggregate-over-N + N=K badge
- 237.4 buildSimExtraContent dispatch wrapper (vs full factory extraction) — deferred deep observability panels to Phase 3.8.2

## §8 Downstream Impact

**Awaiting Ship 7** H4 N=8 performance harness landing (in parallel flight). Once S7 lands, Phase 3.8.1 substrate + UI + harness triad COMPLETE. **Ship 8** close-out consolidation follows.

---

**Filed by:** Claude Opus 4.7 (1M context) via Claude Code
**Session ID:** c70eb795-58d8-4708-933f-acae498a56ce
