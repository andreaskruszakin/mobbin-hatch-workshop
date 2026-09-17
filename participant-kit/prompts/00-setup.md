# 00 — Setup

The short version is in [START-HERE.md](../START-HERE.md) at the root of this folder. This page
is the same thing with the reasoning attached.

Doing this before you arrive saves five minutes on the day. If you don't get to it, that's
fine — we connect Cursor and Mobbin together in the first few minutes of the session.

The Mobbin MCP is slow on first connect. In the dry run the very first call **timed out** and
only worked on retry. That's expected either way; run it again.

## 1. Connect the Mobbin MCP

The folder ships the server config, so there is nothing to paste for Cursor or Claude Code.

- **Cursor** reads `.cursor/mcp.json` when you open the folder. Enable it when asked, or go to
  Settings > Tools & MCPs, find **Mobbin**, click **Connect**, sign in.
- **Claude Code** reads `.mcp.json`. Trust the project when asked, then `/mcp`, **mobbin**,
  **Authenticate**.
- **Codex** has no project-level config. Two lines in a terminal:

  ```bash
  codex mcp add mobbin --url https://api.mobbin.com/mcp
  codex mcp login mobbin
  ```

- **Anything else**: an HTTP MCP server named `Mobbin` at `https://api.mobbin.com/mcp`.
  Per-client steps at [docs.mobbin.com/mcp/clients/overview](https://docs.mobbin.com/mcp/clients/overview).

Authorisation is OAuth in the browser. No API key, no token to paste. You need to already be on
the Mobbin team for this to work — that comes from the email you gave in the Hatch pre-setup
form, not from a link here. If sign-in fails, you may not have been added yet; try again closer
to the day or ask on the Hatch Slack.

## 2. Warm it up

Paste this into your AI tool and let it run to completion:

```
Search Mobbin for "online banking account overview screen", platform web, limit 3.
Show me the app name and mobbin_url for each result.
```

You are ready when you get three results back with URLs. If it times out, **run it again**. The
second call almost always succeeds.

## 3. Have the baselines open

Three screens ship with this kit. You will pick one in the room, so have all three to hand.
Double-click any `index.html`; they open straight from the file system.

- `baselines/a-homepage/index.html`, public homepage, logged out
- `baselines/b-accounts/index.html`, accounts overview, logged in
- `baselines/c-transactions/index.html`, transaction statement, logged in

No server, no build step, no dependencies, no external requests. The same three are live at
`https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/<name>/`.

## What "ready" looks like

- Mobbin MCP returns results without timing out
- All three baselines render in your browser
- Your AI tool can read and edit a local HTML file
