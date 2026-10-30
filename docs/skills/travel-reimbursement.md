---
title: travel-reimbursement
skill: travel-reimbursement
status: brief
comments: true
recipe: 10-automate-paperwork
check_level: machine
does: Fills in the travel reimbursement form from a folder of invoices and tickets.
inputs:
- One folder per trip with invoices, tickets and receipts (PDF or photo).
- The trip's dates, destination and purpose.
- The approval or reference number of the trip request, if your institute issues one.
outputs:
- The filled-in reimbursement form, in the format the institute accepts.
- A table of every receipt with date, amount, currency, category and the file it came from.
- A list of anything missing or unclear.
steps:
- Read every file in the trip folder and list each cost with its source file.
- Convert foreign currencies with the rate the rules prescribe, and record the rate used.
- Apply the per-diem and meal-deduction rules to the trip dates.
- Fill in the form, field by field.
- Compare the form totals with the receipt table.
- Show the user the form, the receipt table and the list of open questions.
local:
- Which reimbursement form does your institute use, and in which format (fillable PDF, web portal, spreadsheet)?
- Where are the form and the travel rules stored, and may the agent read them?
- Which per-diem, meal-deduction and currency-conversion rules apply?
- Which personal and bank details go on every form, and where should the agent read them from?
- Is a trip request or approval number required, and where is it found?
- Who receives the form, and how is it submitted?
never:
- Never submit or send the form; a person signs and submits it.
- Never invent a receipt, an amount or a date; mark gaps instead.
- Never send personal or bank details to any service the institute has not approved.
check: The form totals match the sum of the receipt table, and every row in the table names its source file. A person signs and submits the form.
test: A two-day trip with one train ticket, one hotel invoice and one receipt in a foreign currency. Check the per-diem, the conversion and the total by hand.
---

<!-- SKILL_PAGE -->
