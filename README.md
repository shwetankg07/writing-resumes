# writing-resumes

An agent skill for writing resumes that contain no invented facts.

Every resume tool built on an LLM will happily write "improved performance by
40%" about work you never measured. You are the one who has to defend that
number in an interview. This skill works from a single rule, that every claim
traces back to a profile file you control, and it ships a checker that fails
the draft when one doesn't.

## Install

```bash
npx skills add shwetankg07/writing-resumes
```

Works with any agent that reads `SKILL.md`: Claude Code, Codex, Gemini CLI,
Copilot CLI.

## Use

Ask your agent for a resume. It will ask you two things:

1. Where the facts come from: an existing `profile.yml`, an interview, your
   GitHub and site, or the agent's own memory of you. They all write the same
   `profile.yml`, so you end up with a reusable file either way. Anything drawn
   from memory is shown to you for confirmation first, because memory stores
   assertions rather than evidence.
2. What to render: LaTeX (the default), HTML to PDF, or Markdown.

Paste in a job description and it tailors the resume by selecting and
reordering what is already true. It never adds anything.

## The checker

```bash
python3 check_facts.py resume.tex profile.yml
```

It fails on any number in the draft that isn't in your profile, and on any
`[ASK:]` marker you haven't answered yet. Stdlib only, no dependencies.
`--self-test` runs its own tests.

What it proves is that a number exists somewhere in your profile, not that it
sits in the right claim. That catches invented magnitudes, which is the failure
that actually shows up.

## Layout

```
SKILL.md                        the workflow and the iron rule
references/writing-rules.md     bullet craft, section order, ATS rules
references/memory-as-a-source.md when to trust agent memory, and how
references/profile.example.yml  the schema
templates/                      resume.tex, resume.html, resume.md
check_facts.py                  the guardrail
```

## Rendering

LaTeX needs `tectonic`, `xelatex` or `pdflatex`. Without one of those, the HTML
template prints through `chromium --headless --print-to-pdf=out.pdf
resume.html`, which needs nothing installed.

MIT.
