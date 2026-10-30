---
title: pre-submission-check
skill: pre-submission-check
status: brief
comments: true
recipe: 09-write-review-teach
check_level: machine
does: Checks a manuscript against the journal's author guidelines and lists what is missing.
inputs:
- The manuscript, with figures, tables and supplements.
- The journal's author guidelines for the article type.
outputs:
- 'A checklist with one line per guideline item: met, not met, or unclear, with the location in the manuscript.'
- A list of required statements and files that are missing.
steps:
- 'Extract every checkable requirement from the guidelines: word and reference limits, sections, statements, figure formats, data and code availability.'
- Check the manuscript against each requirement.
- Quote the guideline for each item that is not met.
- List required declarations, such as competing interests and AI use.
local:
- Which journals and article types do you submit to most often?
- Where do you keep manuscripts, and in which format (Word, LaTeX, Markdown)?
- Which institutional requirements apply, such as affiliation wording, funder acknowledgements or open-access policies?
never:
- Never upload a manuscript to a service whose terms do not allow it.
- Never rewrite the scientific content; report, do not edit.
check: Each item names the guideline it comes from, so a person can check it in seconds.
test: A published paper from your group, checked against the guidelines of the journal that published it. Expect few or no missing items.
---

<!-- SKILL_PAGE -->
