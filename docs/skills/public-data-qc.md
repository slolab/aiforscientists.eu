---
title: public-data-qc
skill: public-data-qc
status: brief
comments: true
recipe: 08-pin-down-the-method
check_level: machine
does: Downloads, deduplicates and checks public datasets, with a report for each step.
inputs:
- The list of datasets with their accession numbers or URLs.
- The checks the data must pass.
outputs:
- The data, stored in the agreed place.
- 'A report per dataset: source, checksum, counts before and after each step, duplicates removed.'
steps:
- Download each dataset and record its checksum.
- Check the counts against the source's metadata.
- Find and remove duplicates, and list them.
- Run the agreed checks.
- Write the report.
local:
- Which repositories do you download from?
- Where may the data be stored, and how much space is there?
- Which checks must each dataset pass?
- Which data must not be downloaded, for example controlled-access data?
never:
- Never download controlled-access data without the approval.
- Never change values in the data; only remove listed duplicates.
check: Checksums and counts for each step can be compared with the source.
test: Two public datasets that share some samples. The report should list the shared samples.
---

<!-- SKILL_PAGE -->
