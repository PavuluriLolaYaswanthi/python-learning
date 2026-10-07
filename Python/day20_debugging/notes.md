# Day 20 Notes — Debugging

## Topics Learned

- Reading error messages
- Finding line numbers
- Understanding error types
- Reproducing bugs
- Fixing bugs
- Testing the fix

## Important Rule

When I get an error, I should first try to solve it
myself for 15–20 minutes before asking ChatGPT.

When asking ChatGPT for help, I should ask for an
explanation of the error instead of simply asking for
the answer.

## Errors Practiced

### 1. SyntaxError

Cause:
Missing or incorrect Python syntax.

### 2. NameError

Cause:
Using a variable that has not been defined.

### 3. TypeError

Cause:
Using incompatible data types in an operation.

### 4. ValueError

Cause:
A value has the correct type but cannot be converted
or used in the required way.

### 5. ZeroDivisionError

Cause:
Trying to divide by zero.

### 6. IndexError

Cause:
Trying to access a list index that does not exist.

### 7. KeyError

Cause:
Trying to access a dictionary key that does not exist.

## Debugging Process

1. Read the error message.
2. Find the line number.
3. Look at the line.
4. Understand the error.
5. Reproduce the problem.
6. Try a fix.
7. Run the program again.
8. Verify the result.

## Practice Done

- SyntaxError
- NameError
- TypeError
- ValueError
- ZeroDivisionError
- IndexError
- KeyError
- Expense Tracker testing

## Problems Faced

Write the errors you personally encountered here.

## What I Learned

I learned how to read Python error messages and
systematically find and fix problems instead of
immediately asking for the solution.

## Commands Used

```bash
python debugging_practice.py
git status
git add .
git commit -m "Complete Day 20 debugging practice"
git push
