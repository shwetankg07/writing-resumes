# Writing Rules

## Bullets

**Shape:** `<past-tense verb> <what you built> <outcome>`. Include the outcome
only when the number is in `profile.yml`. One line each, two at the very most.

    BAD   Responsible for the payments integration.
    BAD   Helped improve the checkout flow, leading to better performance.
    GOOD  Shipped the checkout flow for a paid launch; 214 transactions
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
| Student / fresher / <2 yrs | Education, Projects, Skills, Experience |
| Working engineer | Experience, Projects, Skills, Education |
| Career switcher | Summary, Projects, Experience, Skills, Education |

Use the standard headings: `Experience`, `Education`, `Projects`, `Skills`.
Parsers look for those exact words, and a creative heading gets the whole
section dropped.

**One page** under about 10 years of experience. Do not run to two.

## ATS rules

The resume is read by a parser before a human sees it. Non-negotiable:

- Single column. A sidebar scrambles the reading order.
- No tables for layout, no text inside images, no icons carrying meaning.
- Dates in the same text flow as the role, never floated in a graphic.
- Real text layer in the PDF. Check it with `pdftotext file.pdf -` if that is
  installed.
- Nothing load-bearing in a header or footer; some parsers drop them.
- Standard fonts. Contact details as plain text, not glyphs.

## Leave out

Photo, age, gender, marital status, full street address (city and country is
enough), skill proficiency bars or self-rated percentages, *References
available on request*, an objective statement (use a two-line summary only when
switching fields), and anything invented to fill space.

## Gaps

For a missing fact, write `[ASK: <specific question>]` into the draft. Be
specific: `[ASK: metrics?]` gets nothing back, while `[ASK: how many users hit
the beta in month one?]` gets an answer. Collect every marker and ask them
together at the end, in one message.
