---
title: job-babysitter
skill: job-babysitter
status: brief
comments: true
recipe: 06-let-checking-cost-decide
check_level: machine
does: Watches cluster jobs, resubmits failed runs up to a set limit, and logs each change.
inputs:
- The list of jobs to watch.
- The code, configuration and log locations of each job.
outputs:
- 'A log with one line per event: job, failure cause, fix applied, resubmission.'
steps:
- Check the state of each job at a set interval.
- For each failed job, read the log and name the cause.
- If the cause is trivial and on the allowed list, fix it and resubmit.
- Otherwise stop and report the job to the user.
- Write every action to the log.
local:
- Which scheduler does your cluster use (for example Slurm), and which commands may the agent run?
- Which errors may the agent fix alone, for example out-of-memory or time limit?
- What is the maximum number of resubmissions per job, and the quota the agent must stay under?
- Which paths may the agent read and write?
- How should it reach you when it stops?
never:
- Never change the scientific code or the analysis parameters.
- Never delete files or checkpoints.
- Never exceed the resubmission limit or the group's quota.
check: The log lists each resubmission and its cause. The code and parameters of each run are unchanged, which a diff confirms.
test: Submit a job that fails with too little memory. The skill should raise the memory once, resubmit, and log it.
---

<!-- SKILL_PAGE -->
