# Run of show: virtual, 90 minutes

**Research Fast and Design Live with Mobbin MCP.** Designed Minds, Friday 9 October 2026,
7:00 to 8:30 KST. That's Thursday 8 October, 3:00 to 4:30 PM PT, and 00:00 to 01:30 in Amsterdam.
Luma: https://luma.com/tuzxv38k (34 signups on 27 September).

Hosts: Andreas (facilitates), Eunji Jeong, Dali Kim and Inès. The call carries voice and screen
share. All content lives on the [FigJam board](https://www.figma.com/board/uQdulniCnQzptKeFiGs1Vg),
which is the slides, so participants follow on their own laptop.

This run is the dry run for Seoul on 24 October. Write down every place the room stalls.

## What changed since Hatch

Each change answers something the Hatch retro recorded.

| Hatch (18 Sep) | Now | Why |
| --- | --- | --- |
| Three baselines | One template | "Three baselines was too many" |
| "Baseline", "regions", "morphological" | "Template", "parts of the page" | People asked what a baseline was |
| Deck on a projector | The board is the slides, with a screenshot for every setup step | Blown-out projector, no shared link, "what are we supposed to do?" |
| Setup status unknown until hands-on | Green/red sticky at step 5 of setup | Enterprise accounts blocked MCP and nobody knew who was ready |
| Model picks the swaps | The attendee picks 1 to 3 Mobbin screens | Keeps people deciding instead of accepting |
| MCP explained in passing | One station on how it works, plus mobbin.com/mcp on every setup card | "Weak explanation of how Mobbin MCP works" |
| Results stayed on laptops | Everyone pastes before and after into a lane; Vercel link for extra points | Nobody saw each other's work |

## Before the day

- Send the two emails in `docs/EMAILS.md`. Eunji translates.
- Rebuild the kit with `scripts/build-kit.sh` a few days out so the scraped page is current, then
  replace the asset on the release: `gh release upload designed-minds-2026-10 kit.zip --clobber`.
- Board sharing: "anyone with the link can edit". People paste into their lanes.
- Ask Dali and Inès for photos. Their host cards show initials until then.
- If signups pass 40, duplicate a row of lanes (select two lanes, Cmd+D, renumber).
- Rename the FigJam file if it still has an em dash in the name. The API can't rename it.
- Run step 1 of `kit/prompts.md` on your own machine that morning so the demo connection is warm.

## Minute by minute

| Time | Station | What happens |
| --- | --- | --- |
| 0 to 5 | Welcome and hosts | Title, the four hosts, "follow on your laptop" |
| 5 to 15 | Setup, five steps | Download, unzip, add Mobbin MCP, warm up, green/red sticky |
| 15 to 22 | How Mobbin MCP works | One idea, one live search |
| 22 to 27 | The template | Walk the five weak spots |
| 27 to 67 | Hands-on, five steps | Warm up, search, pick, redesign, share into the lanes |
| 67 to 80 | Share-outs | Five or six people, 90 seconds each |
| 80 to 85 | Why this works | Three reasons, roadmap ideas |
| 85 to 90 | Keep building | One sticky each, Seoul teaser |

"If something breaks" sits right after the lanes. Point people there instead of answering the
same question in chat five times.

### 0 to 5, Welcome and hosts

Paste the board link in the call chat before you say a word. "This board is the slides. Keep it
open on your laptop. I move left to right, and every station has a timer." Introduce the four
hosts from their cards. Say the goal once: by the end you'll have your own version of the KORAIL
booking page on this board, built from screens Mobbin found, and you'll be able to say why.

### 5 to 15, Setup, five steps

Walk the five cards in order. Each has a screenshot of exactly what people should see.

1. **Download the kit** from the release page. Point at kit.zip under Assets.
2. **Unzip and open the folder.** The Finder and Cursor screenshots show the three items to
   expect.
3. **Add Mobbin MCP.** Everyone goes to mobbin.com/mcp and picks their tool under "Connect tool".
   The three columns cover Cursor (Marketplace plugin, or the kit's own config via Tools & MCPs),
   Claude Code and Codex.
4. **Warm up.** Block 1 of `prompts.md`. Green looks like the three-result card.
5. **Green or red sticky.** Read the room out loud as they land.

Dealing with red:
- **Enterprise account:** switch to a personal account, or pair with someone green by name.
- **Mobbin says "Upgrade":** they aren't on the workshop team. Inès checks the email they
  registered with.
- **First call timed out:** run it again.

**If most of the room is red at minute 15**, run steps 1 to 4 of the hands-on yourself on screen
share, and have people pick from the backup links in `prompts.md`. Watching you pick and argue
beats 40 minutes of fighting auth.

### 15 to 22, How Mobbin MCP works

The one idea: each Mobbin screen comes with metadata (app, flow, section, UI elements), so the
model reads "search form" and "fare card" instead of guessing from pixels. Then run one live
search on screen share in standard mode, and point at the Klook result: a still plus a
`mobbin_url`. No motion.

### 22 to 27, The template

Open `kit/template/index.html` on screen share and walk the five numbered notes. KORAIL isn't ugly.
It accumulated things, and the page never says what to do first. "This is the only screen we
redesign today."

### 27 to 67, Hands-on, five steps

You are the clock. Call each step as it starts.

| Start | Step | Say |
| --- | --- | --- |
| 27 | 1. Warm up | "Paste block 1. Already green? Read what your AI said was weak." |
| 30 | 2. Search | "Paste block 2. Read the screens. Nobody builds yet." |
| 37 | 3. Pick | "Choose one to three. Write why on a sticky in your lane, then paste block 3." |
| 42 | 4. Redesign | "Paste block 4. Open mine next to the template." |
| 50 | Halfway check | "Same page in new colours? You changed the paint, not the plan. Back to step 3." |
| 57 | 5. Share | "Screenshot before and after into your lane. Bonus: block 5 deploys to Vercel. Paste the link." |

While they work, zoom through the lanes. That's the virtual version of walking the room. Pick
share-out volunteers from lanes with a live link or a structurally different after, and message
them privately.

Failure modes, all on the "If something breaks" station:
- same page in new colours;
- invented prices or routes (KORAIL has none);
- the model describing screens it never opened;
- Korean labels wrapping mid-word when nine links share a row;
- Vercel wanting a login (skip it, the screenshots are enough).

### 67 to 80, Share-outs

Five or six people, 90 seconds each, live links first. One question: which picks did you use,
and what did the change cost? Stop anyone describing colours and ask what moved.

### 80 to 85, Why this works

Three reasons from the board: one template, real references, you picked. Then the ideas Mobbin
heard at Hatch. Present them as ideas, not a roadmap.

### 85 to 90, Keep building

Everyone drops one sticky: what will you try at work this week? Point at mobbin.com/mcp, say the
board and kit stay open, and tease Seoul on 24 October.

## After

- Export the board to PDF for anyone who watched the recording.
- Add a dated entry to `docs/DRY-RUN.md` with these numbers: stickies green at minute 15, lanes
  with an after at minute 67, and live links. Also note where the room stalled.
