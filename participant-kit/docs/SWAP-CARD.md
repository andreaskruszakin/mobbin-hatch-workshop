# The Swap Card

Every baseline is already broken into named parts. Open any of the three screens, view source,
and you will find `data-region` on each section:

```html
<div class="panel" data-region="accounts-table">
```

That is the decomposition. You do not have to derive it, argue about it, or learn a vocabulary
for it — the parts are named inside the artefact.

Which leaves exactly one question, asked once per region:

> **What component is this, and what else could it be?**

Answer it three times, search Mobbin for each answer, regenerate. That's the exercise.

---

## How to use this in the session

1. Open your baseline and find its table below.
2. Pick **three** regions. Not six, not all of them. Three.
3. For each one, write a different component in the empty column. The seeded archetypes are
   there to unstick you, not to be chosen from — a better answer that isn't listed is a
   better answer.
4. Search Mobbin for that component, one search per swap. `prompts/02-ground.md` has the
   query shapes that work.
5. Regenerate with `prompts/03-generate.md`. Same data, same region names, new components.
6. Diff the region names before and after. They should match. If a region vanished, you
   deleted information rather than redesigning it.

---

## The part that decides whether this works

**Pick the regions carrying the most information, not the most pixels.**

Every table below has a **Yield** column. `high` regions carry data, decisions or the reason
the user opened the screen at all — change one and the product changes. `low` regions are
chrome. They are usually the easiest and most satisfying to redesign, which is precisely the
trap.

Anyone who swaps `shortcuts`, `footer` and `utility-bar` will produce something that looks
new and is identical. That is the failure this workshop exists to name, and it is worth
saying out loud before anyone starts rather than after.

---

## Baseline A — Public homepage

`baselines/a-homepage/` · logged out · 15 regions

The problem here is accumulation, not ugliness. Six audience segments before any content,
fourteen stacked sections, a sourced footnote on every claim. The swaps that bite are the
ones that decide **what a stranger sees first** and **how much they have to wade through**.

| Region | What it is now | Yield | What else could this be | Your swap |
| --- | --- | --- | --- | --- |
| `utility-bar` | Six audience segments, always visible | high | One-time audience question · inferred and dismissible · a switcher folded into the header · dropped, with segments merged into content | |
| `header` | Five nav links plus two pill CTAs | med | Mega-menu with previews · search-first command bar · compact sticky bar with one CTA · task-led nav ("I want to…") | |
| `alert` | Permanent red fraud banner | med | Dismissible with memory · a card in a notices feed · interstitial reserved for high severity · a linked status page | |
| `cookie-consent` | Full card in the content flow | med | Bottom-docked two-button bar · settings-first modal · granular toggles inline · essential-only default with a footer link | |
| `hero` | Headline, paragraph, one CTA, decorative art | high | Task-first entry point · search as the hero · editorial feature card · a rotating set of three entry points | |
| `promo-welcome` | Offer block with a footnote | high | Merged with the other promos into one rail · a comparison card · a slim dismissible offer strip · moved into the product pages it applies to | |
| `proof` | Three claims, two with sources | high | Stat row with the numbers as the visual · testimonial cards · one ratio with a source drawer · awards and ratings grid | |
| `offers` | Long copy, bullets, footnote | high | Product card grid · comparison table · configurator or quiz · accordion of details behind a summary | |
| `promo-award` | Award claim plus source | low | Folded into `proof` · a badge strip · a single line in the footer · a press page link | |
| `promo-homji` | Partner product block, two CTAs | med | A card inside `offers` · a guided flow entry · a dedicated page linked from `projects` · removed from the homepage entirely | |
| `projects` | Six plain links in a three-column list | high | Goal chips that filter the page · card grid with imagery · a short quiz that routes you · a search-driven list | |
| `app` | Bullets, two rating badges, a link | med | App-store style block with screenshots · QR download panel · feature carousel · a rating strip only | |
| `missions` | One mission visible, four behind a slider | low | Accordion · numbered editorial list · one line linking to a full page · cut from the homepage | |
| `advice` | Three article cards | med | Topic-filtered feed · featured article plus list · reading-time-led list · personalised by segment | |
| `footer` | Four groups, 23 links, plus an 8-link legal row | low | Collapsed accordion sections · compact footer plus a sitemap page · search-first footer · grouped by task rather than by department | |

---

## Baseline B — Accounts overview

`baselines/b-accounts/` · logged in · 13 regions

This is the screen most people should take. It has real data volume, a genuine decision on it
("am I OK?"), and the widest gap between what it is and what Mobbin's library shows.

| Region | What it is now | Yield | What else could this be | Your swap |
| --- | --- | --- | --- | --- |
| `account-summary` | One total with a disclaimer and a footnote | high | Balance and available split · net worth with a trend sparkline · a safe-to-spend figure · the total plus what changed since last login | |
| `accounts-table` | Four-column HTML table, three rows | high | Card stack · list rows with sparklines · grouped by purpose (spending, saving, borrowing) · a single net figure with drill-down · a swipeable account carousel | |
| `transactions` | Five-column table, eight raw labels | high | Grouped by day with day subtotals · merchant-enriched with logos and categories · search-first · a running-balance feed · a spending timeline | |
| `cards` | Two rows with a CSS chip and limit text | high | Visual card carousel with controls on the card · list rows with inline toggles · a limits-first view · a card detail sheet | |
| `upcoming` | A one-row table | high | A timeline of the next 30 days · a calendar strip · a plain sentence ("894,17 leaves on 5 September, 1 524,45 left after") · a cashflow chart to month end | |
| `nav` | Nine top-level tabs | med | Command palette · five tabs with the rest under "More" · contextual nav per account · a persistent left rail with icons | |
| `side-nav` | Three grouped link lists | med | Merged into `nav` · a contextual panel that changes with selection · removed, actions attached to the objects they act on | |
| `alert` | Static yellow security notice | med | Dismissible with memory · a message-centre badge · a contextual tip at the risky action only · a security score card | |
| `shortcuts` | Four grey buttons in a panel | low | A floating action button · a command palette · actions attached to each account row · removed | |
| `legal` | Two footnotes plus a disclaimer | low | An info popover on the figure it qualifies · an expandable disclosure · a linked terms page | |
| `utility-bar` | Five links on a navy strip | low | Folded into an account menu · removed, links moved to the footer | |
| `header` | Wordmark plus who-am-I block | low | Avatar menu · a greeting with last-login as a security cue · a compact sticky bar | |
| `footer` | Seven links plus a company line | low | Compact single line · accordion · removed from the logged-in area | |

---

## Baseline C — Transaction statement

`baselines/c-transactions/` · logged in · 11 regions

Twenty-four rows with labels like `PRLV SEPA EDF CLIENTS PART 483992017 ECH 220826`. There is
no category, no merchant name, no icon and no grouping — deliberately. Normalising those
labels is the most obvious win on this screen, which makes it a good warm-up and a bad place
to stop.

| Region | What it is now | Yield | What else could this be | Your swap |
| --- | --- | --- | --- | --- |
| `transactions` | 24-row table, raw labels, alternating stripes | high | Grouped by day, merchant or category · enriched rows with logos and clean names · a running-balance timeline · rows that expand into detail · a chart above a filtered list | |
| `filters` | Six inputs and a select in a panel | high | Search-first with filter chips · segmented control plus a date-range picker · saved and suggested filters · natural-language search ("groceries in July") · a facet sidebar that updates live | |
| `account-identity` | Two-column text block with balances | high | A summary header with a balance chart · a sticky compact bar on scroll · an account card with tabs across accounts · opening and closing balances as the anchors of the list | |
| `pagination` | "1 to 24 of 24" plus Previous/Next | med | Infinite scroll · load-more · a virtualised list · month tabs · a scrollbar annotated with dates | |
| `export` | Four format links plus print | med | One download menu · a share sheet · scheduled statements by email · a connect/API option for accounting tools | |
| `nav` | Nine top-level tabs | med | See baseline B | |
| `side-nav` | Three grouped link lists, account switcher inside | med | An account switcher in the header · a segmented control above the list · a contextual panel | |
| `legal` | Two footnotes plus a disclaimer | low | Popover on the figure it qualifies · expandable disclosure · linked terms page | |
| `utility-bar` | Five links on a navy strip | low | See baseline B | |
| `header` | Wordmark plus who-am-I block | low | See baseline B | |
| `footer` | Seven links plus a company line | low | See baseline B | |

---

## Why this is still morphological analysis

It decomposes a problem into independent parts, enumerates real options for each part, and
recombines them deliberately instead of defaulting to the first idea. That is the method,
unchanged.

What it drops is the vocabulary. Nobody has to be taught what a "dimension" is when the parts
are named in the file, and "what component is this, what else could it be" is how designers
already talk. It also maps one-to-one onto how Mobbin search works: you search a component
and get shipped examples, with no translation layer between the exercise and the tool.

A longer, ten-line version of this exists on the facilitator side — each line with a column of
options, plus a map of which lines are alive on which baseline. Good thinking, and the right
tool if you have half a day. It does not fit fifty minutes, which is why it isn't here.
