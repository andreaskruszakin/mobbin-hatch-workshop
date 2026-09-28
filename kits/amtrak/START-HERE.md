# Start here

**Research Fast and Design Live with Mobbin MCP.** Designed Minds, Thursday 8 October 2026,
3:00 to 4:30 PM PT (Friday 9 October, 7:00 to 8:30 KST).

Today you redesign one real screen, the Amtrak booking home page, with your AI tool and real
product screens from Mobbin. You don't need a terminal, Node or Python. Just the AI tool you
already use.

How to add Mobbin MCP to your tool: **[mobbin.com/mcp](https://mobbin.com/mcp)**.

![The template: Amtrak booking home page](template/preview.png)

## Before the session (5 minutes)

0. **Get Mobbin Pro.** Mobbin MCP needs a Pro plan, and code **DESIGNEDMINDS** gets you
   3 months of it. Go to [mobbin.com/pricing](https://mobbin.com/pricing), switch the toggle to
   **Quarterly**, click **Get Pro** on the Pro card, and create a free account or log in. At
   checkout, enter DESIGNEDMINDS as the promotion code.
1. **Get the kit.** You're reading this, so you probably have it. If not:
   [download kit.zip](https://github.com/andreaskruszakin/mobbin-hatch-workshop/releases/download/designed-minds-2026-10/kit.zip)
   and unzip it.
2. **Use a personal account if you can.** Company (enterprise) Cursor or Claude accounts often
   block MCP servers. If your work account is locked down, sign in with a personal one.
3. **Add Mobbin MCP to your AI tool**, then open this folder in it:
   - **Cursor.** Install the Mobbin plugin from the Cursor Marketplace (mobbin.com/mcp > Cursor,
     or Customize > Browse Marketplace > Mobbin), then Customize > Installed > Mobbin >
     **Authenticate** and sign in. Then File > Open Folder and pick this folder. The folder also
     ships its own Mobbin config: if you'd rather skip the plugin, press Cmd+Shift+P, type
     `MCP`, open **Cursor Settings: Tools & MCPs** and connect **Mobbin**.
   - **Claude Desktop.** Open [claude.ai/directory/mobbin](https://claude.ai/directory/mobbin)
     and add it, or in the app go to Customize > Connectors > Add > Browse
     connectors and search "Mobbin". Sign in with your Mobbin account. The listing shows the
     three tools you get: `search_screens`, `search_flows`, `search_sections`. Claude Desktop
     can't open a folder, so drag `template/index.html` and `prompts.md` into the chat instead.
   - **Claude Code.** If you connected Mobbin in Claude Desktop or on claude.ai, Claude Code
     already has it. Otherwise: `cd` into this folder, run `claude`, trust the project's
     `.mcp.json`, then type `/mcp`, pick **mobbin**, choose **Authenticate**.
   - **Codex.** Run `codex mcp add mobbin --url https://api.mobbin.com/mcp`, then
     `codex mcp login mobbin`, then run `codex` inside this folder.
   - **Anything else.** Add an MCP server named `Mobbin` with the URL
     `https://api.mobbin.com/mcp`. Help: [docs.mobbin.com/mcp](https://docs.mobbin.com/mcp/clients/overview).
4. **Run step 1 from `prompts.md`.** If three results come back, you're ready.

The first Mobbin search is often slow or times out. Run it again. The second try almost
always works.

## What Mobbin MCP can search

| Tool | Use it for | Example |
| --- | --- | --- |
| `search_screens` | One screen, like a home page or a checkout | "train booking home page where the search form is the main element" |
| `search_flows` | A journey across several screens | "train ticket booking flow from search to seat selection" |
| `search_sections` | One section of a website, like a hero or a pricing block | "hero section with a booking search form" |

Every result is a real screen from an app that shipped, with a `mobbin_url` you can open.

## What is in this folder

| File | What it is |
| --- | --- |
| `template/index.html` | The screen you redesign. Double-click it to open it in your browser. |
| `template/preview.png` | A screenshot of the same page. |
| `prompts.md` | Five prompts. Paste one at a time. |

The template is a saved copy of [amtrak.com](https://www.amtrak.com/home.html), captured on
28 September 2026. Its images and fonts sit in `template/assets/`, so it works offline.

## In the session

Follow the board. We run the five prompts in `prompts.md` together, one step at a time:

1. **Warm up.** Your AI tool reads the template and Mobbin wakes up.
2. **Search.** Mobbin shows you real screens, flows and sections that could improve the template.
3. **Pick.** You choose one to three of them and say why. Post your picks on the board.
4. **Redesign.** Your AI tool builds `mine/index.html` from your picks.
5. **Share.** Paste your before and after into your lane on the board so everyone can see it.
   Extra points: deploy `mine/` to Vercel and paste the live link.

## If something breaks

- **Mobbin says "Upgrade".** MCP needs Pro. Use code DESIGNEDMINDS for 3 months of Mobbin Pro.
- **Mobbin times out, or says "Failed to execute search".** Wait a few seconds and run it
  again. If it keeps failing, reconnect Mobbin (Cursor: Authenticate again; Claude Code: `/mcp`).
- **Mobbin is blocked (enterprise account).** Switch to a personal account. If you can't, use
  the backup links at the bottom of `prompts.md`: open them in the browser, take screenshots,
  and paste those into your AI tool.
- **The AI describes screens it did not look at.** Ask it to cite each `mobbin_url` and say
  what is actually in the image.
- **The AI invents prices, routes or times.** Tell it to keep only Amtrak's content and numbers.
- **Vercel asks you to log in, or the deploy fails.** Skip it. The screenshot in your lane is enough.
- **The redesign looks like the same page with new colours.** Ask which parts of the page it
  moved. If the layout is the same, send it back to your picks.
