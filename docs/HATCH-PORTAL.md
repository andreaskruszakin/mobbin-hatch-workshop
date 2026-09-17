# Hatch facilitator portal: paste-ready copy

One block per portal field. The setup-documentation and pre-setup-form fields go through the
portal's own renderer, which floats links and inline code as badges — a link or `code span`
followed by more text on the same line comes out scrambled. Inside those two fields, keep every
link or code span alone at the end of its own line, nothing trailing. Replace the `TODO`
markers before publishing; everything else is final.

- `TODO-CURSOR-CREDITS`: the $50 Cursor credits link, Andreas
- `TODO-MOBBIN-DEADLINE`: the date the pre-setup form closes, so submitted emails can be
  batch-added to the Mobbin team before the day (see "Field: Pre-setup form")

There is no Mobbin invite link. Attendees are added to the Mobbin team from the email they
submit in the pre-setup form — batch that list before the day, since adding someone isn't
something either of us can do live in the room for a latecomer.

The participant download is a zip of the `participant-kit/` folder in the repo, not the whole
repo — that folder holds participant files only (baselines, prompts, `START-HERE.md`, the MCP
configs). Whenever `baselines/`, `prompts/`, `START-HERE.md` or the MCP configs change, rebuild
it from the repo root, after committing the `participant-kit/` change:

```
git archive --format=zip -o mobbin-hatch-workshop-kit.zip HEAD:participant-kit
```

`HEAD:participant-kit` roots the archive at that folder, so `START-HERE.md` etc. land at the
top level of the unzipped file, matching what `START-HERE.md` tells participants to expect.

The link everyone gets is a GitHub user-attachment URL — currently
`https://github.com/user-attachments/files/32332286/mobbin-hatch-workshop-kit.zip` — made by
dragging the zip into any GitHub comment box (an issue, a PR, a draft) and copying the link it
generates. That link is permanent but not replaceable: re-attaching a rebuilt file makes a new
URL, it does not update the old one. So after every rebuild:

- Drag the new zip into a comment, copy the new link, and paste it over the old one everywhere
  it's written down: `README.md`'s "Get the folder", and the setup-documentation field on the
  Hatch portal (currently pasted as a plain link where this file used to carry `TODO-KIT-ZIP`).
- Also upload the file itself to the portal's Materials field (see below) — the portal wants a
  literal upload, not a link.

Full repo, for anyone who wants the facilitator material too:
`https://github.com/andreaskruszakin/mobbin-hatch-workshop`.

---

## Field: Workshop description

Stop Designing From Vibes: same data, different components, grounded in what actually shipped.

Ask an AI tool to redesign a screen and you get the average of everything it has seen. Nice
type, soft shadows, and the same table underneath doing the same job. In fifty minutes you will
take one dated banking screen, read the parts it is made of, swap three of them for components
real products ship today (found through the Mobbin MCP inside your own AI tool), and regenerate.
You leave with two versions of one screen that could plausibly come from two different
companies, and you can say why you chose each.

Bring a laptop with the AI coding tool you already use (Cursor, Claude Code or Codex). Fill in
the pre-setup form with your email so we can add you to Mobbin before the day — that's the one
step that isn't optional. Everything else takes five minutes; do it before the session if you'd
like, or we'll help you connect in the first few minutes of the room. No coding experience
needed: the screens are plain HTML files that open by double-click, and the AI does the writing.

Hosted by Andreas Kruszakin (Cursor and Mobbin Ambassador, Netherlands) and Nicolas Chatelain
(Mobbin Ambassador).

---

## Field: Laptop requirements

- A laptop you can install things on, with a browser.
- One AI coding tool installed and signed in: Cursor, Claude Code or Codex. Any of the three
  works; pick the one you already use. Cursor is the easiest if you have none. Optional Cursor
  credits: TODO-CURSOR-CREDITS.
- A Mobbin account. No invite link — you're added to the team from the email you give in the
  pre-setup form.
- No Node, no Python, no git, no terminal required.

---

## Field: Setup documentation

## Setup — one step is required, the rest saves you five minutes

Fill in the pre-setup form's email question if you haven't — that's the only way we can add you
to the Mobbin team, and it can't be done live in the room for someone who skipped it. Do that
by TODO-MOBBIN-DEADLINE even if you skip everything else below.

- [ ] Fill in the pre-setup form on this page with your email — required, adds you to Mobbin
- [ ] Install an AI coding tool and sign in — Cursor is easiest if you have none: [cursor.com](https://cursor.com)
- [ ] Already use Claude Code or Codex instead? Either works too
- [ ] Once you've been added to Mobbin, sign in at [mobbin.com](https://mobbin.com) with that same email
- [ ] Get the workshop folder from: https://github.com/user-attachments/files/32332286/mobbin-hatch-workshop-kit.zip
- [ ] Unzip it, then open the folder in your AI tool — in Cursor: File, then Open Folder
- [ ] In Cursor, the folder brings its own Mobbin config: enable it when asked
- [ ] Not asked? Connect it yourself: Settings, then Tools and MCPs, then Mobbin, then Connect
- [ ] Sign in when the browser opens
- [ ] Using Claude Code or Codex instead? The connection steps are in START-HERE.md inside the folder
- [ ] Paste this into your AI tool and wait for three results with links:

Search Mobbin for "online banking account overview screen", platform web, limit 3. Show me the app name and mobbin_url for each result.

- [ ] If the first try times out, run it again — the second one works
- [ ] Double-click baselines/b-accounts/index.html in the folder — a bank screen opens in your browser, you're ready

## In the room

Everything else is in START-HERE.md in the folder, including the three prompts you will run.
We reveal three screens and you pick one. Didn't finish the setup above? Arrive five minutes
early, or we'll connect you in the first minutes of the session — except Mobbin access, which
needs to already be in place by then. Optional Cursor credits if you need them:
TODO-CURSOR-CREDITS.

## Stuck?

Message us on the Hatch Slack before Friday, or come five minutes early.

Full guide and troubleshooting: [github.com/andreaskruszakin/mobbin-hatch-workshop](https://github.com/andreaskruszakin/mobbin-hatch-workshop)

---

## Field: Pre-setup form

This form is load-bearing now, not just an assessment: question 1 is the only way we get an
attendee's email to add them to the Mobbin team, so it isn't optional even though the rest
still are.

1. Your email — used only to add you to the Mobbin team for the day. Required.
2. Which AI coding tool will you bring? Cursor / Claude Code / Codex / other / none yet
3. Have you used an MCP (a tool connection inside an AI assistant) before? Yes / No / Not sure
   what that is
4. Have you used Mobbin before? Regularly / Once or twice / Never

Use: batch-add every submitted email to the Mobbin team by TODO-MOBBIN-DEADLINE, ideally two
days before the session so nobody's first Mobbin sign-in happens live in the room. If most
answers to question 2 are "none yet", send the Cursor credits link in the reminder email and
budget two extra minutes at the top of the session for Connect.

---

## Field: Materials

Upload `mobbin-hatch-workshop-kit.zip`, built with the `git archive` command above. Nothing
else needs uploading: the slides link is shared on the day.

---

## Reminder email, two days before (if the portal sends one)

Subject: Friday's workshop: one required step, five optional minutes

Hi, one thing before Friday's "Stop Designing From Vibes" session isn't optional: if you
haven't already, fill in the pre-setup form on the workshop page with your email. That's how we
add you to the Mobbin team, and it has to happen before Friday, not in the room.

Everything else on that page is optional and saves five minutes on the day if you do it: one AI
coding tool installed, the workshop folder downloaded, Mobbin connected once you're added. If
you don't get to it, no problem — we'll set it up together in the room.

If you do not have an AI coding tool yet, install Cursor; the credits link on the page covers
the session. Any questions, reply here or find us on the Hatch Slack.

See you Friday. Andreas and Nicolas
