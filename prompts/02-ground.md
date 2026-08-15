# 02 — Ground each decision in something real

Goal: replace "options the model imagined" with "options that shipped".

This is the step that separates this from any other AI prompting session. An AI asked for
alternatives will give you the *average* of alternatives. Mobbin gives you what teams
actually shipped, with a link you can show your stakeholders.

---

```
For each dimension in the table, populate the options column with real, shipped examples
from Mobbin.

Rules for searching:
- One search per dimension. Do not combine two dimensions into one query — the search
  degrades badly when you do.
- Describe the SCREEN you expect to see, in plain language, including the UI elements
  and how they relate. Not keywords. Not adjectives like "modern" or "clean".
- Use platform "web".
- Use limit 4. More results is not better, it just floods your context.
- LOOK AT the returned images. The tool returns almost no metadata — just app name and
  URL — so the actual pattern only exists in the picture. Describe what you see, not
  what the app name suggests.

For every option, record:
- a one-line description of the structural choice
- the app name
- the mobbin_url

If a search returns nothing useful, rephrase once and move on. Do not invent an example
and do not attribute a pattern to an app you did not see.

Output the completed matrix as markdown.
```

---

## Query phrasing that worked in the dry run

Good, returned four distinct patterns each time:

- `signup form showing a step indicator with numbered stages of progress`
- `signup page with customer logos testimonials and security badges alongside the form`
- `form field showing an inline validation error message directly beneath the input`
- `confirmation screen telling the user their application is submitted and under review`
- `onboarding screen asking one single question with large selectable option cards`

Notice the shape: **a subject, the elements on it, and their relationship.** Every one of
those reads like a sentence describing a screenshot.

## Also worth knowing

`search_flows` returns a whole journey, but only as **evenly-spaced stills** — an 18-screen
flow came back as screens 1, 5, 10, 14 and 18. Good for reading the shape of a journey,
useless for motion. There is no animation in the MCP. If you want to see every step, open
the flow's `mobbin_url` in the browser.
