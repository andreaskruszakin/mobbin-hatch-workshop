# Start here

**Research Fast and Design Live with Mobbin MCP.** Designed Minds, Friday 9 October 2026,
7:00 to 8:30 KST (Thursday 8 October, 3:00 to 4:30 PM PT).

Today you redesign one real screen, the KORAIL ticket booking page, with your AI tool and real
product screens from Mobbin. You don't need a terminal, Node or Python. Just the AI tool you
already use.

How to add Mobbin MCP to your tool: **[mobbin.com/mcp](https://mobbin.com/mcp)**. The steps
below cover Cursor, Claude Code and Codex.

![The template: KORAIL ticket booking page](template/preview.png)

## Before the session (5 minutes)

0. **Get the kit.** You're reading this, so you probably have it. If not:
   [download kit.zip](https://github.com/andreaskruszakin/mobbin-hatch-workshop/releases/download/designed-minds-2026-10/kit.zip)
   and unzip it.
1. **Use a personal account if you can.** Company (enterprise) Cursor or Claude accounts often
   block MCP servers. If your work account is locked down, sign in with a personal one.
2. **Sign in on [mobbin.com](https://mobbin.com)** with the email you gave when you registered.
3. **Open this folder in your AI tool** and connect Mobbin:
   - **Cursor.** File > Open Folder, pick this folder. When Cursor asks to enable the Mobbin MCP,
     say yes. If it does not ask, go to Settings > Tools & MCPs, find **Mobbin**, click
     **Connect**. Sign in when the browser opens.
   - **Claude Code.** `cd` into this folder, run `claude`, trust the project's `.mcp.json`, then
     type `/mcp`, pick **mobbin**, choose **Authenticate**.
   - **Codex.** Run `codex mcp add mobbin --url https://api.mobbin.com/mcp`, then
     `codex mcp login mobbin`, then run `codex` inside this folder.
   - **Anything else.** Add an MCP server named `Mobbin` with the URL
     `https://api.mobbin.com/mcp`. Help: [docs.mobbin.com/mcp](https://docs.mobbin.com/mcp/clients/overview).
4. **Run step 1 from `prompts.md`.** If three results come back, you are green. Reply green
   or red to the email so we know who is ready.

The first Mobbin search is often slow or times out. Run it again. The second try almost
always works.

## What is in this folder

| File | What it is |
| --- | --- |
| `template/index.html` | The screen you redesign. Double-click it to open it in your browser. |
| `template/preview.png` | A screenshot of the same page. |
| `prompts.md` | Five prompts. Paste one at a time. |

The template is a saved copy of [korail.com/ticket/main](https://www.korail.com/ticket/main),
captured on 27 September 2026. Its images and fonts sit in `template/assets/`, so it works
offline.

## In the session

Follow the board. We run the five prompts in `prompts.md` together, one step at a time:

1. **Warm up.** Your AI tool reads the template and Mobbin wakes up.
2. **Search.** Mobbin shows you real screens that could improve the template.
3. **Pick.** You choose one to three of them and say why. Post your picks on the board.
4. **Redesign.** Your AI tool builds `mine/index.html` from your picks.
5. **Share.** Paste your before and after into your lane on the board so everyone can see it.
   Extra points: deploy `mine/` to Vercel and paste the live link.

## If something breaks

- **Mobbin times out.** Run it again.
- **Mobbin is blocked (enterprise account).** Pair with a neighbour who is green, or use the
  backup links at the bottom of `prompts.md`: open them in the browser, take screenshots,
  and paste those into your AI tool.
- **The AI describes screens it did not look at.** Ask it to cite each `mobbin_url` and say
  what is actually in the image.
- **The AI invents prices or routes.** KORAIL's page has none. Tell it to keep only KORAIL's content.
- **Vercel asks you to log in, or the deploy fails.** Skip it. The screenshot in your lane is enough.
- **The redesign looks like the same page with new colours.** Ask which parts of the page it
  moved. If the layout is the same, send it back to your picks.
