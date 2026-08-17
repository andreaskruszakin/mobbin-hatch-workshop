# 02 — Ground each swap in something real

Goal: replace "a component the model imagined" with "a component that shipped".

This is the step that separates this from any other AI prompting session. An AI asked for
alternatives gives you the *average* of alternatives. Mobbin gives you what teams actually
shipped, with a link you can put in front of a stakeholder.

One search per swap. Three swaps, three searches. That's the whole step.

---

```
For each of my three region swaps below, find real, shipped examples on Mobbin.

SWAPS
- <region name>: <component it is now> -> <component I want it to be>
- <region name>: <component it is now> -> <component I want it to be>
- <region name>: <component it is now> -> <component I want it to be>

Rules for searching:
- One search per swap. Do not combine two swaps into one query — the search
  degrades badly when you do.
- Search for the component you want, not the region name and not the industry.
  "transactions" is a region; "transaction list grouped by day with merchant
  logos" is a component.
- Describe the SCREEN you expect to see, in plain language, including the UI
  elements and how they relate. Not keywords. Not adjectives like "modern".
- Use platform "web". Use limit 4. More results just floods your context.
- LOOK AT the returned images. The tool returns almost no metadata — app name
  and URL only — so the pattern exists only in the picture. Describe what you
  see, not what the app name suggests.

For each swap, record:
- the structural logic of the pattern in one or two lines: what is on screen at
  once, in what order, and what is deliberately absent
- the app name
- the mobbin_url

If a search returns nothing useful, rephrase once and move on. Do not invent an
example and do not attribute a pattern to an app you did not see.

Output as markdown.
```

---

## Query phrasing that works

Good, returned four distinct patterns each time in the dry run:

- `account list showing balances as cards with a trend line on each`
- `transaction list grouped by date with merchant logos and category labels`
- `search bar with filter chips above a list of results`
- `dashboard showing a single large balance figure with a breakdown below it`
- `upcoming payments shown on a timeline with dates and amounts`

Notice the shape: **a subject, the elements on it, and their relationship.** Every one reads
like a sentence describing a screenshot. Keyword lists and adjectives return mush.

---

## Pre-verified references — the offline fallback

From Nicolas, checked on 16 August 2026. Use these if the MCP times out on the day, or as a
starting point before you search for yourself.

**Baseline B, accounts overview**

- [Monarch](https://mobbin.com/screens/d0887146-3b11-4d63-9bc7-3121dedfba10)
- [Rocket Money](https://mobbin.com/screens/f075dbe0-f75d-4955-9fbb-bca17ef8bb3d)
- [Wise](https://mobbin.com/screens/d104a8bc-bc31-484d-80e8-2c9a2cb1e796)
- [Mercury](https://mobbin.com/screens/d83e2ef6-913d-4ffb-a91d-06568a3d769b)
- [Quicken](https://mobbin.com/screens/926c2d9a-2b7a-40a3-91f0-601109b3bfa9)

**Baseline C, account detail and transactions**

- [Wise, transaction details](https://mobbin.com/screens/cdebb2c8-108a-4a6c-9436-98b9725a15b9)
- [Origin](https://mobbin.com/screens/a6bd5cdc-2251-4231-9cd4-c459aa708dfa)
- [Monarch](https://mobbin.com/screens/e75d351a-b5cc-42e5-a134-79688e30f988)
- [Navan](https://mobbin.com/screens/a8b61ff1-277c-4822-b4f1-0703e10ce2b0)
- [Mercury](https://mobbin.com/screens/aecbbd98-e6f9-4624-8ed4-a173e287cb62)

**Baseline A, homepage** — no pre-verified set. Run
`bank marketing homepage with product discovery and account opening`, platform web.

---

## The absence is the point

Searching Mobbin for `Crédit Mutuel online banking account screen` on 16 August returned no
Crédit Mutuel screens at all. It returned Wise, Mercury, Square and Monarch.

That is not a gap in the library. The "before" comes from a bank Mobbin does not index; the
"after" comes from patterns it does. The distance between the two is the entire demonstration.

## Also worth knowing

`search_flows` returns a whole journey, but only as **evenly-spaced stills** — an 18-screen
flow came back as screens 1, 5, 10, 14 and 18. Good for reading the shape of a journey, useless
for motion. There is no animation anywhere in the MCP. To see every step, open the flow's
`mobbin_url` in a browser.

`deep` mode is genuinely better and costs about 20 seconds a call. Use `standard` while
exploring and `deep` for the one search that matters most.
