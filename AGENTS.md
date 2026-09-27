## Learned User Preferences

- In a live workshop session, run one prompt step at a time so the room can follow.
- The Hatch participant kit lives in `participant-kit/` on `origin/main`, and it is newer than the Hatch portal zip in `~/Downloads`. Don't restore root files from that zip.
- Say "template", never "baseline", in anything a participant reads. Avoid "regions" and "morphological" in the room too.
- In a virtual session the FigJam board is the slides. Don't make participants depend on a shared screen.
- When asked to rerun as a participant, follow the kit 1:1: `prompts/01-decompose.md`, then `02-ground.md`, then `03-generate.md` twice.
- Ground every swap in a Mobbin screen. Do not invent structure.
- Multiple treatments of one baseline belong on one HTML page with a floating bottom picker and `?variant=`, not as three restyled files.
- Keep every number, date, IBAN, raw label, and `data-region` name. Change the component, not the data.
- Redesign around information clarity and visualized amounts, not extra chrome. On baseline B, keep the navy (`#002454`, `#28527f`, `#00337f`) unless asked to leave the brand.
- Use the taste pipeline (ontology first, then morphological variants) when asked to refine past the room exercise.

## Learned Workspace Facts

- Public repo `https://github.com/andreaskruszakin/mobbin-hatch-workshop` is the facilitator kit for "Stop Designing From Vibes" at Hatch Berlin, 18 September 2026, hosted by Andreas Kruszakin and Nicolas Chatelain.
- The participant path is the Hatch kit zip plus `START-HERE.md`. No Node, Python, or server. Each screen is one HTML file; double-click it.
- Three baselines share one fictional French-bank data contract: `baselines/a-homepage` (logged out), `baselines/b-accounts` (logged in, the default), `baselines/c-transactions` (24 raw rows).
- Sections are tagged `data-region`. Generated work lives in `variants/` as self-contained HTML. Screen B's three-way picker is `variants/b-accounts/index.html` (`?variant=mix|due|pots`). Clarity's ontology is `variants/clarity/ontology.js` and `variants/clarity/ontology.html`.
- Mobbin MCP is `https://api.mobbin.com/mcp`, shipped in `.cursor/mcp.json` and `.mcp.json`. Warmup query: "online banking account overview screen", platform web, limit 3. The first call often times out; run it again.
- Use Mobbin `standard` only to wake the connection. Use `deep` for the searches that pick a component.
- Live baselines: `https://andreaskruszakin.github.io/mobbin-hatch-workshop/baselines/<name>/`.
- Workshop deck: `https://www.figma.com/design/CjC0LCU6I7fOERqv9rzQYQ/Mobbin`. Slides are 1920x1080, `#141414`, M Saans headings, Geist Mono body. The Figma MCP sandbox cannot load M Saans and falls back to Inter.
- Next run: Designed Minds virtual, Thursday 8 October 2026, 7:00 KST, 60 minutes, as the dry run for Seoul on Saturday 24 October. The kit is `kit/` (one KORAIL template, `kit/prompts.md` with four steps). The board is `https://www.figma.com/board/uQdulniCnQzptKeFiGs1Vg` in the Andreas Studio team. The script is `docs/RUN-OF-SHOW-VIRTUAL.md`, and the emails are `docs/EMAILS.md`.
- `kit/template/` is a scraped copy of korail.com/ticket/main and stays out of git because the repo is public. Rebuild it and `kit.zip` with `scripts/build-kit.sh` (needs Chrome and Node). korail.com's results page (`/ticket/search/list`) returns no trains to headless browsers, so the template is the booking home.
- The organiser is "Designed Minds" (designedminds.co), not "Design Minds". The board uses their system: talk chips `#F849C1`, activity chips `#488CFC`, a black rule under each chip, pastel sections (`#A0C4FF`, `#BDB2FF`, `#FFADAD`, `#FAFAF7`) holding light rounded cards, yellow `#FFC943` part banners, and a cream `#FBF7EF` hero and close. Their illustrations come from the reference board and the site.
- Retro board for Hatch with next-run decisions (Inès, Eunji): `https://www.figma.com/board/2i6YeuzeUkwVCnakkN7i6s`. Designed Minds reference board format: `https://www.figma.com/board/x7z1du240DH08LfJsCx7Pe`.
- Cursor credits are optional. People use the AI tool they already have (Cursor, Claude Code, or Codex) plus a Mobbin account from the workshop invite.
