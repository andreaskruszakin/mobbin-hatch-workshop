# Changelog

## 17-08-2026

- Replaced the invented Meridian account-opening baseline with Nicolas Chatelain's three
  Crédit Mutuel screens: `baselines/a-homepage/`, `baselines/b-accounts/` and
  `baselines/c-transactions/`, one folder each so GitHub Pages serves them directly. Deleted
  `baseline/` and `variants/`. The workshop now starts from a real screen with a real data
  volume — 24 transactions with raw labels — instead of one written to be criticised.
- Translated all three baselines to English (`lang="en"`) while keeping French product names
  as proper nouns (Eurocompte Confort, Livret Bleu, Plan Épargne Logement, Forfait
  International, Caisse locale), the raw transaction labels untouched
  (`PRLV SEPA EDF CLIENTS PART 483992017 ECH 220826`), European number and date formats, every
  `data-region` attribute and each header data contract. Normalising the labels would have
  handed participants the most obvious available win for free.
- Added `docs/SWAP-CARD.md` and deleted `docs/MATRIX.md`. The six-dimension matrix is replaced
  by one question per region — *what component is this, and what else could it be?* — with
  every region of every baseline listed, seeded alternatives, and a `high`/`low` yield rating
  that encodes the teaching moment: swap the regions carrying information, not pixels. This
  fixes the scope failure measured in `docs/DRY-RUN.md`, where grounding six dimensions took
  19–27 minutes against a 22-minute block.
- Added `docs/NICOLAS-CHART.md`, preserving Nicolas's ten-line chart, relevance map and
  calibration rule ("I've seen worse", not "that's a straw man") as credited background, so
  the compression in the swap card can be checked against what it compressed.
- Rewrote `prompts/00-setup.md` through `03-generate.md` around regions and components.
  `01-decompose.md` now reads the `data-region` tags and ranks them instead of deriving a
  decomposition; `02-ground.md` searches one component per swap and carries Nicolas's ten
  pre-verified Mobbin URLs as an offline fallback; `03-generate.md` gains the hard constraints
  that make the result checkable — keep every number, keep the raw labels reachable, keep the
  region names.
- Updated `docs/RUN-OF-SHOW.md` with the confirmed date (Hatch Berlin, 18 September 2026) and
  Nicolas's pick-your-baseline reveal at minutes 16–18, which replaces the four-zone room
  split. Three starting points make the show-and-tell contrast structural rather than
  aesthetic without imposing an artificial constraint.
- Rewrote `README.md` to lead with the three live Pages links and added an
  educational-reconstruction disclaimer — fictional data, unallocated IBANs, no affiliation or
  endorsement — since the repo is public and carries a real bank's name.
- Updated `docs/FOR-NICOLAS.md` and `docs/DRY-RUN.md` so neither argues for a method the repo
  no longer runs, and updated the Notion workshop page to match.

## 15-08-2026

- Published the kit to a public GitHub repo (`andreaskruszakin/mobbin-hatch-workshop`) and
  enabled GitHub Pages from `main`, so Nicolas can click through the baseline and the three
  variants instead of reading HTML source. `README.md` now leads with the live links.
- Rewrote `docs/FOR-NICOLAS.md` as a note addressed to Nicolas directly rather than a draft
  message about him, and removed the private Notion URL, since the repo is public and he
  will read the file himself.

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
