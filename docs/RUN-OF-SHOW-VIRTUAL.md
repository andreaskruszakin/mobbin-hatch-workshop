# Run of show: virtual, 60 minutes

**Design Minds monthly workshop. Thursday 8 October 2026, 7:00 to 8:00 KST**
(Wednesday 7 October, 22:00 UTC / midnight in Amsterdam).

Facilitator: Andreas. The call is for voice and screen share. All content lives on the
[FigJam board](https://www.figma.com/board/uQdulniCnQzptKeFiGs1Vg), which is the slides.
Participants follow on their own laptop, so nothing depends on someone reading your shared
screen.

This run is the dry run for Seoul on 24 October. Write down every place where the room stalls.

## What changed since Hatch

Each change answers something the Hatch retro recorded.

| Hatch (18 Sep) | Now | Why |
| --- | --- | --- |
| Three baselines | One template | "Three baselines was too many" |
| "Baseline", "regions", "morphological" | "Template", "parts of the page" | People asked what a baseline was |
| Deck on a projector | The board is the slides | Blown-out projector, no shared link |
| Setup status unknown until hands-on | Green/red sticky check-in at minute 3 | Enterprise accounts blocked MCP and nobody knew who was ready |
| Model picks the swaps | The attendee picks 1 to 3 Mobbin screens | Keeps people deciding instead of accepting |
| MCP explained in passing | One station on how it works | "Weak explanation of how Mobbin MCP works" |
| Fictional bank data | A scraped copy of a real page | Nothing to explain about where it came from |

## Before the day

- Send the two emails in `docs/EMAILS.md`: one the day before, one two hours before. Eunji
  translates.
- Rebuild the kit with `scripts/build-kit.sh` no more than a few days out, so the scraped page is
  current. Upload `kit.zip` and put its link in both emails and in the header station on the
  board (the text currently says "download kit.zip from the email").
- Share the board with "anyone with the link can edit". People have to drop stickies.
- Rename the FigJam file if it still has an em dash in the name (the API could not rename it).
- Run step 1 of `kit/prompts.md` on your own machine that morning. It wakes the connection for
  the live demo.
- Count replies. If more than 20 people are green, duplicate a row of lanes on the board.

## Minute by minute

| Time | Station | What happens |
| --- | --- | --- |
| 0 to 3 | Welcome | Goal, hosts, "follow on your laptop" |
| 3 to 8 | Check in | Everyone drops a green or red sticky |
| 8 to 13 | How Mobbin MCP works | One idea, one live search |
| 13 to 16 | The template | Walk the five weak spots |
| 16 to 42 | Hands-on | Four steps, lanes |
| 42 to 52 | Share-outs | Three or four people, 90 seconds each |
| 52 to 56 | Why this works | Three reasons, roadmap ideas |
| 56 to 60 | Wrap up | One sticky each, Seoul teaser |

### 0 to 3, Welcome

Paste the board link in the call chat before you say a word. Then: "This board is the slides.
Keep it open on your laptop. I will move through it left to right, and every station has a
timer."

Say the goal once: by the end you will have your own version of the KORAIL booking page, built
from screens that Mobbin found, and you will be able to say why you chose each one.

### 3 to 8, Check in

Everyone drops one sticky: name, AI tool, green or red. Green means step 1 of `prompts.md` came
back with three links.

Read the room out loud as the stickies land. "I see twelve green, four red." Then deal with red:

- **Enterprise account.** Switch to a personal Cursor or Claude account if they have one. If not,
  pair them with a green person by name and have them follow that person's lane.
- **Not set up.** Give them two minutes with `START-HERE.md` while you run the next station. If
  they aren't green by minute 16, they work from the backup links at the bottom of `prompts.md`.
- **First call timed out.** Run it again. The second call almost always works.

**If most of the room is red**, don't start the exercise. Run steps 1 to 4 yourself on screen
share, and have people post picks in their lanes from the backup links. A room that watches you
pick and argue is better than a room fighting auth for 26 minutes.

### 8 to 13, How Mobbin MCP works

The one idea: each Mobbin screen comes with metadata (app, flow, section, UI elements), so the
model reads "search form" and "fare card" instead of guessing from pixels. The board station has
the text; don't read it out.

Then one live search on screen share. Use the step 1 query from `prompts.md` in standard mode.
You warmed the connection that morning, so it should come back quickly. Point at the Klook
example on the board and say what a result is: a still image plus a `mobbin_url`. No motion.

### 13 to 16, The template

Open `kit/template/index.html` on screen share. Walk the five numbered notes on the board, then
say: "This is the only screen we redesign today."

Say the calibration line too. KORAIL isn't ugly. It accumulated things: a membership banner on
top of the booking tool, a floating quick menu, a discount carousel, two promo banners, guide
icons and notices, all at the same weight. The problem is that the page never says what to do
first.

### 16 to 42, Hands-on

Call each step as it starts. You are the clock.

| Start | Step | Say |
| --- | --- | --- |
| 16 | 1. Warm up | "Paste block 1. If you are already green, read what your AI said was weak." |
| 19 | 2. Search | "Paste block 2. Read the screens. Nobody builds yet." |
| 25 | 3. Pick | "Choose one to three. Write why on a sticky in your lane before you paste block 3." |
| 30 | 4. Redesign | "Paste block 4. When it's done, screenshot both into your lane." |
| 36 | Halfway check | "If yours looks like KORAIL in new colours, you changed the paint, not the plan." |

While they work, zoom through the lanes on the board. That's the virtual version of walking the
room. Pick share-out volunteers from lanes where the picks are specific and the after screenshot
looks structurally different. Message them privately so it isn't a surprise.

Failure modes the dry run saw, and what to say:

- **Same page, new paint.** Ask which part of the page moved. If the answer is "the colours",
  send them back to step 3.
- **Invented content.** The model adds prices or routes KORAIL's page doesn't have, usually after
  picking Klook's "popular routes". Block 4 forbids it. Point them at the line.
- **The model describes screens it didn't open.** Ask it to cite the `mobbin_url` and say what's
  in the image.
- **Long Korean labels wrap mid-word** when nine links go into one row. That's a real cost of the
  change. Keep it for the share-outs.

### 42 to 52, Share-outs

Three or four people, 90 seconds each, one per lane you picked. Each answers one question:
which picks did you use, and what did the change cost? Stop anyone who describes colours and
ask what moved.

### 52 to 56, Why this works

Three reasons, from the board: one template, real references, you picked. Then the ideas Mobbin
heard at Hatch. Present them as ideas, not a roadmap. Nothing on that list is announced.

### 56 to 60, Wrap up

Everyone drops one sticky: what will you try at work this week? Point at mobbin.com/mcp, say
the board and kit stay open, and tease Seoul on 24 October: same template, same four steps, in
person.

## After

- Export the board to PDF for Inès, who planned to watch the recording.
- Add a dated entry to `docs/DRY-RUN.md`: how many were green at minute 8, how many lanes had an
  after screenshot at minute 42, and where the room stalled. Those three numbers decide what
  changes for Seoul.
