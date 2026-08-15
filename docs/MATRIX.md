# The Morphological Matrix — Account Opening

Morphological analysis: take one problem, break it into the **independent decisions**
it is actually made of, list the real options for each decision, then combine options
deliberately instead of defaulting to the first thing that comes to mind.

The point is not the grid. The point is that once a decision is on the grid, you can no
longer make it by accident.

Every option below was pulled from Mobbin during the dry run and links to the screen it
came from. Nothing here is invented — that is what makes it defendable when someone asks
"why this pattern?".

---

## How to use it in the session

1. Look at the baseline (`http://localhost:3160/baseline/`). Name the decisions it made.
2. For each dimension, pick a row that is **not** what the baseline did.
3. Write your combination down as a string: `1C · 2E · 3B · 4D · 5C · 6B`.
4. Hand that string plus the citations to your AI tool using `prompts/02-generate.md`.
5. Change **two** dimensions, regenerate, and compare. If the two outputs look the same,
   your prompt was too weak — the matrix wasn't actually driving the generation.

---

## Dimension 1 — Commitment ramp

*What do we ask for before the user has committed to anything?*

| | Option | Seen in |
| --- | --- | --- |
| 1A | Everything at once, no ramp — the full application is the first thing you see | the baseline |
| 1B | Disqualify first: an eligibility filter runs before any account exists | [Mercury, screen 5](https://mobbin.com/flows/5fcdc0f3-f4bd-4687-8303-a6129ce532cd) |
| 1C | Credentials first: create a login, then the application persists against it | [Mercury, screen 10](https://mobbin.com/flows/5fcdc0f3-f4bd-4687-8303-a6129ce532cd) |
| 1D | SSO as the primary path, email as the fallback | [Supabase](https://mobbin.com/screens/d0d7e649-54fd-4572-b20e-600a39a2373b), [Flodesk](https://mobbin.com/screens/deba3845-8ebb-44d6-a35a-79eed42038bd) |
| 1E | Email captured in the marketing hero, application deferred | [Mercury, screen 1](https://mobbin.com/flows/5fcdc0f3-f4bd-4687-8303-a6129ce532cd) |
| 1F | Lower the stakes explicitly — trial framing, no payment details | [HoneyBook](https://mobbin.com/screens/02dc3d79-c265-4452-b5d6-0af4bb5161bf), [Toggl Track](https://mobbin.com/screens/2ebe9471-f1ec-4430-8dce-d763b420d8f1) |

## Dimension 2 — Progress model

*How does the user know where they are and how much is left?*

| | Option | Seen in |
| --- | --- | --- |
| 2A | Nothing. The user discovers the length by scrolling | the baseline |
| 2B | Micro-label plus hairline bar — "Step 1 of 2", visually quiet | [HoneyBook](https://mobbin.com/screens/02dc3d79-c265-4452-b5d6-0af4bb5161bf) |
| 2C | Full-width bar with the current section named above it | [Zillow](https://mobbin.com/screens/94186d9f-ab6c-4b95-99ab-b4ab218a700c) |
| 2D | Named horizontal stepper, completed stages ticked | [Xero](https://mobbin.com/screens/42756079-865e-4c21-a50a-c86137011348) |
| 2E | Persistent sidebar checklist with `n / N` and every stage visible | [Mercury, screen 14](https://mobbin.com/flows/5fcdc0f3-f4bd-4687-8303-a6129ce532cd) |
| 2F | Count plus a preview of what's coming — "1 of 9 · Next: Your goals" | [Turo](https://mobbin.com/screens/d8edcc8e-5366-4f29-a9f3-75884562e1d8) |

## Dimension 3 — Input density

*How much are we asking for on one screen?*

| | Option | Seen in |
| --- | --- | --- |
| 3A | All ~25 fields on a single page, grouped by fieldset | the baseline |
| 3B | One question per screen, answered with large option cards | [Magnific](https://mobbin.com/screens/5f30270a-1678-4dae-8d4a-1b040688b26e), [Perplexity](https://mobbin.com/screens/a29d7d2c-897e-4876-a130-59935521d7bc) |
| 3C | One question per screen, plain single input, fixed Back/Next bar | [Zillow](https://mobbin.com/screens/94186d9f-ab6c-4b95-99ab-b4ab218a700c) |
| 3D | One coherent section per page, sections listed in a sidebar | [Mercury, screen 14](https://mobbin.com/flows/5fcdc0f3-f4bd-4687-8303-a6129ce532cd) |
| 3E | A grid of choices with a "pick N" constraint | [Bloom](https://mobbin.com/screens/c8920458-8f17-4322-9693-c6b94c688ede) |
| 3F | Stacked single-select list inside a card, dots for remaining questions | [Emergent](https://mobbin.com/screens/1380ff1b-e92b-4330-a2e0-f0bd1b5cc5e8) |

## Dimension 4 — Trust and credibility

*Why should someone hand over their passport and tax number?*

| | Option | Seen in |
| --- | --- | --- |
| 4A | A wall of regulatory boilerplate under the submit button | the baseline |
| 4B | A single customer quote sitting beside the form | [Supabase](https://mobbin.com/screens/d0d7e649-54fd-4572-b20e-600a39a2373b), [Toggl Track](https://mobbin.com/screens/2ebe9471-f1ec-4430-8dce-d763b420d8f1) |
| 4C | Scale metrics, investor badge and a live product preview | [Emergent](https://mobbin.com/screens/68cf5d5f-8483-4f72-bd12-448c4f75f4f5) |
| 4D | The regulatory truth pinned as a persistent bar, stated plainly | [Mercury, screen 1](https://mobbin.com/flows/5fcdc0f3-f4bd-4687-8303-a6129ce532cd) |
| 4E | Partner-bank and deposit protection explained *at the moment of signing* | [Mercury, screen 4](https://mobbin.com/flows/f46b27fd-c406-44ec-ab64-d2e0b7219966) |
| 4F | Anxiety-reducing microcopy attached to the ask itself | [Zillow](https://mobbin.com/screens/94186d9f-ab6c-4b95-99ab-b4ab218a700c) |

## Dimension 5 — Validation and error timing

*When does the user find out they got it wrong?*

| | Option | Seen in |
| --- | --- | --- |
| 5A | After submit, as a summary box at the top, far from the fields | the baseline |
| 5B | Inline under the field with a red border, on blur | [Customer.io](https://mobbin.com/screens/56a263fe-f5aa-496c-b757-b6f1bc9beda3), [Quicken](https://mobbin.com/screens/cde083f2-4dd9-4ff9-8d53-03d55589b020) |
| 5C | Inline with an icon and the specific rule that failed | [Instagram](https://mobbin.com/screens/9b4840c3-9d92-4a7e-b8aa-bd067a966cff) |
| 5D | A live checklist that ticks off as you type | [HoneyBook](https://mobbin.com/screens/02dc3d79-c265-4452-b5d6-0af4bb5161bf), [Emergent](https://mobbin.com/screens/68cf5d5f-8483-4f72-bd12-448c4f75f4f5) |
| 5E | Confirmed-good state, not just error state | [Emergent](https://mobbin.com/screens/68cf5d5f-8483-4f72-bd12-448c4f75f4f5) |

## Dimension 6 — Post-submit state

*The application takes 5–7 days. What does the user hold on to meanwhile?*

| | Option | Seen in |
| --- | --- | --- |
| 6A | A line of thank-you text and nothing else | [Airtable](https://mobbin.com/screens/194c0c3a-cf49-4045-88c2-c0473ab7262d) |
| 6B | A status timeline: Apply → In review → Ready, with dates and support contact | [Mercury, screen 6](https://mobbin.com/flows/f46b27fd-c406-44ec-ab64-d2e0b7219966) |
| 6C | Confirmation plus a numbered "what's next" list | [Zillow](https://mobbin.com/screens/40d14f6b-8626-44b4-ac5f-56132ceb38a9) |
| 6D | Explicit expectation setting plus adjacent next actions | [Mercor](https://mobbin.com/screens/97b22422-b0cb-4d53-b071-166a372b58ca) |
| 6E | Modal confirmation with a persistent status card left in context | [Dribbble](https://mobbin.com/screens/0f3fd32b-886b-46de-b58a-b32a0b7e629d) |
| 6F | Turn the wait into useful work — pre-approval setup tasks | [Mercury, screen 6](https://mobbin.com/flows/f46b27fd-c406-44ec-ab64-d2e0b7219966) |

---

## Bonus dimension — Document capture

Only relevant if you take the KYC step seriously. The baseline uses `<input type="file">`,
which is where most of the drop-off lives.

| | Option | Seen in |
| --- | --- | --- |
| 7A | A file input with a size limit and a list of accepted formats | the baseline |
| 7B | Framed capture with live lighting guidance | [MoonPay](https://mobbin.com/screens/a423d19c-abcf-4555-a1eb-734122c85675) |
| 7C | Instructional motion — "tilt the document back" | [Qonto](https://mobbin.com/screens/04c5ba06-9a74-43b5-b0c5-fdfdb44a81db) |
| 7D | Face oval with a preparation tip before the camera opens | [Yubo](https://mobbin.com/screens/a00976e0-d7b9-437a-999a-522fbd2ff65b) |
| 7E | Capture or upload, with an escape hatch for people without the document | [Cuvva](https://mobbin.com/screens/30133978-af17-4921-a553-8f77729efe4f) |

---

## The rows used in the three sample variants

| Variant | Combination | Character it produced |
| --- | --- | --- |
| A — Gauntlet | `1B · 2C · 3C · 4F · 5B · 6B` | Disqualify early, one question at a time, calm and linear |
| B — Dossier | `1C · 2E · 3D · 4E · 5D · 6F` | Serious, sectioned, everything visible, wait made productive |
| C — Conversation | `1F · 2F · 3B · 4B · 5E · 6D` | Low stakes, card-driven, barely reads as a form |

Same brief, same baseline, three genuinely different products. See `variants/`.
