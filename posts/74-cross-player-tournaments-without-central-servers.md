# Cross-player tournaments without central servers: Bitcoin, HD keys, and public-blockchain proof-of-achievement as the aggregation surface

**Author:** Jimmy McColery
**Date:** 2026-06-09
**Status:** Architectural synthesis from operator-directed scan 2026-06-09; n=1 synthesis case with existing infrastructure unified; concrete pattern with public-domain primitives; generalizes to any cross-player verification domain

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I have been working on a personal indie game project for a while. One of the late-stage design questions I had been putting off was how to handle cross-player tournaments. The game is single-player at its core, but the design has a federation layer that aggregates player achievements across the entire player base and runs periodic tournaments featuring the best performers from across the field. The federation is the kind of feature that conventionally requires a central server, an account system, a player database, a leaderboard infrastructure, and an analytics pipeline. None of those felt right for an indie project I want to ship without operational dependencies I cannot afford to maintain in perpetuity.

The breakthrough came on 2026-06-09 morning when I caught myself for the third time in twelve hours assuming I needed to build new infrastructure that I had already built. The previous assumptions were about closure-window mechanics and single-alley tournament hosting; in both cases the operator-side discipline of scanning the canonical record before designing new systems surfaced the infrastructure already living in the project. The third catch was about cross-player aggregation: I had been treating the federation as a problem that needed central servers because that is how the genre solves it, and I had not noticed that the project already contains the primitives for solving it without central servers.

This post is about the architecture. The primitives are old (Bitcoin, HD keys, OpenTimestamps, public-blockchain anchoring). The synthesis is what was missing from my own thinking until I caught the assumption.

## The aggregation problem

Cross-player tournaments need three things: a way to verify that an individual player has achieved something specific, a way to aggregate the verifications across the player base, and a way to run a tournament against the aggregated set without compromising the privacy of the players whose achievements are aggregated.

The conventional solution treats this as a database problem. The vendor runs a server. Each player has an account that links to a profile that holds their identity and their achievements. The server aggregates achievements across accounts. The tournament selection draws from the aggregated set. Privacy is handled by access controls on the database.

The conventional solution has three costs that matter for an indie project. The first is operational: the server has to run forever, the database has to be backed up, the account system has to be maintained, and the entire infrastructure has to be replaced if the vendor moves to a different cloud provider. The second is compliance: account systems trigger privacy regulations, app-tracking-transparency requirements, and disclosure obligations that scale poorly with operator bandwidth. The third is durability: the player's achievements live in the vendor's database, so the achievements only exist as long as the vendor exists.

Each of these costs is acceptable for a large studio with operational scale. Each is hostile for an indie project with finite operational capacity and a desire to ship something that outlasts the vendor running it.

## The primitives that solve this without central servers

Three primitives, all of them public-domain, all of them established for years. Combining them solves the cross-player aggregation problem without any of the three costs.

The first primitive is HD keys. A hierarchical deterministic key is a public-private key pair derived from a seed, where the public key can be shared without exposing the private key. The player generates an HD key on their device. The public key identifies the player to the federation without exposing any other information about the player. The private key signs the player's achievement claims. No account system is needed because the public key serves as the player's identity within the federation. No central server holds the key; the player holds the key.

The second primitive is OpenTimestamps. OpenTimestamps is an open protocol for committing arbitrary data to the Bitcoin blockchain by aggregating data into Merkle trees and anchoring the tree root in a Bitcoin transaction. The anchoring is cheap (free for the player; the protocol aggregates submissions before anchoring) and durable (the Bitcoin blockchain has been operating for over fifteen years and is not under any single party's control). Anchoring an achievement to the Bitcoin blockchain produces a tamper-evident proof that the achievement existed at a specific time, retrievable by anyone with the original data and the OpenTimestamps proof.

The third primitive is public-blockchain proof-of-achievement. The player's HD-key-signed achievement, anchored to the Bitcoin blockchain via OpenTimestamps, is a verifiable claim that anyone can check without going through the project's infrastructure. The verification reads the OpenTimestamps proof against the public Bitcoin chain and confirms the signature against the player's public key. No central server is involved in the verification. The verifier is whoever wants to verify; the data is whoever has the original achievement record; the chain is public.

## How the federation aggregates without aggregating

This is the part that initially looked impossible to me. The federation needs to aggregate achievements across players to run tournaments. Aggregation conventionally means a database. The primitives above do not give you a database.

What the primitives give you is something better for this use case: a public anchor for each player's achievement record. The federation does not need to aggregate the records into a database; the federation needs to read the anchors. Each player's achievements live in the player's own save data on the player's device. Each achievement is HD-key-signed and OpenTimestamps-anchored. The aggregation is the Bitcoin chain itself; each player's anchors live there, queryable by anyone with the player's public key.

The federation tournament selection process is then: for a tournament covering decade X, the federation NPC entity reads the public OpenTimestamps anchors for the achievement type that decade X requires, identifies players whose anchored records show qualifying performance, and selects the tournament field from that set. The selected players' anchored records are public; the federation can verify the records by reading the chain. The selected players themselves do not have to be online; the tournament can run as a single-player simulation against the verified anchored performance data of the selected players' records.

The tournament outcome is itself anchored: the simulated tournament produces a result; the result is HD-key-signed by the federation NPC (or by the player operating the tournament instance) and anchored via OpenTimestamps. The new anchor enters the public set and is available for future tournament selection.

The aggregation surface is the Bitcoin blockchain. No central server is needed because the chain is the aggregation. The aggregation is read-only (the federation reads anchors; the chain is public) and append-only (new anchors are added by the protocol; no one mutates existing anchors). The federation has no database to maintain because there is no database; there is a query interface against a chain that someone else maintains.

## The privacy properties

The architecture has three privacy properties that fall out of the primitives rather than being designed in.

Zero personally identifiable information is collected at any layer. The HD public key is pseudonymous; it does not link to any account, email address, or identifying information. The player can choose to publish their public key alongside their name if they want their achievements attributed to them; the player can also keep the public key fully pseudonymous and have the achievements aggregate without any external identifying tie. The federation does not need names; the federation needs verifiable performance data, and the HD-key signatures provide that without identity.

Zero central servers run player data. The player's save data lives on the player's device. The anchors live on the Bitcoin chain (which is not under the project's control). No vendor-maintained infrastructure holds any player data at any point. The vendor (me) does not have a player database to back up, restore, audit, or worry about losing.

Zero app-tracking-transparency compliance burden. The architecture does not track players across apps because the architecture does not track players at all. The federation reads public chain anchors; reading public data is not tracking under any framework I am aware of. The operator (me) does not have to navigate the app-store tracking-disclosure flow for this feature.

## The durability properties

The architecture also has three durability properties worth flagging.

The player's achievements outlast the vendor. If I stop maintaining the project tomorrow, the player's anchored achievements still exist on the Bitcoin chain. The player still has their HD private key on their device. The player can produce the original achievement record from their save data and verify it against the chain anchor. The achievements are durable past my involvement because the achievements live in infrastructure I do not control.

The federation outlasts the vendor. A community-maintained federation runner could read the same anchors after the vendor is gone. The federation is a function over the public anchor data; the function can be reimplemented by anyone with access to the public data. The federation is not a vendor lock-in because there is no vendor data to lock.

The cross-player surface outlasts any single client version. New clients can read old anchors. Old clients can read new anchors. The chain is the integration surface; clients have to agree on the achievement-record format, but the record format can be versioned and old versions remain readable. The infrastructure does not break when the client version changes.

## What the operator had been missing

The infrastructure pieces for this architecture had been in the project's canonical record for months. A cryptographic trophy infrastructure had been ratified earlier as a critical-path V1 feature. A single-alley tournament hosting system had been designed for an earlier phase. A trophy display surface had been designed for the trophy room. Each piece existed; the pieces had not been unified.

The reason the pieces had not been unified is the operator-side blind spot I have been describing across recent posts. I had been treating cross-player aggregation as a problem requiring new infrastructure, because the genre solves it that way. I had not scanned the canonical record for the infrastructure I had already built. The third scan-miss in twelve hours triggered the operator-directed scan that surfaced the existing pieces. Once the pieces were on the table, the synthesis was straightforward: anchor the trophies via OpenTimestamps, sign them via HD keys, run the tournament as a query against the anchors.

The synthesis was not a new architecture. The synthesis was a different way of seeing infrastructure I had already built. The reframe came from rejecting the genre's conventional assumption (central server required) and asking what the project's actual primitives can do.

## Why this generalizes beyond games

The architectural pattern is not gaming-specific. The structure is: HD keys for pseudonymous identity, OpenTimestamps for tamper-evident anchoring, public blockchain for aggregation, vendor-independent verification, no central server required. Any cross-party verification domain where the verifier and the verified want to operate without a central party can use the same primitives.

Domains where I would watch for fit: achievement leaderboards across distributed apps where users want their achievements to outlast any single app; credential verification systems where issuers want to issue verifiable credentials that recipients can present anywhere; reputation systems for distributed communities where the community wants reputation to survive any single hosting platform; review-and-rating systems where reviewers want their reviews to be portable across platforms; certification systems where the certified want their certification to be checkable by anyone.

In each of those, the central-server solution is the genre default and the public-blockchain-anchored solution is accessible if the central-server assumption is rejected. The blockchain solution does not solve every problem (it does not give you mutability, fast queries on private data, or real-time interaction), but for problems that fit the verify-public-claim-at-time-T shape, the solution is durable and operationally light.

## What this changed in my workflow

Two specific changes. First, when I face a feature that conventionally requires central server infrastructure, I now ask whether the feature can be reframed as a public-claim verification problem. If the answer is yes, the blockchain-anchored architecture is worth considering. If the answer is no (the feature genuinely requires mutable state, fast private queries, or real-time interaction), I commit to the central-server solution with full operational scope. The decision is upfront rather than drift toward central-server by default.

Second, I run the operator-directed scan against the canonical record before designing any new system. The scan is short; the question is "what infrastructure already exists in this project that could solve this problem if combined differently." The recent scan-miss reproductions taught me the scan is high-value because the operator-side blind spot consistently misses existing infrastructure. The scan costs minutes; the misses cost weeks of designing infrastructure that already existed.

## What I'm not claiming

- I'm not claiming the blockchain-anchored architecture is right for every cross-player feature. Real-time multiplayer, fast leaderboard updates, social-graph features, and features that require server-side moderation all need central infrastructure. The pattern fits the verify-public-claim-at-time-T shape; it does not fit features that need server-side anything-else.

- I'm not claiming the primitives are operator-easy. HD key management, OpenTimestamps integration, and Bitcoin chain queries all require careful implementation. The implementation is bounded and the primitives are well-documented, but the implementation work is real and not hand-waveable. I have not yet shipped the implementation; the architecture is ratified and the implementation is queued.

- I'm not claiming the privacy properties are stronger than they are. The architecture does not collect PII at the layers I have described. Players who choose to publish their public keys alongside identifying information move themselves into a different privacy regime. The architecture is pseudonymous by default and does not prevent the player from opting out of pseudonymity if they want their achievements attributed.

- I'm not claiming this finding is novel in cryptographic-protocol design. HD keys (BIP-32 from 2012), OpenTimestamps (2016), and public-blockchain proof-of-achievement are established primitives with substantial design literature. The contribution is the specific empirical synthesis (combining these primitives for cross-player tournament aggregation in a single-player game with a federation layer) and the demonstration that the central-server assumption is rejectable for this class of feature.

- I'm not claiming the cost-benefit calculation always favors the blockchain solution. The central-server solution is cheaper to implement initially and gives the operator more control over the feature evolution. The blockchain solution costs more upfront and constrains future feature evolution to what the public-claim-verification shape can express. The trade is favorable when the operational cost of running central infrastructure (and the durability concerns of vendor lock-in) outweighs the implementation cost of the blockchain primitives. The trade-off depends on the project's lifecycle horizon.

What I am claiming is that the central-server assumption is more contingent than the genre treats it. A specific class of cross-player verification features can be implemented with public-domain blockchain primitives in a way that eliminates central-server operational cost, eliminates PII collection at the architecture layer, and produces achievements that outlast the vendor. The implementation is real work; the architecture is durable; the trade is worth considering for indie projects with finite operational capacity and an interest in shipping features that survive the operator's involvement.

The operator-side blind spot that hid this architecture from me for months was the assumption that cross-player aggregation requires a central party. The architecture rejects that assumption. The Bitcoin blockchain is the central party in the sense that everyone reads from it; the Bitcoin blockchain is not the central party in the sense that no one controls it. The distinction is what makes this architecture possible.
