# Start here

You are about to redesign one banking screen with your AI tool and real shipped patterns from
Mobbin. Nothing to install beyond the AI tool you already use. No terminal, no Node, no Python.

Setup takes about five minutes. Do it now if you'd rather have it out of the way — otherwise
we'll connect Cursor and Mobbin together in the first few minutes of the session.

## 1. Get this folder onto your laptop

If you downloaded the workshop zip from the Hatch portal and unzipped it, you already have
this folder — skip to step 2.

Looking at this on GitHub instead? Download
[mobbin-hatch-workshop-kit.zip](https://github.com/user-attachments/files/32332286/mobbin-hatch-workshop-kit.zip)
and unzip it. The full repo, including facilitator material you don't need for the workshop, is
at `https://github.com/andreaskruszakin/mobbin-hatch-workshop`.

Either way you end up with a folder containing `baselines/`, `prompts/` and this file.

## 2. Open the folder in your AI tool and connect Mobbin

You need to already be on the Mobbin team for this to work. There's no invite link — you're
added from the email you gave in the Hatch pre-setup form. Sign in on
[mobbin.com](https://mobbin.com) once, with that same email, so the browser remembers you. If
sign-in fails, you may not have been added yet; try again closer to the day.

**Cursor**

1. File > Open Folder, pick the folder from step 1.
2. Cursor notices the Mobbin MCP that ships in this folder and asks to enable it. Say yes.
   If it does not ask: Settings > Tools & MCPs, find **Mobbin**, click **Connect**.
3. A browser tab opens. Sign in with your Mobbin account and allow access.

**Claude Code**

1. In a terminal: `cd` into the folder, run `claude`.
2. It asks to trust the project's `.mcp.json`. Say yes.
3. Type `/mcp`, pick **mobbin**, choose **Authenticate**, sign in when the browser opens.

**Codex**

1. In a terminal, run these two lines, then sign in when the browser opens:

   ```bash
   codex mcp add mobbin --url https://api.mobbin.com/mcp
   codex mcp login mobbin
   ```

2. `cd` into the folder and run `codex`.

**Anything else** (VS Code, Windsurf, Claude Desktop, and so on): add an MCP server named
`Mobbin` with the URL `https://api.mobbin.com/mcp`. The exact clicks are at
[docs.mobbin.com/mcp/clients/overview](https://docs.mobbin.com/mcp/clients/overview).

## 3. Warm it up

Paste this into your AI tool and wait for it to finish:

```
Search Mobbin for "online banking account overview screen", platform web, limit 3.
Show me the app name and mobbin_url for each result.
```

You are ready when three results with links come back. **If the first try times out, run it
again.** The first connection is slow; the second one almost always works.

## 4. Look at the screen you will redesign

Double-click `baselines/b-accounts/index.html`. It opens in your browser. That is a logged-in
accounts overview from a French retail bank, rebuilt for this session with fictional data.

Two more screens ship alongside it. We reveal all three in the room and you pick one, so have a
look at each now:

- `baselines/a-homepage/index.html`, the public homepage
- `baselines/b-accounts/index.html`, the accounts overview (the default if you cannot decide)
- `baselines/c-transactions/index.html`, a transaction statement

They also open online, no download needed:
[a-homepage](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/a-homepage/) ·
[b-accounts](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/b-accounts/) ·
[c-transactions](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/c-transactions/)

That is the whole setup. Everything below happens in the room.

---

## In the room: run the three prompts

Open your baseline's `index.html` in your AI tool so it can read it. Then run these three
files from `prompts/`, one at a time, in order. Change the file path in the first one if you
picked a different screen.

1. `prompts/01-decompose.md` — read the regions, rank them, pick three.
2. `prompts/02-ground.md` — find a real, shipped example for each swap.
   `docs/SWAP-CARD.md` has seeded alternatives per screen if you want a starting point.
3. `prompts/03-generate.md` — build `variants/mine-1/index.html`, then a second round at
   `variants/mine-2/index.html` with two of the three swaps changed.

Each file has one block to paste, and the reasoning behind it if you want it. Paste the block,
look at what comes back, then open the next file.

Then double-click `variants/mine-1/index.html` and look at what you got. Put it next to
`variants/mine-2/index.html`: if they look like siblings, you changed the paint, not the plan.

## Regions give you control. Free-form is more fun.

Working region by region is one way to iterate, and it gives you control: the regions are
already flagged in the HTML, so you point your AI tool at one part at a time. It isn't the
only way. A single open request like "redo this in Revolut's style" is more fun to run, and
worth trying with everything Mobbin MCP and your AI tool can do.

Either way, a more opinionated request produces a better result. Name the component you want,
name the reference, say why. You should be able to explain that why afterward — the same test
applies to a design brief and to a prompt. Having fun with it doesn't get you out of that.

Going free-form doesn't mean skipping what makes Mobbin useful. `prompts/02-ground.md` has the
query phrasing that actually returns something (a sentence describing the screen, not
keywords), and `prompts/03-generate.md` has two checks worth running on whatever you get: is
the data still intact, and could this pass as work from two different companies?

## If something breaks

- **Mobbin search times out**: run it again. Still failing? `prompts/02-ground.md` has ten
  pre-verified Mobbin links to use instead.
- **The model describes screens it has not looked at**: ask it to cite the `mobbin_url` and say
  what is in the image.
- **The output is a prettier version of the same table**: ask which region it changed, then open
  both files. If the table is still a table, it swapped the paint. Send it back to the ranking.
- **Cursor does not show Mobbin**: Settings > Tools & MCPs > New MCP server, paste

  ```json
  { "mcpServers": { "Mobbin": { "type": "http", "url": "https://api.mobbin.com/mcp", "headers": {} } } }
  ```
