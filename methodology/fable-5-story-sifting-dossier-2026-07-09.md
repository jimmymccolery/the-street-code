# Story Sifting and Computational Narrative Pattern Recognition: Research Dossier

## Purpose and Scope

This dossier grounds the design of a "story sifting" layer for a deterministic, no-LLM-at-runtime multi-agent life simulation (1,000–5,000 NPCs, 1940s–1960s American bowling-alley management sim) that must recognize stories in an event stream and surface them diegetically (newspapers, league newsletters, diaries). It covers five areas: (1) the academic story-sifting literature, (2) shipped-game precedents, (3) narratology pattern inventories, (4) life-course and life-narrative psychology, and (5) story-evaluation methodology. Every claim is cited to its source. A final section lists claims that could not be fully verified.

---

## 1. Story Sifting / Story Recognition Literature

### 1.1 Origins: Ryan's "story recognition" and "story sifting"

The term **story recognition** was introduced by James Ryan, Michael Mateas, and Noah Wardrip-Fruin, and the successor term **"story sifting"** was coined in Ryan's 2018 UC Santa Cruz dissertation, *Curating Simulated Storyworlds* ([eScholarship](https://escholarship.org/uc/item/1340j5h2), PDF: [escholarship.org](https://escholarship.org/content/qt1340j5h2/qt1340j5h2.pdf)). Ryan has identified story sifting as one of four major open challenges in interactive emergent narrative, as reported in Kreminski, Dickinson & Wardrip-Fruin's Felt paper ([Felt: A Simple Story Sifter, ICIDS 2019 PDF](https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf)). The dissertation introduces the **Sheldon** story-sifting system and the **Sheldon County** simulated-storyworld podcast, built atop the **Hennepin** simulation engine, and frames sifting as a "curationist" alternative to fully generative storytelling ([Kreminski Winnow paper, AIIDE 2021 PDF](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf) — Related Work section cites Ryan 2018 directly).

**Exact definition (Kreminski, Dickinson & Wardrip-Fruin, "Felt: A Simple Story Sifter," ICIDS 2019):**

> "The problem of story sifting involves the selection of events that constitute a compelling story from a larger chronicle of events. Often this chronicle is generated through the computational simulation of a storyworld, whose output consists of a profusion of events, many of which are relatively uninteresting as narrative building blocks. The challenge, then, is to sift the wheat from the chaff, identifying event sequences that seem to be of particular narrative interest or significance and bringing them to the attention of a human player or interactor." ([Felt paper, dl.acm.org / mkremins.github.io PDF](https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf))

Felt frames story sifters as "mixed-initiative creativity support tools" that help players narrativize play experiences, and explicitly credits the Bad News project as motivating the need for a computational sifting engine ([Felt paper](https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf)).

### 1.2 Felt (ICIDS 2019)

Felt is a "language-based story sifter and rules-based simulation engine" implemented over a DataScript/Datalog-style relational event database, allowing sifting patterns to be expressed as declarative queries over event predicates and bound variables ([Felt, ICIDS 2019, mkremins.github.io PDF](https://mkremins.github.io/publications/Felt_SimpleStorySifter.pdf)). The paper positions story sifting patterns as retrospective — matched against a complete chronicle after the fact — in contrast to the incremental matching later introduced by Winnow ([Winnow paper](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)).

### 1.3 Winnow (AIIDE 2021)

Winnow (Kreminski, Dickinson & Mateas) is a **domain-specific language for incremental story sifting** that introduces "clear acceptor-based semantics around the maintenance of partial sifting pattern matches, which can be narrativized or exposed to a human user prior to their completion" ([Winnow, AIIDE 2021 PDF](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)). Where Felt patterns can only be evaluated retrospectively against a full chronicle, Winnow patterns can be evaluated incrementally as new events arrive, and can be compiled directly to Felt-equivalent patterns when incremental matching is unneeded ([Winnow paper](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)). Source code is public on GitHub ([mkremins/winnow](https://github.com/mkremins/winnow)).

**Reported benchmark result:** On the most demanding tested condition (1,000 partial pattern matches maintained simultaneously), Winnow updated its partial-match pool in an average of 912ms per incoming event (min 443ms, max 1,097ms), which the authors note falls "within the one-second response window suggested by usability experts as sufficient for maintaining the user's [attention]" ([Winnow, AIIDE 2021 PDF](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)). Benchmarks were run in Firefox 87.0 on a 2019 MacBook Pro (2.6GHz 6-core i7, 16GB RAM), with 30 event types and 5 characters ([Winnow paper](https://mkremins.github.io/publications/Winnow_AIIDE2021.pdf)).

### 1.4 Loose Ends (AIIDE 2022)

Loose Ends is a "mixed-initiative creative interface for playful storytelling" evaluated with **five expert evaluators** using a questionnaire adapted from the Germinate expert evaluation instrument (Q1–Q5) plus three new questions (Q6–Q8) targeting co-creative storytelling experience, on a 1–5 agreement scale ([Loose Ends, AIIDE 2022, dl.acm.org](https://dl.acm.org/doi/abs/10.1609/aiide.v18i1.21955)). Reported mean scores: Usability (Q2) 4.2, Effortlessness (Q3) 4.8, Control (Q4) 3.8, Fun (Q5) 4.2, Ownership (Q6) 3.2, Curiosity (Q7) 4.0, Direction (Q8) 4.0 (all out of 5) (Loose Ends paper, per fetched full text). The paper's central design goal was to mitigate "directionlessness" reported by 4 of 5 playtesters of the predecessor system *Why Are We Like This?*; all Loose Ends evaluators but one scored Q8 (sense of direction) at 4 or higher, and evaluators E4/E5 explicitly reported never experiencing "writer's block" during play (Loose Ends full paper text, fetched from ACM DL record above).

### 1.5 Why Are We Like This? (FDG 2020)

*Why Are We Like This?* is described in its own paper as "The AI Architecture of a Co-Creative Storytelling Game," a system in which four of five playtesters reported a sense of directionlessness at least once during play — the empirical finding that directly motivated Loose Ends's design goals ([Loose Ends paper](https://dl.acm.org/doi/abs/10.1609/aiide.v18i1.21955), citing Kreminski et al. 2020a).

### 1.6 Storylets design-space papers (with Wardrip-Fruin)

"Sketching a Map of the Storylets Design Space" (Kreminski & Wardrip-Fruin, ICIDS 2018) frames **storylets** as modular, self-contained units of narrative content gated by preconditions and identifies multiple design dimensions along which storylet-based systems vary (e.g., authored vs. procedurally generated, single-use vs. repeatable, player-facing vs. simulation-only) (per fetched ICIDS2018 full text, workspace batch1.json[4]).

### 1.7 Authoring for Story Sifters; Synthesifter

"Authoring for Story Sifters" (Kreminski et al.) addresses the authorial burden of specifying sifting patterns by hand. "Toward Example-Driven Program Synthesis of Story Sifting Patterns" (the *Synthesifter* system, INT 2020) proposes synthesizing sifting patterns from user-provided examples rather than requiring hand-authored declarative queries, directly addressing the technical-authoring bottleneck that later motivated Arc Sift's visual "draw the arc" interface ([Arc Sift, AAMAS 2022](https://www.ifaamas.org/) — cites this bottleneck explicitly, see Section 1.10 below).

### 1.8 Toward Narrative Instruments (ICIDS 2021)

Kreminski & Mateas's "Toward Narrative Instruments" (ICIDS 2021) proposes that some interactive emergent narrative systems are better understood as **narrative instruments** — analogous to musical instruments — that support authorship-oriented play, rather than as games with a pre-authored "multiform plot" (per fetched full text, workspace batch10.json[0]). The paper draws on the study of **retellings** (player-created stories about gameplay), and explicitly cites Dwarf Fortress's characteristic story shape — "a gradual rise followed by sudden precipitous decline" — as an example of an emergent narrative arc recognizable to players without formal sifting tooling (per fetched full text).

### 1.9 Talk of the Town and Bad News (Ryan, Samuel, et al.)

**Bad News** is an interactive theatrical experience built on the **Talk of the Town (ToT)** simulation engine, in which a live actor (the "Wizard") uses a WizActor interface to portray simulated townsfolk to a human interactor delivering news of a relative's death ([Quantified Analysis of the Bad News interactive experience, Samuel/Summerville/Ryan/England, per fetched full text](https://mkremins.github.io/) — see workspace batch2.json[0]). Talk of the Town models **knowledge propagation** among agents — characters learn about events through simulated gossip and direct observation — as well as **fallibility**: characters may hold false, incomplete, or outdated beliefs, and their retellings of events can **mutate or decay** as they are passed between agents, modeling real social information degradation (per fetched GameAIPro3 ToT chapter, workspace batch3.json[1], titled "433" in fetch metadata). This knowledge-propagation/fallibility/mutation model is directly relevant to a bowling-alley sim's diegetic newspapers and league newsletters, which would plausibly contain second-hand, imperfect renderings of underlying simulated events rather than ground truth.

**Gossamer** (CoG 2023) extends this line of work with a dedicated gossip-simulation model exploring how information (accurate or distorted) propagates through a social network of simulated agents (per fetched full text, workspace batch2.json[4]).

### 1.10 2022–2026 follow-on work

- **Automated Story Sifting Using Story Arcs / Arc Sift** (Leong, Porteous & Thangarajah, AAMAS 2022 Extended Abstract) lets users specify sifting criteria by **freehand-drawing a story arc shape** rather than writing a technical query. The system builds **Dynamic Character Networks** tracking relationship scores between agents over time from an **Abstract Interaction Log**, converts these into simulation story arcs, and uses **Dynamic Time Warping** to compute similarity between a drawn query arc and simulation arcs, returning best-matching event sequences ([Arc Sift, AAMAS 2022, full text fetched](https://www.ifaamas.org/), workspace batch3.json[4]). The arc shapes tested were drawn from a "set of common shapes" — explicitly named **RagsToRiches, RichesToRags, ManInHole, Icarus, Cinderella, Oedipus** — the same six shapes later formalized by Reagan et al. 2016 (see Section 3.7) (Arc Sift paper, full text).
- **ChatGPT for story sifting** (ICCC 2023) explores using a large language model to perform or assist story-sifting tasks (per fetched full text, workspace batch2.json[7]) — relevant as a contrast case for the target system's explicit no-LLM-at-runtime constraint.
- Kreminski's continuing publication record (bibliography and CV, fetched in full) shows an unbroken line of work from Felt (2019) through Winnow (2021), Loose Ends (2022), and Toward Narrative Instruments (2021), with the CV confirming Kreminski's later academic appointment and continued narrative-systems research program (per fetched Kreminski publications and CV pages, workspace batch10.json[1–2]).

### 1.11 Emily Short: storylets and quality-based narrative design (Failbetter/Fallen London)

Emily Short's "Survey of Storylets-Based Design" blog post surveys the storylet pattern as used in **Fallen London** and its successor **StoryNexus** (Failbetter Games), where narrative content is authored as discrete storylets gated by "qualities" (numeric or boolean state variables) rather than a branching tree, letting a large combinatorial space of content be authored modularly and surfaced contextually as qualities change (per fetched blog excerpt, workspace batch6.json[6]). This quality-based storylet model is a direct ancestor of the storylets-design-space formalism in Section 1.6 and is architecturally close to a "typed event bus + preconditioned content" pattern.

---

## 2. Shipped-Game Precedents

| System | Mechanism | Authored vs. Emergent | Strengths | Failure Modes |
|---|---|---|---|---|
| **Dwarf Fortress** (Legends Mode) | Procedurally generates and logs a full world history (wars, migrations, deaths, artifact creation) that players can browse after or during play; per "Toward Narrative Instruments," the game's characteristic arc is "a gradual rise followed by sudden precipitous decline" ([Kreminski & Mateas, ICIDS 2021](https://mkremins.github.io/), fetched full text) | Emergent (simulation-driven; no authored plot) | Extremely rich, replayable emergent history; source of widely retold community stories ("retellings") | No built-in sifting layer — players must manually browse legends text to find compelling threads; the game itself does not surface "this is a story" signals |
| **RimWorld** (AI Storyteller) | Three named "storyteller" AIs — **Cassandra Classic** (rising-tension curve: push, breathing room, push again), **Phoebe Chillax** (long gaps between disasters), **Randy Random** (fully random, no dramatic shaping) — that generate raids, trade events, and disasters based on colony wealth, population, and time since last major event ([RimWorld Wiki, AI Storytellers](https://rimworldwiki.com/wiki/AI_Storytellers), fetched full text) | Authored *pacing curves* driving emergent *content* — the storyteller doesn't write stories, it schedules event *triggers* according to a tension curve | Simple, transparent tunable "director" pattern; produces felt dramatic pacing without needing to model semantic content of what happens | The storyteller has "no in-game body, location, or manifestation" — it is pure pacing, not narrative recognition; it cannot tell you *what story just happened*, only when to inject the next event ([RimWorld Wiki](https://rimworldwiki.com/wiki/AI_Storytellers)) |
| **Caves of Qud** (mythic biographies) | Procedurally generates "mythic" character biographies using a **state machine plus replacement grammar**, then applies a **rationalization** pass that reframes raw generated events into causally and thematically coherent biographical narrative ([Grinblat & Bucklew, "Subverting the Mythos: Procedural Generation of Mythic Biographies in Caves of Qud," PCG Workshop/FDG 2017 PDF](https://www.pcgworkshop.com/archive/grinblat2017subverting.pdf), fetched full text) | Emergent generation + authored rationalization layer | Produces flavorful, individually distinct legendary-figure lore for procedurally generated content without manual authoring per-character | Rationalization is a post-hoc narrative gloss on essentially random generative output — risk of producing narrative-shaped text that doesn't correspond to meaningfully differentiated underlying gameplay events |
| **Wildermyth** (event templates) | Authored **event templates** (an "Event" system, documented on the Wildermyth wiki) written under an explicit "Poetics for Emancipation of Events" design philosophy, combined with procedural slotting of specific characters/relationships into template events ([Wildermyth Wiki, Event design philosophy](https://wildermyth.com/wiki/Event_design_philosophy), fetched full text; [Template:Event](https://wildermyth.com/wiki/Template:Event)) | Authored templates + emergent character/context binding | Preserves high narrative craft/voice of hand-authored vignettes while letting *which* characters experience them emerge from play | Template combinatorics are finite — repeat playthroughs can expose the underlying template pool; requires substantial authored content to avoid repetition |
| **Shadows of Doubt** | Procedurally generates an entire city, its NPC citizens (with schedules, apartments, relationships), and murder cases per save-file seed; the player must gather evidence (fingerprints, camera footage, witness statements) and submit a case-resolution form identifying suspect, address, evidence, and weapon ([Wikipedia, Shadows of Doubt](https://en.wikipedia.org/wiki/Shadows_of_Doubt), fetched full text) | Fully emergent per-seed generation of citizens and cases; no fixed authored mystery plots | High replayability; every case is a genuinely novel configuration of the simulated world | The "mystery" is procedurally assembled from simulation state, not authored for narrative payoff — investigative logic can occasionally feel arbitrary since it is not curated to any narrative pattern |
| **Crusader Kings III** (character memories) | Since the "Friends & Foes" free update, characters accumulate discrete **Memory** objects (children born, battles won, rivals killed, etc.) that are consumed by later events — e.g., an assassin citing a specific past grievance memory as motive; a **Memory Viewer** lets players browse a character's memories chronologically; **private memories** (e.g., taking a lover, committing murder) are hidden unless viewing your own character or in Observer mode; memories can fade over time, and most are lost on death except for player-controlled rulers and high-tier rulers, whose memories persist longer or permanently ([GamingOnLinux, "Crusader Kings III: Friends & Foes out with free update," 2022](https://www.gamingonlinux.com/2022/09/crusader-kings-iii-friends-a-foes-out-with-free-update-and-free-weekend/), fetched full text) | Emergent generation of memory *objects*; authored consumption rules for how memories feed back into event/dialogue triggers | Directly analogous to a "typed event bus with decay" — memories are structured, typed, timestamped, and explicitly designed to feed back into future narrative content, closely matching the target system's own three-horizon memory design | Memory *decay* is simple (time-based fade, loss on death) rather than psychologically modeled; memories are consumed by scripted event conditions rather than sifted for emergent higher-order story shapes |
| **The Sims** (memories/wants system) | Sims accumulate discrete memory entries tied to life events, which can trigger emotional "moodlets" and feed into a separate wants/fears (Sims 2) or whims (Sims 4) system that generates short-term goals from personality and recent memories ([Sims community search results on wants/fears mechanic](https://www.reddit.com/r/sims2/comments/1ekqyxl/wants_fears_and_memories_are_so_important/); wants/fears documented on Sims Wiki) | Emergent memory accrual driving authored want/fear generation rules | Long-running proof that a life-sim can sustain legible personal narratives (romance, rivalry, career arcs) purely from discrete typed memory events plus a motivational layer | Memories in most Sims titles are largely a **flavor/UI layer** rather than a systemic story-recognition mechanism — the game does not identify or foreground which combinations of memories constitute a "story" for the player |

**Cross-cutting observation for the target design:** Only Dwarf Fortress, Caves of Qud, and (partially) Talk of the Town treat *narrative shape recognition* as a first-class problem the way the academic story-sifting literature does; RimWorld, CK3, and The Sims solve the adjacent-but-distinct problem of *pacing* or *content-triggering* from structured event/memory state without attempting to recognize which sequences constitute a "story" worth surfacing. This gap is precisely what the story-sifting literature in Section 1 was built to fill, and is the strongest argument for adopting Felt/Winnow-style declarative sifting patterns rather than a RimWorld/CK3-style trigger-and-memory approach alone.

---

## 3. Narratology Pattern Inventories

### 3.1 Propp's 31 functions

Vladimir Propp's *Morphology of the Folktale* (1928) analyzed Russian fairy tales and identified **31 recurring narrative functions** performed by characters (e.g., "1. Absentation," "2. Interdiction," "3. Violation," ... through functions describing departure, testing, receipt of a magical agent, struggle, pursuit, rescue, unrecognized arrival, exposure, transfiguration, punishment, and wedding) ([full numbered list, billstifler.org](http://billstifler.org/), fetched full text; corroborated by [Wikipedia, Vladimir Propp](https://en.wikipedia.org/wiki/Vladimir_Propp), fetched full text covering functions 1–12 in detail). Propp argued that while the *dramatis personae*, motivations, and means of function execution vary across tales, the functions themselves and their sequence are stable — a claim later echoed structurally by the Reagan et al. six-shape reduction (Section 3.7).

### 3.2 Aarne–Thompson–Uther Index (ATU)

The Aarne–Thompson tale-type index, originally published by Antti Aarne in 1910 and revised by Stith Thompson (1928, further revised as Aarne–Thompson–Uther by Hans-Jörg Uther in 2004), classifies folktales by recurring **tale types** (e.g., "The Dragon-Slayer," "Cinderella") rather than by granular motifs ([Wikipedia, Aarne–Thompson–Uther Index](https://en.wikipedia.org/wiki/Aarne%E2%80%93Thompson%E2%80%93Uther_Index), fetched full text). The ATU index and Thompson's Motif-Index (Section 3.3) are explicitly designed to be used together and cross-indexed ([Wikipedia, Motif-Index of Folk-Literature](https://en.wikipedia.org/wiki/Motif-Index_of_Folk-Literature), fetched full text, quoting folklorist Mary Beth Stein: "Together with Thompson's six-volume *Motif-Index of Folk-Literature*, with which it is cross-indexed, *The Types of Folktale* constitutes the most important reference work and research tool for comparative folk-tale analysis").

### 3.3 Thompson Motif-Index

Stith Thompson's *Motif-Index of Folk-Literature* (1932–1936, revised 1955–1958) is a six-volume catalogue of **motifs** — granular recurring narrative elements — organized under umbrella topical categories (e.g., category "S" = "Unnatural Cruelty," subdivided into specific entries such as "S50") ([Wikipedia, Motif-Index of Folk-Literature](https://en.wikipedia.org/wiki/Motif-Index_of_Folk-Literature), fetched full text). Thompson defined a *motif* two ways: the "striking" definition — "the smallest element in a tale having a power to persist in tradition. In order to have this power it must have something unusual and striking about it" — and a broader, more "cautious" definition covering "[a]nything that goes to make up a traditional narrative... any of the elements of narrative structure" (Wikipedia, Motif-Index of Folk-Literature, exact quotes as fetched). Critic Alan Dundes, despite being an outspoken critic of the broader indexing project, still called the Motif-Index and ATU together "two of the most valuable tools in the professional folklorist's arsenal of aids for analysis" (Wikipedia, Motif-Index of Folk-Literature).

### 3.4 Tobias's 20 Master Plots

Ronald B. Tobias's *20 Master Plots (And How to Build Them)* identifies twenty recurring master plots. Confirmed entries (from the first eleven, directly fetched): **1. Quest**, **2. Adventure**, **3. Pursuit**, **4. Rescue**, **5. Escape**, **6. Revenge**, **7. The Riddle**, **8. Rivalry**, **9. Underdog**, **10. Temptation**, **11. Metamorphosis** ([ChangingMinds.org, Tobias' 20 Plots](http://changingminds.org/disciplines/storytelling/plots/tobias_plots.htm), fetched full text). The remaining nine plots in Tobias's list (commonly cited elsewhere as including Transformation, Maturation, Love, Forbidden Love, Sacrifice, Discovery, Wretched Excess, Ascension, and Descension) are attested at title level in search results (e.g., [Writer's Digest, "20 Master Plots"](https://www.writersdigest.com/improve-my-writing/20-master-plots)) but the full text of that specific page could not be fetched successfully — see Unverified section.

### 3.5 Booker's Seven Basic Plots

Christopher Booker's *The Seven Basic Plots: Why We Tell Stories* (2004) proposes seven archetypal plots: **Overcoming the Monster, Rags to Riches, The Quest, Voyage and Return, Comedy, Tragedy, and Rebirth** ([Wikipedia, The Seven Basic Plots](https://en.wikipedia.org/wiki/The_Seven_Basic_Plots), fetched full text). Booker additionally proposes a "meta-plot" underlying all seven, structured in five stages: **Anticipation, Dream, Frustration, Nightmare, and Resolution** (Wikipedia, The Seven Basic Plots, fetched full text).

### 3.6 Polti's 36 Dramatic Situations

Georges Polti's *Les Trente-Six Situations Dramatiques* (1895) catalogues 36 recurring dramatic situations, each defined by a configuration of character roles (e.g., "Supplication," "Deliverance," "Crime Pursued by Vengeance," "Vengeance Taken for Kindred Upon Kindred," "Pursuit," "Disaster," "Falling Prey to Cruelty/Misfortune," "Revolt," "Daring Enterprise," "Abduction," "The Enigma," "Obtaining," "Enmity of Kinsmen," "Rivalry of Kinsmen," "Murderous Adultery," "Madness," "Fatal Imprudence," "Involuntary Crimes of Love," "Slaying of a Kinsman Unrecognized," "Self-Sacrificing for an Ideal," "Self-Sacrifice for Kindred," "All Sacrificed for Passion," "Necessity of Sacrificing Loved Ones," "Rivalry of Superior and Inferior," "Adultery," "Crimes of Love," "Discovery of the Dishonor of a Loved One," "Obstacles to Love," "An Enemy Loved," "Ambition," "Conflict with a God," "Mistaken Jealousy," among others), with the Wikipedia list captured up through roughly situation 32 in the fetched content ([Wikipedia, The Thirty-Six Dramatic Situations](https://en.wikipedia.org/wiki/The_Thirty-Six_Dramatic_Situations), fetched full text — near-complete list).

### 3.7 Vonnegut's story shapes and Reagan et al. 2016

Kurt Vonnegut proposed, in a rejected master's thesis and later popularized in talks, that story emotional trajectories can be plotted on axes of **"Beginning–End"** (time) and **"Ill Fortune–Great Fortune"** (protagonist fortune), famously stating: "There is no reason why the simple shapes of stories can't be fed into computers, they are beautiful shapes" (quoted in [Reagan, Mitchell, Kiley, Danforth & Dodds, "The emotional arcs of stories are dominated by six basic shapes," EPJ Data Science 2016, full text fetched](https://epjdatascience.springeropen.com/)).

**Verified exact citation:** Andrew J. Reagan, Lewis Mitchell, Dilan Kiley, Christopher M. Danforth, Peter Sheridan Dodds, "The emotional arcs of stories are dominated by six basic shapes," *EPJ Data Science*, vol. 5, article 31 (2016), DOI: 10.1140/epjds/s13688-016-0093-1 (confirmed via [Semantic Scholar citation record](https://www.semanticscholar.org/), fetched full text, which lists 443 citing works, and via the fetched full paper text itself).

**Method (from the fetched full paper):** The authors used **sentiment/emotional-valence time-series extraction** on the text of **1,327 fiction books drawn from Project Gutenberg**, applied **Singular Value Decomposition (SVD)** to reduce dimensionality of the resulting emotional-arc time series, then performed **hierarchical clustering with Ward's method** and cross-validated cluster structure using a **self-organizing map (SOM)**, converging on **six dominant emotional-arc shapes**.

**Exact six shape names with rise/fall notation (from the fetched full paper):**

| Shape | Arc pattern |
|---|---|
| Rags to riches | Rise |
| Tragedy / Riches to rags | Fall |
| Man in a hole | Fall–rise |
| Icarus | Rise–fall |
| Cinderella | Rise–fall–rise |
| Oedipus | Fall–rise–fall |

These same six shape names were independently adopted as the query-arc vocabulary in Arc Sift's user study (Section 1.10), demonstrating the shapes' direct usability as a **sifting-pattern taxonomy**, not merely a literary-critical curiosity ([Reagan et al. 2016, EPJ Data Science full text](https://epjdatascience.springeropen.com/); [Arc Sift, AAMAS 2022 full text](https://www.ifaamas.org/)).

### 3.8 Freytag's Pyramid

Gustav Freytag's *Die Technik des Dramas* (1863) proposed a five-part dramatic structure — **Exposition, Rising Action, Climax, Falling Action, and Denouement (Catastrophe/Resolution)** — visualized as a pyramid or triangle with the climax at the story's structural midpoint, built from a "play" (rising) and "counterplay" (falling) half ([The Write Practice, "Freytag's Pyramid"](https://thewritepractice.com/freytags-pyramid/); [Scribophile, "Freytag's Pyramid: Definitions and Examples"](https://www.scribophile.com/academy/what-is-freytags-pyramid)). Notably, the term "denouement" never actually appears in Freytag's original German text — it was added by later interpreters (The Write Practice, "Freytag's Pyramid"). Freytag conceived the climax not simply as "the exciting part" but as the scene portraying the *fullest energy* of the protagonist, after which that same energy/ambition reverses against the protagonist in a tragedy or resolves favorably in a comedy (The Write Practice, "Freytag's Pyramid," paraphrasing Freytag's *Technique of the Drama*).

### 3.9 Labov & Waletzky's 1967 narrative structure

William Labov and Joshua Waletzky's 1967 sociolinguistic model of oral personal-narrative structure identifies six potential components: **Abstract, Orientation, Complication, Evaluation, Resolution, and Coda** ([Labov and Waletzky narrative model, uniroma2.it teaching document](https://didattica.uniroma2.it/files/scarica/insegnamento/39508-Lingua-Inglese-3/5829-Labov-Narrative-Model), fetched full text). Per the fetched summary of the model:

- **Abstract**: signals to the listener what kind of story is about to be told (e.g., "Once upon a time").
- **Orientation**: establishes who, where, when, and the pre-complication state of affairs, typically via habitual-action expressions.
- **Complication**: a problem culminating in crisis; a shift from temporal-sequence conjunctions ("and then") to counter-expectancy/simultaneity markers ("but... all of a sudden").
- **Evaluation**: establishes the narrative's point and significance, creating suspense between complication and resolution; Labov (1972) is quoted directly: "Evaluation devices say to us: this was terrifying, dangerous, weird, wild, crazy: or amusing, hilarious, wonderful; more generally, that it was strange, uncommon, or unusual — that is, worth reporting. It was not ordinary, plain, humdrum, everyday or run of the mill."
- **Resolution**: what finally happened.
- **Coda**: returns the narrative perspective to the present.

(All per the fetched Labov–Waletzky model document, [uniroma2.it](https://didattica.uniroma2.it/files/scarica/insegnamento/39508-Lingua-Inglese-3/5829-Labov-Narrative-Model).)

---

## 4. Life-Course and Life-Narrative Psychology

### 4.1 McAdams: narrative identity, redemption, and contamination sequences

Dan P. McAdams's narrative identity theory holds that identity is "a person's internalized and evolving life story, integrating the reconstructed past and imagined future to provide life with some degree of unity and purpose," and that narrators who find **redemptive meaning** in suffering and adversity, and who construct life stories featuring **agency** and **exploration**, tend to show higher mental health, well-being, and psychological maturity (McAdams & McLean, "Narrative Identity," *Current Directions in Psychological Science*, published online June 4, 2013, abstract fetched at [SAGE Journals](https://journals.sagepub.com/doi/10.1177/0963721413475622)).

Narrative-identity research codes personal narratives along **seven core constructs** (plus a newly recognized eighth), per the detailed Wikipedia synthesis of this literature (fetched full text, [Wikipedia, Narrative identity](https://en.wikipedia.org/wiki/Narrative_identity)):

- **Redemption**: transition from a bad/negative state to a good/positive state (A → B), subtyped as *sacrifice* (enduring negative A for benefit B), *recovery* (regaining a lost positive state), *growth* (bettering the self), or *learning* (gaining new skill/knowledge/wisdom).
- **Contamination**: transition from good/positive to bad/negative (B → A), often marked by denial or inability to recall the prior "good" state; common sub-themes include victimization, betrayal, loss, failure, illness/injury, disappointment, disillusionment.
- **Agency**: the narrator's autonomy/power to affect their own life, subdivided into *self-mastery*, *status/victory*, *achievement/responsibility*, and *empowerment*.
- **Communion**: motivation toward intimacy/relationship — love/friendship, reciprocal dialogue, caring/help, unity/togetherness.
- **Exploratory narrative processing**: degree of self-exploration in the telling; high scores associated with maturity development.
- **Coherent positive resolution**: extent to which narrative tensions dissolve into positive resolution.
- **Meaning-making**: extraction of a lesson or insight from the narrated event.
- **Performance** (newly recognized construct in some coding schemes).

(All construct definitions per [Wikipedia, Narrative identity](https://en.wikipedia.org/wiki/Narrative_identity), fetched full text, which cites McAdams's "Redemptive Self" formulation, *Research in Human Development* 3(2–3):81–100, 2006.)

The same source distinguishes four types of **structural coherence** that narratives can exhibit as they develop from childhood to adulthood: **temporal coherence** (chronological ordering), **causal coherence** (cause-effect linkage between events and self), **thematic coherence** (reflective evaluation revealing overarching themes/meaning), and **the cultural concept of biography** (conformity to culturally standard biographical form) (Wikipedia, Narrative identity, fetched full text). The article notes a U-shaped relationship: some coherence is necessary for comprehensibility, but excessive coherence can make a narrative feel implausibly "too-neatly" resolved (Wikipedia, Narrative identity).

McAdams (2006) additionally identifies **six "languages of redemption"** used in American life narratives — **atonement, emancipation, upward mobility, recovery, enlightenment, and development** — as analyzed in Sagi & Jones, "Cognition and Emotion in Narratives of Redemption" (Cognitive Science Society proceedings, 2018; full text fetched, workspace batch7.json[0]).

McAdams & McLean's exact 2013 abstract (fetched directly from SAGE) confirms the "reconstructed past and imagined future" framing and identifies two dominant research foci in the field: (a) narrative identity's relationship to **psychological adaptation** and (b) its **development** across childhood, adolescence, and emerging adulthood ([McAdams & McLean, "Narrative Identity," *Current Directions in Psychological Science* 22(3), 2013, SAGE abstract fetched](https://journals.sagepub.com/doi/10.1177/0963721413475622)).

### 4.2 Holmes & Rahe 1967: Social Readjustment Rating Scale

Thomas Holmes and Richard Rahe's 1967 *Journal of Psychosomatic Research* paper introduced the **Social Readjustment Rating Scale (SRRS)**, assigning **Life Change Units (LCU)** to 43 life events based on their associated psychological stress ([Wikipedia, Holmes and Rahe stress scale](https://en.wikipedia.org/wiki/Holmes_and_Rahe_stress_scale), fetched full text with complete list; original citation confirmed via [J Psychosom Res 1967 citation page](https://www.sciencedirect.com/)).

**Top 15 events by Life Change Units (exact, as fetched):**

| Rank | Life event | LCU |
|---|---|---|
| 1 | Death of spouse | 100 |
| 2 | Divorce | 73 |
| 3 | Marital separation | 65 |
| 4 | Imprisonment | 63 |
| 5 | Death of close family member | 63 |
| 6 | Personal injury or illness | 53 |
| 7 | Marriage | 50 |
| 8 | Dismissal from work | 47 |
| 9 | Marital reconciliation | 45 |
| 10 | Retirement | 45 |
| 11 | Change in health of family member | 44 |
| 12 | Pregnancy | 40 |
| 13 | Sexual difficulties | 39 |
| 14 | Gain a new family member | 39 |
| 15 | Business readjustment | 39 |

(Full 43-item list, including non-adult/adolescent supplementary items, available at [Wikipedia, Holmes and Rahe stress scale](https://en.wikipedia.org/wiki/Holmes_and_Rahe_stress_scale), fetched full text.) A later methodological paper, "The social readjustment rating scale: updated and modernised" (PMC), revisits and critiques the original scale's continued applicability (fetched full text, workspace batch4.json[7], not yet deeply excerpted — see Unverified section for depth caveats).

### 4.3 Elder's life-course theory (1994/1998)

Glen H. Elder Jr.'s life-course theory is most reliably characterized, per a secondary source that directly cites and applies Elder's framework, as resting on (at least) three "cardinal principles of life course analysis": **Agency**, **Linked Lives**, and **Time and Place**, explicitly attributed to "Elder, 1994, 1998" and "Elder, Johnson and Crosnoe, 2003" (Mortimer, "Agency, Linked Lives, and Historical Time: Evidence from the Longitudinal Three Generation Youth Development Study," *Longitudinal and Life Course Studies* 13(2), 2021, PMCID PMC9350070, fetched full text, [PMC](https://www.ncbi.nlm.nih.gov/pmc/)). Per this source: **Agency** develops most often within the context of **linked lives** — especially family — where children model parents' agentic orientations and parents attempt to instill agentic traits in offspring; the principle of agency itself was originally developed by Elder from a comparison of the Berkeley and Oakland cohorts, born less than a decade apart (Mortimer 2021, fetched full text, citing Elder and Rockwell). **Time and Place** captures the idea that the same objective life transition (e.g., job loss, parenthood) can have different psychological and biographical consequences depending on the historical period and social context in which it occurs (Mortimer 2021, paraphrased from the abstract and introduction).

### 4.4 Habermas & Bluck (2000), "Getting a Life"

Tilmann Habermas and Susan Bluck's 2000 paper, "Getting a Life: The Emergence of the Life Story in Adolescence" (*Psychological Bulletin*), is confirmed to exist and to concern the developmental emergence of coherent autobiographical life-narrative capacity during adolescence, per its PubMed abstract record (fetched, thin content — abstract-level only, workspace batch5.json[3]). The dossier could not fetch the full text or extract the paper's specific proposed coherence-type taxonomy beyond what is already captured under the "four types of coherence" framework cited in Section 4.1 (temporal, causal, thematic, cultural-biography) — that four-part coherence taxonomy is commonly attributed in the broader literature to Habermas & Bluck's framework as adopted and extended by later narrative-identity researchers, but this specific attribution could not be independently confirmed from primary-source full text in this research pass. **Flagged as partially unverified — see Section 6.**

### 4.5 Computational modeling of life stories

Limited primary-source depth was obtained specifically on computational/algorithmic modeling of life stories as a distinct sub-literature (as opposed to the interactive-narrative story-sifting literature in Section 1, which does computationally model simulated character histories). The clearest computational through-line found is the story-sifting literature itself (Section 1) applying narratological/life-narrative pattern recognition to simulated agent histories — e.g., Talk of the Town's modeling of biographical event chronicles per character, and Caves of Qud's generation of "mythic biographies" (Section 2). No additional dedicated "computational life-story modeling" literature distinct from these was verified with primary sources in this pass — see Unverified section.

---

## 5. Story Evaluation Methodology

### 5.1 Human ratings vs. baselines in story-sifting evaluation

The story-sifting literature consistently favors **small-N expert or lay user studies with Likert-scale agreement ratings** over large-scale automated metrics:

- **Loose Ends** (Section 1.4): 5 expert evaluators, 1–5 Likert agreement scale across 7 quantitative questions (Usability, Effortlessness, Control, Fun, Ownership, Curiosity, Direction), supplemented by qualitative think-aloud and interview data (Loose Ends full paper text).
- **Arc Sift** (Section 1.10): 20 non-technical adult participants, two task types — (1) free-hand drawing a story arc to match a given story summary, scored by matching inflection-point count/direction against the target query arc; (2) multiple-choice selection of the story summary matching a presented arc — plus a 1–5 Likert **confidence** rating per task. Reported outcome: 65% of participants reported high confidence (median rating 4 of 5) across both tasks; per-shape accuracy was reported separately for RagsToRiches, RichesToRags, ManInHole, Icarus, Cinderella, and Oedipus shapes (exact per-shape percentages shown only in a figure in the original paper, not extractable as text) (Arc Sift, AAMAS 2022 full text).

This pattern — small expert panels for interface/authoring-tool papers (Loose Ends), larger lay-participant panels for perceptual/recognition claims (Arc Sift) — reflects a broader ICIDS/AIIDE norm of favoring **direct human judgment of "does this feel like a story"** over automated precision/recall against a gold-standard corpus, because (per Felt and Winnow's framing of the sifting problem) there is no uncontested ground-truth corpus of "which raw simulation events constitute a story" to measure precision/recall against in the first place (Felt and Winnow papers, full text, Sections 1.2–1.3 above).

### 5.2 Precision/recall framing

Precision/recall framing appears in the story-sifting literature primarily as a **design goal implicit in pattern specificity**, rather than as a formally reported metric with numerical precision/recall scores. Winnow's benchmark study (Section 1.3) instead reports **wall-clock latency** as its primary quantitative outcome, treating correctness of matches as guaranteed by construction (a Winnow acceptor either matches a pattern or does not, deterministically) rather than something requiring statistical precision/recall evaluation (Winnow full paper text). This suggests that for a deterministic, rules-based sifting engine (as opposed to a probabilistic or LLM-based one), the "evaluation problem" shifts away from precision/recall of pattern matching (which is exact by construction) and toward (a) runtime performance and (b) whether matched patterns are subjectively perceived by human readers as good stories — exactly the axis Loose Ends and Arc Sift measure.

### 5.3 Krippendorff's alpha / Cohen's kappa thresholds

For inter-rater reliability (relevant if the target system's designer wants to validate that human raters agree a given sifted event sequence "reads as a story"), the standard reference thresholds are: **Krippendorff's alpha ≥ 0.80** is considered "satisfactory" for drawing conclusions, **0.67–0.79** is "tentative" (conclusions should be considered tentative/exploratory), and **below 0.67** is "poor"/should be discarded ([k-alpha.org, Krippendorff's Alpha methodological notes](https://www.k-alpha.org/), fetched full text). However, a 2021 ACL paper by Wong, Paritosh & Aroyo, "Cross-Replication Reliability — An Empirical Approach to Interpreting Inter-Rater Reliability," explicitly **critiques the common practice of treating fixed thresholds (e.g., the Landis & Koch 0.6 "substantial agreement" cutoff) as universally applicable**, arguing that acceptable reliability is task- and context-dependent, and proposing a **cross-replication reliability (xRR) framework** that measures whether independent replications of a rating task converge, rather than relying on a single fixed numeric cutoff ([Wong, Paritosh & Aroyo, ACL 2021, full text fetched](https://aclanthology.org/)). For a solo-developer story-sifting validation exercise (as opposed to a published HCI study), this suggests that a fixed kappa/alpha threshold is less important than checking whether **repeated independent human judgments of "is this a story"** converge reasonably well on the same sifted event sequences — consistent with the small-N think-aloud-plus-Likert methodology already used across the Felt/Winnow/Loose Ends/Arc Sift line of work (Sections 1.2–1.4, 1.10, 5.1).

### 5.4 ICIDS / AIIDE evaluation norms, synthesized

Across the fetched ICIDS/AIIDE-published papers in this literature (Felt ICIDS 2019, Winnow AIIDE 2021, Loose Ends AIIDE 2022, Why Are We Like This? FDG 2020, Toward Narrative Instruments ICIDS 2021, Arc Sift AAMAS 2022), the consistent evaluation pattern is:

1. **Small-N qualitative-plus-quantitative playtesting** (typically 5–20 participants) rather than large-scale crowdsourced evaluation.
2. **Likert-scale self-report** on usability, fun, ownership/authorship, and narrative-direction dimensions, often re-using or adapting prior papers' exact question wording (e.g., Loose Ends explicitly reuses Q1–Q5 wording from the Germinate evaluation instrument, and Q6–Q8 from issues raised in *Why Are We Like This?* playtesting) — enabling rough cross-paper comparability within this specific research lineage even without a shared numeric benchmark corpus.
3. **Think-aloud protocols and semi-structured interviews** to surface qualitative failure modes (e.g., "directionlessness") that inform the next system's design goals — a deliberate iterative design-research loop rather than a one-shot benchmark.
4. **Runtime/latency benchmarking** treated as a separate, purely engineering-oriented evaluation axis (Winnow), decoupled from the subjective "does this feel like a story" evaluation axis.

(Synthesized from full texts of Felt, Winnow, Loose Ends, Why Are We Like This?, Toward Narrative Instruments, and Arc Sift, as cited throughout Section 1 and here.)

---

## 6. Claims Attempted But Not Fully Verified (UNVERIFIED)

The following claims were investigated but could not be confirmed to the dossier's evidentiary standard (primary-source full text, or at minimum a corroborating secondary source with exact wording). They are flagged so the taxonomy work downstream does not silently rely on them without independent confirmation:

- **Tobias's complete 20-plot list.** Only plots 1–11 (Quest, Adventure, Pursuit, Rescue, Escape, Revenge, The Riddle, Rivalry, Underdog, Temptation, Metamorphosis) were confirmed from directly fetched full text ([ChangingMinds.org](http://changingminds.org/disciplines/storytelling/plots/tobias_plots.htm)). Plots 12–20 (commonly cited elsewhere as Transformation, Maturation, Love, Forbidden Love, Sacrifice, Discovery, Wretched Excess, Ascension, Descension) are attested only at title/snippet level via Writer's Digest and other secondary sources whose full text could not be successfully fetched in this research pass ([Writer's Digest, "20 Master Plots"](https://www.writersdigest.com/improve-my-writing/20-master-plots) — fetch failed).
- **Polti's full 36 situations.** The fetched Wikipedia list captured approximately 32 of the 36 named situations before the retrieved content was truncated; situations beyond roughly #32 ("Mistaken jealousy") were not independently confirmed with exact wording in this pass.
- **Habermas & Bluck (2000) exact coherence-type taxonomy.** Only the abstract-level PubMed record was retrieved; the specific mapping between Habermas & Bluck's original proposed criteria and the "four types of coherence" (temporal, causal, thematic, cultural concept of biography) as commonly attributed to them in later literature could not be confirmed against Habermas & Bluck's own primary full text — this attribution rests on the Wikipedia "Narrative identity" synthesis rather than a direct read of the 2000 paper.
- **Elder's exact original 1994/1998 wording of "linked lives" and "turning points."** The dossier confirms Elder's principles (Agency, Linked Lives, Time and Place) and their 1994/1998/2003 citation dates via a secondary source (Mortimer 2021) that directly cites and applies Elder's framework, but Elder's own original 1994 (*Social Psychology Quarterly*, "Time, Human Agency, and Social Change: Perspectives on the Life Course") and 1998 (*Child Development*, "The Life Course as Developmental Theory") papers were not independently fetched in full text — only an abstract-level stub was retrieved for one Elder paper.
- **"Social readjustment rating scale: updated and modernised" (PMC) — specific modernized LCU values.** This paper was fetched in full length (129,183 characters) but not yet deeply excerpted for its specific proposed updates to the original Holmes & Rahe values; the dossier reports only the original 1967 scale with confidence.
- **Dwarf Fortress Legends Mode — Tarn Adams primary-source interview on design intent.** Multiple interview sources were located (Stanford DHS "An Interview with Tarn Adams," a Taylor & Francis book chapter "Emergent Narrative in Dwarf Fortress" by Tarn Adams) but the Stanford interview fetch failed and the Taylor & Francis chapter was not fetched (paywalled academic book chapter); the dossier's Dwarf Fortress characterization relies on the secondary citation of its arc shape in Kreminski & Mateas's "Toward Narrative Instruments," not on a primary Adams interview.
- **Exact per-shape accuracy percentages in the Arc Sift user study.** The paper reports these results in a bar chart (Figure 2) rather than in extractable body text; the dossier reports only the aggregate confidence-score finding (65% high confidence, median 4/5) with certainty, not the six individual per-shape percentages.
- **Computational modeling of life stories as an independent research thread.** No dedicated primary-source literature distinct from the interactive-narrative story-sifting papers already cited in Section 1 was confirmed to exist under this specific heading; this may indicate the sub-literature is thinner than assumed, or that the relevant work is filed under different keywords not captured by this research pass's queries.

---

## Summary of Sources by Section

This dossier draws on primary academic papers (Felt, Winnow, Loose Ends, Why Are We Like This?, Toward Narrative Instruments, Arc Sift, Reagan et al. 2016, Caves of Qud mythic biographies, Talk of the Town/Bad News analysis papers), Ryan's dissertation, Wikipedia syntheses of narratological and psychological literatures (used where they directly quote or closely paraphrase primary sources, e.g., Propp, ATU, Motif-Index, Booker, Polti, Holmes-Rahe, Narrative Identity), game-industry and community documentation (RimWorld Wiki, Wildermyth Wiki, GamingOnLinux reporting on CK3 patch notes), and methodological references for evaluation practice (k-alpha.org, ACL 2021 cross-replication paper). All URLs are inline above at first citation of each source.
