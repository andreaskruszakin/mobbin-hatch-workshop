# Run of show — 50 minutes

Presentation is capped at 15 minutes (30%). Everything after that is hands or voices in the
room. Timings below come out of `docs/DRY-RUN.md`, not out of optimism.

| Time | Block | Lead |
| --- | --- | --- |
| 0–5 | The slop problem | Andreas |
| 5–9 | Mobbin, and the MCP live | Nicolas |
| 9–13 | Decompose the baseline, together | Andreas |
| 13–15 | The assignment and the room split | Nicolas |
| 15–37 | Hands on, individually | both floating |
| 37–45 | Show and contrast | Nicolas chairs |
| 45–48 | What just happened | Andreas |
| 48–50 | Takeaway page, codes, feedback | Nicolas |

---

## 0–5 · The slop problem

Open cold, with the demo rather than the claim. Same brief, twice, into the same tool. Two
outputs, both fine, both the average of everything it has seen. That is the problem — not
speed, not quality, **reference**. AI has no taste and no memory of what shipped; it has a
mean.

Land the promise in one sentence: *by 15:00 you will have two interfaces from one brief that
could plausibly be from different companies, and you will be able to say why you chose each.*

Do not explain morphological analysis yet.

## 5–9 · Mobbin, and the MCP live

Assume a third of the room has never opened it. Four minutes, no feature tour.

- What is in there: real shipped screens, curated, searchable by pattern and flow.
- The MCP: the same library, inside the tool you already write in.
- One live search on the projector. Something that returns immediately — do not gamble on a
  cold connection in front of the room.

Say the honest part out loud: the MCP returns **stills**, not motion, and it returns almost
no metadata. It is a reference feed, not a design system. That framing buys credibility with
a senior room and saves you from the question later.

## 9–13 · Decompose the baseline, together

The projector, `baseline/index.html`, four minutes, called out from the floor.

Ask: *what decisions did this screen make?* Push back every time someone answers with
styling. "It's ugly" is not a decision. "It only tells you what's wrong after you submit" is.

Land on the six dimensions live. This is where the method actually gets taught, and doing it
as a room is faster and better than twenty-two people doing it alone — which is exactly what
the dry run showed.

## 13–15 · The assignment and the room split

The brief: **same product, same information collected, different structure.** Two versions.

Ground three dimensions only — progress model, input density, post-submit state. The other
three are in the takeaway page for later. This is the cut that makes the block fit.

Then split the room in four, each with one dimension they are **not allowed** to leave alone:

| Zone | Must change |
| --- | --- |
| 1 | Progress model — the user must always know where they are |
| 2 | Input density — no more than one decision per screen |
| 3 | Post-submit — the 5–7 day wait has to become useful |
| 4 | Commitment ramp — nothing is asked before it is earned |

Individual work, not groups. Thirty people in fifty minutes cannot do group work without
losing ten minutes to organising themselves. The zones exist to guarantee the show-and-tell
contrasts, not to make teams.

## 15–37 · Hands on

Both of us circulating. Watch for the three known failure modes:

- **Timed-out first search.** Tell them to just run it again.
- **The model describing screens it hasn't looked at.** Symptom: pattern descriptions that
  match the app's reputation rather than the screenshot. Fix: make it cite the `mobbin_url`
  and say what is actually on the image.
- **Two variants that are the same product in different colours.** The most common failure
  and the most important one to catch. Ask them which dimension they think they varied, then
  open both and show them they only restyled it. That conversation *is* the workshop.

Called from the front at 15-minute mark: *"if your two versions look like siblings, you
changed the paint, not the plan."*

## 37–45 · Show and contrast

Three volunteers, roughly two minutes each, and pick them while circulating rather than
asking for hands — ask people whose two versions genuinely diverged.

Each shows both versions and answers one question: **which dimension did you change, and
what did it cost you?** Every structural choice has a price. One question per screen means
more clicks. An eligibility gate means turning people away early. Naming the cost is the
difference between a designer and someone with a moodboard.

Try to pick three from different zones so the contrast is structural rather than aesthetic.

## 45–48 · What just happened

Restate the method in a form they can run on Monday, without Mobbin and without us:

1. Break the problem into independent decisions.
2. Find what shipped, for each decision.
3. Combine deliberately.
4. Be able to say why.

The defensible part is step 4. Everything else is preparation for being asked "why this
pattern?" in a review and having a link instead of a feeling.

## 48–50 · Takeaway

The Notion page: matrix, prompts, baseline, the three sample variants, Mobbin code, Cursor
credits. Feedback link. Done.

---

## Variations we considered and rejected

**Splitting the room MCP versus screenshots.** Genuinely interesting comparison and it would
answer a real question about whether the MCP earns its place. Rejected for this session: the
hands-on block is already tight, and deliberately handicapping half the room in a
Mobbin-sponsored workshop is a hard sell. Worth doing as its own session.

**Group work.** Rejected on time. See above.

**Building from a real bank's scraped HTML.** Rejected: auth walls, cookie banners and thirty
different DOMs. The baseline gives everyone an identical, licence-safe starting point and
costs zero setup minutes.
