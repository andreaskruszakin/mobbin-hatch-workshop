# Dry runs

## 6 September, 10:00–10:05: the simplified setup, re-run

Trigger: Nicolas cloned the repo on a fresh laptop on 4 September and the first thing the
README asked him for was Python. Nothing in the kit needs it. This run re-tests the loop as a
participant would meet it after the setup rewrite: folder open, Mobbin connected via the shipped
`.cursor/mcp.json`, `START-HERE.md`'s one prompt, baseline B.

### What was measured

| Step | Wall clock | Note |
| --- | --- | --- |
| Fresh clone, both MCP configs parse, three baselines open by double-click | under a minute | No Python, Node or git needed for the zip path |
| Ten pre-verified Mobbin URLs in `prompts/02-ground.md` | all `200` | Offline fallback is intact |
| Warm-up query, `standard`, limit 3 | 10:00:01 → 10:00:19 | **No timeout this time.** First call succeeded. Do not count on that in a room of 28 |
| Three grounding searches, `deep`, limit 4, run in parallel | 10:00:34 → 10:01:18 | Reading the twelve images included |
| Generate `variants/mine-1/index.html` | 10:01:18 → 10:02:43 | 85 seconds for the model |
| Data check plus headless render | ~2 min | Script under `/tmp`, not in the repo |
| **Whole loop, model time** | **under 5 minutes** | Human deciding time is on top, as before |

### The data check

13 of 13 `data-region` names preserved. 15 of 15 amounts, 3 IBANs, 9 dates and all 9 raw
transaction labels present in the output. One new number appeared: a `19 145,31` Savings
subtotal the model derived from two balances. Expect that. Group subtotals are the one kind
of invented number a grouped layout produces, and they are not a disqualification; a changed or
missing baseline number is.

### The gap test, finally run

Same baseline, Nicolas's "just make it better" prompt, twice.

**Without Mobbin, no structure in the prompt.** The model restyled the same DOM: Inter, cards
with rounded corners, more whitespace, a blue tab bar. It **passed the data check completely**:
13 regions, every number, every label. It also kept all three `<table>` elements. Same
four-column accounts table, same debit/credit split, same one-row upcoming table. It looks
enormously better than the baseline and changed nothing about what the user can find out.

**With Mobbin, no structure in the prompt.** A broad query (`modern online banking dashboard`)
returned YNAB, Mercury, Monarch and Wise. That is the average of the library, and a model
handed those four images without being told which region to swap produces a Mercury-flavoured
reskin. Mobbin on its own does not fix the prompt.

**With Mobbin and the one prompt from `START-HERE.md`.** Three swaps, one search each, zero
`<table>` elements left in the output, and the structure moved: accounts grouped under a net
figure (Quicken, Monarch), transactions grouped by day with the merchant first and the raw label
underneath (Wise, Copilot Money), the upcoming payment on a fourteen-day strip with the due date
marked (Origin, Klarna).

So the claim holds, with a sharper edge than we had written down: **the data check cannot
catch the beautiful reskin.** It passes it. What catches it is the second question ("could two
companies have made these?") and one cheap tell to say out loud in the room: *count the tables.*
Baseline B has three. If your redesign still has three, you changed the paint.

### Smaller things

- Headless screenshots caught the variant's 300ms entrance animation mid-flight and the page
  looked half-rendered. Irrelevant to participants, relevant to anyone verifying outputs by
  screenshot: give the page a second first.
- `standard` mode returned one irrelevant screen in three on the warm-up (a credit-usage panel
  from an unrelated app). `deep` returned twelve relevant screens out of twelve. The advice
  stands: `standard` to warm up, `deep` for the searches that matter.
- The prompt asks the model to stop after each step. In a tool that runs steps autonomously
  that is the only moment a participant gets to reject a swap before it is built. Keep it.

---

## 15 August, 20:38–20:50: the first run

I ran the exercise end to end before asking thirty people to. What follows is what actually
happened, including the parts that didn't work.

**Headline: the method works and produces genuinely different outputs. The scope does not
fit 22 minutes.** Six dimensions has to come down to three.

> **Status: superseded in part, kept in full.** This was run against an invented
> account-opening baseline ("Meridian") and a six-dimension matrix, both since retired in
> favour of Nicolas's three Crédit Mutuel screens and the component swap in
> `docs/SWAP-CARD.md`. The scope finding below is what drove that change. The MCP timings,
> failure modes and query-phrasing notes were measured against the live Mobbin MCP and still
> hold — they are the reason this file stays in the repo. The Meridian screens themselves are
> gone, so the links to them have been removed rather than left dangling.

---

## What was measured

| Step | Measured | Note |
| --- | --- | --- |
| Build the baseline | ~4 min | One-off. Participants get it pre-made. |
| Six Mobbin searches, sourcing all dimensions | 20:39:17 → 20:40:47 (**90s**) | Run two at a time, `standard` mode |
| One `deep` mode search | **20s** | Measured start to finish |
| Write the matrix from the results | ~3 min | Mostly reading images and judging |
| Generate three full variants | 20:44 → 20:46:34 (**~2.5 min**) | ~50s each |
| Verify all three render and their JS runs | ~3 min | Headless Chrome |

**These are machine timings, not human timings.** I did not have to read the screens and
decide — deciding is the slow part, and it is the part with the value in it. My honest
estimate for a competent participant working alone:

| Step | Realistic human time |
| --- | --- |
| Decompose the baseline into dimensions | 4–6 min |
| Ground **six** dimensions in Mobbin | 8–12 min |
| Generate variant 1 | 3–4 min |
| Generate variant 2 and compare | 4–5 min |
| **Total** | **19–27 min** |

Against a 22-minute hands-on block that is a coin flip, and it assumes nothing goes wrong.
Something always goes wrong.

---

## The cut

**Ground three dimensions, not six.** Progress model, input density, post-submit state.

Those three are enough to force structurally different output — they are the ones that
change what the user does and in what order. Trust, validation and commitment ramp are
genuinely interesting but they can be varied without changing the shape of the product,
which means a participant can spend eight minutes on them and still produce a reskin.

Revised, and this fits with room to spare:

| | |
| --- | --- |
| Decompose | 4 min (facilitated together, not alone — see below) |
| Ground three dimensions | 6 min |
| Generate variant 1 | 4 min |
| Change two dimensions, generate variant 2 | 5 min |
| Slack | 3 min |

**Decompose together, on the projector.** It is the step most likely to go sideways alone,
it is the step where the method actually gets taught, and doing it as a room takes four
minutes instead of six and produces a shared vocabulary for the rest of the session.

*How this was resolved.* The four-minute decompose became zero minutes. Nicolas's baselines
carry `data-region` tags, so the decomposition ships with the artefact and participants read
it instead of deriving it. `docs/SWAP-CARD.md` lists the regions per screen with seeded
alternatives, which is the takeaway that `docs/MATRIX.md` used to be.

---

## Failure modes hit, in order

**1. The first MCP call timed out.** Not slow — timed out with a connection error. The retry
worked and every call after that was fine. This is a cold start, and it will happen to
roughly thirty people at once if we let them connect in the room.

*Mitigation:* `prompts/00-setup.md` has a warm-up query, and it goes in the registration
email, not just the workshop page. Say it out loud at the start too: "if your first search
times out, run it again, that's expected."

**2. `search_screens` returns almost no metadata.** Just `app_name`, `platform`,
`mobbin_url` and the image. There is no structured pattern data to read. Everything useful
is *in the picture*, which means the model has to actually look, and a model that skims will
confidently describe a screen it hasn't examined.

*Mitigation:* the grounding prompt explicitly instructs it to describe what it sees and
forbids inferring from the app name. Worth saying from the front — it is the single most
common way this exercise produces confident nonsense.

**3. `search_flows` returns stills, not motion.** This answers Nicolas's question directly.
An 18-screen Mercury flow came back as screens 1, 5, 10, 14 and 18 — evenly spaced previews.
You get the *shape* of a journey, never the animation. There is no motion anywhere in the
MCP. To see every step you open the flow URL in a browser.

*Mitigation:* don't promise animation exploration. If someone wants motion, send them to
mobbin.com in the browser.

**4. `deep` is the default mode and costs 20 seconds a call.** It is genuinely better — the
deep query returned [Bonsai](https://mobbin.com/screens/0f7dd0bb-9527-4261-9246-d1d59cb7b23c),
[Wave](https://mobbin.com/screens/72e925c7-164f-48f6-9343-e66c8fa99e8b) and
[Jobber](https://mobbin.com/screens/7f4968b2-e7c5-49e5-a525-cc799eda40bd), all three dead on
target, better than `standard` managed. But at six searches that is two minutes of staring.

*Mitigation:* tell the room to use `standard` while exploring and `deep` for the one search
that matters most. This is a real tradeoff, not a bug.

**5. Both browser MCPs failed** while I was verifying the variants (`No active page`).
Irrelevant to participants, but it is why the screenshots came from headless Chrome. Noting
it because if we demo anything through a browser MCP on the day, it needs testing on the
actual machine first.

---

## Did it actually work?

Yes, and this is the part I was least sure of. Three combinations, same brief, same baseline:

| Variant | Combination | What it became |
| --- | --- | --- |
| A — Gauntlet | `1B · 2C · 3C · 4F · 5B · 6B` | Eligibility gate first, one question per screen, top progress bar, ends in a status timeline |
| B — Dossier | `1C · 2E · 3D · 4E · 5D · 6F` | Login first, persistent 1/5 sidebar, whole sections per page, the wait turned into setup work |
| C — Conversation | `1F · 2F · 3B · 4B · 5E · 6D` | Four card questions, a customer voice alongside, ends in a recommendation with three exits |

They do not read as the same product in different clothes. A is a form that respects your
time, B is a serious application you'll return to across two sittings, C barely reads as a
form at all and ends without opening anything. Different information architecture, different
number of steps, different DOM. That is the proof the matrix is doing the work rather than
the model's defaults.

**Caveat, stated plainly:** I wrote the baseline, so I already knew its dimensions when I
decomposed it. Step 01 is therefore the one step in this kit that has not been genuinely
tested cold. It is also why I want it facilitated from the front rather than left to
twenty-two solo attempts.

That caveat is now spent rather than answered. Nicolas wrote the current baselines and named
the regions inside them, so step 01 no longer asks anyone to derive a decomposition under
time pressure — it asks them to read one. What still needs a cold test is the swap itself:
whether a participant picks the regions carrying information rather than the ones carrying
pixels. That is the timed run on baseline B still open on Nicolas's list.

---

## Smaller things worth knowing on the day

- Query phrasing matters more than anything else. "A subject, the elements on it, and their
  relationship" works. Keyword lists and adjectives return mush. There are five queries in
  `prompts/02-ground.md` that were verified to work — hand them out.
- `limit: 4` is the sweet spot. Higher floods context and the model starts skimming images,
  which triggers failure mode 2.
- Mercury is the strongest reference in the library for this exact brief. Expect several
  people to find it and converge. Worth pre-empting from the front: "if you all copy
  Mercury, you have proven my point about the average of everything."
- Plain HTML was the right call. No install, no build, opens from the file system, and every
  AI tool writes it natively. Nothing in the dry run needed a framework.
