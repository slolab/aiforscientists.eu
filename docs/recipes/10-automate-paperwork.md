---
title: Automate the paperwork you control, and build interfaces to the rest
nav_title: "Automate paperwork"
recipe_icon: receipt-text-outline
try: "Automate your own forms and reports first, then give agents read access to finance, personnel and grant systems where the rules allow."
recipe_id: R-10
status: tried
stage: Implement with agents
verifiability: Machine-checkable
autonomy: Fills in forms; a person signs and submits
first_added: 2026-09-25
last_reviewed: 2026-10-30
skills:
  - name: travel-reimbursement
    does: fills in the travel reimbursement form from a folder of invoices and tickets.
practices:
  - title: Default to agent-accessibility
    slug: 02-default-to-agent-accessibility
    note: most time would be saved if the institute's own systems were open to agents.
  - title: State human-in-the-loop requirements
    slug: 09-human-in-the-loop
    note: the agent fills in the form, and a person submits it.
tags: [Implement with agents, Machine-checkable]
comments: true
---

<!-- RECIPE_TITLE -->

## Summary

Administration drew both the most enthusiasm and the most frustration at the round-table.
So far, researchers automate the forms and requests they receive, and almost all the time saved is theirs.
The administration changes more slowly, for good reasons: it is bound by rules on data protection, accounting and employment, and it runs on finance, personnel, grant and travel systems that rarely connect to each other.
Instead of waiting for these systems to be replaced, build agent interfaces on top of them, with read access where the rules allow and a person approving anything that is submitted.
What group leaders want most is one such assistant: it tells them how much money is left on each grant and who is paid from it, and tells the administration what it still needs from them.

## Steps

1. Automate your own forms and reports first.
   Put the invoices and tickets for each trip in one folder, and let an agent fill in the reimbursement form.
2. Let an agent update CVs and answer reporting requests from documents you already have.
3. Check the totals, then sign and submit the form yourself.
4. Ask your institute for agent licences for administrative staff.
5. Build agent interfaces on top of the finance, personnel, grant and travel systems, with read access where the rules allow.
   A person approves anything that is submitted.

## How to check the output

The totals on a form must match the receipts.
A person submits the form.

## Examples

- Travel reimbursement from a folder of hotel and train invoices, including the institute's PDF forms, was the skill most people asked for.
- For a funding review, an agent mapped the centre's international collaborations from existing documents.
  The result was more complete than a survey of group leaders.
- Other uses: conflict-of-interest checks, a database of group leaders for funding presentations, and an agent that answers admin questions from the institute's shared documents.
- Requested next: take photos of receipts during a trip, and have the agent file the claim.

## Known problems

- Admin and HR staff often do not have access to agents, so only researchers save time.
  A licence costs about €30 per person a month.
- An agent with access to finance or HR data handles personal data.
  See [Where to draw the line](../guide/limits.md#handle-with-care).

<!-- RECIPE_SKILLS -->

<!-- RECIPE_PRACTICES -->

## Change history

- 2026-10-30: Renumbered to follow point 10 of the submitted Comment (formerly "Fill in admin forms").
- 2026-10-28: Updated to match the presubmission draft of the Comment.
- 2026-09-25: Updated to match the first full draft of the Comment.
- 2026-09-25: First draft, from the first round-table.
