# The Ten-Line Chart — background

**By Nicolas Chatelain.** Preserved here because the swap card in `docs/SWAP-CARD.md` is a
compression of it, and a compression is easier to trust when you can see what was compressed.

The chart is the fuller instrument: ten lines a screen can be varied along, each with a column
of options, with the baseline deliberately sitting in column A of every line. Every pick a
participant makes then becomes a measurable distance from a fixed origin rather than a
preference.

We are not running it on 18 September. Ten lines does not fit fifty minutes — the dry run in
`docs/DRY-RUN.md` measured six dimensions at 19–27 minutes of human time against a 22-minute
block, and ten is worse. The swap card keeps the mechanism and drops the vocabulary. If you
have half a day rather than an hour, use this instead.

---

## The ten lines

1. **Entry point** — how the user arrives and what greets them
2. **Info density** — how much is on screen at once
3. **Primary input** — the main thing the user does here
4. **Navigation** — how they move between places
5. **Data viz** — whether numbers are shown as numbers or as shapes
6. **Trust signal** — what makes this feel safe or official
7. **Feedback** — how the system tells the user what happened
8. **Motion** — what moves, and why
9. **Copy** — register, length and who it is written for
10. **Personalisation** — how much the screen knows about this particular person

The per-line option columns live in Nicolas's own chart and were not part of the baselines
handover. They are not reproduced here rather than guessed at.

---

## Relevance map

Not every line is alive on every baseline. A participant who picks a dead line burns minutes
they do not have, in a format capped at fifty.

| # | Line | A — homepage | B — accounts | C — transactions |
| --- | --- | --- | --- | --- |
| 1 | Entry point | live | live | weak |
| 2 | Info density | live | live | live |
| 3 | Primary input | weak | live | live |
| 4 | Navigation | live | live | live |
| 5 | Data viz | dead | live | live |
| 6 | Trust signal | live | live | weak |
| 7 | Feedback | dead | live | live |
| 8 | Motion | live | live | live |
| 9 | Copy | live | live | live |
| 10 | Personalisation | live | live | weak |

Read down the columns and baseline B is the only screen with ten live lines. That is why it is
the recommended default when someone cannot decide at the reveal.

---

## The calibration rule

> A senior designer must be able to say **"I've seen worse"**, not **"that's a straw man"**.

An obviously catastrophic baseline ruins the demonstration. Any AI output would beat it,
including AI without Mobbin — and that is precisely the comparison the workshop needs to win.

This is the sharpest thing in the handover and it is the reason baseline A ships as it does.
The real Crédit Mutuel homepage was recently refreshed and is not ugly. It sits in column A by
**accumulation**, not by ugliness: six audience segments before any content, fourteen stacked
sections, a sourced footnote on every claim, a blocking consent card, zero personalisation.
Say that from the front, or the room will contest the premise and be right to.

Baselines B and C carry the genuine visual lag. That is where the gap against Mobbin's library
is widest.

---

## Two constraints that look like bugs

**Twenty-four transactions, not three.** Without real volume, the Info density and Data viz
lines have nothing to bite on. This is the constraint most easily lost when someone trims a
file for size.

**B and C are non-responsive on purpose.** Both are fixed at 980px and overflow on mobile.
That is a column-A trait, not an oversight. Making them responsive would hand participants one
of the most obvious available wins for free. Baseline A is fluid, because the real homepage is.

---

## Still open, from Nicolas's list

- Reconcile B and C against real Espace client captures. Both were built from the French
  banking idiom rather than from screenshots. They stand up alone; a calibration pass would
  make them bite harder.
- Zip the three files for the pre-workshop email. On the day participants open, they do not
  download — that removes the risk of thirty people hitting venue wifi at once.
- Timed dry run on baseline B. Target: one full loop under seven minutes.
- **The gap test.** Same baseline, same prompt, run twice: once with the Mobbin URLs and once
  without. If the outputs look alike, the references are not pulling their weight. This is the
  one that decides whether the workshop's core claim holds, and it is worth doing before the
  slides are finished rather than after.
