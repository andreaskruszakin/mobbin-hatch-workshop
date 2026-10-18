# Mobbin x Hatch — Workshop Lab

## Next run: Designed Minds Seoul, in person, Saturday 24 October 2026, 12:00 to 2:00 PM

One template, five prompts, one bilingual FigJam board that doubles as the slides. Seoul redesigns
the home screen of SC제일은행's SC Mobile app (Standard Chartered Bank Korea), in Korean and English
because the room has foreign attendees. The online run on 8 October used the Amtrak kit. Participants join the Designed Minds team on Mobbin through https://mobbin.com/team/join/0fba9939-3fe3-4f87-adfe-c29ee0211caf, and an admin approves them.

| Path | What it is |
| --- | --- |
| `kits/amtrak/` | Online kit: `START-HERE.md`, `prompts.md` (five steps), MCP configs. Download from the [designed-minds-2026-10 release](https://github.com/andreaskruszakin/mobbin-hatch-workshop/releases/tag/designed-minds-2026-10) |
| `kits/scmobile/` | Seoul kit: bilingual `START-HERE.md` and `prompts.md`, MCP configs, and `template/index.html`, the SC Mobile home screen rebuilt in React with a 한국어 / English switch. Download from the [seoul-2026-10-24 release](https://github.com/andreaskruszakin/mobbin-hatch-workshop/releases/tag/seoul-2026-10-24) |
| `kits/korail/` | Retired Seoul kit (KORAIL booking page), kept as the record |
| `kits/*/template/` | Not in git, apart from `kits/scmobile/template/index.html`. Amtrak and KORAIL are scraped copies of the live sites; SC Mobile's images are cut from app screenshots by `scripts/crop-scmobile.py`. `scripts/build-kit.sh amtrak\|korail\|scmobile` regenerates a template and packs `dist/<name>/kit.zip` |
| [Seoul FigJam board](https://www.figma.com/board/ta8xP6bThj8jAshgtjOIXE) | Seoul: bilingual setup steps, the three Mobbin MCP tools, the annotated SC Mobile screenshots, the hands-on lanes |
| [Online FigJam board](https://www.figma.com/board/uQdulniCnQzptKeFiGs1Vg) | The 8 October online session, kept as the record |
| `docs/RUN-OF-SHOW-VIRTUAL.md` | Minute-by-minute script for the 90 minutes |
| `docs/EMAILS.md` | The two pre-session emails (one day before, two hours before) |

Everything below this section is the Hatch Berlin run, kept as the record.

---

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
connect Mobbin, run the three prompts. Five minutes, no terminal required.

## Get the folder

Download [mobbin-hatch-workshop-kit.zip](https://github.com/user-attachments/files/32332286/mobbin-hatch-workshop-kit.zip) —
`participant-kit/` zipped, nothing else. Unzip it; `START-HERE.md` is at the top level. This is
the same file distributed from the Hatch portal — see `docs/HATCH-PORTAL.md` for how it's
rebuilt.

Want the full repo, including facilitator material? Browse it at
[github.com/andreaskruszakin/mobbin-hatch-workshop](https://github.com/andreaskruszakin/mobbin-hatch-workshop).

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
| `prompts/` | The three-step version of the prompt, for anyone who wants to steer each step |
| `docs/SWAP-CARD.md` | The method — every region per screen, with seeded alternatives and a high/low yield rating |
| `participant-kit/` | The zip source: a copy of everything above plus the MCP configs, nothing else. Kept in sync by hand — see its own note if you edit the source files |
| `docs/RUN-OF-SHOW.md` | Minute-by-minute facilitation script (facilitator only) |
| `docs/NICOLAS-CHART.md` | The fuller ten-line chart, its relevance map and the calibration check (facilitator only) |
| `docs/DRY-RUN.md` | Measured MCP timings, failure modes, and what got cut to fit the slot (facilitator only) |
| `docs/HATCH-PORTAL.md` | Paste-ready copy for the Hatch facilitator portal fields (facilitator only) |

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

A laptop, an AI coding tool they already use (Cursor, Claude Code or Codex), and their email
submitted in the Hatch pre-setup form — that's how they get added to the Mobbin team, and it's
the one step that has to happen before the day, not in the room. Connecting Mobbin and running
the warm-up query in `START-HERE.md` before the session saves five minutes on the day, since
the MCP cold start is slow — but that part isn't required. We connect stragglers in the first
minutes of the room instead.

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
