# Writing Rules

## Bullets

**Shape:** `<past-tense verb> <what you built> <outcome>` — outcome only if the
number is in `profile.yml`. One line each; two is the hard ceiling.

    BAD   Responsible for the payments integration.
    BAD   Helped improve the checkout flow, leading to better performance.
    GOOD  Shipped Cashfree checkout for a live paid event; 214 transactions
          cleared in the first weekend.
    GOOD  Cut cold-start latency by moving the OSM graph load off the request
          path.                              <- true, specific, no fake metric

Cut on sight: *responsible for*, *helped with*, *worked on*, *assisted*,
*various*, *utilized*, *leveraged*, *spearheaded*, *passionate*, *team player*,
*results-driven*.

- Lead with the outcome, not the task.
- No first-person pronouns. Drop leading articles.
- Past tense for past roles, present tense for the current one.
- Verbs that mean something: *built, shipped, cut, migrated, merged, automated,
  designed, debugged, replaced*. Not *managed, handled, supported*.
- A bullet without a metric is fine. A bullet with a fake one is not.

## Sections

Order by what is strongest, not by convention:

| Situation | Order |
|---|---|
| Student / fresher / <2 yrs | Education → Projects → Skills → Experience |
| Working engineer | Experience → Projects → Skills → Education |
| Career switcher | Summary → Projects → Experience → Skills → Education |

Use the standard headings — `Experience`, `Education`, `Projects`, `Skills`.
Parsers key off them; a clever heading is a dropped section.

**One page** under ~10 years of experience. No exceptions worth taking.

## ATS rules

The resume is read by a parser before a human sees it. Non-negotiable:

- Single column. A sidebar scrambles reading order.
- No tables for layout, no text inside images, no icons carrying meaning.
- Dates in the same text flow as the role, never floated in a graphic.
- Real text layer in the PDF — verify with `pdftotext file.pdf -` if available.
- Nothing load-bearing in a header or footer; some parsers drop them.
- Standard fonts. Contact details as plain text, not glyphs.

## Leave out

Photo, age, gender, marital status, full street address (city + country is
enough), skill proficiency bars or self-rated percentages, *References
available on request*, an objective statement (a two-line summary only when
switching fields), and anything you had to invent to fill space.

## Gaps

Missing fact → `[ASK: <specific question>]` in the draft. Specific: not
`[ASK: metrics?]` but `[ASK: how many users hit the beta in month one?]`.
Collect every marker and ask them together at the end, in one message.
