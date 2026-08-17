# Nicolas — where the workshop stands

Updated after your baselines landed. Short version: your three screens are in, translated, and
the method got simpler because of them.

## What your baselines changed

The `data-region` tags are the thing. I had participants spending four to six minutes deriving
a decomposition from a screen, and it was the step the dry run flagged as most likely to go
sideways. Your files ship the decomposition inside the artefact, so that step is now reading
rather than deriving, and it takes two minutes on the projector.

That let me drop the six-dimension matrix entirely. The method is now one question per region:
**what component is this, and what else could it be?** Four-column accounts table becomes a
card stack, a list with sparklines, accounts grouped by purpose, or one net figure with
drill-down. One question, one Mobbin search, one swap, done three times.

It is still morphological analysis — decompose, enumerate, recombine — but the room never
needs the word. And it maps one-to-one onto how Mobbin search actually works, which the
abstract dimensions never did.

Your ten-line chart is preserved in `docs/NICOLAS-CHART.md` with the relevance map, credited,
as the longer form for anyone who wants it. It is the better instrument if you have half a
day. It does not fit fifty minutes — the dry run measured six dimensions at 19–27 minutes of
human work against a 22-minute block, and ten is worse.

## What I did to the files

- Moved them to `baselines/{a-homepage,b-accounts,c-transactions}/index.html`, one folder each
  so GitHub Pages serves them directly. Links are in the README.
- Translated the UI chrome to English and set `lang="en"`.
- **Kept the French product names** as proper nouns — Eurocompte Confort, Livret Bleu, Plan
  Épargne Logement, Forfait International, Caisse locale. Translating them turns a specific
  bank into a generic one.
- **Kept the raw transaction labels untouched.** `PRLV SEPA EDF CLIENTS PART 483992017 ECH
  220826` is the best artefact in the kit. It is exactly the machine output a good redesign has
  to deal with, and normalising it would hand participants the insight for free.
- Kept European number and date formats, every `data-region`, and your header data contracts
  verbatim.

Nothing else was touched — CSS, structure and the deliberate non-responsiveness of B and C are
all as you wrote them.

## The reveal is in, at 16–18

Your pick-your-baseline reveal replaced the four-zone room split I had planned. It does the
same job better: three different starting points make the show-and-tell contrast structural
instead of aesthetic, and it comes from the artefact rather than from a constraint we imposed.
Show-and-tell is now one volunteer per baseline.

Baseline B is the recommended default for anyone who cannot decide — your own relevance map
shows it is the only screen with ten live lines.

Your calibration rule is in the run of show as a line to say out loud, especially for baseline
A. "I've seen worse, not a straw man" is the sharpest thing in the handover.

## Your animation question, answered

The MCP does not do motion. `search_flows` returns evenly-spaced stills — an 18-screen Mercury
flow came back as screens 1, 5, 10, 14 and 18. Good for reading the shape of a journey, useless
for animation. We should not promise motion exploration in the description, and if someone asks
on the day the honest answer is "open the flow on mobbin.com".

## Finance+

There is no dedicated space. The add-on just unlocks finance apps inside normal search — search
Bank of America and it appears instead of being gated. We both went looking for a separate
section and neither of us found one. Worth telling Mobbin that two ambassadors could not find
the thing they had been given.

## The branding call

I kept Crédit Mutuel. The README now carries a disclaimer: educational reconstruction,
fictional data, no affiliation, no endorsement. The repo is public so you and anyone else can
click straight through to the screens, which is exactly why the disclaimer needed to be
written down rather than assumed.

If you would rather switch to a fictional name before the pre-workshop email goes out, the
wordmark is text in three files and it is one find-and-replace. Say the word.

## What I need from you

- Mobbin guest accounts — 30, ideally with Finance+ since the brief leans on finance apps
- A promo code for the takeaway page
- Confirmation the slot really is 50 minutes, and that the room has a projector

I will chase Cursor for participant credits on my side.

## Still open, yours and mine

From your list:

- Reconcile B and C against real Espace client captures.
- Zip the three files for the pre-workshop email.
- Timed dry run on baseline B, target one full loop under seven minutes.
- **The gap test** — same baseline, same prompt, once with the Mobbin URLs and once without.
  This is the one that decides whether the workshop's core claim holds. Worth doing before the
  slides are finished rather than after.
- The Mobbin intro slides.

From mine:

- Whether the room machine can run the live demo. Both browser tools failed on mine, so I would
  rather test on the actual machine than find out live.
- Prerequisites on the registration page before it goes live. The MCP is slow on first connect
  and thirty simultaneous cold starts would cost us five minutes we do not have.
