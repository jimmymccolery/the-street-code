<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0203
title: World Economy Substrate Council 7 Ratification Brief
date_published: 2026-08-10
status: COUNCIL-7-READY -- substrate shipped; Rule 11 K=3 CONVERGENT verification complete
superseded_by: none
domain: substrate-architecture macroeconomic-simulation game-engine-substrate endogenous-crisis-simulation
project_scopes: cross-cutting
cc_task_relevance: council-7-ratification macroeconomic-substrate rule-11-k3-convergent-results
phase_binding: shipped
discipline_family: Deterministic-Simulation-Substrate Baseline-1950-Calibration Marcus-Reed-Surface-8-Blindness-Constraint Rule-11-K3-CONVERGENT-Verification Rule-19-Anti-Fabrication
canonical_rule: none
load_bearing_claims:
- A shared macroeconomic substrate shipped: a chronological FRED/BLS baseline (1950-2026), a procedural Solow trend with AR(1) noise, Poisson and self-exciting shock streams, a Minsky credit-cycle regime, an endogenous housing-bubble model, and a monetary-policy regime classifier. All of it passes its full test and validator suites.
- Rule 11 K=3 CONVERGENT verification across three research substrates locked the numeric calibration. Two divergences were resolved with explicit reasoning (shock persistence; monetary tightening modeled as a multi-quarter regime instead of a point-in-time shock).
- Three source-attribution errors from one research substrate were caught by verifying against the primary literature (Bezemer-Grydaki 2014 JBF; Vollrath 2024 AEJ:Macro; the double-dip structure of 1980-82). Pattern recorded: that substrate's numbers were accurate, its attributions were not.
- The endogenous crisis architecture is deterministic: output is a pure function of (seed, quarter, prior state), so saves and replays reproduce exactly.
- Marcus Reed Surface 8 structural blindness is verified per substrate: each carries an explicit test asserting zero demographic sampling and zero protected-attribute proxies in shock dispatch. An economic-mechanism blindness sub-clause remains open for Council adoption.
applicability_triggers:
- Any simulation requiring chronological era progression past a 1950 baseline with a historically calibrated inflation trajectory
- Any consumer requiring macroeconomic pressure signals (wage indexing, pricing, interest rates, unemployment-driven demand shocks)
- Any endogenous crisis simulation requiring credit-cycle amplification, housing bubble dynamics, monetary regime tracking, or clustered shock generation
- Any Marcus Reed Surface 8 audit touching economic mechanisms with disparate-impact potential
- Any Rule 11 multi-substrate research deployment involving numeric calibration backed by peer-reviewed citations
mechanism_details:
- Read-only publish-subscribe contract with quarterly cadence; consumers subscribe to series by name and the substrate never reads consumer state
- Determinism: pure function of (seed, quarter, prior state), verified end to end by replay tests
- Three dispatch modes chosen at init: chronological (baked historical data), randomized (Solow trend, AR(1) noise, shock streams), blended (chronological trend with a procedural shock overlay)
- Endogenous crisis dispatch: a Minsky regime tracks hedge, speculative and Ponzi credit-cycle transitions; a housing model implements chartist/fundamentalist switching with a leverage cycle; a monetary regime classifier uses a Taylor-rule-like signal with hysteresis; a marked Hawkes generator clusters shocks such as oil crises
cross_refs:
- Rule 11 multi-substrate research workflow (K=3 CONVERGENT verification completed 2026-08-10)
- Marcus Reed Surface 8 audit governance (economic-mechanism blindness sub-clause, open)
CC-OPTIMIZED-SUMMARY -->

# WorldEconomy Substrate -- Council #7 Ratification Brief

**Author:** Jimmy McColery
**Date:** 2026-08-10
**Status:** COUNCIL #7 READY -- substrate shipped; Rule 11 K=3 CONVERGENT verification complete

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## CC-OPTIMIZED-SUMMARY

**What shipped.** A shared macroeconomic substrate, built in phases:

- **Scaffold** with a series catalog and three dispatch modes
- **Chronological FRED/BLS baseline** for 1950-2026 quarterly data, with source provenance
- **Savings-rate baseline** built from the Regulation Q ceiling schedule and the Drechsler-Savov-Schnabl 2017 QJE deposit-beta result for the post-Reg-Q period
- **Consumer wiring** so the game's 1950 baseline constants are read through the substrate
- **Numeric refresh** adopting the Smets-Wouters 2007 shock-persistence baseline
- **Event-rate correction** that removes endogenously generated events from the exogenous stream
- **Monetary policy regime** classifier (accommodative, neutral, tightening, zero lower bound) with hysteresis
- **Marked Hawkes generator** for self-exciting clustered shocks with a fat-tailed severity distribution
- **Minsky refinement** of the financial-cycle horizon per Bezemer-Grydaki 2014 JBF and Borio-Drehmann 2011 BIS WP 380
- **Endogenous housing bubble model** with a multi-phase lifecycle, Kouwenberg-Zwinkels 2015 chartist/fundamentalist switching, a Geanakoplos 2009 leverage cycle, and a rent-based fundamental value

**All green.** The full test and validator suites pass.

**Rule 11 K=3 CONVERGENT verification complete.** Three research substrates (Perplexity, Grok, Gemini) independently answered six prompts covering 22 sub-values. The result was 20 strongly canonical numeric anchors, each locked with a peer-reviewed citation, plus two divergent items resolved with explicit reasoning and three source-attribution errors caught and corrected.

**The endogenous crisis architecture is complete.** The simulation follows history (FRED 1950-2026), extrapolates plausibly (Solow trend plus AR(1) noise), generates crises endogenously (Minsky regime, housing bubble, monetary regime), and clusters shocks empirically (Marked Hawkes for oil-shock-style events).

**Cross-product discipline preserved.** The substrate lives in a shared layer, not in any single product, so any consumer can be added or removed without touching it.

**Governance asks:** (1) promote the substrate from candidate to canonical, (2) ratify the associated calibration arc, (3) ratify the Rule 11 K=3 CONVERGENT calibration schedule, (4) formally adopt the Marcus Reed Surface 8 economic-mechanism blindness sub-clause.

---

## Background

A set of simulation products shares household and business economic layers. Payroll fires. Revenue streams accumulate. Operating costs debit. All of it is calibrated to 1950 constants.

**The diagnostic that surfaced the gap:** the moment a game needs to progress past its starting year, it needs inflation. Wages don't stay at $0.75/hr forever. Bread doesn't stay at 15¢ forever. The passbook savings rate at a business's account doesn't sit at the same level forever. Chronological progression is impossible without a macro layer.

And it's not just chronological mode. Even in procedurally generated eras, several downstream mechanics need a world-level signal:

- **Technology adoption:** pressure to automate is not just a technology unlock. It is driven by labor-cost inflation crossing a payback threshold.
- **Competition:** independent-versus-chain price competition requires a shared price signal. Two independent economic layers producing prices out of thin air cannot compete coherently.
- **Rate-shock eras:** any event that hinges on interest rates spiking or credit tightening (loan defaults, banking-era transitions, real-estate cycles) requires a world signal that both sides read from.

Household and business layers, on their own, cannot generate these signals. They react to prices; they don't set them at the world level. That is what this substrate does.

## Motivation

Three converging considerations:

**1. A prior architecture decision already flagged this.** A cross-product decoupling mandate, which surfaced during an earlier substrate extraction, named a generalized city-engine layer with macroeconomic pressure as a category of shared work that must live in the shared layer and not inside any one product. That decision is the direct authority for where this substrate lives, not just that it exists.

**2. A prior design lock pre-scoped it.** An earlier architecture lock identified macro-inflation as a compatible extension pathway for the bowling tycoon product, and its reviewer confirmed that no amendment was required.

**3. Marcus Reed Surface 8 audit governance imposes an economic-mechanism blindness constraint.** Recession-driven layoffs, credit-denial events, and price-shock cascades all have disparate-impact potential if a shock dispatcher inadvertently correlates with protected-attribute proxies (neighborhood indexing, occupation with demographic correlation, name features). Every new substrate in this arc carries an explicit structural-blindness test asserting zero demographic sampling in shock dispatch. The Surface 8 rubric doesn't yet name economic mechanisms as a distinct surface; see Open Questions.

## Design (as shipped)

### Three dispatch modes

- **Chronological.** Reads baked FRED/BLS data per quarter, 1950 through 2026, so a game can progress through real history year by year.
- **Randomized.** Runs a Solow-Swan production trend, AR(1) noise, a Poisson shock stream, and a Marked Hawkes clustered oil-shock stream, for procedurally generated eras.
- **Blended.** A chronological trend with a procedural shock overlay, for cross-era switching.

Dispatch mode is selected at substrate init and cannot change mid-run, because that would violate the determinism contract.

### Quarterly tick cadence

Four samples per simulated year. This matches the granularity of FRED/BLS headline series and the typical macroeconomic simulation literature, and it is sufficient for game-tick resampling.

### Read-only publish-subscribe contract

The substrate publishes series values. Consumers subscribe by name. The substrate never reads consumer state. This is the load-bearing architectural discipline: the substrate can run in complete isolation under its own test suite, and any consumer can be added or removed without touching substrate code.

### Deterministic per (seed, quarter, prior state)

Substrate output is a pure function of `(seed, quarter, prior state)`. Save/load parity, cross-session bug reproduction, and substrate identity verification all require this contract. It is verified end to end across all four substrates (WorldEconomy, Banking with the Minsky regime, Housing, and the Hawkes generator).

### Baseline anchoring

All series ship with baseline constants matching the 1950 calibration. The savings-rate baseline was corrected during the savings-rate work so that it matches the Regulation Q ceiling and the Drechsler-Savov-Schnabl deposit-beta formula, a strongly canonical correction backed by the 1954 Federal Reserve Bulletin range.

### Academic backbone (as shipped)

- **Solow-Swan** for the long-run GDP trend, with a capital share below one confirmed by the K=3 results (a Piketty r>g overlay was deprecated by a K=3 divergent fold)
- **Minsky Financial Instability Hypothesis** for credit cycle amplitude, with hedge, speculative and Ponzi transitions over a financial-cycle horizon per Borio-Drehmann 2011 BIS WP 380
- **Smets-Wouters 2007** for AR(1) shock persistence
- **Kouwenberg-Zwinkels 2015** for chartist/fundamentalist switching in housing bubble formation
- **Geanakoplos 2009** for the leverage cycle and forced-sale feedback in the housing cascade
- **Taylor 1993 (Carnegie-Rochester)** for the monetary policy regime classifier
- **Hawkes 1971 and Bacry et al. 2015** for self-exciting clustered shock generation
- **Mandelbrot 1963** as motivation for a fat-tailed severity distribution

Explicitly skipped: Keynesian, Monetarist, and RBC overlays, which are post-1950 political-economy frameworks incompatible with substrate neutrality.

### Canonical implementation pattern

The reference implementation is **Victoria 3 (Paradox 2022)**: a base price times a bounded multiplier. Bounded multipliers preserve deterministic replay under the `(seed, quarter, prior state)` contract while allowing controlled shock injection.

## Rule 11 K=3 CONVERGENT Results

**Verification protocol.** Three substrates (Perplexity, Grok, Gemini) independently answered six Rule 11 prompts covering 22 sub-values across the numeric calibration surface. Convergence means 3-of-3 agreement on both value and citation. Divergence (2-of-3 or a split) requires explicit resolution reasoning.

### 20 strongly canonical anchors locked

The calibrated values themselves live in the substrate's module documentation. These are the anchors and their canonical sources:

| Anchor | K=3 canonical source |
|---|---|
| Shock persistence (AR(1)) | Smets-Wouters 2007 (K=2 with divergent resolution) |
| Exogenous event rate: oil shock | Hamilton 2003 and Kilian 2009 |
| Exogenous event rate: pandemic | Fan-Jamison-Summers 2018 |
| Exogenous event rate: trade war | Bown-Kolb 2023 PIIE |
| Savings-rate ceiling schedule, 1950-1986 | Federal Reserve Bulletin (primary source) |
| Post-Reg-Q deposit beta | Drechsler-Savov-Schnabl 2017 QJE |
| Savings-rate baseline, 1950 | Regulation Q and the 1954 Federal Reserve Bulletin |
| Financial cycle length | Borio-Drehmann 2011 BIS WP 380 and Bezemer-Grydaki 2014 JBF |
| Rent-based fundamental value | Poterba 1984 and Himmelberg-Mayer-Sinai 2005 |
| Tiered bubble detection | Case-Shiller 2003 and Shiller 2015 |
| Housing default model | Perplexity K=3 result |
| Leverage and volatility scaling | Geanakoplos 2009 |
| Monetary regime hysteresis | Taylor 1993 (Carnegie-Rochester) |
| Credit-spread adjustments by regime | Bernanke-Lown-Friedman 1991 BPEA |
| Hawkes self- and cross-excitation | Perplexity K=3 result |
| Hawkes decay | Bacry et al. 2015, adapted to quarterly cadence |
| Severity tail | Mandelbrot 1963 tradition |
| Severity cap | stability convention |
| Capital share | Rognlie 2015 and Koh-Santaeulàlia-Llopis-Zheng 2020 |

### Two K=3 DIVERGENT resolutions

**(a) AR(1) persistence.** Perplexity and Grok converged on the Smets-Wouters baseline; Gemini pushed for a lower value citing lower-frequency data. **Resolution:** adopt the K=2 canonical value and extend the memory window to accommodate the longer persistence tail.

**(b) Monetary tightening as a Poisson event.** Grok proposed keeping it in the Poisson catalog; Perplexity flagged it as methodologically incorrect ("Fed tightening cycles are multi-quarter regimes, not point-in-time shocks"); Gemini agreed with Perplexity. **Resolution:** remove it from the Poisson catalog and implement the monetary policy regime as a state-based classifier. The K=3 DIVERGENT surface became the substrate design driver.

### Three source-attribution errors caught and corrected

Gemini's numeric claims were accurate, but its source attributions were unreliable and had to be verified against primary sources:

1. **Private-debt-to-GDP series.** Gemini cited Keen 2013; the actual peer-reviewed source is Bezemer-Grydaki 2014 JBF.
2. **US TFP series.** Gemini cited BLS multifactor productivity; the actual source for the specific value it quoted is Vollrath 2024 AEJ:Macro.
3. **1980-82 mislabeling.** Gemini described this as a single contraction; the actual FRED record is a double-dip recession sequence with an intervening recovery.

The pattern is recorded for future Rule 11 deployments: **use Gemini for numeric anchors, and cross-verify every attribution against the peer-reviewed source before shipping a citation manifest**.

## Phased Plan -- as executed

| Phase | Status |
|---|---|
| Scaffold | Shipped |
| Chronological FRED/BLS baseline | Shipped |
| Savings-rate (Regulation Q and deposit-beta) baseline | Shipped |
| Consumer wiring | Shipped |
| Numeric refresh (shock persistence) | Shipped |
| Event-rate correction | Shipped |
| Monetary policy regime | Shipped |
| Marked Hawkes and fat-tailed severity | Shipped |
| Minsky refinement (financial-cycle horizon) | Shipped |
| Endogenous housing bubble model | Shipped |
| Regional decomposition and inequality overlay | Deferred ("do not build speculatively") |

**Deferred (not blocking Council #7):**

- Banking loan pricing subscribing to the monetary regime's credit-spread adjustment
- An optional Hawkes replacement for the Poisson oil shock in randomized mode
- A housing-burst to credit-cycle-reset wire
- Dashboard subscriptions for regime and intensity graphs

These are optional consumer wires; the substrates themselves are shipped and stable.

## Open Questions for Council

**1. Rule 11 K=3 CONVERGENT calibration schedule: ratify as canonical governance precedent?** The six-prompt, 22-sub-value, three-substrate verification protocol used here is itself a candidate governance pattern. Is it the canonical Rule 11 K=3 pattern going forward, or is it scoped to macroeconomic calibration and does it require re-authorization per domain?

**2. Marcus Reed Surface 8 economic-mechanism blindness sub-clause: formally adopt?** All four substrates carry explicit blindness tests. The Surface 8 audit rubric does not currently name economic mechanisms as a distinct surface. Recommendation: adopt the sub-clause. Auditability is already implemented; formal recognition closes the governance loop.

**3. Optional consumer wires: schedule or hold?** Four consumer wires are listed as deferred above. Are they scheduled for a post-ratification workstream, or held pending explicit demand per "do not build speculatively"?

## Ratification Ask

Council #7 is asked to:

1. **Promote the WorldEconomy substrate from candidate to canonical**, governed by the design commitments above, with the shipped work verified against its full test and validator suites.

2. **Ratify the associated calibration and endogenous-crisis arc**, executed under that substrate.

3. **Ratify the Rule 11 K=3 CONVERGENT calibration schedule:** 20 strongly canonical numeric anchors, two divergent resolutions, three attribution corrections, and the documented pattern of verifying Gemini's attributions. A SKETCH-CLASS flag remains applied to cross-section derived thresholds pending playtest ratification.

4. **Formally adopt the Marcus Reed Surface 8 economic-mechanism blindness sub-clause.** Auditability is already implemented across all four substrates via explicit structural-blindness tests; formal recognition closes the governance loop.

5. **Schedule or hold the optional consumer wires**, directing whether they are queued for the next cycle or held pending explicit demand.
