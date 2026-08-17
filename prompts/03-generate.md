# 03 — Generate, twice

Goal: two outputs from one screen that are structurally different, not two skins.

Pick your three swaps on paper first, before the model sees anything. If you let the model
choose, it will choose the average.

---

```
Build a single self-contained HTML file at variants/mine-1/index.html.

Start from the baseline file I have open. Read its header comment: it states
which parts are data and which parts are the visual system.

SWAPS
- <region name>: <component now> -> <component instead>
- <region name>: <component now> -> <component instead>
- <region name>: <component now> -> <component instead>

Leave every other region as the same component archetype. Restyling them to fit
is fine; turning them into something else is not. Three swaps, not eight.

HARD CONSTRAINTS — these are what make the result checkable
- Keep every number, date, amount, account name, IBAN and balance exactly as it
  is. Do not round, recalculate, invent or drop a single one.
- Keep the raw transaction labels. If you enrich them with a clean merchant name
  or a category, the original string must still be reachable — on the row, in a
  detail view, on hover. It is the underlying data and it does not go away.
- Keep every data-region attribute, with the same names, on whatever element
  now plays that role. Same names before and after is how we verify this.
- Everything else — layout, hierarchy, typography, colour, density, grouping,
  interaction model — is yours to replace. Do not preserve the visual system.

GROUNDING
For each swap, re-read the Mobbin screen I cited and follow its structural logic:
the ordering, the density, what is on screen at once, what is deliberately
absent. Do not copy its colours, its brand or its copy.

TECHNICAL
- Plain HTML and CSS in one file. No frameworks, no build step, no external
  requests, no external images.
- Vanilla JS only where the structure genuinely requires it.
- It must run by opening the file. Assume no npm install.
- Animate transform and opacity only. Respect prefers-reduced-motion.

At the top of the file, put an HTML comment listing the three swaps and the
mobbin_urls you followed, so the choices stay traceable.
```

---

Now change **two** of the three swaps and generate `variants/mine-2/index.html`.

Change them where it hurts. Two different treatments of the same table are not two swaps.
Swapping `transactions` and `upcoming` changes what the user understands about their money;
swapping `footer` and `utility-bar` changes nothing and takes just as long.

---

## The check that matters

Two questions, in this order.

**1. Is the data intact?** Diff the numbers. Same balances, same 24 transactions, same IBANs,
same dates. Then diff the region names — if one disappeared, you deleted information rather
than redesigning it, and the output is disqualified no matter how good it looks.

**2. Could these have been made by two different companies?** Put both variants side by side.
If yes, the method worked. If no, name out loud which swap you failed to actually make.

That second answer is the takeaway, more than either artefact is.

## The failure to watch for

The most common bad output is a beautiful reskin: new typeface, generous spacing, soft
shadows, and the same four-column table underneath doing the same job in the same order. It
will look enormously better than the baseline and it will have changed nothing.

Check it against the region ranking from step 01. If your three swaps all came from the bottom
of that list, you made a theme, not a redesign.
