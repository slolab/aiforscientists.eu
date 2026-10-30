---
title: literature-to-table
skill: literature-to-table
status: brief
comments: true
recipe: 04-literature-as-data
check_level: expert
does: Extracts values from papers into a table, with the source and page for every value.
inputs:
- The papers, with supplements.
- The columns the table needs.
outputs:
- A table with one row per finding, and the source and page for every value.
- A list of papers where values could not be extracted.
steps:
- Read each paper and its supplements.
- Extract one row per finding.
- Record the source, page, and whether the value came from text, a table or a figure.
- Mark values read from figures for extra checking.
local:
- Which full-text access does your institution have, and how does the agent use it?
- Which columns does your table need?
- Which confounders or later corrections should the agent look for?
never:
- Never fill in a value without a source.
- Never use full texts in a way the publisher's licence does not allow.
check: A person checks a random sample of rows against the papers. Values from figures are checked more often.
test: Ten papers you know well. Check every row.
---

<!-- SKILL_PAGE -->
