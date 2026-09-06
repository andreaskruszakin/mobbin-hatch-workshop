# Hatch facilitator portal: paste-ready copy

One block per portal field. The setup-documentation field takes markdown with headings,
checklists, links and inline code (the toolbar in the portal), so that block is written in
exactly that subset. Replace the two `TODO` links before publishing; everything else is final.

- `TODO-MOBBIN-INVITE`: the team invite link from Jovan (back Wednesday 9 September)
- `TODO-CURSOR-CREDITS`: the $50 Cursor credits link, Andreas

Live copies of everything linked below: repo
`https://github.com/andreaskruszakin/mobbin-hatch-workshop`, zip
`https://github.com/andreaskruszakin/mobbin-hatch-workshop/archive/refs/heads/main.zip`.

---

## Field: Workshop description

Stop Designing From Vibes: same data, different components, grounded in what actually shipped.

Ask an AI tool to redesign a screen and you get the average of everything it has seen. Nice
type, soft shadows, and the same table underneath doing the same job. In fifty minutes you will
take one dated banking screen, read the parts it is made of, swap three of them for components
real products ship today (found through the Mobbin MCP inside your own AI tool), and regenerate.
You leave with two versions of one screen that could plausibly come from two different
companies, and you can say why you chose each.

Bring a laptop with the AI coding tool you already use (Cursor, Claude Code or Codex). Five
minutes of setup before the session; the steps are on this page. Mobbin access is provided for
the day. No coding experience needed: the screens are plain HTML files that open by
double-click, and the AI does the writing.

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

## Before the session (5 minutes)

Please do this at home, not in the room. The first Mobbin connection is slow and thirty people
doing it at once costs us the hands-on time.

- [ ] Install one AI coding tool and sign in: [Cursor](https://cursor.com), [Claude Code](https://claude.com/claude-code) or [Codex](https://openai.com/codex). Cursor if you have none.
- [ ] Join Mobbin through the workshop invite: TODO-MOBBIN-INVITE. Sign in once at [mobbin.com](https://mobbin.com).
- [ ] Get the workshop folder. Either [download the zip](https://github.com/andreaskruszakin/mobbin-hatch-workshop/archive/refs/heads/main.zip) and unzip it, or clone `https://github.com/andreaskruszakin/mobbin-hatch-workshop.git`.
- [ ] Open the folder in your AI tool (Cursor: File > Open Folder).
- [ ] Connect Mobbin. In Cursor the folder brings its own config: enable it when asked, or Settings > Tools & MCPs > **Mobbin** > **Connect**, then sign in when the browser opens. Claude Code and Codex steps are in `START-HERE.md` inside the folder.
- [ ] Paste this into your AI tool and wait for three results with links:

`Search Mobbin for "online banking account overview screen", platform web, limit 3. Show me the app name and mobbin_url for each result.`

- [ ] If the first try times out, run it again. The second one works.
- [ ] Double-click `baselines/b-accounts/index.html` in the folder. A bank screen opens in your browser. You are ready.

## In the room

Everything else is in `START-HERE.md` in the folder, including the one prompt you will paste.
We reveal three screens and you pick one. Optional Cursor credits if you need them:
TODO-CURSOR-CREDITS.

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

Upload `mobbin-hatch-workshop.zip` (built from `main` with `git archive`; the same bytes as the
GitHub zip link, for people who would rather download from the portal). Nothing else needs
uploading: the slides link is shared on the day and the takeaway is the repo itself.

---

## Reminder email, two days before (if the portal sends one)

Subject: Friday's workshop: five minutes of setup, please

Hi, two things before Friday's "Stop Designing From Vibes" session.

First, please run the setup on the workshop page before you arrive. It takes five minutes: one
AI coding tool installed, Mobbin joined through the invite link, the workshop folder downloaded
and opened once with Mobbin connected. The first Mobbin connection is slow and we would rather
spend our fifty minutes designing than connecting.

Second, if you do not have an AI coding tool yet, install Cursor; the credits link on the page
covers the session. Any questions, reply here or find us on the Hatch Slack.

See you Friday. Andreas and Nicolas
