# writing-resumes

An agent skill for writing resumes that **do not contain invented facts**.

Every resume tool built on an LLM will happily write "improved performance by
40%" about work you never measured. You then have to defend that number in an
interview. This skill is built around one rule — every claim traces to a
profile file you control — and ships a checker that fails the draft when it
doesn't.

## Install

```bash
npx skills add shwetankg07/writing-resumes
```

Works with any agent that reads `SKILL.md` (Claude Code, Codex, Gemini CLI,
Copilot CLI).

## Use

Ask your agent for a resume. It will ask you two things:

1. **Where the facts come from** — an existing `profile.yml`, an interview, or
   pulled from your GitHub and site. All three write the same `profile.yml`, so
   you end up with a reusable file either way.
2. **What to render** — LaTeX (default), HTML→PDF, or Markdown.

Paste a job description and it tailors — by *selecting and reordering* what is
already true, never by adding.

## The checker

```bash
python3 check_facts.py resume.tex profile.yml
```

Fails on any number in the draft that isn't in your profile, and on any
unanswered `[ASK:]` marker. No dependencies, stdlib only. `--self-test` runs
its own tests.

It proves a number exists in your profile, not that it sits in the right claim
— it catches invented magnitudes, which is the failure that actually happens.

## Layout

```
SKILL.md                      the workflow and the iron rule
references/writing-rules.md   bullet craft, section order, ATS rules
references/profile.example.yml the schema
templates/                    resume.tex · resume.html · resume.md
check_facts.py                the guardrail
```

## Rendering

LaTeX needs `tectonic`, `xelatex` or `pdflatex`. Without one, the HTML template
prints via `chromium --headless --print-to-pdf=out.pdf resume.html` and needs
nothing installed.

MIT.
