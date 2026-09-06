# Run of show — 50 minutes

**Hatch Berlin · Friday 18 September 2026**

Presentation is capped at 15 minutes (30%). Everything after that is hands or voices in the
room. Timings below come out of `docs/DRY-RUN.md`, not out of optimism.

| Time | Block | Lead |
| --- | --- | --- |
| 0–5 | The slop problem | Andreas |
| 5–9 | Mobbin, and the MCP live | Nicolas |
| 9–13 | Read the regions, together | Andreas |
| 13–16 | The assignment | Andreas |
| 16–18 | The reveal — pick your screen | Nicolas |
| 18–38 | Hands on, individually | both floating |
| 38–45 | Show and contrast | Nicolas chairs |
| 45–48 | What just happened | Andreas |
| 48–50 | Takeaway page, codes, feedback | Nicolas |

---

## 0–5 · The slop problem

Open cold, with the demo rather than the claim. Same brief, twice, into the same tool. Two
outputs, both fine, both the average of everything it has seen. That is the problem — not
speed, not quality, **reference**. AI has no taste and no memory of what shipped; it has a
mean.

Land the promise in one sentence: *by 15:00 you will have two interfaces from one screen that
could plausibly be from different companies, and you will be able to say why you chose each.*

Do not explain morphological analysis. Not yet, and ideally not at all — the room never needs
the phrase to run the method.

## 5–9 · Mobbin, and the MCP live

Assume a third of the room has never opened it. Four minutes, no feature tour.

- What is in there: real shipped screens, curated, searchable by pattern and flow.
- The MCP: the same library, inside the tool you already write in.
- One live search on the projector. Something that returns immediately — do not gamble on a
  cold connection in front of the room.

Say the honest part out loud: the MCP returns **stills**, not motion, and it returns almost no
metadata. It is a reference feed, not a design system. That framing buys credibility with a
senior room and saves you from the question later.

The search worth doing live is the absent one. `Crédit Mutuel online banking account screen`
returns Wise, Mercury, Square and Monarch — no Crédit Mutuel at all. The "before" is from a
bank the library does not index; the "after" comes from patterns it does. That gap is the
whole workshop in one search.

## 9–13 · Read the regions, together

The projector, baseline B on screen, four minutes.

View source. Show them `data-region="accounts-table"`, `data-region="transactions"`,
`data-region="upcoming"`. The screen names its own parts — nobody has to be taught a
vocabulary or argue about where the seams are.

Then ask one question and take answers from the floor: **what component is this, and what else
could it be?** A four-column table of three accounts could be a card stack, a list with
sparklines, accounts grouped by purpose, or one net figure with drill-down. Take four or five
answers, write them up, move on.

Push back every time someone answers with styling. "It's dated" is not a swap. "The table
could be a timeline" is.

*This block used to be six minutes of deriving a decomposition from scratch, and the dry run
found it was the step most likely to go sideways. Nicolas's region tags removed the problem
rather than shortening it.*

## 13–16 · The assignment

The brief: **same data, different components.**

Three rules, and say all three:

1. **Pick three regions.** Not six, not all of them.
2. **Keep every number and label.** Same balances, same 24 transactions, same raw labels. If a
   number changes, the output is disqualified — the point is that the *structure* moved.
3. **Keep the region names.** Same `data-region` values before and after. That is how
   "structurally different, same data" stops being a claim and becomes something you can diff.

Then the one that decides whether this works: **pick the regions carrying the most
information, not the most pixels.** Anyone who swaps the footer, the utility bar and the
shortcut buttons will produce something that looks new and is identical. Name that failure
now, from the front, so they recognise it in their own output at minute 30.

## 16–18 · The reveal — pick your screen

Three screens, not one. Reveal them here rather than in the pre-read, so the choice is made in
the room with the method already in their heads.

| | Screen | State | Take it if |
| --- | --- | --- | --- |
| A | Public homepage | Logged out | You work in marketing or content. The problem is accumulation: six audience segments before any content, fourteen stacked sections, a footnote on every claim |
| B | Accounts overview | Logged in | Default. Most data, widest gap, the most live regions. Recommend this to anyone who cannot decide |
| C | Transaction statement | Logged in | You like dense data. 24 rows, raw labels, no categories, no grouping |

Three different starting points across the room is what makes the show-and-tell contrast
structural rather than aesthetic. It replaces the four-zone split we planned earlier and does
the same job better: the contrast comes from the artefact rather than from a constraint we
imposed.

Say the calibration line out loud, for baseline A especially: **this page is not ugly.** It
was recently refreshed. Its problem is accumulation. Frame it that way or the room will
contest the premise, and they will be right to.

## 18–38 · Hands on

Twenty minutes. One full loop should take under seven, so there is room for two loops and
slack. Both of us circulating. Watch for the four known failure modes:

- **Timed-out first search.** Tell them to just run it again.
- **The model describing screens it hasn't looked at.** Symptom: pattern descriptions that
  match the app's reputation rather than the screenshot. Fix: make it cite the `mobbin_url`
  and say what is actually on the image.
- **Swapping only chrome.** Someone redesigns the footer and the nav and reports being done.
  Send them back to the region ranking.
- **A beautiful reskin.** New typeface, generous spacing, soft shadows, same four-column table
  underneath. This is the most common failure and the most important one to catch. Ask which
  region they think they changed, then open both and show them the table is still a table.
  That conversation *is* the workshop. The 6 September re-run measured this: the reskin
  **passes the data check** (every region, every number) and keeps all three `<table>`
  elements. So give the room the cheap tell: *baseline B has three tables. Count yours.*

Called from the front at the halfway mark: *"if your two versions look like siblings, you
changed the paint, not the plan."*

## 38–45 · Show and contrast

Three volunteers, roughly two minutes each — **one per baseline**. Pick them while circulating
rather than asking for hands, and pick people whose two versions genuinely diverged.

Each shows both versions and answers one question: **which regions did you swap, and what did
it cost you?** Every structural choice has a price. Grouping transactions by day means you
cannot scan for one merchant. Turning the accounts table into a single net figure means hiding
the Livret Bleu. Naming the cost is the difference between a designer and someone with a
moodboard.

## 45–48 · What just happened

Restate the method in a form they can run on Monday, without Mobbin and without us:

1. Find the parts the screen is already made of.
2. Ask what else each part could be.
3. Find what shipped, for each answer.
4. Be able to say why.

The defensible part is step 4. Everything else is preparation for being asked "why this
pattern?" in a review and having a link instead of a feeling.

Only now, if at all, is it worth naming what they just did: decompose, enumerate, recombine.
That is morphological analysis. They ran it without the word, which is the point.

## 48–50 · Takeaway

The repo is the takeaway: `START-HERE.md` with the one prompt, the three baselines, the swap
card, the three-step prompts, Nicolas's ten-line chart for anyone who wants the longer form.
Mobbin invite, Cursor credits, feedback link. Done.

## Setup, and why it happens before the room

Participants get `START-HERE.md` and the Hatch portal checklist (`docs/HATCH-PORTAL.md`) in
advance: one AI tool, Mobbin joined, the folder downloaded or cloned, Mobbin connected, one
warm-up search. The folder ships its own `.cursor/mcp.json` and `.mcp.json`, so Cursor and
Claude Code users click Connect rather than paste JSON. Nothing needs Python, Node or git.

28 people had signed up on 4 September against a room that seats about 20. Expect standing
laptops, and expect a few who did none of the setup. Say the cold-start line at minute 0
anyway: *if your first search times out, run it again.*

---

## Variations we considered and rejected

**The four-zone room split.** Each quarter of the room assigned one dimension they were not
allowed to leave alone. Superseded by the three baselines — the contrast now comes from the
artefact instead of from an imposed constraint, which is both simpler to explain and harder to
ignore.

**Running the full ten-line chart.** Nicolas's fuller instrument, preserved in
`docs/NICOLAS-CHART.md`. Rejected on time: the dry run measured six dimensions at 19–27
minutes of human work against a 22-minute block, and ten is worse. It is the right tool for
half a day.

**Splitting the room MCP versus screenshots.** Genuinely interesting, and it would answer a
real question about whether the MCP earns its place. Rejected for this session: the hands-on
block is already tight, and deliberately handicapping half the room in a Mobbin-sponsored
workshop is a hard sell. Worth doing as its own session — and worth running privately as the
gap test before the day.

**Group work.** Rejected on time. Thirty people in fifty minutes cannot form groups without
losing ten minutes to organising themselves.

**Building from a real bank's scraped HTML.** Rejected: auth walls, cookie banners and thirty
different DOMs. The baselines give everyone an identical, licence-safe starting point and cost
zero setup minutes.
