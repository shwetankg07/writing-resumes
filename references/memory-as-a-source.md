# Memory as a source

Persistent agent memory is the richest source of facts about a person and the
most dangerous one. It stores **assertions**, not evidence.

Memory cannot distinguish:

| What it stored | What it might actually mean |
|---|---|
| "shipped the payments integration" | shipped it · started it · planned it |
| "team of 6" | true in March, 3 people now |
| "raised a seed round" | signed · in conversation · hoped for |

A resume claim has to survive an interview. A memory note only had to survive
being written down. So memory **proposes; the person disposes.**

## The rule

Read memory. Propose every relevant fact back to the person as a checklist.
Only what they confirm gets written into `profile.yml`. Nothing reaches the
resume except through `profile.yml` — so `check_facts.py` still holds the line
without changing.

Never write a memory-derived fact straight into the profile, not even one that
looks obviously true. "Obviously true" is how a wrong number gets into the room
with a hiring manager.

## Where to look

Runtime-dependent; check what exists and skip the rest:

- Claude Code — `~/.claude/projects/*/memory/*.md` and its `MEMORY.md` index;
  `CLAUDE.md` at user and project level
- A connected memory MCP server — read the graph, treat nodes as proposals
- `AGENTS.md`, `GEMINI.md`, or the runtime's own memory directory
- The conversation itself: facts stated earlier in this session count as
  memory, and get the same confirmation gate

## How to ask

Batch it. One message, one checklist, specific claims:

    From memory, these look like resume material. Confirm what is accurate:
    1. chalyaaar processes real payments through Cashfree on Neon Postgres
    2. the platform is 8 sub-apps
    3. one paid event has run end to end on it
    Anything with a number I should attach?

Not: "I remember some things about your startup, should I use them?"
