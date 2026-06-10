# Drafting brief — Post 97 "Generative Agents Are the Backbone, Not the Runtime"

**Status:** Brief only; not yet drafted. NEW brief 2026-06-10 PM per Round 7 R5 design.
**Target slot:** Post 97 — opens the Posts 97-99 hybrid-path block. Per R5 design: Park 2023 supplies observation/reflection/planning machinery; direct LLM scaling not viable for 88 NPCs over decades.
**Scope verdict:** SAFE — methodology + open-academic + commercial-precedent META-level discussion. No Memory Lanes protected scope.
**Length target:** 3000-4500 words.

## Thesis

Park et al. 2023 "Generative Agents" (arXiv:2304.03442) is the canonical recent precedent for procedural-character architectures that use LLM machinery for observation, reflection, and planning. Modified-C-bis adopts the Park 2023 architecture's THREE-PROCESS DECOMPOSITION (observe → reflect → plan) as conceptual backbone but does NOT adopt direct-LLM scaling as runtime. The arithmetic: 88 NPCs × ~10 decisions per game-minute × continuous play sessions = LLM compute cost that breaks indie-budget reasoning. Park 2023's published evaluation ran 25 agents in a confined scenario; scaling to 88 NPCs across 30 game-years requires architectural surgery that subsequent posts (98 multi-graph memory, 99 cached policies) cover. Post 97 explains the Park 2023 grounding + the scaling-constraint that forces the hybrid path.

## Sections (outline)

1. **Hook:** "Park 2023's 'Generative Agents' is the closest published precedent for what Modified-C-bis tries to do. It is also a worked example of why you can't just scale LLM-driven agents to my actual game's NPC count."

2. **What Park 2023 contributes.** Three-process decomposition:
   - **Observe:** agent records relevant environmental events
   - **Reflect:** agent periodically synthesizes observations into higher-level inferences ("the player has been bowling on Lane 5 every Saturday for two months")
   - **Plan:** agent uses reflections to score candidate actions
   - LLM (GPT-3.5 in the paper) drives each process
   - Memory stream as the persistent state across episodes
   - Published evaluation: 25 agents in a constrained sandbox; user study supported believability claims
   - The paper is arXiv:2304.03442; primary-text grounding for the architecture pattern

3. **Why this maps cleanly to Modified-C-bis.** The three-process decomposition matches the framework's three-layer memory:
   - Park 2023 Observe ≈ Layer 1 raw events
   - Park 2023 Reflect ≈ Layer 2 encoded-and-reconstructed perspective + consolidation pass
   - Park 2023 Plan ≈ active-inference decision-scoring layer (Friston 2017/2021 substrate-neutrality bridge per Round 8 R4 single-leap reframe)

4. **The scaling-constraint that forces the hybrid path.** Walk through the arithmetic:
   - Park 2023: 25 agents × LLM call per observation/reflection/plan + paper-evaluation duration limited
   - Modified-C-bis target: 88 NPCs (Memory Lanes V1 NPC roster size; per content-kb)
   - Per-decision LLM compute at ~$0.001-0.01 per inference (current pricing) × 10 decisions/game-minute × 60 minutes/game-hour × N game-hours per player session = real-world cost per player session
   - Direct-scaling math doesn't close for indie-budget. Period.
   - PLUS: per-frame latency budget on iOS V1 (~33ms target) cannot tolerate LLM-call-per-decision

5. **The architectural surgery the framework adopts.** Park 2023 backbone + Modified-C-bis runtime substitutions:
   - Observe layer: cached/sampled events + Markov-blanket isolation (NPC reads only its own perceptual window, not player-side narrative)
   - Reflect layer: yearly consolidation pass (Post 94) drives Layer 2 promotion; LLM can drive consolidation summaries IF computationally affordable at yearly cadence (much rarer than per-decision)
   - Plan layer: cached active-inference policies (Post 99 hybrid path) at runtime; sophisticated-inference EFE evaluation at consolidation boundaries (audit layer; Post 95)

6. **What this gets right vs what Park 2023 leaves open.**
   - Park 2023 doesn't address multi-decade NPC arcs (paper evaluation is single-session)
   - Park 2023 doesn't address per-frame latency budgets for shipping games (research prototype)
   - Park 2023 doesn't address cross-cultural disclosure discipline (research scope; not commercial product)
   - Modified-C-bis extends Park 2023 in all three directions; that extension is the framework's contribution

7. **Honest scope: what Modified-C-bis IS and IS NOT.**
   - IS: a procedural-character cognitive architecture spec for a specific cozy-sim game
   - IS NOT: a published research contribution to the agent-architecture literature (operator publishes on GitHub research blog, not peer-reviewed venue)
   - IS: extensible to other simulation games at the META-architecture level
   - IS NOT: a general-purpose agent framework competing with Park 2023's research-system role

8. **The "novel in combination, not in components" honesty.** R5 design language. Modified-C-bis combines:
   - Park 2023 three-process decomposition (NOT NOVEL — borrowed)
   - Friston 2017/2021 active inference (NOT NOVEL — borrowed)
   - Hawkins-Carrère-Gottman 2002 sentiment override (NOT NOVEL — borrowed)
   - Russell 1980 circumplex DC1 split (NOT NOVEL — established)
   - Fraley-Waller-Brennan 2000 ECR-R attachment (NOT NOVEL — established)
   - Wiredu 1992 personhood-as-achievement (NOT NOVEL — borrowed philosophy)
   - The COMBINATION (multi-decade + emotion-conditioned + pair-specific + active-inference-grounded + cross-cultural-disciplined) is what's novel
   - This honesty is the framework's commercial-precedent post bridge

9. **V1 implementation cost.** Adopting Park 2023 backbone in Modified-C-bis is structural design choice (no direct code cost). The implementation-side cost is in the runtime substitutions (Posts 98 + 99 specify).

10. **Closing.** "Park 2023 showed me what was possible. The arithmetic showed me what was actually shippable. The hybrid path is the synthesis."

## Key citations

- **Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023).** Generative Agents: Interactive Simulacra of Human Behavior. arXiv:2304.03442. (Conditionally also in UIST 2023.)
- LLM-pricing context: any current OpenAI/Anthropic API pricing page (cite responsibly with date).

## Cross-links

- LINKS BACK TO: Post 92 (commercial precedent comparison includes Park 2023 in agent-architecture lineage)
- LINKS FORWARD TO: Post 98 (multi-graph memory; MAGMA-style typed indexes for V1) + Post 99 (cached policies; Project Zomboid offscreen storylet pattern)
- IMPLEMENTATION TIE: Round 9 Q4 EFE decomposition + Q3 belief-update integrate Park 2023 three-process at the formalization layer

## Drafting prerequisites

- Park 2023 full primary-text read (~2-3h; arXiv:2304.03442 + supplementary materials).
- LLM-pricing analysis update (~30 min; current API rates as of drafting time).

## Hour estimate

At observed velocity: ~5-7 hours drafting + revision + arithmetic analysis. Target 3000-4500 words.
