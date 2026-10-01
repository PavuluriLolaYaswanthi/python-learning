# Day 16 — Expense Tracker File Storage

## Topics Practiced

- File handling
- Persistent data
- Read mode (r)
- Append mode (a)
- with open()
- FileNotFoundError
- Functions
- Modules

## Expense Tracker Practice

Tested the Expense Tracker file storage.

Current features:

- Add Expense
- View Expenses
- View Total Expenses
- View Category-wise Spending
- Save expenses permanently
- Read saved expenses
- Handle invalid amounts

## File Storage

Expenses are stored in:

expenses.txt

Example:

Food - 500.0
Travel - 1200.0
Shopping - 2000.0

## Important Concept

Append mode:

"a"

adds new data without deleting existing expenses.

Read mode:

"r"

reads existing expenses from the file.

## Persistent Data

I closed the Expense Tracker and opened it again.

The previous expenses were still available because they
were stored in expenses.txt instead of only being stored
in program memory.

## Improvement

Used:

.strip().title()

to clean category input.

Example:

food -> Food
FOOD -> Food

## What I Learned

I learned how my Expense Tracker saves information
permanently using a text file.

I also understood how expense_tracker.py communicates
with expense_utils.py to save, read, and process expenses.
