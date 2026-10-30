---
title: Make your materials accessible to agents
nav_title: "Make materials accessible"
recipe_icon: folder-text-outline
try: "Keep specifications, meeting notes, designs and reusable skills as plain text where agents can read them."
recipe_id: R-01
status: tried
stage: Prepare for agents
verifiability: Expert-checkable
autonomy: Proposes changes as pull requests; scheduled runs report what they did
first_added: 2026-09-25
last_reviewed: 2026-10-30
skills:
  - name: lab-meeting-digest
    does: reads the week's project updates and posts a summary on the morning before lab meeting.
  - name: slide-library
    does: finds slides from earlier talks for reuse in a new one.
practices:
  - title: Write documentation and data for agents
    slug: 05-documentation-and-data-for-agents
    note: the same rule, applied to a lab.
  - title: State human-in-the-loop requirements
    slug: 09-human-in-the-loop
    note: decide when a person reads what a scheduled agent produced.
tags: [Prepare for agents, Expert-checkable]
comments: true
---

<!-- RECIPE_TITLE -->

## Summary

An agent can only use information it can read.
It cannot read slides, chat threads, or what people remember.
Groups that benefit from agents keep their project knowledge in plain text, next to the code.
Once the material is readable, recurring lab tasks can run on a schedule, and reusable workflows can be shared as skills.

## Steps

1. Add a folder for the agent to every repository, with specs, transcribed meeting notes and links to related projects.
2. Write model assumptions and experimental designs as short text files.
   Let people and agents propose changes to them as pull requests.
3. Choose tools that store content as Markdown and can be used from the command line.
4. Schedule an agent to read the week's project updates and post a digest on the morning before lab meeting.
   The digest lists overlaps between projects, overdue items and suggested priorities.
5. Index old material, such as slide decks, so an agent can find and reuse it.
6. When you build something reusable, add it to a shared skills repository.

## How to check the output

A person reviews each pull request that changes a design or an assumption.
Every scheduled run posts a report of what it did.
The group leader reads the digest before the meeting.

## Examples

- In one lab, every repository has a folder for the agent with specs, transcribed meeting notes and links to related projects.
- In another, a scheduled agent posts a digest of overlaps, overdue items and suggested priorities on the morning before each lab meeting.
- An agent indexed years of old slide decks into one master deck with a short description of every slide.
  It now drafts new talks from an abstract by reusing existing slides.
- Groups across the centre had often built the same workflows independently.
  A colleague hired for the purpose now maintains a shared skills repository, and anyone who builds something reusable is asked to add it.
- One lab works with its cluster agent only through the issue tracker of its code repository.
  Requests go in as issues, the agent replies in comments, and changes arrive as pull requests for review.
- Meeting transcription works for up to about five speakers.
  Larger meetings need recorders that can tell voices apart.

## Known problems

- If nobody updates the agent's folder, the agent works from an old plan.
  Date the notes, and delete what is no longer true.
- A skills repository with no one responsible for it goes out of date.
- A scheduled agent should not delete files without a person's confirmation.
  See [Where to draw the line](../guide/limits.md#do-not-delegate).

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-10-30: Renumbered to follow point 1 of the submitted Comment.
  Merged the former recipes "Keep project documents as text" and "Schedule recurring lab tasks".
- 2026-10-28: Updated to match the presubmission draft of the Comment.
- 2026-09-25: Updated to match the first full draft of the Comment.
- 2026-09-25: First draft, from the first round-table.
