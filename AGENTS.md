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
- Next run: Designed Minds online, "Research Fast and Design Live with Mobbin MCP", Thursday 8 October 2026, 3:00 to 4:30 PM PT (Friday 9 October, 7:00 KST), 90 minutes (Luma: https://luma.com/tuzxv38k). The room is international and mostly US, so its kit is `kits/amtrak/` (the Amtrak booking home page). It is the dry run for Seoul on Saturday 24 October, which uses `kits/korail/` in the same format. The board is `https://www.figma.com/board/uQdulniCnQzptKeFiGs1Vg` in the Andreas Studio team. The script is `docs/RUN-OF-SHOW-VIRTUAL.md`, and the emails are `docs/EMAILS.md`.
- `kits/*/template/` are scraped copies of amtrak.com/home.html and korail.com/ticket/main and stay out of git because the repo is public. `scripts/build-kit.sh amtrak|korail` rebuilds a template and packs `dist/<name>/kit.zip` (needs Chrome and Node; `--skip-scrape` repacks only). The Amtrak scrape strips the cookie banner, sign-in popup and sticky callout, and removes `loading=lazy` so the offline copy shows its photos. korail.com's results page returns no trains to headless browsers, so that template is the booking home.
- Mobbin promo: code DESIGNEDMINDS gives 3 months of Mobbin Pro (Quarterly plan at checkout). Mention the code whenever Mobbin comes up, but never the redemption count or the expiry.
- Mobbin MCP sometimes answers "Failed to execute search" for a while, even on a query that worked a minute earlier. Wait, retry, or re-authenticate. Keep search queries short; long ones with colons failed more often in testing.
- The organiser is "Designed Minds" (designedminds.co), not "Design Minds". The board uses their system: talk chips `#F849C1`, activity chips `#488CFC`, a black rule under each chip, pastel sections (`#A0C4FF`, `#BDB2FF`, `#FFADAD`, `#FAFAF7`) holding light rounded cards, yellow `#FFC943` part banners, and a cream `#FBF7EF` hero and close. Their illustrations come from the reference board and the site.
- Kit downloads: GitHub releases `designed-minds-2026-10` (Amtrak) and `seoul-2026-10-24` (KORAIL), each with asset `kit.zip`. After a rebuild: `gh release upload designed-minds-2026-10 dist/amtrak/kit.zip --clobber`, same for korail and seoul. Hosts (Luma): Andreas, Eunji Jeong, Dali Kim, Inès. The board has 40 lanes; add rows if signups pass 40. Mobbin MCP needs Pro (the "Upgrade" screen means they don't have it; the code fixes that). The official Cursor route is the Mobbin plugin in the Cursor Marketplace; Claude Desktop's is the connector at claude.ai/directory/mobbin.
- Retro board for Hatch with next-run decisions (Inès, Eunji): `https://www.figma.com/board/2i6YeuzeUkwVCnakkN7i6s`. Designed Minds reference board format: `https://www.figma.com/board/x7z1du240DH08LfJsCx7Pe`.
- Cursor credits are optional. People use the AI tool they already have (Cursor, Claude Desktop, Claude Code, or Codex) plus Mobbin Pro from the DESIGNEDMINDS code.
- No pairing and no green/red check-in on the board or in the emails. Andreas cut them after Inès's board comments; the time went to the Mobbin MCP station.
