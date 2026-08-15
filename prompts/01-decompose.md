# 01 — Decompose

Goal: turn one screen into a list of **decisions**, not a list of complaints.

Anyone can say "this form is ugly". Morphological analysis forces you to say *which
independent choices produced it*, and that is the thing you can then vary.

Open `baseline/index.html` in your AI tool and run this.

---

```
Read baseline/index.html.

This is a business bank account application. Do not redesign it and do not give me
a critique.

Instead, decompose it into the independent DESIGN DECISIONS it embodies. A design
decision is a choice that could have been made differently without changing what the
product does. "Uses a blue button" is not one. "Reveals errors only after submit" is.

For each decision give me:
- the dimension (the question being answered)
- the option this screen picked
- two or three other options that exist in the world

Aim for 6 to 8 dimensions. They must be independent — if changing one forces a change
in another, you have merged two dimensions and need to split them.

Output as a markdown table. No preamble.
```

---

## What good output looks like

Dimensions that are genuinely orthogonal: commitment ramp, progress model, input density,
trust placement, validation timing, post-submit state.

## What to push back on

If the model gives you "colour scheme", "typography" or "spacing", reject them. Those are
styling, not structure, and varying them only produces the same product in different
clothes. That is exactly the slop we are trying to avoid.

Re-run with: `Those are surface styling choices. Give me structural decisions only —
things that change what the user does, in what order, and what they know when.`
