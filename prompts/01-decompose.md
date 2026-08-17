# 01 — Read the regions

Goal: know what the screen is **made of**, and which three parts are worth changing.

The decomposition is already done. Open your baseline and view source — every section carries
a `data-region` attribute:

```html
<div class="panel" data-region="accounts-table">
```

That is not a formatting detail. It is the screen telling you its own parts. Your job in this
step is not to invent a breakdown, it is to read the one that is there and decide where the
information actually lives.

Takes two minutes, not six. Run this in your AI tool with the baseline file open.

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

Then rank the regions by how much the screen would change if that one region
became a different component. Highest first.

Output as a markdown table. No preamble.
```

---

## What good output looks like

The top of the ranking should be regions holding data or decisions — `accounts-table`,
`transactions`, `upcoming`, `filters`, `hero`, `projects`. The bottom should be chrome —
`footer`, `utility-bar`, `legal`, `shortcuts`.

If the ranking puts `footer` above `transactions`, the model ranked by pixel area. Say so and
re-run: `Rank by how much the user's understanding changes, not by how much of the page moves.`

## What to push back on

Reject anything about colour, typography, spacing or "modernising the look". Those vary the
clothes, not the product. You can restyle every one of these screens and change nothing about
what the user can find out or do — which is exactly the outcome this workshop exists to avoid.

Re-run with: `Those are surface styling choices. Tell me what component each region is and
what else that component could be.`

## Then pick three

Three regions, from the top of the ranking. Write them down before you search for anything.
`docs/SWAP-CARD.md` has the full region list for each baseline with seeded alternatives if you
want a starting point — but a better answer that isn't on the card is a better answer.
