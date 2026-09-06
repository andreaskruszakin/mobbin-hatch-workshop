# Start here

You are about to redesign one banking screen with your AI tool and real shipped patterns from
Mobbin. Nothing to install beyond the AI tool you already use. No terminal, no Node, no Python.

Setup takes about five minutes. Do it before the session, not in the room.

## 1. Get this folder onto your laptop

Pick one:

- **Download the zip** (easiest):
  [mobbin-hatch-workshop/archive/refs/heads/main.zip](https://github.com/andreaskruszakin/mobbin-hatch-workshop/archive/refs/heads/main.zip).
  Unzip it. You get a folder called `mobbin-hatch-workshop-main`.
- **Clone it**, if you use git:

  ```bash
  git clone https://github.com/andreaskruszakin/mobbin-hatch-workshop.git
  ```

Either way you end up with a folder containing `baselines/`, `prompts/` and this file.

## 2. Open the folder in your AI tool and connect Mobbin

You need a Mobbin account first. The workshop page has the invite link; sign in on
[mobbin.com](https://mobbin.com) once so the browser remembers you.

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

## In the room: the one prompt

Open your baseline's `index.html` in your AI tool so it can read it, then paste this. Change
the file path if you picked a different screen.

```
Read baselines/b-accounts/index.html. Its header comment says which parts are data
and which parts are the visual system.

STEP 1. List every element with a data-region attribute. For each: the region
name, what component it is now (table, link list, banner, nav bar, and so on),
and what information or decision it carries. Rank them by how much the user's
understanding would change if that region became a different component. Do not
rank by how much of the page it covers.

STEP 2. Take the top three regions. For each one, propose a different component
it could be, then run ONE Mobbin search per region for that component. Describe
the screen you want to see in plain language (a subject, the elements on it, how
they relate), platform "web", limit 4. Look at the returned images and tell me
what is actually on them. For each swap record: the structural logic in two
lines, the app name, and the mobbin_url. Do not invent examples.

STEP 3. Build one self-contained HTML file at variants/mine-1/index.html.
Apply the three swaps, following the structural logic of the Mobbin screens you
cited, not their colours or brand. Leave every other region as the same kind of
component.

Hard rules:
- Keep every number, date, amount, account name, IBAN and balance exactly as it
  is. Do not round, recalculate, invent or drop any.
- Keep the raw transaction labels reachable. Enriching them is fine; the original
  string must still be visible somewhere.
- Keep every data-region attribute with the same name on whatever element now
  plays that role.
- Plain HTML and CSS in one file. No frameworks, no build, no external requests.
  It must open by double-clicking. Vanilla JS only where the structure needs it.
- Put an HTML comment at the top listing the three swaps and the mobbin_urls.

Stop after each step and show me the result before continuing.
```

Then double-click `variants/mine-1/index.html` and look at what you got.

**Second round:** tell it to change two of the three swaps and build `variants/mine-2/index.html`.
Put both side by side. If they look like siblings, you changed the paint, not the plan.

## Want more control?

The prompt above is `prompts/01-decompose.md`, `02-ground.md` and `03-generate.md` in one
paste. Run them separately if you want to steer each step, and use `docs/SWAP-CARD.md` for
the full list of regions per screen with seeded alternatives.

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
