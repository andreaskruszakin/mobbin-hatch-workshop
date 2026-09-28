# Prompts

Five steps. Paste one block at a time. Read what comes back before you paste the next one.

## 1. Warm up

```
This folder is the Mobbin MCP workshop. The file template/index.html is a saved copy of the
Amtrak booking home page. It is the only screen we redesign today.

1. Read template/index.html and tell me, in five short bullets, what is weak about it for
   someone who just wants to book a train. Think about what the page makes you do first.
2. List the Mobbin MCP tools you have access to, with one line each on what they search.
3. Search Mobbin for "train ticket booking home page with a journey search form",
   platform web, mode standard, limit 3. Show the app name and mobbin_url for each result.

Stop after that.
```

Three results with links means you're ready. If Mobbin times out, paste the block again.

## 2. Search

```
Using Mobbin MCP, find real references that would improve this template. Use all three tools,
platform web, limit 4 each:

1. search_screens, mode deep, twice. Describe each screen in one sentence: what it shows and
   how its parts relate. Good examples:
   - "train booking home page where the journey search form is the main element above the fold"
   - "travel booking home page showing deals as cards with who each deal is for"
2. search_flows, once: "train ticket booking flow from journey search to results to seat selection".
3. search_sections, once: "hero section with a booking search form".
Change the queries to match what you found weak in step 1.

For every result, give me the app name, the mobbin_url, and one sentence about what is
actually in the image. Do not describe a screen from the app's reputation. Look at it.

Do not redesign anything yet. Stop after the list.
```

## 3. Pick

This step is yours, not the AI's. Choose one to three references from step 2. For each one,
write one sentence: which part of the Amtrak page it fixes, and why. Post your picks on the board.

Then paste this, with your picks filled in:

```
These are my picks:
1. [mobbin_url], because [the part of the page it fixes, and why]
2. [mobbin_url], because [...]
3. [mobbin_url], because [...]

Before building, tell me in two lines how each pick changes the structure of the page.
Do not start building yet.
```

## 4. Redesign

```
Build mine/index.html from template/index.html using my picks.

Rules:
- Keep Amtrak's content: every label, deal, destination, link and footer line. Keep every
  number exactly as it is (like "up to 60% off" or "20,000 bonus points").
  Do not invent prices, routes, times or numbers the template does not have.
- Change how the page is arranged, not only the colours and fonts.
- Reuse images from template/assets/ with relative paths (../template/assets/...).
- One HTML file, no build step, it must open by double-click.
- Put my picks as mobbin_url links in an HTML comment at the top.

When you are done, list which parts of the page moved and which Amtrak labels you removed, if any.
```

Open `mine/index.html` next to `template/index.html`. If they look like the same page in new
colours, you changed the paint, not the plan. Go back to step 3.

## 5. Share

Put your work on the board so everyone can see it. Screenshot `template/index.html` and
`mine/index.html` in the browser (Cmd+Shift+4 on Mac, Win+Shift+S on Windows) and paste both into
your lane: Before on the left, After on the right. Your picks go on stickies next to them.

**Extra points: put it online.** Paste this:

```
Deploy the mine/ folder to Vercel as a static site. It needs ../template/assets/, so first copy
the images it uses into mine/assets/ and update the paths. Then run npx vercel deploy mine --prod
and give me the live URL.
```

Paste the URL into the "Live link" slot in your lane. If Vercel asks you to log in and you can't,
or the deploy fails, skip it. The screenshots are enough.

## More prompts to try

- Make "Find Trains" the one thing the page asks you to do. The booking form has about a dozen
  controls: which ones can wait until after the search?
- The Deals section mixes a credit card offer with train fares. Separate them and say who each
  deal is for.
- Track-A-Train is the most useful thing on the page and it sits at the bottom. Where should it go?
- Compare two of your picks. Build a second version at `mine-2/index.html` with the other one.
- Rebuild the page for someone planning a first weekend trip by train.

## Backup links (if Mobbin MCP is blocked)

Open these in the browser, screenshot what you like, and paste the screenshots into your AI tool.

- [Klook, Japan trains booking with the search form in the hero](https://mobbin.com/screens/05009b01-6fb3-45ad-ba20-5f0e7a2ad661)
- [Klook, popular routes as cards with duration and price](https://mobbin.com/screens/dc7b91b1-62b6-4fb7-8638-c71082474032)
- [KAYAK, search-first home with recent searches](https://mobbin.com/screens/41289ff6-f7ce-459e-8e06-e421e24138b7)
- [TravelPerk, train search with swap, time and traveller discount cards](https://mobbin.com/screens/c81a60ad-a8c7-437a-9dcd-04da75da98a3)
- [Navan, travel booking tabs with one search row](https://mobbin.com/screens/aae111e3-8a44-4e15-9a09-65549a4108df)
- [Kiwi.com, upcoming trip with service shortcuts](https://mobbin.com/screens/84199f37-f637-4ebf-bbf7-cf87ebd8de05)
- [TravelPerk flow, searching trains in seven screens](https://mobbin.com/flows/6452558b-044f-4a0f-b673-6177f6af2eea)
- [OpenTable section, hero with a date, time and party-size search bar](https://mobbin.com/sites/sections/65d3c9ef-1e92-487a-a7c5-48c166bd63c0)
