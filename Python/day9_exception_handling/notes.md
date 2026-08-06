# Day 9 Notes — Exception Handling

## Topics Learned

- Exceptions
- try
- except
- else
- finally
- raise

---

## What is an Exception?

An exception is an error that occurs during program execution.

---

## Why Use Exception Handling?

Without exception handling, the program stops when an error occurs.

With exception handling, the program continues and provides a user-friendly message.

---

## Syntax

```python
try:
    # Risky code

except:
    # Handle error
```

---

## Exception Types

### ValueError

Occurs when the input type is incorrect.

Example:

```python
int("abc")
```

---

### ZeroDivisionError

Occurs when dividing by zero.

```python
10 / 0
```

---

## else

Runs only when no exception occurs.

---

## finally

Runs whether an exception occurs or not.

---

## raise

Used to create custom exceptions.

---

## Practice Done

- Used try and except
- Handled invalid input
- Handled divide-by-zero errors
- Used else and finally
- Created a custom exception with raise
- Updated Expense Tracker to validate amount input

---

## Problems Faced

- Forgetting exception types
- Not understanding when else executes
- Confusing except with finally

---

## What I Learned

Today I learned how to prevent programs from crashing using exception handling. I practiced handling invalid user input, divide-by-zero errors, and improved my Expense Tracker to handle incorrect amount entries safely.

---

## Interview Questions

### What is an exception?

An exception is an error that occurs while a program is running.

### What is the purpose of try?

It contains code that might produce an error.

### What is the purpose of except?

It handles the error without stopping the program.

### Difference between else and finally?

- `else` runs only if no exception occurs.
- `finally` always runs.

---

## Commands Used

```bash
python try_except.py
python multiple_exceptions.py
python else_finally.py
python raise_exception.py

git add .
git commit -m "Day 9 exception handling"
git push
```