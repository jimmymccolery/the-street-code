# Path A Cross-Device Browser Testing Methodology Guide v1

**Established:** 2026-07-04
**Empirical foundation:** Phase D Tier A empirical close arc executed at real iPhone 17 + iPad Mini via Path A (mobile Safari on same-WiFi local dev server pattern) per Posts 0152 + 0153 + 0154 + 0155
**Scope:** Reusable procedural guide for future cross-device browser testing sessions covering React/Next.js measurement harnesses at iOS Safari + iPadOS Safari runtime
**Companion posts:** Post 0154 (path enumeration completeness), Post 0155 (Next.js dev-mode HMR blocks iOS Safari hydration + diagnostic discipline)

---

## What Path A is

Path A is a cross-device browser testing pattern where the operator's Mac runs a local dev server exposed on the WiFi network at the Mac's IP address, and iOS devices (iPhone + iPad) on the same WiFi navigate to the Mac's IP via mobile Safari. Real device WebKit + JavaScriptCore + hardware CPU + hardware memory get exercised; measurement runs on the device with results captured either on-device or POSTed back to the Mac's server.

Path A does not use Capacitor or Xcode. Path A does not require an Apple Developer account. Path A does not require a cloud device farm subscription. Path A does not require a shipping-app build. What Path A requires is a Mac + a dev server + iOS devices on the same WiFi.

## What Path A closes and does not close

**What Path A closes:**
- Real iOS Safari WebKit rendering engine
- Real iOS JavaScriptCore JIT tier-up behavior + GC pause distribution + heap allocation patterns
- Real iPhone or iPad hardware CPU + memory + GPU envelope
- Cross-device generational coverage when multiple iOS devices are available
- Short-duration measurement scope (single-session testing)

**What Path A does not close:**
- Capacitor JS-to-native IPC bridge overhead (WKWebView vs Safari differ)
- iOS memory pressure + WKWebView killer thresholds (Safari and Capacitor WKWebView have different memory watermarks)
- Thermal throttling under sustained load (requires extended-duration testing)
- App lifecycle concerns (backgrounding + termination signals)

For framework foundational-readiness ratification at target hardware envelope Path A is sufficient. For iOS ship-prep ratification the remaining concerns close as part of actual Capacitor build workflow.

## Prerequisites

**On Mac (one-time setup):**
- Safari Preferences → Advanced → Show Develop menu in menu bar
- Node.js + Next.js project with production build capability (`npm run build && npm start`)
- Network connection with WiFi access

**On each iOS device (one-time setup):**
- Settings → Safari → Advanced → Web Inspector = ON

**Every test session:**
- Mac + iOS device(s) connected to same WiFi network
- Mac's local IP address noted via `ifconfig` (usually 10.0.0.X or 192.168.X.X)

## Deployment sequence

### Step 1: Production build the Next.js app

```bash
cd /path/to/next-app
npm run build
```

**Critical:** Use production build, not dev mode. Next.js dev-mode HMR WebSocket connection fails cross-device on WiFi networks and blocks React client-component hydration on iOS Safari. Symptoms: page loads but React fiber never attaches to DOM; button click fires no handler. Native HTML controls (checkboxes, form inputs) still work via browser default behavior which misleads diagnosis. Production build bypasses HMR entirely.

### Step 2: Start server on all network interfaces

```bash
npm start -H 0.0.0.0 -p 3000
```

The `-H 0.0.0.0` binds to all interfaces. Without it Next.js binds to localhost only, unreachable from other devices.

### Step 3: Note Mac IP address

```bash
ifconfig | grep "inet " | grep -v "127.0.0.1"
```

Look for the entry on the WiFi interface (usually not the first one). Expected format like `inet 10.0.0.91 netmask ...`.

### Step 4: Navigate iOS Safari to Mac IP

On iOS device Safari, navigate to `http://<mac-ip>:3000/<route>`. Example: `http://10.0.0.91:3000/sim-ai-test/scale-run`.

No HTTPS. No trailing slash unless the route has one. Case sensitive on the path.

### Step 5: Verify page loads on iOS device

Confirm expected page renders. If page does not load, check:
- Mac firewall not blocking port 3000
- Both devices on same WiFi (not one on WiFi, other on cellular)
- Mac IP typed correctly

### Step 6 (optional): Attach Web Inspector for diagnostics

If deeper profiling required or if button click does not appear to trigger handler:

1. Connect iOS device to Mac via cable (Lightning or USB-C)
2. On iOS device tap "Trust This Computer" if prompted; enter passcode
3. On Mac Safari: Develop menu → your iOS device name → the loaded page entry
4. Web Inspector opens on Mac attached to iOS Safari

### Step 7: Verify React hydration if using React app

If the app is React or Next.js and the button click does not appear to trigger the handler, run the fiber-attachment check first. In Web Inspector Console on Mac:

```javascript
const btn = Array.from(document.querySelectorAll('button')).find(b => b.textContent.includes('Your Button Text'));
console.log('React fiber attached?', Object.keys(btn ?? {}).some(k => k.startsWith('__reactFiber')));
```

If output is `false`: React did not hydrate. Return to Step 1 and verify production build was used. If output is `true`: React hydrated; problem is elsewhere in the handler or its dependencies.

### Step 8: Run measurement + capture results

Two patterns for result capture:

**Pattern A: On-device DOM rendering.** Results table renders on the iOS device screen. Screenshot the table for record.

**Pattern B: Server-side POST capture.** The measurement code POSTs results to a server-side endpoint on the Mac. Server writes results to a JSONL log file. Advantage: results captured even if DOM render fails; also allows headless / hands-free workflows.

Recommended: implement both patterns for redundancy. Pattern A gives operator immediate feedback. Pattern B gives durable record.

## Instrumentation additions for Path A resilience

The following instrumentation additions to your measurement UI component make Path A self-diagnosing:

### Console.log at every state transition

```typescript
const log = (msg: string, extra?: unknown) => {
  console.log(`[YourComponent] ${msg}`, extra ?? '');
};
log('runMeasurement START', { config });
// ... work
log('runMeasurement DONE');
```

Web Inspector Console on Mac shows every log line from the iOS device. Where the log lines stop = the exact point of failure.

### Server-side POST endpoint

Next.js app router API endpoint example:

```typescript
// app/api/results/route.ts
export async function POST(request: Request) {
  const body = await request.json();
  console.log('[Results captured]', JSON.stringify(body, null, 2));
  await appendFile('results.jsonl', JSON.stringify(body) + '\n', 'utf-8');
  return NextResponse.json({ ok: true });
}
```

Client-side fetch:

```typescript
await fetch('/api/results', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ /* results */ }),
});
```

### Auto-run via URL parameter

For hands-free workflows when tap-based UI is blocked or unavailable:

```typescript
useEffect(() => {
  if (typeof window === 'undefined') return;
  const params = new URLSearchParams(window.location.search);
  if (params.get('autorun') === '1' && status === 'idle') {
    const t = setTimeout(() => runMeasurement(), 500);
    return () => clearTimeout(t);
  }
}, [status, runMeasurement]);
```

Navigate to `http://mac-ip:3000/route?autorun=1` and measurement fires on page load.

### Prominent error display

Rather than a single-line error paragraph, use a bordered error box with pre-formatted error stack trace:

```tsx
{error && (
  <div style={{ background: '#ffe8e8', border: '2px solid #cc0000', padding: 16 }}>
    <p style={{ fontWeight: 600, color: '#cc0000' }}>Error:</p>
    <pre style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>{error}</pre>
  </div>
)}
```

Ensures errors are visible on iOS Safari where scrolling might miss a small paragraph.

## Diagnostic discipline

**CPU activity plus DOM rendering are not sufficient evidence a specific handler has fired.** Verify the specific handler side effect explicitly. Web Inspector Timelines may show CPU + rendering activity that is unrelated to your handler (initial hydration, HMR retries, page-load work).

**React fiber attachment is the load-bearing hydration verification.** For React apps if the handler is not firing, the first check is Fiber attachment. One Console line answers the diagnosis before you invest in instrumentation additions on the wrong root cause.

**Native HTML control behavior is misleading.** HTML checkboxes toggle their `checked` attribute on click without any JavaScript. Form inputs, radio buttons, and select dropdowns behave similarly. Visible interaction on these controls does not prove React is running.

**Console must show manual `console.log` output before instrumentation logs.** If a manual `console.log('test')` typed in Web Inspector Console does not appear, the Console display itself is broken (wrong context, filter set, or Console cleared setting). Fix Console visibility before debugging harness.

## When to escalate from Path A to Path B

Path B (full Capacitor + Xcode iOS build) is required when:

- Testing Capacitor plugin behavior (camera, filesystem, sensors, native storage)
- Testing app lifecycle events (backgrounding, foregrounding, termination)
- Testing WKWebView memory watermarks under sustained load
- Testing thermal throttling under extended-duration workloads
- Testing production-signed distribution builds

Estimated Path B setup cost from empty state: approximately 4-6 hours. Includes Xcode install + Apple Developer account signup + Capacitor dependencies + iOS platform add + build + code signing + device installation.

Path A does not require any of these prerequisites. Path A is the correct default for framework-foundational-readiness testing. Escalate to Path B when Capacitor-specific concerns become load-bearing for the specific test being run.

## Empirical foundation

Path A operationalized at Phase D Tier A empirical close arc 2026-07-04:

- Device 1: iPhone 17 (A19 Pro chip, iOS 18.7, Safari 26.6)
- Device 2: iPad Mini (iOS 18.7, Safari 26.5)
- Test: framework population-scale harness at N=50/500/1000/5000 with 200 ticks + 5000-tick deterministic replay validation
- Results captured via both on-device DOM rendering + server-side POST JSONL log
- Total operator-active time: approximately 45 minutes execution + 20 minutes diagnostic + 20 minutes write-up

Cost: zero dollars. Zero infrastructure setup beyond existing Mac + iOS devices + WiFi. Zero cloud services.

## Cross-references

- Post 0152 Phase D empirical scaling closes at Node tier plus Safari Tier B route plus device farm Tier A prep
- Post 0153 Tier A Empirical Close Real iPhone 17 Plus iPad Mini Ratify Framework Failure Budgets Against Target Hardware
- Post 0154 The Path the Plan Did Not Enumerate: Post 0152 Tier A Four-Path Enumeration Plus Path A as the Fifth
- Post 0155 The React Fiber That Was Not There: Next.js Dev-Mode HMR Blocks iOS Safari Hydration Plus the False-Positive Diagnostic Misdirect
- Population-scaling-foundation-pass methodology guide v1
- Framework operational discipline rules canonical file

## Notes for future revisions

This guide is v1.0, established after Phase D Tier A close arc single execution. Revise when:

- Second-fire Path A execution reveals additional prerequisites or gotchas
- Next.js version bump changes HMR behavior (may or may not resolve the cross-device hydration failure)
- iOS Safari version bump changes WebKit or JavaScriptCore runtime characteristics
- Capacitor version bump changes IPC bridge overhead making Path A remaining-10% gap smaller or larger
- New instrumentation pattern proves useful across multiple sessions

Don't add new procedure steps until observed working across multiple sessions. Premature additions produce steps that don't generalize.
