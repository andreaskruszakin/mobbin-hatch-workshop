# Hatch facilitator portal: paste-ready copy

One block per portal field. The setup-documentation field takes markdown with headings,
checklists, links and inline code (the toolbar in the portal), so that block is written in
exactly that subset. Replace the two `TODO` links before publishing; everything else is final.

- `TODO-MOBBIN-INVITE`: the team invite link from Jovan (back Wednesday 9 September)
- `TODO-CURSOR-CREDITS`: the $50 Cursor credits link, Andreas
- `TODO-KIT-ZIP`: the uploaded `mobbin-hatch-workshop-kit.zip` link (see "Field: Materials")

The participant download is a zip of the `participant-kit/` folder in the repo, not the whole
repo — that folder holds participant files only (baselines, prompts, `START-HERE.md`, the MCP
configs). Keep it in sync by hand if `baselines/`, `prompts/` or `START-HERE.md` change. Full
repo, for anyone who wants the facilitator material too:
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

Bring a laptop with the AI coding tool you already use (Cursor, Claude Code or Codex). Setup
takes five minutes; do it before the session if you'd like, or we'll help you connect in the
first few minutes of the room. Mobbin access is provided for the day. No coding experience
needed: the screens are plain HTML files that open by double-click, and the AI does the
writing.

Hosted by Andreas Kruszakin (Cursor and Mobbin Ambassador, Netherlands) and Nicolas Chatelain
(Mobbin Ambassador).

---

## Field: Laptop requirements

- A laptop you can install things on, with a browser.
- One AI coding tool installed and signed in: Cursor, Claude Code or Codex. Any of the three
  works; pick the one you already use. Cursor is the easiest if you have none. Optional Cursor
  credits: TODO-CURSOR-CREDITS.
- A Mobbin account, joined through the workshop invite: TODO-MOBBIN-INVITE.
- No Node, no Python, no git, no terminal required.

---

## Field: Setup documentation

## Setup — optional, before you arrive

Five minutes now saves five minutes on the day. If you'd rather not, that's fine: we set up
Cursor and Mobbin MCP together at the start of the session.

- [ ] Install one AI coding tool and sign in: [Cursor](https://cursor.com), [Claude Code](https://claude.com/claude-code) or [Codex](https://openai.com/codex). Cursor if you have none.
- [ ] Join Mobbin through the workshop invite: TODO-MOBBIN-INVITE. Sign in once at [mobbin.com](https://mobbin.com).
- [ ] Get the workshop folder: download it from TODO-KIT-ZIP and unzip it.
- [ ] Open the folder in your AI tool (Cursor: File > Open Folder).
- [ ] Connect Mobbin. In Cursor the folder brings its own config: enable it when asked, or Settings > Tools & MCPs > **Mobbin** > **Connect**, then sign in when the browser opens. Claude Code and Codex steps are in `START-HERE.md` inside the folder.
- [ ] Paste this into your AI tool and wait for three results with links:

`Search Mobbin for "online banking account overview screen", platform web, limit 3. Show me the app name and mobbin_url for each result.`

- [ ] If the first try times out, run it again. The second one works.
- [ ] Double-click `baselines/b-accounts/index.html` in the folder. A bank screen opens in your browser. You are ready.

## In the room

Everything else is in `START-HERE.md` in the folder, including the three prompts you will run.
We reveal three screens and you pick one. Didn't get to the setup above? Arrive five minutes
early, or we'll connect you in the first minutes of the session. Optional Cursor credits if you
need them: TODO-CURSOR-CREDITS.

## Stuck?

Message us on the Hatch Slack before Friday, or come five minutes early. The full guide, with
troubleshooting, is at
[github.com/andreaskruszakin/mobbin-hatch-workshop](https://github.com/andreaskruszakin/mobbin-hatch-workshop).

---

## Field: Pre-assessment (optional, three questions)

1. Which AI coding tool will you bring? Cursor / Claude Code / Codex / other / none yet
2. Have you used an MCP (a tool connection inside an AI assistant) before? Yes / No / Not sure
   what that is
3. Have you used Mobbin before? Regularly / Once or twice / Never

Use: if most answers to question 1 are "none yet", send the Cursor credits link in the reminder
email and budget two extra minutes at the top of the session for Connect.

---

## Field: Materials

Upload `mobbin-hatch-workshop-kit.zip`: zip the `participant-kit/` folder from the repo, not
the whole repo. Nothing else needs uploading: the slides link is shared on the day.

---

## Reminder email, two days before (if the portal sends one)

Subject: Friday's workshop: five minutes of setup, if you want them

Hi, one thing before Friday's "Stop Designing From Vibes" session.

If you'd like to save five minutes on the day, run the setup on the workshop page before you
arrive: one AI coding tool installed, Mobbin joined through the invite link, the workshop
folder downloaded and opened once with Mobbin connected. If you don't get to it, no problem —
we'll set it up together in the room.

If you do not have an AI coding tool yet, install Cursor; the credits link on the page covers
the session. Any questions, reply here or find us on the Hatch Slack.

See you Friday. Andreas and Nicolas
