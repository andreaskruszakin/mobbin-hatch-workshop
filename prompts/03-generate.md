# 03 — Generate, twice

Goal: two outputs from one brief that are structurally different, not two skins.

Pick your combination first, on paper, before the model sees anything. If you let the
model choose, it will choose the average.

---

```
Build a single self-contained HTML file at variants/mine-1/index.html.

Same product as baseline/index.html: opening a business bank account. Same information
must eventually be collected. Everything about HOW is determined by the combination below.

COMBINATION
- Commitment ramp: <your option, e.g. 1B — eligibility filter before any account exists>
- Progress model: <e.g. 2C — full-width bar with the current section named>
- Input density: <e.g. 3C — one question per screen>
- Trust: <e.g. 4F — reassuring microcopy attached to the ask itself>
- Validation: <e.g. 5B — inline under the field, on blur>
- Post-submit: <e.g. 6B — status timeline with dates>

GROUNDING
For each choice above, re-read the Mobbin screen I cited for it and follow its structural
logic — the ordering, the density, what is on screen at once, what is deliberately absent.
Do not copy its colours, brand or copy.

CONSTRAINTS
- Plain HTML and CSS in one file. No frameworks, no build step, no external requests.
- Vanilla JS only where the structure genuinely requires it (step navigation, validation).
- It must run by opening the file. Assume no npm install.
- Animate transform and opacity only. Respect prefers-reduced-motion.

At the top of the file, put an HTML comment listing the combination and the mobbin_urls
you followed, so the choices are traceable.
```

---

Now change **two** dimensions and generate `variants/mine-2/index.html`.

Change them where it hurts: a progress model plus an input density, not two flavours of
trust badge. If your two outputs still feel like siblings, the combination wasn't doing
the work — the model fell back to its defaults and you let it.

## The check that matters

Put them side by side and answer: **could these have been made by two different companies?**

If yes, the method worked. If no, say out loud which dimension you failed to actually vary.
That answer is the takeaway, more than the artefact is.
