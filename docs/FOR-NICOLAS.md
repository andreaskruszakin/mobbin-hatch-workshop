# Nicolas — where the workshop stands

Written for you after our call, once I'd built the exercise and actually run it end to end.
The short version is that it works, but it needed cutting.

## Your animation question, answered

The MCP does not do motion. `search_flows` returns evenly-spaced stills — an 18-screen
Mercury flow came back as screens 1, 5, 10, 14 and 18. It's good for reading the shape of a
journey and useless for animation. So we shouldn't promise motion exploration in the
description, and if someone asks on the day the honest answer is "open the flow on
mobbin.com".

## The exercise works, but six dimensions was too many

I ran the whole thing myself before asking thirty people to. Same brief, same starting
screen, three different combinations from the matrix — and the three outputs genuinely don't
read as the same product in different clothes. Different structure, different number of
steps, different endings. That was the part I was least confident about, so it's good news.

The bad news is timing. Grounding six dimensions in Mobbin took me well past what anyone can
do in the 22 minutes of hands-on we actually have. So the session grounds **three** —
progress model, input density, post-submit state. Those three change what the user does and
in what order. The other three can be varied without changing the shape of the product,
which means someone could spend eight minutes on them and still hand in a reskin.

The full six-dimension matrix still goes in the takeaway page, so nobody loses the rest.

## One change to the structure we agreed

I'd like the decompose step done together on the projector rather than left to everyone
individually. It's the step where the method actually gets taught, it's the one most likely
to go sideways when people are alone with it, and as a room it takes four minutes instead of
six while giving everyone shared vocabulary for the rest of the session.

Everything else is as we discussed: short tool intro at the start, individual work, a couple
of people showing results, recap page at the end.

## Finance+

There's no dedicated space. The add-on just unlocks finance apps inside normal search —
search Bank of America and it appears instead of being gated. We both went looking for a
separate section and neither of us found one. Worth telling Mobbin that two ambassadors
couldn't find the thing they'd been given.

## What I've built

All in this repo, running and tested:

- The baseline screen participants fork — a deliberately mediocre business bank account
  application. Plain HTML, no install, opens from a file.
- The matrix, with every option linked to the real Mobbin screen it came from.
- Four prompt scaffolds: setup, decompose, ground, generate.
- Three worked variants, for the show-and-tell.
- A minute-by-minute run of show.

One caveat I should be upfront about: I wrote the baseline, so I already knew its structure
when I decomposed it. That's the one step in the kit I haven't tested cold, and it's part of
why I want it facilitated from the front.

## What I need from you

- Mobbin guest accounts — 30, ideally with Finance+ since the brief leans on finance apps
- A promo code for the takeaway page
- Confirmation the slot really is 50 minutes, and that the room has a projector

I'll chase Cursor for participant credits on my side.

## Still open

- Whether the room machine can run the live demo — both browser tools failed on mine, so I'd
  rather we test on the actual machine than find out live
- Whether we put the prerequisites on the registration page before it goes live. The MCP is
  slow on first connect and thirty simultaneous cold starts would cost us five minutes we
  don't have, so I'd like people warmed up before they walk in.
