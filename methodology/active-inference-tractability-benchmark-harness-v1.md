# Active-Inference Tractability Benchmark Harness Execution Guide

**Established:** 2026-07-01 (post-Council-#3-close session; ablation-gate-relationship-mode-v1.md sibling artifact)
**Maintained by:** operator; Claude Code updates on empirical contact
**Purpose:** Standalone-executable operational procedure for the Swift on-device benchmark harness that adjudicates sophisticated active inference tractability at consolidation-pass cadence per Council #3 close. Any fresh CC session, fresh substrate, or future-operator can open this file with zero prior context and run the harness end-to-end.
**Provenance:** Council #3 (Active-Inference Tractability Under Realistic Branch Factors) closed 2026-07-01 at Pattern B ADOPT-FOLD via Option B per-item deliberation. ADOPT half executed as posts 0131 + 0132 plus Post 0119 operational-contract amendment. This guide is the BANK half — the operational procedure the operator schedules pre-V1 before committing to the ~130-230h sophisticated-active-inference apparatus build.

---

## What this guide is and is NOT

**This guide is** the standalone-executable operational procedure for the benchmark harness. It enumerates the harness components with specific Swift implementation targets; the fractional sweep design; the metrics collection via XCTest + OSSignposter; the pymdp correctness oracle; the three-tier verdict adjudication with specific pass/fail thresholds; the per-phase cost estimates; the failure modes and fallbacks.

**This guide is NOT** the architectural spec for the harness (post 0132 in this arc is the spec at meta-architecture level) or the narrative of how Council #3 arrived at the harness (post 0131 in this arc is the narrative) or the substrate outputs themselves (archived at `~/Projects/the-street-code/_archive/2026-07-01-council-3-active-inference-tractability/`).

---

## The three-tier verdict the harness produces

All measurements target N=100 NPCs at τ=3 across A ∈ {3,5,8} × b_o ∈ {2,3,4} × pruning-toggle. The verdict tier depends on outcomes at the target cells:

**Tier 1 PASS — V1-CRITICAL runtime-critical claim upheld.** At N=100, in at least one deployable regime, p95 per-frame AI utilization ≤ ~10ms AND zero budget-overrun frames over a 10-game-year replay, with A ≥ 5 and τ = 3.

**Tier 2 CONDITIONAL PASS — V1-CRITICAL as consolidation-pass machinery.** N=100 fails R1 (per-frame) but passes R3 (consolidation) with p95 slice ≤ ~10ms AND total pass latency amortizable within one consolidation window. Player-facing consolidation-pass tolerance: 30s-10min band per operator judgment.

**Tier 3 FAIL — DEMOTE-TO-AUDIT-METAPHOR.** Even R3 at N=100, A=3, τ=3 with pruning cannot keep time-sliced per-frame contribution under budget. Triggers Path-A-ratification re-evaluation.

---

## Phase 1 — Harness skeleton (~0.5 day = 4h)

**Objective:** produce the XCTest measure scaffolding + Swift struct definitions for the five mocked components.

1. Create new Swift Package or add XCTest target to existing project. Set optimization to `-O` / whole-module optimization for measurement builds.
2. Define mocked NPC state struct: `NPCState` with `beliefs: [Float]` (n_s × n_f = 32 defaults). Contiguous memory layout for `Accelerate`/`simd` friendliness.
3. Define mocked generative model: `GenerativeModel` with `A: [[Float]]` (likelihood; n_o × n_s) + `B: [[[Float]]]` (transition; n_s × n_s × n_actions). Populate with plausible sparse-ish values (Dirichlet-drawn or block-sparse).
4. Define mocked action-set generator: `ActionSet.generate(context:, cardinality:)` returning `[Action]` of size in {3, 5, 8}.
5. XCTest scaffolding: `XCTestCase` subclass with `measure(metrics: [XCTClockMetric(), XCTCPUMetric()], options:)` for the microbenchmark and `OSSignposter` instrumentation for the integration cells.
6. Verify skeleton compiles + runs empty measure block at approximately 0µs baseline.

---

## Phase 2 — Sophisticated policy evaluator (~1-1.5 days = 8-12h)

**Objective:** implement the recursive EFE tree per Friston 2021.

1. `SophisticatedEvaluator.evaluate(state:, model:, actions:, horizon:, b_o:, pruningThreshold:)` recursive function.
2. At depth d, branch over `actions.count` (=A) candidate actions.
3. For each action, branch over `b_o` predicted outcomes weighted by predictive probability.
4. Recurse to depth τ; terminate when d = τ OR when action prior falls below pruning threshold (Friston 2021's 1/16 example anchor) OR when outcome predictive probability falls below same.
5. Compute EFE per leaf: KL(Q(s'|π) || P(s')) + expected utility per Friston 2021 equation (paper's canonical decomposition).
6. Return best-action-index per top-of-tree action-utility ordering.
7. Expose `pruningEnabled: Bool` toggle to permit measurement with and without Occam-window pruning.
8. Use `Accelerate.vDSP` or `simd_float4` for the B·Q matrix-vector products; use `Accelerate.vvlogf` for the log evaluations in KL computation. Avoid `Foundation` math per node — the pessimistic column is 10-20µs/node driven exactly by `Foundation` overhead.

---

## Phase 3 — Correctness oracle via pymdp (~0.5 day = 4h) [OPTIONAL BUT RECOMMENDED]

**Objective:** cross-verify Swift EFE numbers against pymdp (arXiv:2201.03904; https://github.com/infer-actively/pymdp) on a toy POMDP.

1. Install pymdp in a Python environment: `pip install inferactively-pymdp`.
2. Define the same 32-state POMDP toy problem in pymdp: same A + B matrices, same action set, same τ.
3. Export Swift's per-decision EFE scores for the toy problem via CSV.
4. Run pymdp's sophisticated inference on the same toy; export same EFE scores.
5. Diff. Discrepancies > 1% indicate an implementation bug in the Swift evaluator; fix before proceeding to timing measurements.

**Why this matters:** the harness's timing numbers are worthless if the evaluator isn't computing sophisticated-scheme EFE correctly. pymdp is the community-canonical reference implementation; matching it validates the Swift port at correctness level even though the timing numbers themselves must come from Swift (pymdp is JAX/NumPy-batched; timing numbers are non-transferable).

---

## Phase 4 — Many-NPC driver + three regimes (~1 day = 8h)

**Objective:** aggregate single-decision cost measurements into population-scale wall-clock envelopes at each regime.

1. `RegimeDriver.runR1(npcs:, evaluator:, frames:)` — every NPC re-decides every frame. Measure total per-frame time.
2. `RegimeDriver.runR2(npcs:, evaluator:, frames:)` — stagger NPCs so ~3-4 decide per frame. Measure per-frame time slice.
3. `RegimeDriver.runR3(npcs:, evaluator:, windowGameYears:)` — batched at consolidation boundary. Measure total pass time + time-slice contribution when spread across real frames.
4. `OSSignposter` intervals: bracket each regime's per-frame or per-consolidation-pass work with `OSSignpostInterval` for Instruments-readable measurements.
5. Deploy to minimum-spec target device (per operator's V1 target device). Run on-device, NOT in simulator (thermal + scheduling behavior differs materially).
6. Instruments profile with signposts + CPU counters. Export as `.trace` alongside CSV.

---

## Phase 5 — Sweep automation + statistical rigor (~0.5-1 day = 4-8h)

**Objective:** run the fractional sweep + produce distributions with confidence intervals per Kalibera + Jones 2013 discipline.

1. Fractional sweep design: A(3) × τ(3) × b_o(3) = 27 microbenchmark cells + N(1=100) × A(3) × regime(3) = 9 integration cells = 36 total cells.
2. Per cell: warmup (5 iterations discarded) + measurement (30+ iterations). Report median + MAD + bootstrap 95% CI + Tukey outlier count.
3. Automate sweep via Swift `XCTestCase` parameterized over cell configs.
4. Export as CSV: one row per cell × iteration.
5. Statistical pass via Python (pandas + scipy): compute per-cell median, MAD, bootstrap CI, outlier counts.
6. Plot: per-cell median with error bars; per-cell overrun-frame counts; per-cell peak transient memory.

---

## Cost aggregation

| Phase | Hours |
|---|---|
| Phase 1 — Harness skeleton | ~4h |
| Phase 2 — Sophisticated evaluator | ~8-12h |
| Phase 3 — pymdp correctness oracle | ~4h (optional but recommended) |
| Phase 4 — Many-NPC driver + regimes | ~8h |
| Phase 5 — Sweep automation + statistics | ~4-8h |
| **Total** | **~28-36h** (3.5-4.5 focused solo dev-days) |

Cost aligns with Substrate B's own itemized breakdown from Council #3 substrate output. The Council brief's original characterization was ~30-40h; Substrate B's actual figure is ~28-36h at 8h dev-days. Fits within Substrate C's cut-candidate headroom (40-80h available via methodology maintenance reduction + Councils #2/#4/#5 defer-to-post-V1).

---

## Post-harness decision matrix

Once the harness runs and produces measurements:

**If Tier 1 PASS:** proceed with sophisticated-inference apparatus build at V1 as runtime-critical machinery. The 130-230h apparatus build (per Post 0119 line 59 audit-layer apparatus + Post 0119 line 67 four-audit surface + Post 0123 line 87 cached-policies infrastructure) proceeds with confidence. Update Post 0131 + Post 0132 with dated update-notes documenting the Tier 1 empirical outcome.

**If Tier 2 CONDITIONAL PASS (expected outcome):** proceed with sophisticated-inference apparatus build at V1 as consolidation-pass machinery specifically. The apparatus build proceeds with the specific consolidation-pass regime parameters the harness validated (specific b_o value; specific pruning threshold; specific expansion budget K). Update Post 0131 + Post 0132 with dated update-notes documenting the Tier 2 empirical outcome and the specific validated parameters.

**If Tier 3 FAIL:** demote sophisticated active inference to non-runtime audit metaphor. Trigger Path-A-ratification re-evaluation. Update Post 0131 + Post 0132 + Post 0119 with dated update-notes documenting the DEMOTE outcome. The 130-230h apparatus build is retired at near-zero apparatus-build sunk cost (only the ~28-36h harness cost is sunk). Draft new post documenting the Path A ratification re-evaluation.

---

## Failure modes + fallbacks

**Failure mode 1: Swift + Xcode fluency ramp exceeds Substrate B's fluent-baseline assumption.** Fallback: extend Phase 1 + Phase 2 timelines by 4-8h each for less-fluent operators. If fluency ramp exceeds 2x the baseline estimate, redirect to pymdp-only sweep at lower rigor (loses on-device Apple silicon per-node µs precision but provides directional answer).

**Failure mode 2: Instruments on-device profiling produces unreadable traces due to thermal throttling.** Fallback: run in cool environment; add cooldown intervals between sweep cells; verify device temperature via Xcode Instruments thermal-state indicator before each measurement pass.

**Failure mode 3: pymdp correctness oracle diverges from Swift by > 1% and root cause not found.** Fallback: accept Swift-only measurement with explicit disclaimer that correctness is unverified against community-canonical reference. Note as HIGH-severity limitation in the harness output. Do NOT proceed to canonical-mutation execution without either (a) resolved oracle diff or (b) explicit operator judgment accepting the residual correctness uncertainty.

**Failure mode 4: Sweep cell measurement produces bimodal distribution rather than unimodal.** Fallback: increase per-cell iteration count from 30 to 100+; investigate whether E-core vs P-core scheduling is the cause via XCTCPUMetric readings. If bimodality persists, report both modes separately with explicit distribution shape flag.

**Failure mode 5: Total pass latency (Metric 2) exceeds player-facing tolerance band (Substrate C's 30s-10min inference).** Fallback: this is not a harness failure; it is a Tier 3 FAIL verdict outcome. Proceed to DEMOTE decision-matrix branch.

---

## Cross-references

- **Post 0131** — Council #3 close narrative; documents Pattern B ADOPT-FOLD adjudication + Riders 1-3 + terminology refinement
- **Post 0132** — Harness architectural spec at META level + Post 0119 operational-contract amendment (B_max + pruning budget + K expansion + interruptibility)
- **Post 0119** — Original audit-first sequencing post; operational contract being amended
- **Post 0120** — V1 spec; 2026-10-31 ship target
- **Post 0123** — Cached policies + slow consolidation pattern; Tier 2 architecture the harness measures
- **Post 0129** — Council #1 close narrative; Rule 14 Pattern B canonical case study
- **Post 0130** — Council #1 spec; ablation gate parallel to this harness gate
- **`~/Projects/the-street-code/methodology/ablation-gate-relationship-mode-v1.md`** — sibling methodology artifact; Council #1 BANK half execution guide
- **`~/Projects/the-street-code/_archive/2026-07-01-council-3-active-inference-tractability/`** — Council #3 substrate outputs + orchestrator synthesis
- **`~/.claude/projects/-Users-jimmy/memory/project_council_3_close_pattern_b_2026-07-01.md`** — Council #3 arc close memory
- **Friston et al. 2021** — https://doi.org/10.1162/neco_a_01351 — sophisticated-scheme canonical anchor; 1/16 pruning-threshold example
- **Champion et al. 2022** — https://doi.org/10.1016/j.neunet.2022.03.036 — BTAI/MCTS complexity-reduction; O([K+t]×|S|) space complexity
- **de Vries 2023** — https://arxiv.org/abs/2307.14145 — sparse factor-graph + interruptibility
- **pymdp** — https://github.com/infer-actively/pymdp + arXiv:2201.03904 — community-canonical reference implementation for correctness oracle

---

## Guide revision protocol

Update this guide when:
- The harness runs and surfaces procedure refinements (Phase 1-5 timing corrections; sweep design refinements; oracle diff-resolution patterns)
- Apple silicon generation changes shift the per-node µs envelope (A20+ devices)
- pymdp community reference implementation updates affect the correctness oracle
- Framework canonical files this guide cross-references (Post 0119 + 0131 + 0132) update in ways that affect guide content
- Rule 14 Pattern B classification vocabulary evolves

Do NOT retroactively edit the guide's core procedure after harness execution begins; per the framework's immutability convention, mid-execution scope changes are anti-pattern territory. Append dated update-notes at guide foot instead.
