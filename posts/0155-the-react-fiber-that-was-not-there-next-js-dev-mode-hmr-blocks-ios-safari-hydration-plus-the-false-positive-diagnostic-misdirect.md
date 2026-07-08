<!-- CC-OPTIMIZED-SUMMARY v2.0
post_id: 0155
title: React Fiber That Was Not There Next.js Dev-Mode HMR Blocks iOS Safari Hydration Plus False-Positive Diagnostic Misdirect
date_published: 2026-07-04
status: published
superseded_by: none
domain: technical debugging Next.js Turbopack dev-mode HMR versus iOS Safari WebKit hydration surface
project_scopes: framework-methodology, sim-ai, roomtolife
cc_task_relevance: react-hydration-debugging, nextjs-dev-hmr, ios-safari-webkit, false-positive-diagnostic
phase_binding: era-independent
discipline_family: cross-device debugging discipline
canonical_rule: Next.js dev-mode Turbopack HMR blocks iOS Safari WebKit hydration; false-positive diagnostic can misdirect toward unrelated framework fault
load_bearing_claims:
  - Next.js Turbopack dev-mode HMR blocks iOS Safari WebKit hydration when accessed via same-WiFi local dev server
  - False-positive diagnostic can misdirect toward unrelated framework fault
  - Broadly reproducible for React developers testing cross-device on same-WiFi local dev server
applicability_triggers:
  - Cross-device debugging via same-WiFi local dev server
  - iOS Safari hydration fails but macOS Safari and Chrome DevTools mobile mode succeed
  - React Fiber not rendered on iOS Safari but SSR HTML delivered
mechanism_details:
  - Next.js Turbopack dev-mode HMR uses websocket for hot module reload
  - iOS Safari blocks websocket in some cases on same-WiFi with self-signed cert
  - Diagnostic misdirect toward framework code when actual issue is dev-mode tooling
  - Mitigation next start with production build for iOS device testing
cross_refs:
  - Post 0153 (Tier A empirical close with Path A operationalized after resolving this gotcha)
  - Post 0154 (Path A as fifth path Post 0152 enumeration gap fire)
CC-OPTIMIZED-SUMMARY -->

# The React Fiber That Was Not There: Next.js Dev-Mode HMR Blocks iOS Safari Hydration Plus the False-Positive Diagnostic Misdirect

**Author:** Jimmy McColery
**Date:** 2026-07-04
**Status:** Single-finding arc; technical debugging story; n=1 empirical fire at Next.js Turbopack dev-mode HMR versus iOS Safari WebKit hydration surface; broadly reproducible for React developers testing cross-device on same-WiFi local dev server

*Note: I'm a tech professional documenting my work in personal AI-assisted projects. I produce these posts directly from my own work and findings, with AI writing assistance helping to shape the prose. The implementation, the diagnosis, and the analysis are mine; AI assistance shaped the prose from my raw session notes and canonical record.*

---

I lost about forty-five minutes today debugging what looked like a React measurement harness that ran to completion on iPhone Safari but never displayed results. CPU activity showed in Web Inspector Timelines. Layout and Rendering rows were dense with continuous activity. The button tapped without any visible freeze. But no results table appeared on the page and no POST request from the harness reached my server. Something was clearly running. Something was clearly not.

The diagnosis turned out to be that React had never hydrated the client component on the iPhone. The page loaded as static server-rendered HTML with zero interactivity. The onClick handler was never bound to the DOM node. What I was seeing in the timeline was iPhone Safari executing initial page-load JavaScript plus retrying failed Next.js HMR WebSocket connections, not the harness itself. The measurement code never ran.

This post is about the diagnostic chain that surfaced the hydration failure, the false-positive that misled me initially, and the specific Next.js dev-mode behavior that caused the failure. The technical fix is small. The diagnostic discipline is the point.

## The setup

I had a measurement harness at a Next.js page route (`/sim-ai-test/scale-run`) that I needed to run on my iPhone 17 to close a Council-methodology-ratified target-hardware measurement condition. The harness is a React client component (marked with the `'use client'` directive at the top). It calls a synchronous JavaScript function that runs a population-scale simulation harness at multiple tier configurations, then displays results in a table.

The path I chose was to run the Next.js dev server on my Mac, expose it on the local WiFi network at the Mac's IP address, and navigate iPhone Safari to that IP directly at the same-WiFi network scope. Mac Safari Web Inspector attached to the iPhone via cable for diagnostic Console visibility.

The harness worked on Mac Safari in 664 milliseconds. Same harness on iPhone Safari, tapped the Run measurement button, waited ten seconds. Nothing on the page changed.

## The false-positive

My first instinct was that the harness was running but the page was not repainting the results table. Web Inspector Timelines showed continuous CPU activity plus dense Layout and Rendering activity for roughly ten seconds. I read that as "the harness is running." Which meant my instinct was that something in the setState-plus-render pipeline had failed to fire.

I added console.log statements at every state transition in the harness code plus a POST to a new API endpoint so I could capture results server-side even if the DOM render failed. Refreshed the iPhone. Tapped Run measurement. Nothing on the page changed. Nothing in the server logs either.

The console.log statements would have surfaced any of the state transitions plus the POST fetch call would have hit my server. Neither happened. Which meant the harness code was not running at all. Which meant the button click was not triggering the handler. Which meant the pattern I was seeing in the timeline was not what I thought it was.

The false-positive was the mental model that CPU activity plus rendering activity in the timeline meant the harness was executing. The timeline showed real work but the work was not the harness. It was probably initial hydration attempts plus the Next.js dev-mode HMR WebSocket retry loop, both of which do produce CPU activity plus rendering, both of which are unrelated to the button click handler.

The lesson from the false-positive is that CPU activity plus DOM rendering are not sufficient evidence that a specific handler has fired. They are evidence that the browser is doing work of some kind. Verifying which specific work requires looking at the specific handler's specific side effects.

## The diagnostic that broke through

I had been assuming the button click was reaching the handler. That assumption was wrong. To test it I paused the mental model and ran a definitive test. In the Web Inspector Console I typed a manual `console.log('MANUAL TEST from Console at ' + new Date().toISOString())` plus pressed Enter. The output appeared in Console immediately. Which meant Console filters plus display were working. Which meant if my instrumentation logs were not showing it was because the instrumentation code was not running.

I ran a second test to isolate the button-click path. In the Console:

```javascript
const btn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('Run measurement'));
console.log('button found:', btn ? 'YES' : 'NO');
console.log('button disabled?', btn?.disabled);
console.log('React fiber attached?', Object.keys(btn ?? {}).some(k => k.startsWith('__reactFiber')));
btn?.click();
```

The output made the diagnosis definitive:

- Button found: YES (the DOM element existed)
- Button disabled: false (no obvious blocker)
- React fiber attached: false (the smoking gun)
- Programmatic click: fired no handler (confirmed by no subsequent instrumentation logs)

React tracks its component tree via internal Fiber node references attached to DOM nodes as properties with the prefix `__reactFiber$`. On a hydrated React app these properties exist on every DOM element that React manages. When they are absent, React has not attached itself to that node. Which means client-side hydration failed silently. Which means no event handlers are bound. Which means clicking the button does nothing regardless of how you click it.

The observation that checkboxes on the page toggled when tapped had misled me earlier. Native HTML checkbox inputs toggle their `checked` attribute on click via browser default behavior with no JavaScript required. The visible toggling was HTML native behavior, not React handling the click. It had looked like React was working. It was not.

## Why hydration failed

Next.js in dev mode uses Turbopack for module bundling plus Hot Module Reload for live code updates. HMR opens a WebSocket connection from the client back to the dev server so code changes propagate to the running page without a full reload. When the client-server connection succeeds, HMR works. When it fails, HMR retries plus logs the WebSocket error.

The specific WebSocket error I had been ignoring was:

```
WebSocket connection to 'ws://10.0.0.91:3000/_next/webpack-hmr?id=...' failed: cannot parse response
```

The connection was failing because HMR expects same-origin plus specific handshake behavior that does not consistently work when the client is at a different device on the local WiFi network reaching the Mac dev server. Cross-device HMR is not a supported configuration in dev mode.

My mental model had been that the HMR error was noise unrelated to the actual page. Which turned out to be wrong. Somewhere in the Next.js dev-mode hydration flow the HMR connection failure was blocking client-side hydration in a way that let the SSR HTML render but prevented React from attaching event handlers. I have not traced the specific Next.js internal code path that produces this behavior. What I can confirm empirically is that switching from dev-mode to production build resolved the problem.

## The fix

`npm run build` produces a production Next.js bundle with no HMR dependency plus no WebSocket connection back to the dev server. `npm start -H 0.0.0.0 -p 3000` serves the production bundle on all network interfaces so cross-device WiFi access works.

Total time to switch from dev to production: about ninety seconds. Refreshed the iPhone Safari page. Ran the diagnostic again in Console:

- Button found: YES
- Button disabled: false
- React fiber attached: TRUE
- Programmatic click: fired the handler, instrumentation logs cascaded through Console, POST reached my server

Overall measurement duration on iPhone 17: 526 milliseconds. Instrumentation logs showed the full state-transition chain from runMeasurement START through runMeasurement DONE through POST OK. Server-side capture logged the per-tier results table. Path A closed at 66 times headroom at N equals 5000.

## The diagnostic discipline

The lesson generalizes to any React or Next.js app being tested cross-device. The specific failure mode is Next.js dev-mode HMR versus cross-device WiFi. The generalizable discipline is that CPU activity plus DOM rendering are not sufficient evidence that a specific handler has fired. Verify the handler side effect explicitly.

For React specifically, the load-bearing hydration check is whether a Fiber reference is attached to the DOM element that the handler is bound to. The check is one line in the Console:

```javascript
Object.keys(someElement).some(k => k.startsWith('__reactFiber'))
```

If it returns false on the device where the handler is not firing plus true on a device where the handler works, the diagnosis is hydration failure. The check does not tell you why hydration failed. But it separates hydration failure from all the other possible causes: button-selector wrong, disabled state set incorrectly, event.preventDefault interfering, useState closure capturing stale state, and so on.

The false-positive mental model I had been in was that CPU activity meant the harness was running. The observable evidence that broke that model was: manual console.log worked (so Console displays my instrumentation), instrumentation logs did not appear (so instrumentation code did not run), React fiber attached returned false (so React did not hydrate). Three independent observations converging on hydration failure specifically.

If I had checked the Fiber attachment first, the false-positive misdirect would not have happened. The instrumentation additions plus the API endpoint plus the auto-run URL parameter I built in the middle of the debugging were not wasted work (they are useful for future device testing) but they were not what solved the problem. What solved the problem was one line of Console code that answered a yes-or-no question.

## What actually shipped

The diagnostic chain resolved the hydration failure in favor of production-build deployment. The Next.js dev-mode HMR-versus-iOS-Safari failure is a known Next.js internal behavior that I have documented in the project's operational memory for future reference.

The instrumentation additions ship at the measurement harness code: console.log statements at every state transition, a POST fetch call to a server-side result-capture API endpoint, plus an auto-run URL parameter that fires the measurement on page load. These additions ship regardless of whether they were the specific fix. They make future device testing self-diagnosing.

The measurement pass on iPhone 17 completed successfully. The population-scale harness FRAMEWORK_FAILURE_BUDGETS ratified at real target hardware at 66 times headroom at N equals 5000. The iPad Mini cross-device measurement completed successfully at 33 times headroom at N equals 5000. Both devices sustained deterministic replay at 5000-tick horizons.

## What I'm not claiming

I'm not claiming the Next.js HMR-versus-iOS-Safari cross-device hydration failure is a bug in Next.js. Dev-mode HMR is designed for same-origin single-device workflows. Cross-device WiFi access is outside the supported use case. The behavior I observed is consistent with HMR failing gracefully by not attempting to hydrate rather than by throwing an error. Whether Next.js should handle this specific case better is a legitimate question. Whether it currently is a bug is not what this post is claiming.

I'm not claiming the React Fiber attachment check is a new diagnostic. React developers have used the `__reactFiber$` property inspection for years. What I'm claiming is that the check is the load-bearing hydration verification specifically, and it should be run early in cross-device debugging rather than after chasing false-positives on CPU-activity-plus-rendering evidence.

I'm not claiming CPU activity in Web Inspector Timelines is worthless as a diagnostic signal. CPU activity plus rendering do tell you the browser is doing work. What they do not tell you is which specific handler is producing the work. The failure mode I hit was mistaking "the browser is doing work" for "my specific handler is running." Those are different claims and confusing them costs debugging time.

I'm not claiming the specific fix (switch to production build) is the only way to resolve the hydration failure. Setting up an HTTPS reverse proxy at the Mac dev server might let HMR work cross-device. Configuring Next.js to disable HMR while keeping dev-mode plus other features might work. Adding a service worker that intercepts the HMR connection might work. What I chose was the fastest path back to working measurement plus documenting the failure for future reference. Whether other paths would resolve the same underlying problem is not what this post is claiming.

I'm not claiming this failure mode applies to production Next.js apps. Production builds bypass HMR entirely. The failure surface I documented is specific to dev-mode cross-device WiFi testing. Production apps deployed to a hosted domain plus accessed from a real device do not hit this specific failure surface. What I'm documenting is a specific pattern in a specific workflow (Next.js dev mode plus cross-device WiFi plus iOS Safari) that produces a specific false-positive misdirect during debugging.

## What I am claiming

CPU activity plus DOM rendering in Web Inspector Timelines are not sufficient evidence that a specific event handler has fired. Verifying which specific handler is running requires checking that handler's specific side effects, not inferring from browser-level work activity.

For React applications specifically, hydration failure produces a false-positive misdirect where SSR HTML renders correctly plus native HTML controls (checkboxes, form inputs) behave normally via browser defaults, but React-managed event handlers never fire. The load-bearing hydration check is whether a React Fiber reference is attached to the DOM element. That check is one Console line. Running it early in cross-device debugging catches hydration failure before instrumentation additions plus fix attempts on the wrong root cause.

Next.js dev-mode HMR versus cross-device WiFi produces this specific hydration failure at the observed reproduction pattern of Mac dev server plus iPhone or iPad WiFi client. The empirical fix is switching to production build. The specific Next.js internal code path that produces the failure is not documented here. What is documented is the reproducible empirical pattern plus the diagnostic sequence that surfaces it plus the fix that resolves it. Future framework testing on iOS devices via same-WiFi network deployment should default to production build rather than dev mode.
