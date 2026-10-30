---
title: Establish agent guardrails
nav_title: "Establish guardrails"
recipe_icon: shield-lock-outline
try: "Limit agents to listed folders and minimal rights, and approve every email or form before it goes out."
recipe_id: R-02
status: tried
stage: Prepare for agents
verifiability: Machine-checkable
autonomy: Sandboxed to listed paths; a person approves outgoing messages
first_added: 2026-10-30
last_reviewed: 2026-10-30
skills: []
practices:
  - title: Govern agent autonomy and accountability
    slug: 04-govern-autonomy-and-accountability
    note: a sandbox and a list of allowed paths limit what the agent can do.
  - title: Decide where research data may be sent
    slug: 11-decide-where-research-data-may-go
    note: the sandbox also decides which data an agent can read.
  - title: State human-in-the-loop requirements
    slug: 09-human-in-the-loop
    note: no message or form goes out without a person approving it.
tags: [Prepare for agents, Machine-checkable]
comments: true
---

<!-- RECIPE_TITLE -->

## Summary

Shared storage was set up before agents existed, and often lets anyone write anywhere.
One misbehaving agent could delete a group's work.
Telling an agent which folders to stay in is not enough.
Run agents in sandboxes that can reach only a listed set of paths, under accounts with the narrowest rights that still let them do the job.

## Steps

1. Check which shared folders anyone can write to, and which data are not backed up.
2. Run agents in a sandbox that can reach only a listed set of paths.
3. Run them under an account with the narrowest rights that still let them do the job.
4. Do not rely on instructions in the prompt to keep an agent inside a folder.
5. If agents get access to email or calendars, stay within data-protection rules, and approve every message before it goes out.

## How to check the output

A script lists the paths the sandbox can reach and the rights of the agent's account.
File permissions and backups are checked at regular intervals.
Outgoing messages and forms wait in a queue until a person approves them.

## Examples

- On one shared cluster, many group folders could be written to by any user, and the data were too large to back up.
- A user told an agent it could now look at a second folder.
  The agent replied that it already had.
- Some group leaders would like to give agents their email and calendars, within data-protection rules, if no message goes out without their approval.

## Known problems

- Reading data outside the allowed folders can breach data-protection law, for example the GDPR, even if nothing is changed.
- A sandbox that is too narrow makes people switch it off.
  Start from the folders the task needs, and add paths on request.

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-10-30: New recipe for point 2 of the submitted Comment.
  The sandbox and folder-permission steps moved here from the former recipe "Review methods, limit file access".
