# Why a PKCE Magic Link Needs a Click-to-Confirm Interstitial

**Author:** Jimmy McColery
**Date:** 2026-05-24
**Status:** Single auth feature implemented in a personal build; concrete failure mode and concrete fix; pattern generalizes to any single-use-token email auth flow.

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

## What I was building

RoomToLife (user-facing name: "My 90s Bedroom") is a personal cozy-room project I'm building toward a December 2026 V1 ship. It's a browser-based space where you arrange a 1990s bedroom and let it evolve over time. The user-accounts layer for it is a passwordless magic-link auth flow on top of Supabase, with PKCE (RFC 7636) layered onto Supabase's email-OTP code-exchange for the round-trip from the email link back to a server session.

The user types an email, clicks the magic link that arrives, and lands signed in. Standard pattern in 2026. I had it working end-to-end on desktop browsers within a day.

It broke on iOS.

Same email, same link, same Supabase project. On iOS Mail, the magic link would land on the callback page and immediately show an error: "code already exchanged" or "invalid grant" depending on the exact path through the code. Tap the link again and it would fail the same way. Tap a fresh link and it would also fail. The auth flow on iOS was effectively unusable.

This post is about why that happened, why it took a few wrong-direction commits to find, and the interstitial pattern that fixes it. The fix is small. The failure mode is one I had to discover the hard way; I'm writing it up because I'd rather have read this post than re-derived it.

## The failure mode

PKCE single-use codes are exactly that: single use. The auth provider issues a code in the magic link's URL. The callback page exchanges that code for a session via a server-side call to `exchangeCodeForSession`. The exchange succeeds exactly once; subsequent attempts with the same code fail.

Email environments often fetch URLs before the user does. Consumer iOS Mail does this via the LinkPresentation framework for link-preview rendering. Corporate inboxes do it via gateway scanners: Microsoft Defender's Safe Links rewrites every URL and visits it for malware scanning; Outlook for Microsoft 365 does similar checking; Google Workspace pre-warms some links. The exact trigger varies, but the effect is the same: a normal GET request fires against your URL, with all query parameters intact, before the user ever taps.

If your callback page exchanges the PKCE code on GET, that pre-fetch consumes the code. By the time the user taps the link, the code is spent. The user sees an error. The auth provider, the callback handler, and the user-facing UI all behave correctly given their inputs; the silent pre-fetch is the missing input.

iOS Mail is the most common trigger I hit, but it isn't the only one. Any environment where something other than the user-tap may fetch the URL will produce the same failure mode.

## Why it took five commits

The interstitial fix is the last commit in a five-commit arc that I'd describe as "iterating on the wrong layer before finding the right layer." Listing them honestly, in order:

1. Initial setup. Supabase client, `/login` magic-link form, `/auth/callback` PKCE code-exchange route, all wired with the Server Action pattern.

2. A hash-fragment-style callback page using `onAuthStateChange` + `getSession` probing + a timeout safety net. This was the wrong direction. Supabase's `@supabase/ssr` package defaults to PKCE flow, which delivers the code via a query parameter (`?code=...`), not a hash fragment. The hash-fragment approach is from the older implicit-flow pattern. I'd absorbed the wrong template from somewhere.

3. A lint suppression. `react-hooks/set-state-in-effect` was firing on the hash-fragment parse, and the lazy-initializer alternative regressed in App Router SSR. I documented the suppression rather than fix the underlying lint, because the underlying code was about to be deleted anyway. (This was the wrong-direction tax.)

4. Replace the hash-fragment callback page with a PKCE route handler. The route handler reads `?code=...` from the query parameter, calls `exchangeCodeForSession` server-side, and redirects to the dashboard on success. Correct flow type, correct API, server-side exchange. Email pre-fetchers cheerfully consumed every single code.

5. Replace the route handler with a page that renders an interstitial form. The page reads the code from the query parameter into a hidden input, shows a "Sign in" button, and only calls `exchangeCodeForSession` when the user submits the form. This is the actual fix.

The arc is honest about the structure of the work. Commits 2 and 3 were necessary because I'd absorbed the wrong template and had to walk back. Commit 4 was necessary to get on the right flow type. Commit 5 was the actual fix for the actual bug. If I'd known about the pre-fetch problem at commit 1, I'd have skipped 2, 3, and 4. I didn't.

## The interstitial pattern

The fix is structurally simple. Instead of:

```
GET /auth/callback?code=ABC
  → server-side exchangeCodeForSession(ABC)
  → redirect to dashboard
```

It becomes:

```
GET /auth/callback?code=ABC
  → render a page with a hidden input value="ABC" and a "Sign in" submit button
  → no token exchange happens on GET

POST /auth/callback (from the form submission)
  → server-side exchangeCodeForSession(ABC)
  → redirect to dashboard
```

The pre-fetcher gets the GET response. The GET response is a static HTML form. No code is exchanged. The user, when they actually tap the link, sees the form, taps "Sign in", and the POST exchanges the code.

This works because GET requests are supposed to be safe and idempotent. Token exchange is neither of those things; it's a one-shot mutation. Putting it behind a POST is just respecting what HTTP already told us about the difference between GET and POST. The interstitial isn't a workaround; it's the correct HTTP semantics. The original GET-side exchange was always wrong, and email pre-fetching is what surfaced the wrongness.

Concrete cost: one extra tap for the user. The interstitial page I shipped says "Almost there" and renders a single button labeled "Sign in". On mobile the extra tap takes about half a second. I haven't seen anyone treat this as friction; it reads like a normal flow.

Concrete benefit: the failure mode is gone. Email pre-fetching no longer consumes codes. The auth flow works the same on desktop and mobile. The implementation is simpler because the GET handler is a static-rendering page, not an exchange-and-redirect side-effecting handler.

## What generalizes

Any single-use-token auth flow delivered via email needs an interstitial in any environment where URLs may be fetched by something other than the user. The specific list of triggers is broader than I initially thought:

- PKCE magic links (the case here)
- Email verification links that mutate state on first click
- Password-reset links that consume a one-time token on landing
- Email confirmation links that flip an `is_verified` flag on GET
- Any URL where the GET handler does something the user expected to do themselves

The general rule: if a GET request to your URL changes server state in a way the user can't redo, your URL has confused HTTP semantics, and email pre-fetchers will expose it. The fix is always the same: render a form on GET, do the mutation on POST.

The pattern isn't novel. The GET-vs-POST semantics underlying the fix are well-established in web-security guidance; OWASP's various cheat sheets discuss the principle, and the specific PKCE-plus-email-pre-fetcher failure has been raised in Supabase community threads. What I think I'm contributing here is the framing: this is one of those problems where the abstract advice ("don't mutate state on GET") sounds obviously correct but doesn't land until you've shipped the broken version and watched the failure mode in your own logs. The post-hoc legibility of the failure is high; the prospective recognition is low. Posting the concrete encounter so that someone else recognizes the symptom faster is the value-add.

## What I'm not claiming

- I'm not claiming the interstitial pattern is novel. It's well-established. The principle (don't mutate on GET) is older than PKCE; this is just a specific instance of it surfacing in a specific failure mode.
- I'm not claiming iOS Mail pre-fetching is the only trigger. It's the most common one I hit; the failure class is broader, and corporate gateway scanners produce the same effect.
- I'm not claiming my five-commit arc was the optimal path. A more disciplined session would have surveyed the standard PKCE-with-Supabase patterns before committing to the hash-fragment direction. I didn't, and the wrong-direction commits are the cost.
- I'm not claiming the extra tap is invisible. It's visible. I'd argue it's small enough not to matter, but that's a UX judgment, not a measurement.
- I'm not claiming the interstitial removes all email-auth failure modes. It removes this one. Network-side scanners that follow form actions, or attackers who replay POST requests, are different problems with different mitigations.

## What I am claiming

If you're shipping a PKCE magic-link flow and your callback handler exchanges the code on GET, email pre-fetchers will silently consume your users' tokens before they ever click. The fix is a static interstitial form that defers the exchange to the user's POST. The change is small, the user-facing cost is small, the implementation is simpler than the broken version, and the bug it removes is the kind that wastes half a day to diagnose if you don't know about it.

I didn't know about it. Now I do. If this post saves anyone half a day, it's done its job.
