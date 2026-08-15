# Mobbin x Hatch — Workshop Lab

Facilitator kit and dry-run record for **"Stop Designing From Vibes"**, a 50-minute
hands-on workshop at Hatch. Andreas Kruszakin + Nicolas Chatelain.

Participants take one mediocre finance screen, break it into design decisions with
morphological analysis, ground each decision in real shipped patterns via the Mobbin
MCP, and generate structurally different interfaces from one brief.

## See it

One brief, one starting screen, three combinations from the matrix:

- [The baseline](https://andreaskruszakin.github.io/mobbin-hatch-workshop/baseline/) — the as-is screen everyone forks
- [Variant A — Gauntlet](https://andreaskruszakin.github.io/mobbin-hatch-workshop/variants/a/) — eligibility gate first, one question per screen, ends in a status timeline
- [Variant B — Dossier](https://andreaskruszakin.github.io/mobbin-hatch-workshop/variants/b/) — login first, sectioned, the wait turned into setup work
- [Variant C — Conversation](https://andreaskruszakin.github.io/mobbin-hatch-workshop/variants/c/) — four card questions, ends in a recommendation rather than an account

## Run it locally

No install, no build step. Everything is plain HTML and CSS.

```bash
python3 -m http.server 3160
```

Then open `http://localhost:3160/baseline/`.

## What's here

| Path | What it is |
| --- | --- |
| `baseline/` | The deliberately mediocre account-opening screen participants fork |
| `docs/MATRIX.md` | The morphological matrix — 6 dimensions, 5 options each, every option cited to a Mobbin screen |
| `docs/DRY-RUN.md` | Measured timings, MCP failure modes, and what got cut to fit the slot |
| `docs/RUN-OF-SHOW.md` | Minute-by-minute facilitation script |
| `prompts/` | Copy-paste prompt scaffolds that force Mobbin grounding and citation |
| `variants/` | Three generated outcomes from the same brief, different matrix rows |

## Prerequisites we ask of participants

A laptop, an AI coding tool they already use, and the Mobbin MCP connected **before**
the session starts. Mobbin licences are provided. See `docs/RUN-OF-SHOW.md` for the
pre-warm instructions — the MCP cold start is slow and should not happen in the room.
