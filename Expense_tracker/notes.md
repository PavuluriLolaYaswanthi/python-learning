# Day 7 Notes — Expense Tracker

## Project Name

Expense Tracker

---

## Project Goal

Build a simple Python application that allows users to:

- Add expenses
- View expenses
- Calculate total spending
- Exit the program

---

## Topics Used

- Variables
- Input/Output
- Data Types
- If/Else
- Loops
- Lists
- Dictionaries

---

## Data Structures Used

### List

Stores all expenses.

```python
expenses = []
```

Example:

```python
[
    {"category": "Food", "amount": 250},
    {"category": "Travel", "amount": 500}
]
```

---

### Dictionary

Stores information for a single expense.

```python
{
    "category": "Food",
    "amount": 250
}
```

---

## Logic Used

### Add Expense

Take category and amount from user.

Store them inside a dictionary.

Add dictionary to expenses list.

```python
expenses.append(expense)
```

---

### View Expenses

Loop through expenses list.

```python
for expense in expenses:
```

Display category and amount.

---

### Calculate Total Spending

Initialize total.

```python
total = 0
```

Add every expense amount.

```python
total += expense["amount"]
```

Display total spending.

---

## Problems Faced

- Converting amount to float
- Accessing dictionary values
- Using loops correctly
- Calculating total spending

---

## What I Learned

Today I built my first mini project using Python fundamentals. I learned how to combine loops, conditions, lists, and dictionaries to create a useful application. I also learned how to store structured data and calculate totals from user input.

---

## Interview Questions

### Why use a List?

A list stores multiple items in a single variable.

### Why use a Dictionary?

A dictionary stores information using key-value pairs.

### Why use a Loop?

A loop helps repeat code without writing it multiple times.

### Why use If/Else?

If/Else controls program flow based on user choices.

---

## Commands Used

```bash
python expense_tracker.py

git add .
git commit -m "Build Expense Tracker mini project"
git push
```
