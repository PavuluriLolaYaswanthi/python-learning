# Day 17 — Exception Handling

## Topics Learned

- Exceptions
- try
- except
- else
- finally
- ValueError
- ZeroDivisionError
- FileNotFoundError
- IndexError
- KeyError

## What is Exception Handling?

Exception handling allows a Python program to handle
runtime errors without crashing.

## Basic Structure

try:
    risky code

except:
    handle the error

## ValueError

Occurs when a value has the correct general type of
operation but an invalid value is provided.

Example:

int("hello")

## ZeroDivisionError

Occurs when dividing a number by zero.

Example:

10 / 0

## FileNotFoundError

Occurs when trying to read a file that does not exist.

## IndexError

Occurs when accessing an invalid list index.

## KeyError

Occurs when accessing a dictionary key that does not exist.

## else

Runs when no exception occurs.

## finally

Runs whether an exception occurs or not.

## Practice Done

- Invalid number handling
- Division by zero
- Missing file
- Invalid list index
- Missing dictionary key
- Safe Calculator

## Connection to Expense Tracker

The Expense Tracker uses ValueError when validating
the amount entered by the user.

It uses FileNotFoundError when the expenses file
does not exist.

## What I Learned

I learned how to prevent a program from crashing when
expected runtime errors occur.

I also learned that different errors should be handled
using appropriate exception types.

## Next Step

Day 18 — Python Modules
