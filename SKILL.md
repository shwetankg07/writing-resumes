---
name: writing-resumes
description: Use when writing, rewriting, reviewing, or tailoring a resume or CV, when targeting one at a specific job description, or when asked about ATS compatibility, resume bullet points, or turning a profile into a PDF resume.
---

# Writing Resumes

Turn verified facts into a targeted, ATS-parseable resume. The document must
contain nothing the person did not actually do.

## The Iron Rule

**Every number, title, employer, date and claim must trace to `profile.yml`.**
Not in the profile, not in the resume.

When a fact is missing, write a visible marker instead of filling the gap:

    [ASK: metric for the checkout rewrite - % faster, or users affected?]

Markers are cheap. Fabrication is not — the person has to defend every line of
this document in an interview, under questioning, without you there.

### Rationalizations — every one of these means STOP

| Excuse | Reality |
|---|---|
| "They obviously did X, it's implied" | Implied is not stated. Emit `[ASK:]`. |
| "A placeholder number shows them the format" | Placeholders get shipped. Emit `[ASK:]`. |
| "I'll hedge it: 'helped improve performance'" | A vague invented claim is still invented. |
| "JD wants Kubernetes, they have Docker — close enough" | Adjacent is not the same. This fails at the interview. |
| "I'll align their title with the JD's title" | Retitling is falsifying employment history. |
| "It looks weak without a metric" | A weak true resume beats a strong false one. |
| "The user said make it impressive" | They meant from their real work. Ask for the missing number. |

Tailoring **selects and reorders** existing facts. It never adds one.

## Workflow

1. **Ask two questions**, both in one message:
   - Facts source — existing `profile.yml` · interview · pull from GitHub/site
   - Output — **LaTeX (default)** · HTML→PDF · Markdown
2. **Build `profile.yml`.** All three sources write the same file; interview and
   auto-pull are populators, not separate paths. Schema:
   `references/profile.example.yml`. Auto-pull records only what the repos and
   site actually prove — everything else becomes `[ASK:]`.
3. **Ask for the target job description** (optional). With one, select and order
   facts against it. Without one, write the general version.
4. **Write the content.** Read `references/writing-rules.md` first — before the
   first bullet, not after.
5. **Render** with the chosen template from `templates/`. For LaTeX try
   `tectonic`, `xelatex`, `pdflatex` in that order. If no engine exists, say so
   and offer the HTML path (`chromium --headless --print-to-pdf`). Never
   silently switch format.
6. **Verify.** `python3 check_facts.py <rendered-file> profile.yml`
   It fails on numbers absent from the profile and on leftover `[ASK:]`.
   A failing check is not done: fix it, or ask the person for the fact.

## Red flags — stop and re-read the Iron Rule

- About to write a percentage you did not read in `profile.yml`
- Rewording a JD requirement into an accomplishment
- Deleting an `[ASK:]` marker without an answer to put there
- The bullet reads better than the fact it came from
