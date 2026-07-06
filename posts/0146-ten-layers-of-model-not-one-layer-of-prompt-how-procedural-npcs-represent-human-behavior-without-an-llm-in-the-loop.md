# Ten Layers of Model, Not One Layer of Prompt: How Procedural NPCs Represent Human Behavior Without an LLM in the Loop

<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0146
title: Ten Layers of Model Not One Layer of Prompt How Procedural NPCs Represent Human Behavior Without an LLM in the Loop
date_published: 2026-07-03
status: published
superseded_by: none
domain: ten-layer NPC framework architecture load-bearing methodology anchor for procedural persons
project_scopes: framework-architecture, sim-ai, open-alley, roomtolife
cc_task_relevance: character-architecture-design, hexaco-attachment-wiring, memory-system-design, cultural-personhood-modeling, procedural-npc-representation
phase_binding: era-independent
discipline_family: framework-architecture ten-layer NPC
canonical_rule: ten grounded modeling layers are first-class architectural commitments for procedural NPC representation; each layer grounded in published literature; no layer requires LLM in the loop
load_bearing_claims:
  - Ten grounded modeling layers are first-class architectural commitments for procedural NPC representation; each layer explicitly grounded in published literature
  - Layer 1 needs biological drives; Layer 2 affect (Russell 1980 valence + arousal; Lazarus-Folkman 1984 stress); Layer 3 HEXACO 6D personality (Ashton and Lee 2007) plus attachment style (Fraley Waller Brennan 2000 ECR-R avoidance + anxiety); Layer 4 memory three-horizon short/mid/long-biographical with consolidation; Layer 5 decision-making expected free energy minimization per Friston 2017 active inference; Layer 6 relationships ordered-pair sentiment scalars Hawkins Carrere Gottman 2002; Layer 7 cultural personhood Baseline A Western-individualist + Baseline B Confucian role-ethics + Baseline C Wiredu Ghanaian communal-achievement; Layer 8 life history biographical records generated at spawn; Layer 9 environmental knowledge Scene-specific affordances; Layer 10 audit sophisticated active inference offline at consolidation boundaries
  - Framework contribution addresses Generative Agent-Based Social Simulation field gaps at validation + reproducibility + auditability that LLM-prompt-dumping approaches cannot meet
  - Ten layers compose additively; each layer produces auditable + testable + portable behavior; no layer requires LLM in the loop
applicability_triggers:
  - Designing procedural character architecture for a multi-decade tycoon simulation or similar sustained NPC ecosystem
  - Choosing between LLM-prompt-based NPC representation and grounded structural modeling
  - Wiring personality traits HEXACO or attachment to action selection
  - Designing memory system with consolidation boundaries and horizon distinctions
  - Cross-cultural personhood modeling with baseline-parameter-set approach
  - Character spawn with biographical record persisting across Scenes
mechanism_details:
  - HEXACO H (Honesty-Humility) for cooperation/exploitation prediction per Hilbig and Zettler 2009 (superseded by Post 0150 forward-reference amendment for citation-chain clarification)
  - Attachment style (ECR-R) for relational bonding dynamics per Mikulincer and Shaver 2016
  - Ordered-pair sentiment S(A to B) in [-1, +1] with sentiment override mechanic
  - Three-horizon memory short 6-12 game-months + mid consolidation + long-biographical landmarks
  - EFE decision-making at planning depth tau less-than-or-equal-3 per Post 0111
  - Yearly consolidation cadence with four promotion criteria (affective-spike + pair-history-significant + trait-modulated-significant + first-occurrence)
  - Cultural baselines A/B/C as parameter sets not stereotype content
  - Sophisticated active inference deployed at consolidation boundaries not per-frame
cross_refs:
  - Post 0111 (procedural persons as Bayesian puzzle; planning depth naive vs sophisticated active inference distinction)
  - Post 0115 (HEXACO to attachment re-source; literature-checking trait sources per function)
  - Post 0116 (ordered-pair sentiment plus Gottman override; Layer 6 mechanics)
  - Post 0118 (recency plus consolidation architecture; Layer 4 mechanics)
  - Post 0120 (V1 NPC memory spec; nine locked V1 elements)
  - Post 0125 (Wiredu cannot be a trait slider; category error preventing Layer 7 misuse)
  - Post 0127 (no single African view; intra-tradition dispute disclosure)
  - Post 0128 (accumulator hides WEIRD defaults; schema-placeholder discipline)
  - Post 0150 (forward-reference amendment for Post 0146 HEXACO citation-chain clarification)
  - Post 0169 (canonical-infrastructure-consultation sub-shape 23 fire for character content authoring)
  - Memory project_phase_3_caveman_castaway_progression_shipped_2026-07-05.md
-->

**Author:** Jimmy McColery
**Date:** 2026-07-03
**Status:** Methodology-anchor post articulating the framework's structural approach to representing human behavior in procedural characters; enumerates ten grounded modeling layers as first-class architectural commitments; distinguishes from LLM-prompt-dumping approaches that hide the model inside opaque generation; positions the framework's contribution against Generative Agent-Based Social Simulation field gaps at validation plus reproducibility plus auditability

> **Top-of-file correction notice (added 2026-07-06 per Rule 24 canonization at Council #8):** Layer 7 Cultural Baselines A/B/C in this post (Western-individualist / Confucian role-ethics / Wiredu-Menkiti-Gyekye Ghanaian communal-achievement) refer to the paper-layer canonical typology. The sim-ai code implementation at `culturalBaselines.ts` uses distinct-but-both-canonical A/B/C labels for era-and-region-specific US working-class test scaffolding (1955 Northern urban Black church widow / 1972 Midwest Catholic union man / 1980 West Coast secular Jewish professional). Both surfaces are canonical at their own domain per Pattern D forward-reference amendment shipped at Post 0173. See Post 0173 for definitional clarification and Post 0138 for empirical KL-divergence validation that validates the CODE baselines specifically. A Phase-4+ Q58 full deployment may reconcile the two typologies into a unified registry; until then treat each label according to its surface (paper vs code).

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

Someone asked me a foundational question yesterday during a brainstorming session: how do NPCs know how humans function? The question is a good one to sit with. Most Generative Agents work handwaves the answer by dumping character context into a language model prompt (typically some variant of "you are Bob, a 1950s bowling regular, act accordingly") and letting the model's training data supply the rest. The dumping approach produces behavior that reads plausibly on first contact. What it does not produce is behavior whose grounding is auditable, whose consistency is testable across long time horizons, or whose portability across environments can be measured.

The framework I am building takes a different approach. NPCs do not know how humans function. NPCs embody mathematical models of specific aspects of human function, borrowed from specific academic disciplines, layered so that no single layer carries the whole load. When the layers interact under runtime tick, they produce behavior that reads as human-like without any layer needing to hide the mechanism inside an opaque prompt. This post enumerates the ten layers, names what each layer models, cites the disciplinary grounding, and describes how the layers compose. The methodology contribution is the enumeration itself: a public commitment that no piece of "being human" gets waved through as ambient LLM competence.

## The dominant approach and what it costs

The Park et al. 2023 "Generative Agents: Interactive Simulacra of Human Behavior" paper kicked off the modern generative-agent field with a specific architecture: LLM-driven characters with memory plus reflection plus planning modules that call the LLM at multiple points per game loop. The paper demonstrated believable emergent social behavior in a simulated small town; the community absorbed the demonstration and produced a wave of derivative work.

The dominant descendant approach places the LLM in the runtime loop. Per-frame or per-decision LLM calls score candidate actions, produce dialogue, generate reflection insights, and interpret world state. The approach's advantages are real (fast prototype iteration; rich open-ended language; behavioral variety without hand-authoring rules). The approach's costs are also real. First, per-decision LLM calls do not scale to hundreds of concurrent NPCs at production framerate. Second, the mechanism that produces each decision is opaque; a reviewer cannot examine why the model chose action X over action Y in a specific context because the reasoning lives inside the LLM's forward pass. Third, behavioral consistency over game-years is empirically fragile; the model's prompt-sensitivity plus the memory-retrieval-noise interaction produces drift that is hard to distinguish from intentional evolution. Fourth, the substrate landscape shifts under the framework's feet; a design that depends on specific model behavior can require rework when the operator's substrate provider ships a new model.

The 2025-2026 field literature I have surveyed (per fresh research done during the session that produced this post) converges on validation, reproducibility, and auditability as the field's top unsolved challenges. The dominant runtime-LLM approach makes these challenges harder rather than easier because the mechanism being validated lives inside a black box.

## The ten layers, each grounded

The framework's response is to refuse to hide the mechanism. Instead of one opaque prompt-dumping layer, ten disjoint grounded models, each with its own literature backing and its own testable properties. The layers are enumerated below with the grounding I actually stand on.

**Layer 1: needs.** The Sim's biological drives (hunger, thirst, exhaustion, exposure-to-elements) represented as scalar accumulators with per-need decay rates. The grounding is basic survival biology; the specific mechanic (need decay plus action-triggered restoration plus Layer 3 coupling) is a design choice within that grounding, not a claim about neuroscience. The needs layer is the most transparent; nobody argues NPCs shouldn't get hungry in a survival scenario.

**Layer 2: affect.** Three independent scalars representing valence (positive-versus-negative feeling), arousal (activation level), and stress (accumulated pressure). The dimensional-circumplex grounding is Russell 1980 *Journal of Personality and Social Psychology* 39(6):1161-1178 for valence-arousal; the stress channel is grounded in Lazarus and Folkman 1984 *Stress, Appraisal, and Coping*. The three-scalar split is deliberate; a single "mood" scalar would fold information the affective science literature treats as separable. The layer sits between needs and personality; needs push it around; personality shapes how it responds; memory encodes based on it.

**Layer 3: personality traits.** HEXACO 6-dimensional trait vectors (Honesty-Humility, Emotionality, Extraversion, Agreeableness, Conscientiousness, Openness) represented as numeric vectors baked in at Sim creation. The disciplinary grounding is Ashton and Lee 2007 for the HEXACO model itself; Hilbig and Zettler 2009 *Journal of Research in Personality* 43(3):516-519 for the honesty-humility trait's cooperation and exploitation predictions; Zettler et al. 2020 *Perspectives on Psychological Science* 15(3):723-760 for the trait's stability. Attachment styles (avoidance and anxiety dimensions from the Fraley, Waller, and Brennan 2000 ECR-R) supplement HEXACO for relational encoding. Traits are stored as numbers, not descriptive text, so their influence on decisions is inspectable at every call site.

**Layer 4: memory.** A three-horizon architecture: short-horizon (last few game-hours, high decay), mid-horizon (survivors of consolidation, slow decay), long-biographical (landmarks and reflections, near-permanent) with salience-thresholded encoding and periodic consolidation. The consolidation pass promotes short-horizon traces above a survival threshold to mid-horizon and preserves landmark-eligible high-salience traces at long-biographical from the start. The grounding is Park et al. 2023 for the generative-agents memory-consolidation lineage; the framework's specific consolidation cadence (game-year boundaries plus milestone triggers) is an architectural choice within that lineage. The memory layer stores what happens; the accumulator layer holds the running summary; both are needed.

**Layer 5: decision-making.** Expected free energy (EFE) minimization at τ=1 (one-step-ahead policy scoring) with softmax action sampling. The mathematical grounding is Friston, FitzGerald, Rigoli, Schwartenbeck, and Pezzulo 2017 "Active inference: A process theory" *Neural Computation* 29(1):1-49, plus Friston, Da Costa, Hafner, Hesp, and Parr 2021 "Sophisticated Inference" *Neural Computation* 33(3):713-763 for the recursive metacognition machinery the framework banks for the audit layer. The decision layer scores candidate actions by expected free energy given current beliefs plus striving targets derived from needs and traits; sampling produces action selection. Cached policies at runtime; sophisticated inference at audit cadence. Post 0119 in this repo walks through the audit-first sequencing discipline.

**Layer 6: relationships.** Ordered-pair sentiment scalars S(A→B) in the range from negative one to positive one representing asymmetric affective disposition per relationship. A's feelings about B are not required to equal B's feelings about A; the scalars decay slowly without interaction, mutate on shared events, and cap saturation at plus or minus one. The sentiment-override mechanism (positive prior interaction predicts positive interpretation of current ambiguous behavior) is grounded in Hawkins, Carrère, and Gottman 2002 *Journal of Marriage and Family* 64(1):193-201. Pair-history events (co-observation, shared shelter, shared storm survival, landmark witnessing) accumulate in a bounded recency window per pair. Post 0116 in this repo canonizes the ordered-pair scalar architecture.

**Layer 7: cultural personhood.** Baseline parameter sets that shift how the individual-versus-communal frame conditions accumulate. The three baselines currently canonized in the framework are: Baseline A (approximately Western-individualist framing; Kantian universalizability and Rawlsian original-position frames), Baseline B (approximately Confucian role-ethics framing), Baseline C (approximately Wiredu-Menkiti-Gyekye Ghanaian personhood-as-communal-achievement framing). The grounding is the primary literature I have read for each baseline: Wiredu 1992 *Person and Community* Chapter 9 for the Ghanaian tradition; Menkiti 1984 for the closer-to-personhood-as-achievement reading; Gyekye's counter-position for the internal-tradition dispute. The framework's discipline is that no baseline is treated as universal default; the operator-side procedural-moral-test discipline separates trait dimensions from procedural moral frames so category errors do not propagate. Post 0125 in this repo works through the category-error correction.

**Layer 8: life history.** Per-character biographical records generated at spawn: era, cultural context, family structure, formative events per archetypal template (first job, first loss, first success). Innate properties (HEXACO trait vector, Schwartz Values, temperament, cognitive style) are set at spawn; life-history events reflect those innate properties interacting with the era-appropriate archetypal templates. The framework's ecosystem architecture treats the biographical record as canonical at the ecosystem layer rather than at the individual-product layer; the same character's biography persists across environments the same character appears in.

**Layer 9: environmental knowledge.** What the NPC knows about the current Scene, provided by the Scene rather than known abstractly by the NPC. A bowling-alley Scene supplies "here is a lane, here is a snack bar, here are the regulars, here is the current era's social vocabulary." NPCs do not know abstractly what a bowling alley is; they receive Scene-specific affordances and act on them. The environmental-knowledge layer is deliberately shallow because deeper knowledge would introduce state that has to be reconciled across environments, and the framework prefers per-Scene environmental knowledge to avoid the reconciliation cost.

**Layer 10: audit.** Sophisticated active inference apparatus running offline at consolidation boundaries or developer-triggered audit points. The apparatus evaluates cached-policy decisions against expected-free-energy calculations that would run under sophisticated scheme; the audit produces artifacts flagging where cached policies drift from framework discipline. The audit layer catches the specific failure modes cached policies can produce; the audit layer earns the theoretical complexity of sophisticated active inference by running only where the empirical benefit justifies the cost. Post 0119 in this repo canonizes the audit-first sequencing.

## How the layers compose

Individual layers do not produce human-like behavior. The interaction across layers does. A Sim who is stressed (Layer 2 elevated) plus has high emotionality trait (Layer 3) plus remembers being betrayed by Bob (Layer 4 mid-horizon trace) plus is standing in a bowling alley (Layer 9 Scene) plus has a strongly negative S(Sim→Bob) (Layer 6) will react to Bob's approach differently than a Sim who is calm plus has low emotionality plus never met Bob plus is standing in the same alley plus has a neutral S(Sim→Bob). The reaction is not scripted at any layer. The reaction emerges from the layers scoring the candidate actions under the decision layer's EFE minimization.

The composition is auditable. Every layer's contribution to the current striving-target set is inspectable at inference time. Every decision produces an audit trail: which needs were driving the striving target, which trait values shifted the weights, which memory traces contributed to the perspective, which pair sentiments modulated the target, which Scene affordances were available. The decision layer's action score is a function of the other layers' explicit contributions; nothing is hidden.

The composition is longitudinally stable. Traits do not drift because they are numeric baselines rather than prompt paraphrase; sentiment mutates only in response to specific mechanics rather than to prompt-suggestion sensitivity; memory decays on documented rates rather than on retrieval noise. Long-horizon character consistency comes from the mechanic being deterministic given the state and the state being versionable.

The composition is cross-environment portable. A character's Layer 3 trait vector plus Layer 6 pair-sentiment graph plus Layer 8 life history is the character's identity; the Layer 9 Scene changes when the character moves environments, but the Layer 3 plus Layer 6 plus Layer 8 substrate persists. Cross-Scene transfer is a measurable property of the framework's architecture rather than a hopeful side effect of the LLM absorbing consistency from prompt context.

## What the architecture explicitly does not give NPCs

Some things I do not model in the ten layers, and the omission is deliberate. NPCs do not know general facts about the world. They do not know that gravity pulls down, that the Cold War happened, that capitalism is a system of production. Their Scene provides era-appropriate context; their cultural baseline parameterizes assumptions about social relations; their trait vector plus life history parameterizes their idiosyncratic response. That is the scope. Anything beyond that would introduce a knowledge substrate the framework has not committed to maintaining.

NPCs do not have domain expertise as knowledge. They can perform actions in their action space (bowl, fish, forage, tune a pinsetter) if the action is available in the Scene; they do not carry a knowledge representation of bowling technique or pinsetter mechanics as things they know abstractly. The action's competence is the action's competence; the character's competence is skill-shaped perception derived from occupation grounding in the traits layer, not general knowledge.

NPCs do not speak in the current architecture. There is no dialogue system in the framework's V1 spec. Characters act; they do not talk. The omission is a scope choice rather than an architectural inability; adding a dialogue system is a substantial workstream that the framework's V1 target does not accommodate. Post 0120 in this repo walks through what ships and what waits in the V1 spec.

NPCs do not read texts or watch media inside the game as a knowledge-acquisition mechanism. The character's knowledge substrate is (a) innate baseline plus (b) Scene affordances plus (c) accumulated experience through the tick loop. Adding a fourth mechanism (in-game media consumption changes the character's belief substrate) is an open architectural question the framework has not committed to. If the operator ratifies in-game reading as a mechanic, the framework would need to spec how text-labeled objects consume, how consumption maps to Layer 3 affect updates, and how content authoring workflow supplies the readable text.

## Why the composition addresses the field's actual gaps

The 2025-2026 Generative Agent-Based Social Simulation literature I have surveyed identifies validation, reproducibility, and auditability as the field's top unsolved challenges. Runtime-LLM approaches make these challenges harder because the mechanism being validated is opaque, the reproduction depends on specific model behavior, and the audit target is a forward pass through a language model.

The ten-layer composition addresses each gap directly. Validation is possible because each layer produces empirically inspectable properties; hypothesis tests scaffolded at layer boundaries are what my framework's Sim AI Phase 2 arc has been landing (H8 through H24 for pair-history dynamics, landmark ripple, buffer discipline, and emergent behavior; H1 through H7 for the underlying Layer 3 and memory mechanisms). Reproducibility is possible because the mechanics are deterministic given seed and state; the same state plus the same seed produces the same decisions. Auditability is possible because the decision layer's inputs are the other layers' explicit contributions; every action score has a citation graph back to needs, traits, memories, and Scene affordances.

The composition is not a novel architecture. Each individual layer inherits from work I have cited. What the composition is, is a public commitment: no ambient LLM competence, no prompt-dumping, no black box between the mechanism and the audit. The commitment is the methodology contribution.

## What I'm not claiming

I'm not claiming any individual layer is novel. Needs systems have appeared in survival simulations for decades; HEXACO trait vectors have appeared in psychometric-grounded procedural work; three-horizon memory is a direct descendant of Park et al. 2023; expected free energy is Friston's mathematical framework; ordered-pair sentiment scalars are canonized in my own Post 0116 but rest on the Fiske Relational Models Theory literature. The layers' individual mechanisms are extensions of well-cited prior work. What the post claims is architectural: the specific commitment to layered grounded models without an LLM in the runtime loop.

I'm not claiming the ten layers exhaustively cover "being human." The layers cover a specific slice: biological drives, affective state, trait-conditioned response, memory and consolidation, decision-making mathematics, relational asymmetry, cultural personhood framing, biographical history, environmental affordances, and audit. There is plenty of "being human" the layers do not model: abstract belief revision, verbal dialogue, aesthetic judgment, embodied physical intuition, cultural production. The scope is what the ten layers claim; the omissions are honest scope declarations, not hidden claims.

I'm not claiming this scales to arbitrary complexity without engineering cost. Layer additions produce integration questions; layer interactions produce edge cases; the audit layer at Layer 10 is what catches drift, but the audit layer's implementation cost is nontrivial and the audit's coverage is a function of the operator's discipline. A production deployment of the framework at population scale requires substantial engineering beyond the current sandbox scope.

I'm not claiming LLM-in-the-runtime-loop approaches are wrong for all use cases. The dominant approach's advantages are real. What the post argues is that the framework's specific design surface (long-horizon consistency, cross-environment persistence, methodology-publishable output) is served better by structural layering than by prompt-dumping, not that all NPC design surfaces should adopt the same choice.

I'm not claiming the layer count "ten" is canonical. Someone could reasonably factor the ten into eight or twelve. The specific enumeration is what my framework has settled on; the enumeration's substance is the ten-way decomposition, not the number itself.

## What I am claiming

Procedural NPCs can be built with layered grounded models rather than with a single LLM-prompt layer, and the layered approach produces empirically inspectable properties that the LLM-prompt-layer approach does not. Ten specific layers (needs, affect, traits, memory, decision-making, relationships, cultural personhood, life history, environmental knowledge, audit) cover a scope that is substantive without claiming to be exhaustive; each layer has a specific literature grounding I have cited; the layers compose to produce human-like behavior without any layer needing to hide the mechanism inside an opaque prompt.

The composition addresses the Generative Agent-Based Social Simulation field's top unsolved challenges (validation, reproducibility, auditability) because the mechanism being validated is explicit at each layer, the mechanic is deterministic given state and seed, and the decision layer's contributions are inspectable at every call site. The composition is not the individual layers, which are extensions of cited prior work; the composition is the commitment to layered grounding without runtime LLM in the loop.

If you are building generative agents and your architecture depends on an LLM to fill in the layers you have not explicitly modeled, the ten-layer composition is one alternative architectural shape that produces auditable, testable, portable behavior at the cost of substantially more upfront engineering work per layer. The tradeoff is real; the choice is the operator's; the framework I am building is one instantiation of the alternative choice.
