# Comet Computer Council-Deployment Script v1

**Established:** 2026-07-01 (post-Council-#1-close session; ablation-gate guide sibling artifact)
**Maintained by:** operator; Claude Code updates on empirical contact
**Purpose:** Comprehensive Comet Computer workflow for automating the substrate-deployment mechanics of Council methodology deployments (Councils #2 through #5). Reduces operator wall-time per Council from ~2-4 hours to ~30-45 min of unattended Comet execution + ~30-60 min operator ratification. Structural precondition: the substrate prompts + orchestrator synthesis prompt are already drafted and calibrated (per the paired-n=4 substrate-discipline lesson at `feedback_substrate_opaque_citation_format_as_risk_signal.md`); Comet just deploys them.
**Provenance:** Council #1 closed 2026-06-30 evening; the four remaining Councils (#2 Appraisal Tags, #3 Active-Inference Tractability, #4 Cross-Cultural Discipline Audit, #5 Longitudinal Benchmark Design) are drafted and staged on operator's Desktop. Operator asked whether Comet could automate the deployment mechanics; this script is the affirmative answer.

---

## The three-layer architecture

The Council methodology runs across three distinct substrates. Comet CANNOT do all of it; it does the transport layer only.

- **Comet Computer = TRANSPORT LAYER.** Drives browser tabs; deploys substrate prompts to Perplexity DR / Claude Web / Grok / Gemini; waits for responses; captures outputs; hands off to orchestrator. Executes mechanical labor unattended.
- **Claude Code = LOCAL-FILESYSTEM LAYER.** Archives outputs to `_archive/`; ingests substrate contributions into `post-ideas.md`; runs `scripts/audit.sh`; executes canonical mutations; commits + pushes; regenerates the Treasure Map. Requires local terminal access Comet cannot provide.
- **Claude Web Master Setup Project (orchestrator) = JUDGMENT LAYER.** Applies Rule 14 verdict-pattern classification; Rule 19 Marcus Reed three-condition fabrication gate; ECHO/NOVEL discipline; independent citation verification. Produces the synthesis that determines what gets ratified.

Comet is the arm; Claude Code is the disk; the orchestrator is the brain. Confusing these produces the failure mode where mechanical automation displaces judgment (which the framework's discipline exists to prevent).

**One important boundary condition:** for Councils where any substrate is Claude Code itself (Council #3 Substrate C: V1-budget evaluation; Council #5 Substrate B: V1-compatible scenario design), Comet CANNOT deploy that substrate. The operator triggers a Claude Code session in parallel with Comet's browser-substrate deployments; the outputs converge at the orchestrator handoff.

---

## Pre-flight checks (operator side; verify BEFORE triggering Comet)

Comet fails silently if any of these are false. Verify each:

1. **Comet Computer session active + credits sufficient.** Estimated Comet execution: ~30-45 min unattended per Council; approximately 15-30 substantive browser actions per Council.
2. **Operator logged into every target platform:**
   - Perplexity (perplexity.ai) — required for Substrates A on Councils #2, #3, #4, #5
   - Claude (claude.ai) — required for Substrates B on Councils #2, #3, #4, #5; required for orchestrator on all Councils
   - Grok (grok.com or x.com) — required for Substrates C on Councils #2, #4; required for Substrate C on Council #5
   - Gemini (gemini.google.com) — required for Substrate A' on Council #4 (4-substrate deployment; cross-family verification of Perplexity)
3. **Claude Master Setup Project is refreshed** (per the CW Master Setup Refresh Kit at `~/Desktop/cw-master-setup-refresh-2026-06-30/` or equivalent current-version staging). The orchestrator synthesis step deploys into this project; stale project knowledge produces stale orchestrator judgment.
4. **`~/Desktop/council-orchestrator-synthesis-prompt.md` exists** and matches the current framework version. This is the orchestrator prompt Comet attaches to the synthesis chat.
5. **`~/Desktop/council-N-<name>.md` exists** for the Council being deployed (staged from Council #1 workflow; four Councils staged on 2026-06-30).
6. **Downloads folder is empty of stale Council files** OR the operator has moved them to `_archive/` — Comet writes to Downloads, and mixed old + new Council outputs create ambiguity.
7. **Claude Code session (this one, or a fresh one) is available for Substrates C (Council #3) or Substrate B (Council #5)** where Claude Code is the assigned substrate.

If any check fails, fix the failing check before triggering Comet.

---

## Comet Council-Deployment Prompt (COPY-PASTE THIS INTO COMET)

The prompt below is the TEMPLATE. Council-specific instantiations follow in the next section (Council #3 is a full worked example; Councils #2/#4/#5 are adaptation notes). To trigger a Council deployment via Comet:

1. Open a fresh Comet Computer chat.
2. Paste the template below AS-IS.
3. Immediately after, paste the Council-specific instantiation block (from the next section).
4. Comet will execute the workflow autonomously and report progress at each substrate boundary.

````
You are executing the framework's Council Deployment Automation. Your role is the TRANSPORT LAYER: deploy substrate prompts to browser-based AI platforms, wait for outputs, capture outputs, hand off to the orchestrator. You are NOT the judgment layer, NOT the local-filesystem layer, NOT the verification layer.

The operator will provide, after this template, a Council-specific instantiation block containing: (1) the Council number and name; (2) the substrate deployment order with per-substrate platform + prompt text; (3) the orchestrator trigger message; (4) any Council-specific special handling (e.g., 4-substrate deployment for Council #4).

MANDATORY EXECUTION DISCIPLINE:
- Execute substrate deployments in the specified order. Do not skip. Do not reorder.
- Wait for each substrate response to fully complete before capturing the output.
- After each substrate output is captured, report to the operator in the Comet chat: "Substrate [LETTER] deployment complete. Output saved to [FILENAME]."
- If any step fails, STOP the workflow, report the failure state with as much detail as possible, and wait for operator instruction. Do not silently retry or substitute.

PLATFORM-SPECIFIC DEPLOYMENT PATTERNS:

Perplexity Deep Research (perplexity.ai):
1. Open perplexity.ai in a new tab. Verify operator is logged in.
2. Click the model/mode selector in the input area. Select "Deep Research" mode. Verify Deep Research mode is active (should be indicated in the input area) before proceeding.
3. Paste the substrate prompt text exactly. Do not modify, paraphrase, or add framing.
4. Send the prompt (click Send button or press Enter).
5. WAIT for Perplexity Deep Research to complete. Signal: response text has stopped streaming AND no "researching" or "searching" indicator is visible AND the citation panel is fully rendered. Typical duration: 5-15 minutes. Timeout: 30 minutes.
6. If Perplexity shows a rate-limit error, session expiration, or platform outage, STOP and report to operator with the specific error message.
7. Capture the response: prefer Perplexity's native "Copy" button on the response (usually top-right of the response block) which copies as markdown with citations. If native copy is unavailable, use browser select-all on the response text + copy.
8. Save the captured text as a plain markdown (.md) file to ~/Downloads/. Filename per Council instantiation block.
9. Verify saved file size > 5KB (sanity check: Perplexity DR responses are substantial). If < 5KB, STOP and report.

Claude Web Opus extended thinking (claude.ai):
1. Open claude.ai in a new tab. Verify operator is logged in.
2. Start a new chat. Verify no Master Setup Project is selected (the substrate deployment is not project-scoped; only the orchestrator deployment uses the Master Setup Project).
3. In the chat's model selector, choose "Claude Opus" (the highest-capability model available; specific model name may vary as Anthropic updates their lineup — pick the most capable Opus available).
4. Enable "Extended thinking" mode via the input-area toggle. Verify extended thinking is active before proceeding.
5. Paste the substrate prompt text exactly.
6. Send.
7. WAIT for Claude to complete. Signal: response streaming has stopped AND the extended-thinking indicator is dismissed AND no "thinking..." spinner is visible. Typical duration: 2-10 minutes. Timeout: 20 minutes.
8. If Claude shows extended-thinking rate-limit warning, message-length error, or platform outage, STOP and report.
9. Capture the response using Claude's native "Copy" button on the response block if available; else browser select-all + copy on the response body. IMPORTANT: capture the FINAL response text; do NOT capture the extended-thinking trail unless the Council-specific instantiation block explicitly requires it.
10. Save to ~/Downloads/ per Council instantiation filename.
11. Verify file size > 3KB.

Grok DeepSearch (grok.com or x.com/grok):
1. Open the Grok interface in a new tab. Verify operator is logged in.
2. Start a new chat.
3. Enable "DeepSearch" mode via the interface toggle (specific location may vary; typically a button near the input area). Verify DeepSearch is active before proceeding.
4. Paste the substrate prompt text exactly.
5. Send.
6. WAIT for Grok to complete. Signal: response streaming stopped AND no "searching" indicator AND source list (if provided) is fully rendered. Typical duration: 5-15 minutes. Timeout: 30 minutes.
7. Capture per Grok's native copy affordance or browser select-all + copy.
8. Save to ~/Downloads/ per Council instantiation filename.
9. Verify file size > 4KB.

Gemini Deep Research (gemini.google.com; required only for Council #4):
1. Open gemini.google.com in a new tab. Verify operator is logged in.
2. Enable Deep Research mode via the model/mode selector.
3. Paste the substrate prompt text exactly.
4. Send.
5. Gemini Deep Research typically works in two phases: research-plan review (Gemini proposes a plan; operator/agent must approve) + research-execution. If a plan-review step appears, click "Start research" or equivalent to approve the proposed plan.
6. WAIT for Gemini to complete. Typical duration: 5-20 minutes. Timeout: 30 minutes.
7. Capture the response text + citations. Save per Council instantiation filename.

CLAUDE CODE HANDOFF (for Councils where any substrate is assigned to Claude Code):
When the Council-specific instantiation block routes a substrate to Claude Code:
1. Report to operator: "Substrate [LETTER] is assigned to Claude Code (local terminal). Comet cannot deploy this substrate. Please trigger a Claude Code session with the substrate prompt, save the CC output to ~/Downloads/[FILENAME], and notify me via chat when complete. I will WAIT before proceeding to orchestrator deployment."
2. Enter WAIT state. Poll the operator's chat channel every 5 minutes for confirmation. Timeout: 4 hours (Substrate C may take substantial operator + CC time).
3. When operator confirms Substrate C is complete, verify the expected output file exists in ~/Downloads/ before proceeding.

ORCHESTRATOR DEPLOYMENT (final step; runs after all substrate outputs are captured):
1. Verify all substrate output files exist in ~/Downloads/ per the Council instantiation block's naming convention.
2. Open claude.ai in a new tab.
3. Navigate to the Master Setup Project (should be visible in the project selector or via URL).
4. Start a new chat in the Master Setup Project.
5. Verify the Master Setup Project's Custom Instructions are the ORCHESTRATOR-mode paste block (should reference Rule 14 six-pattern verdict classification and Rule 19 Marcus Reed Protocol). If Custom Instructions look stale (no Rule 14/19 references, or version mismatch), STOP and report to operator: "Master Setup Project Custom Instructions may be stale. Verify refresh per ~/Desktop/cw-master-setup-refresh-YYYY-MM-DD/ before proceeding."
6. Attach all substrate output files via the chat's file-upload affordance (paperclip icon or drag-and-drop). Verify all files are attached before sending.
7. Additionally attach the orchestrator synthesis prompt from ~/Desktop/council-orchestrator-synthesis-prompt.md.
8. In the chat message body, paste the orchestrator trigger message from the Council instantiation block.
9. Send.
10. WAIT for the orchestrator synthesis to complete. Typical duration: 2-5 minutes. Timeout: 15 minutes.
11. Capture the orchestrator response. Save to ~/Downloads/council-N-orchestrator-synthesis.md per instantiation filename.

POST-DEPLOYMENT:
Report to operator in Comet chat: "Council #N deployment complete. All substrate outputs and orchestrator synthesis saved to ~/Downloads/. Ready for Claude Code ingestion. Do NOT execute any local-filesystem operations or canonical mutations; those are Claude Code's responsibility."

Do NOT open the framework's GitHub repo. Do NOT execute git operations. Do NOT modify any local files beyond writing to ~/Downloads/. Do NOT judge the substrate outputs; that is the orchestrator's role. Your job ends when the operator has been notified that deployment is complete.

BANS:
- No silent retries. If a step fails, report to operator and wait.
- No output substitution. If a substrate produces obviously fabricated / rate-limit-error / null response, do NOT capture it as if it were valid; STOP and report.
- No workflow reordering. Execute in the specified order.
- No prompt paraphrasing. Paste exactly as provided in the Council instantiation block.
````

---

## Council-specific instantiation blocks

The template above is generic. Each Council's specific deployment is triggered by pasting the Council's instantiation block into Comet immediately after the template.

### Council #3 — Active-Inference Tractability (highest priority per prior recommendation)

**Substrate routing (per operator's Council #3 file on Desktop):**
- Substrate A: Perplexity Deep Research (active-inference theory + complexity literature)
- Substrate B: Claude Web Opus extended thinking (benchmark harness specification)
- Substrate C: Claude Code (V1-budget evaluation; requires local repo access)

**Council #3 instantiation block (paste into Comet after the template):**

```
Council: #3 — Active-Inference Tractability Under Realistic Branch Factors
Substrates: 3 total (A: Perplexity DR; B: Claude Web Opus extended thinking; C: Claude Code)

Filenames to save to ~/Downloads/:
- Substrate A: council-3-substrate-a-perplexity-dr.md
- Substrate B: council-3-substrate-b-claude-opus-extended.md
- Substrate C: council-3-substrate-c-claude-code.md (produced by operator's local CC session)
- Orchestrator: council-3-orchestrator-synthesis.md

Deployment order:
1. Substrate A (Perplexity DR) — paste the Substrate A prompt from ~/Desktop/council-3-active-inference-tractability.md. The prompt begins after the "## Substrate A" section header at the line "Copy everything below this line into the substrate verbatim:" — paste ONLY the verbatim block; do not include the routing table or the substrate-role header.
2. Substrate B (Claude Web Opus extended thinking) — paste the Substrate B prompt from the same file. Same extraction rule.
3. Substrate C handoff (Claude Code) — enter the Claude Code handoff pattern. Substrate C's prompt is in the same file, section "## Substrate C". The operator will trigger a Claude Code session locally with this prompt. Wait for operator confirmation.
4. Orchestrator deployment — after all 3 substrate outputs are captured in ~/Downloads/, execute the orchestrator deployment sub-workflow.

Orchestrator trigger message (paste into the Master Setup Project chat after attaching the 3 substrate files + council-orchestrator-synthesis-prompt.md):

"Council #3 orchestrator synthesis deployment. Attached: the synthesis prompt (see council-orchestrator-synthesis-prompt.md) + 3 substrate outputs (A: Perplexity DR active-inference theory + complexity literature; B: Claude Web Opus extended-thinking benchmark harness specification; C: Claude Code V1-budget evaluation).

Run the Madisonian Gate synthesis per the attached prompt. Classify the outcome using Rule 14's 6-pattern vocabulary. Surface any load-bearing evidence gaps or subtle reasoning-chain disagreements not caught by verdict-tier convergence alone. Apply Rule 19 Marcus Reed 3-condition gate to all substrate citations.

Note: Council #3's substantive question is whether audit-first sequencing for sophisticated active inference (Post 0119) is operationally tractable at 80-100 NPCs given realistic branch factors — a V1-blocking question. If the verdict is DEMOTE (sophisticated active inference cannot run at V1 scale), the framework's Path A commitment requires re-evaluation."

Special handling: Substrate C is Claude Code. Enter WAIT state at step 3; do not proceed to orchestrator deployment until operator confirms Substrate C's output is saved to ~/Downloads/council-3-substrate-c-claude-code.md.
```

### Council #2 — Appraisal Tags vs. Accumulator Minimalism

**Substrate routing:**
- Substrate A: Gemini Deep Research (OCC + CiF + EMA appraisal literature)
- Substrate B: Claude Web Opus extended thinking (architecture pressure-test)
- Substrate C: Grok DeepSearch (player-visible-difference evaluation)

**Council #2 instantiation notes:**
- Same template pattern as Council #3
- All three substrates are browser-based; Comet deploys all three without Claude Code handoff
- Filenames: `council-2-substrate-a-gemini-dr.md`, `council-2-substrate-b-claude-opus-extended.md`, `council-2-substrate-c-grok-deepsearch.md`, `council-2-orchestrator-synthesis.md`
- Wall-time estimate: ~30-45 min Comet execution + ~30-60 min operator ratification (no Claude Code handoff pause)

### Council #4 — Cross-Cultural Discipline Audit (HIGHEST fabrication risk; 4 substrates)

**Substrate routing:**
- Substrate A: Perplexity Deep Research (primary-text mapping Wiredu/Gyekye/Menkiti/Mbiti)
- Substrate A': Gemini Deep Research (cross-family verification; specifically watches for Wiredu-citation fabrication documented at `feedback_substrate_fabricates_quotes_when_inaccessible_source.md`)
- Substrate B: Claude Web Opus extended thinking (five-element discipline audit)
- Substrate C: Grok DeepSearch (player-facing language stress-test)

**Council #4 instantiation notes:**
- FOUR substrates instead of three (per Council #4's HIGHEST fabrication-risk framing)
- Substrate A and Substrate A' produce paired primary-text mappings for cross-family fabrication catch (n=1 Gemini DT Wiredu-citation fabrication on record; deploying Gemini as A' + Perplexity as A cross-verifies)
- Filenames: `council-4-substrate-a-perplexity-dr.md`, `council-4-substrate-a-prime-gemini-dr.md`, `council-4-substrate-b-claude-opus-extended.md`, `council-4-substrate-c-grok-deepsearch.md`, `council-4-orchestrator-synthesis.md`
- Wall-time estimate: ~45-75 min Comet execution (four substrates instead of three) + ~45-90 min operator ratification (higher-scrutiny mechanical spot-check of A vs A' agreement/divergence per framework's paired-substrate discipline)
- **Additional operator step BEFORE orchestrator deployment:** operator manually diffs A vs A' output for verbatim-quote overlap on Wiredu citations. Any citation appearing in one but not the other is flagged for manual primary-text verification before orchestrator sees the outputs. This is the specific Rule 19 fire-mitigation for Council #4's known-high-risk substrate territory.

### Council #5 — Longitudinal Benchmark Design

**Substrate routing:**
- Substrate A: Perplexity Deep Research (LIFELONG-SOTOPIA + SocialBench + STSS literature mapping)
- Substrate B: Claude Code (V1-compatible scenario design; requires local repo access)
- Substrate C: Grok DeepSearch (commercial-precedent mechanic review)

**Council #5 instantiation notes:**
- Same shape as Council #3 (one substrate assigned to Claude Code)
- Substrate B is Claude Code (not Substrate C as in Council #3); the CC handoff step occurs at position 2 in the deployment order, not position 3
- Filenames: `council-5-substrate-a-perplexity-dr.md`, `council-5-substrate-b-claude-code.md`, `council-5-substrate-c-grok-deepsearch.md`, `council-5-orchestrator-synthesis.md`
- **Parallelization opportunity:** Substrate C (Grok DeepSearch) can run in parallel with the Substrate B Claude Code handoff. Comet deploys Substrate C to Grok immediately after Substrate A completes, while operator runs Substrate B locally in Claude Code. Both complete concurrently; orchestrator deploys once both are done. Saves ~15-30 min wall-time vs strict sequential.

---

## Failure modes catalogue + fallbacks

Comet is not infallible. The below are documented failure modes with recovery patterns.

### Comet-side failure modes

1. **Comet session timeout.** Comet browser sessions have their own timeouts (typically 30-60 min). If a substrate's response exceeds session timeout, Comet may lose state. Mitigation: for long-running substrates (Perplexity DR, Gemini DR), instruct Comet to check session state before capturing output. Fallback: operator manually captures the substrate output from the still-open browser tab and hands off to Comet for orchestrator deployment.

2. **Comet UI-interaction failure.** Substrate platform redesigns can break Comet's UI-element identification (e.g., "Deep Research mode selector" moves; "Send" button changes label). Fallback: Comet reports the specific interaction that failed; operator manually completes that step; instructs Comet to resume from the next step.

3. **Comet download failure.** Comet cannot always guarantee successful save-to-Downloads. Fallback: instruct Comet to verify file existence + size after each save. If verification fails, operator manually saves the visible browser content.

### Substrate-platform failure modes

4. **Rate limit hit.** Perplexity DR, Claude Web extended thinking, Grok DeepSearch, and Gemini Deep Research all have daily/hourly rate limits on some tiers. Fallback: Comet reports the specific rate-limit error message; operator waits for reset window or upgrades tier; deployment resumes from the failed substrate.

5. **Platform outage.** Any substrate platform can go down. Fallback: Comet reports; operator waits; deployment resumes.

6. **Session expiration.** Operator logs out or session expires mid-deployment. Fallback: Comet reports; operator re-authenticates; deployment resumes.

### Substrate-output failure modes

7. **Fabrication in substrate output.** Comet cannot detect this; the framework's Rule 19 Marcus Reed Protocol runs at the orchestrator layer, not the transport layer. Fallback: orchestrator catches; if orchestrator flags fabrication, the operator + Claude Code either re-run the affected substrate with tightened prompt or accept the flagged output with dissent-log annotation.

8. **Truncated response.** Some substrates truncate on long outputs. Fallback: Comet verifies file size against expected minimum; if truncated, escalates to operator for re-deployment with reduced scope or chunked prompting.

9. **Wrong-mode capture.** Comet accidentally captures the substrate's thinking-trail instead of final response, or captures a rate-limit error page as if it were the response. Fallback: file-size sanity checks catch most; residual cases require operator manual verification before orchestrator deployment.

### Claude Code handoff failure modes (Councils #3 + #5)

10. **Operator forgets to trigger Claude Code session.** Comet enters WAIT state at step 3 (Council #3) or step 2 (Council #5); 4-hour timeout fires without operator confirmation. Fallback: Comet reports timeout to operator's Comet chat; deployment can be resumed once operator confirms Substrate C/B is complete.

11. **Claude Code output missing when Comet resumes.** Operator confirms but forgets to save output to expected filename. Fallback: Comet verifies file existence at expected path; if missing, escalates to operator for file-move.

### Orchestrator failure modes

12. **Master Setup Project custom instructions stale.** Orchestrator applies wrong version of Rule 14 or Rule 19 discipline. Fallback: Comet's pre-orchestrator check identifies staleness; operator refreshes project per current version; deployment resumes.

13. **Orchestrator produces incomplete synthesis.** Missing sections; verdict pattern not classified; escalation criteria fired but not surfaced. Fallback: operator reviews synthesis before accepting; if incomplete, re-prompts orchestrator with specific gap identification.

---

## Post-Comet handoff to Claude Code (operator + CC responsibilities)

After Comet reports "Council #N deployment complete," the operator triggers a Claude Code session and pastes:

```
Ingest Council #N: attached is the Comet deployment output at ~/Downloads/council-N-*.md (five files: 3-4 substrate outputs + orchestrator synthesis). Apply the Council #1 ingestion pattern per project_council_1_close_pattern_b_2026-06-30.md:

1. Independently verify any load-bearing external citations via WebFetch.
2. Audit each substrate output for verification-trail completeness, fabrication risk, and Rule 19 clean-negative status.
3. Contest or concur with the orchestrator's Rule 14 pattern classification; if contest, explain reasoning-chain shift.
4. Update post-ideas.md Idea [N] with substantive contributions.
5. If verdict is a canonical mutation candidate, propose the write-back scope for operator ratification.
6. Archive all 4-5 files to ~/Projects/the-street-code/_archive/YYYY-MM-DD-council-N-<name>/.
7. Regen Treasure Map after any commit.
```

Claude Code executes the ingestion + audit + optional canonical mutations (posts / spec files / methodology guide updates) per operator ratification.

---

## Total wall-time envelope per Council

| Council | Substrates | Comet wall-time | Operator wall-time | Total |
|---|---|---|---|---|
| #2 (all browser) | 3 (Gemini + Claude + Grok) | ~30-45 min | ~45-90 min ratification + CC ingest | ~1.5-2.5 h |
| #3 (with CC handoff) | 3 (Perplexity + Claude + CC) | ~15-25 min for A + B; ~1-3 h wait for C; ~10-15 min for orchestrator | ~1-3 h for Substrate C + ~45-90 min ratification | ~2.5-5.5 h |
| #4 (4 substrates, high-risk) | 4 (Perplexity + Gemini + Claude + Grok) | ~45-75 min | ~15-30 min manual A-vs-A' diff + ~60-120 min ratification + CC ingest | ~2.5-4 h |
| #5 (with CC handoff, parallelizable) | 3 (Perplexity + CC + Grok) | ~15-25 min for A + orchestrator prep; ~1-3 h wait for B (parallel with Grok) | ~1-3 h for Substrate B + ~45-90 min ratification | ~2.5-5 h |

**Compare to prior (all-manual) wall-time: ~2-4 hours per Council × 4 Councils = 8-16 hours operator wall-time.**

**With Comet automation: ~9-15 hours total (partial reduction; the CC-handoff Councils don't save much because Substrate B/C still requires operator time).**

Where Comet actually saves time: Council #2 and Council #4 (all-browser substrates); ~2-3 hours saved per Council. Councils #3 and #5 (with CC handoff): ~30-60 min saved per Council (the Comet-scriptable browser deployments run unattended while operator focuses on the CC-handoff substrate).

---

## Guide revision protocol

Update this guide when:
- A Comet deployment surfaces a platform UI change that breaks the current script
- A new Council is added to the queue beyond #2-#5
- A substrate platform is added (e.g., a new AI research surface) or removed
- The paired-n=4 substrate-discipline calibration evolves (Comet prompt discipline changes)
- The framework's Rule 14 verdict-pattern vocabulary extends (orchestrator trigger message changes)

Do NOT retroactively edit the guide during a Council deployment. Per the framework's immutability convention, mid-execution scope changes are anti-pattern territory. Complete the current Council with the current guide; document surfaced issues in the operator's session notes; apply revisions between Councils.

---

## Cross-references

- `~/Projects/the-street-code/methodology/ablation-gate-relationship-mode-v1.md` — sibling methodology artifact; Council #1 BANK half execution guide
- `~/Projects/the-street-code/methodology/post_audit_checklist.md` — sibling methodology artifact; pre-commit post audit discipline
- `~/Desktop/council-2-appraisal-tags-vs-minimalism.md` through `~/Desktop/council-5-longitudinal-benchmark-design.md` — Council prompt files staged 2026-06-30
- `~/Desktop/council-orchestrator-synthesis-prompt.md` — reusable orchestrator synthesis prompt template
- `~/Desktop/cw-master-setup-refresh-2026-06-30/` — CW Master Setup Project refresh kit (deploy before first Council to ensure orchestrator layer is current)
- `~/.claude/projects/-Users-jimmy/memory/feedback_substrate_opaque_citation_format_as_risk_signal.md` — paired-n=4 substrate-discipline calibration lesson (informs prompt discipline; irrelevant to transport-layer automation but load-bearing for what Comet deploys)
- `~/.claude/projects/-Users-jimmy/memory/feedback_substrate_fabricates_quotes_when_inaccessible_source.md` — n=1 Gemini DT fabrication on Wiredu citations; motivates Council #4's 4-substrate deployment with A+A' cross-verification
- `~/.claude/projects/-Users-jimmy/memory/project_council_1_close_pattern_b_2026-06-30.md` — Council #1 close arc; ingestion pattern reference for Comet-deployment aftermath
- `~/.claude/projects/-Users-jimmy/memory/feedback_rule_14_pattern_a_vs_b_modal_status_check.md` — Rule 14 discipline informing orchestrator verdict-pattern classification
