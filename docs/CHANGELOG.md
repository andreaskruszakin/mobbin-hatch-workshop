# Changelog

## 15-08-2026

- Created the facilitator kit for the Mobbin x Hatch Workshop Lab. New project at
  `mobbin-hatch-workshop/`, served statically on port 3160 via `python3 -m http.server`
  with no build step, so participants with no local environment can still take part.
- Added `baseline/index.html`, a deliberately mediocre business bank account application
  (25 fields on one page, submit-time error summary, boilerplate trust signals). Gives all
  thirty participants an identical, licence-safe starting point instead of each scraping a
  live bank site, which would have burned the hands-on block on auth walls and cookie
  banners.
- Added `docs/MATRIX.md` — six morphological dimensions plus a bonus KYC dimension, each
  with five to six options cited to a real Mobbin screen URL. Makes every design choice in
  the workshop defendable with a link rather than a feeling.
- Added `prompts/00-setup.md`, `01-decompose.md`, `02-ground.md`, `03-generate.md`. The
  grounding prompt forbids inferring patterns from app names, which addresses the fact that
  `search_screens` returns only `app_name`, `platform` and `mobbin_url` — all real
  information lives in the image, so a skimming model invents patterns confidently.
- Added `variants/a`, `variants/b`, `variants/c` — three self-contained HTML outputs from the
  same brief using different matrix rows (Gauntlet, Dossier, Conversation). Verified via
  headless Chrome that all three render and their JS executes. Proves the matrix drives
  structural divergence rather than restyling, which was the core untested assumption.
- Added `docs/DRY-RUN.md` recording measured timings (90s for six `standard` searches, 20s
  for one `deep` search, ~50s per generated variant) and five failure modes hit, including a
  Mobbin MCP cold-start timeout on the first call. Drove two design changes: cut the exercise
  from six dimensions to three, and move the decompose step to facilitated projector work.
- Added `docs/RUN-OF-SHOW.md` with a minute-by-minute 50-minute script holding presentation
  to the agreed 30% cap, plus a four-zone room split that forces structural contrast in the
  show-and-tell.
- Added `docs/FOR-NICOLAS.md`, a paste-ready co-facilitator summary, and published the
  workshop page to Notion at https://app.notion.com/p/3bd5f205f61381c2b36af6f32d8d515f
  covering landing copy, run of show, prerequisites, open dependencies and owners.
- Answered two open questions from the 7 Aug call: `search_flows` returns evenly-spaced
  stills and never motion (an 18-screen flow returned screens 1, 5, 10, 14, 18), and Finance+
  is not a dedicated space but unlocked apps inside normal search.
