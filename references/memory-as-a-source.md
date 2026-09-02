# Memory as a source

Agent memory usually holds more facts about a person than any other source,
and less evidence behind them. What it stores are assertions.

Memory cannot distinguish:

| What it stored | What it might actually mean |
|---|---|
| "shipped the payments integration" | shipped it, started it, or planned it |
| "team of 6" | true in March, 3 people now |
| "raised a seed round" | signed, in conversation, or hoped for |

A resume claim has to hold up in an interview. A memory note only had to be
worth writing down at the time.

## The rule

Read memory. Propose every relevant fact back to the person as a checklist.
Only what they confirm gets written into `profile.yml`. Nothing reaches the
resume except through `profile.yml`, so `check_facts.py` still holds the line
without needing to change.

Never write a memory-derived fact straight into the profile, including one that
looks obviously true. Those are the ones that get written down without
checking, and then have to be defended in front of a hiring manager.

## Where to look

This depends on the runtime. Check what exists and skip the rest:

- Claude Code: `~/.claude/projects/*/memory/*.md` and its `MEMORY.md` index,
  plus `CLAUDE.md` at user and project level
- A connected memory MCP server: read the graph, treat every node as a proposal
- `AGENTS.md`, `GEMINI.md`, or whatever memory directory the runtime keeps
- The conversation itself. Facts stated earlier in this session are memory too,
  and get the same confirmation gate.

## How to ask

Batch it. One message, one checklist, specific claims:

    From memory, these look like resume material. Confirm what is accurate:
    1. the payments flow runs on Stripe against Postgres
    2. the product is split into 8 services
    3. one paying customer has run through it end to end
    Anything with a number I should attach?

Not: "I remember some things about your startup, should I use them?"
