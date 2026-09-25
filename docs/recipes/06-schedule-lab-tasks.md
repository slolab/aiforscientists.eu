---
title: Run recurring lab tasks on a schedule
nav_title: "Schedule recurring lab tasks"
recipe_id: R-06
status: tried
stage: Operate
verifiability: Machine-checkable
autonomy: Runs on a schedule and reports what it did
first_added: 2026-09-25
last_reviewed: 2026-09-25
skills:
  - name: lab-meeting-digest
    does: reads the week's project updates and posts a summary on the morning before lab meeting.
  - name: job-babysitter
    does: watches cluster jobs, resubmits failed runs, and logs each change.
practices:
  - title: State human-in-the-loop requirements
    slug: 09-human-in-the-loop
    note: decide when a person reads the agent's report.
tags: [Operate, Machine-checkable]
---

<!-- RECIPE_TITLE -->

## Summary

Agents can run recurring lab tasks on a schedule: summaries, reminders, job monitoring and storage clean-up.
Each run is small, and its result is easy to check.

## Steps

1. Schedule an agent to read the week's project updates and post a summary on the morning before lab meeting.
   The summary lists overlaps between projects, reminders and open decisions.
2. Let an agent watch cluster jobs, fix and resubmit failed runs, and log each change.
3. Let it remind people to delete old checkpoints when storage is low.

## How to check the output

Every run posts a report of what it did.
A person reads the summary before the meeting and the job log once a day.

## Examples

- With an agent monitoring its jobs, one group went from tens of runs to hundreds.
- Meeting transcription works for up to about five speakers.
  Larger meetings need recorders that can tell voices apart.

## Known problems

- An agent that resubmits jobs can use up a shared quota.
  Set a limit on the number of runs.
- An agent should not delete files without a person's confirmation.
  See [Where to draw the line](../guide/limits.md#do-not-delegate).

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-09-25: First draft, from the first round-table.
