# Run of show: virtual, 90 minutes

**Research Fast and Design Live with Mobbin MCP.** Designed Minds online, Thursday 8 October 2026,
3:00 to 4:30 PM PT. That's Friday 9 October, 7:00 to 8:30 KST, and 00:00 to 01:30 in Amsterdam.
Luma: https://luma.com/tuzxv38k (34 signups on 27 September). The room is international and
mostly US, so the template is a US product: the Amtrak booking home page.

Hosts: Andreas (facilitates), Eunji Jeong, Dali Kim and Inès. The call carries voice and screen
share. All content lives on the [FigJam board](https://www.figma.com/board/uQdulniCnQzptKeFiGs1Vg),
which is the slides, so participants follow on their own laptop.

This run is the dry run for Seoul on 24 October, which uses the KORAIL kit from the
`seoul-2026-10-24` release. Write down every place the room stalls.

## What changed since Hatch

Each change answers something the Hatch retro recorded, or a comment from Inès on the board.

| Hatch (18 Sep) | Now | Why |
| --- | --- | --- |
| Three baselines | One template | "Three baselines was too many" |
| "Baseline", "regions", "morphological" | "Template", "parts of the page" | People asked what a baseline was |
| Deck on a projector | The board is the slides, with a screenshot for every setup step | Blown-out projector, no shared link, "what are we supposed to do?" |
| Nobody had Pro | Setup step 1 is the DESIGNEDMINDS code: 3 months of Mobbin Pro | MCP needs Pro |
| Claude users left to guess | Claude Desktop has its own setup column, with the connector listing | Inès: Claude Desktop needs its own explanation |
| MCP explained in passing | A 15-minute station: the three tools, the website next to the MCP result, deep versus standard | Inès: show every tool, not only screen search |
| Model picks the swaps | The attendee picks 1 to 3 Mobbin references | Keeps people deciding instead of accepting |
| Results stayed on laptops | Everyone pastes before and after into a lane; Vercel link for extra points | Nobody saw each other's work |

## Before the day

- Send the two emails in `docs/EMAILS.md`.
- Rebuild the kit a few days out so the scraped page is current, then replace the release asset:
  `scripts/build-kit.sh amtrak` and
  `gh release upload designed-minds-2026-10 dist/amtrak/kit.zip --clobber`.
- Board sharing: "anyone with the link can edit". People paste into their lanes.
- Ask Dali and Inès for photos. Their host cards show initials until then.
- If signups pass 40, duplicate a row of lanes (select two lanes, Cmd+D, renumber).
- Rename the FigJam file if it still has an em dash in the name. The API can't rename it.
- Run step 1 of `prompts.md` on your own machine that morning so the demo connection is warm.
  If Mobbin answers "Failed to execute search", reconnect it (Cursor: Authenticate) and retry.

## Minute by minute

| Time | Station | What happens |
| --- | --- | --- |
| 0 to 5 | Welcome and hosts | Title, the four hosts, "follow on your laptop", the DESIGNEDMINDS code |
| 5 to 15 | Setup, five steps | Mobbin Pro, download, unzip, add Mobbin MCP, warm up |
| 15 to 30 | How Mobbin MCP works | The three tools, website versus MCP, deep versus standard |
| 30 to 35 | The template | Walk the five weak spots on the Amtrak page |
| 35 to 75 | Hands-on, five steps | Warm up, search, pick, redesign, share into the lanes |
| 75 to 85 | Share-outs | Five or six people, 90 seconds each |
| 85 to 88 | Why this works | Three reasons, roadmap ideas |
| 88 to 90 | Keep building | One sticky each, Seoul teaser |

"If something breaks" sits right after the lanes. Point people there instead of answering the
same question in chat five times.

### 0 to 5, Welcome and hosts

Paste the board link in the call chat before you say a word. "This board is the slides. Keep it
open on your laptop. I move left to right, and every station has a timer." Introduce the four
hosts from their cards. Say the goal once: by the end you'll have your own version of the Amtrak
booking page on this board, built from references Mobbin found, and you'll be able to say why.

Point at the yellow badge: with code DESIGNEDMINDS you get 3 months of Mobbin Pro. Say it plainly
and move on. No redemption counts, no expiry date.

### 5 to 15, Setup, five steps

Walk the five cards in order. Each has a screenshot of what people should see.

1. **Get Mobbin Pro.** mobbin.com/pricing, switch to Quarterly, Get Pro, create a free account or
   log in, then enter DESIGNEDMINDS at checkout.
2. **Download the kit** from the release page. Point at kit.zip under Assets.
3. **Unzip and open the folder.** The Finder and Cursor screenshots show what to expect.
4. **Add Mobbin MCP.** Four columns: Cursor (Marketplace plugin, or Tools & MCPs), Claude Desktop
   (claude.ai/directory/mobbin, or Customize > Connectors > Browse connectors), Claude Code and
   Codex. Claude Desktop can't open a folder, so those people drag `template/index.html` and
   `prompts.md` into the chat.
5. **Warm up.** Block 1 of `prompts.md`. Three results with links means ready. Standard mode is
   loose, so the results won't all be trains. That's fine here.

The two fixes on the step 5 card cover most trouble:
- **Timed out, or "Failed to execute search":** wait a few seconds and run it again. Still failing?
  Reconnect Mobbin in the tool.
- **Mobbin says "Upgrade":** back to step 1 and the code.
- **Enterprise account blocks MCP:** switch to a personal account. If they can't, the backup links
  at the bottom of `prompts.md` still let them pick references by hand.

**If most of the room is stuck at minute 15**, run steps 1 to 4 of the hands-on yourself on screen
share, and have people pick from the backup links. Watching you pick and argue beats 40 minutes of
fighting auth.

### 15 to 30, How Mobbin MCP works

The one idea: each Mobbin screen comes with metadata (app, flow, section, UI elements), so the
model reads "search form" and "fare card" instead of guessing from pixels.

Then walk the three tool cards. Each shows the page on mobbin.com next to what the same search
returns in the AI tool:

- **search_screens**, one screen. Website: Explore > Web > Screens. MCP: TravelPerk's train search
  and Klook's train form for "train booking home page where the journey search form is the main
  element".
- **search_flows**, a journey. Website: Explore > Web > Flows. MCP: TravelPerk's seven-screen
  "Searching trains" flow.
- **search_sections**, one part of a website. Website: Explore > Sites > Sections. MCP:
  Tripadvisor, OpenTable and Fresha heroes with a search bar.

Finish on the deep versus standard card. Same query, standard mode returns GetYourGuide, a Klaviyo
helpdesk and Sweatpals; deep mode returns TravelPerk and Klook. That's why block 2 uses deep.

If there's time, run one live search on screen share and open the `mobbin_url` of a result.

### 30 to 35, The template

Open `template/index.html` on screen share and walk the five numbered notes. Amtrak isn't ugly. It
accumulated things: a dozen form controls, a pale Find Trains button, a promo bigger than the form,
a credit card ad inside the train deals, and Track-A-Train at the very bottom. "This is the only
screen we redesign today."

### 35 to 75, Hands-on, five steps

You are the clock. Call each step as it starts.

| Start | Step | Say |
| --- | --- | --- |
| 35 | 1. Warm up | "Paste block 1. Read what your AI said was weak, and which Mobbin tools it lists." |
| 38 | 2. Search | "Paste block 2. Screens, a flow and a section. Read them. Nobody builds yet." |
| 45 | 3. Pick | "Choose one to three. Write why on a sticky in your lane, then paste block 3." |
| 50 | 4. Redesign | "Paste block 4. Open mine next to the template." |
| 58 | Halfway check | "Same page in new colours? You changed the paint, not the plan. Back to step 3." |
| 65 | 5. Share | "Screenshot before and after into your lane. Bonus: block 5 deploys to Vercel. Paste the link." |

Lane 1 holds a worked example: three picks (TravelPerk, Klook, OpenTable) and a before and after
where the search form became the hero.

While they work, zoom through the lanes. That's the virtual version of walking the room. Pick
share-out volunteers from lanes with a live link or a structurally different after, and message
them privately.

Failure modes, all on the "If something breaks" station:
- same page in new colours;
- invented fares, routes or times (Amtrak's only numbers are "up to 60% off" and
  "20,000 bonus points");
- the model describing screens it never opened;
- "Passenger with Disability or Assistance Needed?" quietly removed from a simpler form;
- Vercel wanting a login (skip it, the screenshots are enough).

### 75 to 85, Share-outs

Five or six people, 90 seconds each, live links first. One question: which picks did you use,
and what did the change cost? Stop anyone describing colours and ask what moved.

### 85 to 88, Why this works

Three reasons from the board: one template, real references, you picked. Then the ideas Mobbin
heard at Hatch. Present them as ideas, not a roadmap.

### 88 to 90, Keep building

Everyone drops one sticky: what will you try at work this week? Point at mobbin.com/mcp and the
DESIGNEDMINDS code, say the board and kit stay open, and tease Seoul on 24 October.

## After

- Export the board to PDF for anyone who watched the recording.
- Add a dated entry to `docs/DRY-RUN.md` with these numbers: people through setup step 5 at
  minute 15, lanes with an after at minute 75, and live links. Also note where the room stalled.
