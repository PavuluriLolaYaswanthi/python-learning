# Day 18 — Python Modules

## Topics Learned

- Python modules
- Creating a module
- import
- from ... import ...
- Importing multiple functions
- Import aliases using as
- Separating reusable code

## What is a Module?

A module is a Python file containing reusable code,
such as functions and variables.

Example:

mymodule.py

## Importing a Module

import mymodule

Then functions can be accessed using:

mymodule.function_name()

## Importing Specific Functions

from mymodule import add

Then the function can be used directly:

add(10, 20)

## Importing Multiple Functions

from mymodule import add, subtract, multiply

## Alias

import mymodule as mm

The module can then be accessed using:

mm.add()

## Practice Done

- Created mymodule.py
- Imported a custom module
- Created calculator_utils.py
- Created student_utils.py
- Used functions from separate modules

## Connection to Expense Tracker

The Expense Tracker uses:

expense_tracker.py
expense_utils.py

expense_utils.py contains reusable functions such as:

- save_expense()
- read_expenses()
- calculate_total()
- calculate_category_totals()

expense_tracker.py imports these functions.

## What I Learned

Modules allow code to be separated into different
files and reused in other Python programs.

This makes programs easier to organize and maintain.

## Next Step

Day 19 — pip and virtual environments.
