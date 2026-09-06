# Mobbin x Hatch — Workshop Lab

Facilitator kit for **"Stop Designing From Vibes"**, a 50-minute hands-on workshop at
**Hatch Berlin, 18 September 2026**. Andreas Kruszakin + Nicolas Chatelain.

Participants take one dated banking screen, read the parts it is already made of, swap three
of those parts for different components grounded in real shipped patterns via the Mobbin MCP,
and regenerate. Same data, different structure — and they can say why.

## The three baselines

Everyone picks one in the room at minute 16. They share a single fictional data contract, so
outputs stay comparable across the room.

- [A — Public homepage](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/a-homepage/)
  · logged out · 15 regions · the problem is accumulation, not ugliness
- [B — Accounts overview](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/b-accounts/)
  · logged in · 13 regions · **the default** — most data, widest gap
- [C — Transaction statement](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/c-transactions/)
  · logged in · 11 regions · 24 rows of raw, uncategorised labels

Each screen tags its sections with `data-region`. That is the decomposition, shipped inside
the artefact — nobody has to derive it, and "structurally different, same data" becomes
something you can diff rather than something you assert.

## Participants: read `START-HERE.md`

[START-HERE.md](START-HERE.md) is the whole setup: get the folder, open it in your AI tool,
connect Mobbin, paste one prompt. Five minutes, no terminal required.

## Get the folder

- Zip: [archive/refs/heads/main.zip](https://github.com/andreaskruszakin/mobbin-hatch-workshop/archive/refs/heads/main.zip)
- Clone: `git clone https://github.com/andreaskruszakin/mobbin-hatch-workshop.git`

## Open it

No install, no server, no build step. Each screen is one HTML file with its CSS inside.
Double-click `baselines/b-accounts/index.html` and it opens in your browser, or use the live
links above.

The folder ships a project-level Mobbin MCP config (`.cursor/mcp.json` for Cursor, `.mcp.json`
for Claude Code), so opening it in either tool registers the server; participants only click
Connect and sign in.

## What's here

| Path | What it is |
| --- | --- |
| `START-HERE.md` | Participant setup and the one workshop prompt |
| `baselines/` | The three screens participants fork, one folder each |
| `docs/SWAP-CARD.md` | The method — every region per screen, with seeded alternatives and a high/low yield rating |
| `docs/RUN-OF-SHOW.md` | Minute-by-minute facilitation script |
| `docs/NICOLAS-CHART.md` | The fuller ten-line chart and its relevance map, kept as background |
| `docs/DRY-RUN.md` | Measured MCP timings, failure modes, and what got cut to fit the slot |
| `docs/HATCH-PORTAL.md` | Paste-ready copy for the Hatch facilitator portal fields |
| `prompts/` | The three-step version of the prompt, for anyone who wants to steer each step |

## The method, in one question

Every region gets asked: **what component is this, and what else could it be?**

A four-column table of three accounts could be a card stack, a list with sparklines, accounts
grouped by purpose, or a single net figure with drill-down. One question, one Mobbin search,
one swap. Do it three times.

It is still morphological analysis — decompose, enumerate options, recombine deliberately —
but the room never needs the phrase, because the parts are already named in the file.

The rule that decides whether it works: **swap the regions carrying the most information, not
the most pixels.** Anyone who redesigns the footer and the nav produces something that looks
new and is identical.

## Prerequisites we ask of participants

A laptop, an AI coding tool they already use (Cursor, Claude Code or Codex), a Mobbin account
from the workshop invite, and this folder opened once with Mobbin connected **before** the
session starts. `START-HERE.md` has the warm-up query; the MCP cold start is slow and should not
happen thirty times at once in the room.

---

## About the baselines

These screens are **reconstructions built for design critique in a teaching setting**. They
are hand-written HTML made from the French retail-banking idiom and from the public homepage
as it appeared on 16 August 2026 — not scraped assets, not production code, and not screenshots
of anyone's logged-in session.

All personal data is fictional: the account holder, the client number, the balances and the
transactions are invented, and the IBANs are well-formed but unallocated. The UI copy has been
translated to English for the room; French product names are kept as proper nouns and the raw
transaction labels are left exactly as a bank emits them, because cleaning them up would hand
participants the most obvious win for free.

The workshop's subject is a category-wide pattern in European retail banking, not one
institution. Crédit Mutuel is not affiliated with, and has not endorsed, this material. No
trademark or copyright claim is made or implied.
