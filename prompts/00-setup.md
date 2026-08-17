# 00 — Setup (do this BEFORE you arrive)

The Mobbin MCP is slow on first connect. In the dry run the very first call **timed out** and
only worked on retry. Thirty people doing that simultaneously at 14:00 is the single most
likely way this workshop stalls.

## 1. Add the Mobbin MCP to your AI tool

Use the licence details from the workshop page. Cursor, Claude Code, VS Code and Windsurf all
read an `mcp.json`; the Mobbin docs have the exact snippet for each.

## 2. Warm it up

Paste this into your AI tool and let it run to completion:

```
Search Mobbin for "online banking account overview screen", platform web, limit 3.
Show me the app name and mobbin_url for each result.
```

You are ready when you get three results back with URLs. If it times out, **run it again** —
the second call almost always succeeds.

## 3. Have the baselines open

Three screens ship with this kit. You will pick one in the room, so have all three to hand.

```bash
python3 -m http.server 3160
```

- `http://localhost:3160/baselines/a-homepage/` — public homepage, logged out
- `http://localhost:3160/baselines/b-accounts/` — accounts overview, logged in
- `http://localhost:3160/baselines/c-transactions/` — transaction statement, logged in

They also open straight from the file system if you would rather not run a server. No build
step, no dependencies, no external requests.

## What "ready" looks like

- Mobbin MCP returns results without timing out
- All three baselines render in your browser
- Your AI tool can read and edit a local HTML file
