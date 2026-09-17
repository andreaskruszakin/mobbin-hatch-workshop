# 01 — Read the regions

Goal: know what the screen is made of, and which three parts are worth changing.

Every baseline carries a `data-region` attribute on each section. Open it and view source:

```html
<div class="panel" data-region="accounts-table">
```

Read that decomposition. Do not invent a new one.

---

```
Read the baseline HTML file I have open.

Do not redesign it. Do not give me a critique.

List every element carrying a data-region attribute. For each one, tell me:
- the region name, exactly as written
- what component archetype it currently is (table, link list, banner, form,
  card row, nav bar, and so on)
- what information or decision it carries for the user, in one line
- whether that information is the reason someone opened this screen, or chrome

Rank the regions by how much the user's understanding would change if that
region became a different component — not by how much of the page it covers.
If footer outranks transactions, that's a pixel-area ranking, redo it.

Ignore colour, typography, spacing and "modernising the look" entirely. They
change nothing about what the user can find out or do, so leave them out of
the ranking and out of your answer.

Output as a markdown table. No preamble.
```

---

## Then pick three

Three regions, from the top of the ranking. Write them down before you search for anything.
`docs/SWAP-CARD.md` has the full region list for each baseline with seeded alternatives if you
want a starting point — but a better answer that isn't on the card is a better answer.
