# Day 14 Notes — Expense Tracker V2

## Topics Learned

- Lists of dictionaries
- Storing multiple expenses
- Accessing dictionary values
- Looping through expenses
- Calculating total spending
- Category-wise spending
- Using dictionaries for totals
- Input validation using try/except

---

## 1. Lists of Dictionaries

In V1, an expense was stored as a single line in a text file.

In V2, each expense is stored as a **dictionary**, and every dictionary is placed inside a **list**.

```python
expense = {
    "category": "Food",
    "amount": 500
}
```

This groups the category and amount together as one record, instead of two separate pieces of data.

A single dictionary can only hold **one** expense. To hold many expenses, the dictionaries are collected into a list:

```python
expenses = []
```

This is called a **list of dictionaries** — a list where every item has the same shape (`category` and `amount`).

```python
expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1200},
    {"category": "Food", "amount": 300},
]
```

This structure is why the project is called a "tracker" — it keeps a growing history of entries, not just one value.

---

## 2. Storing Multiple Expenses

Every time the user adds an expense, a new dictionary is built and appended to the list.

```python
def add_expense(expenses):
    category = input("Enter category: ").strip()
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")
```

`append()` adds the new dictionary to the **end** of the list, so `expenses` keeps growing as the program runs.

Example after adding three expenses:

```python
expenses = [
    {"category": "Food", "amount": 500.0},
    {"category": "Travel", "amount": 1200.0},
    {"category": "Food", "amount": 300.0},
]
```

---

## 3. Accessing Dictionary Values

Each dictionary is accessed using its **keys**: `"category"` and `"amount"`.

```python
expense = {"category": "Food", "amount": 500}

print(expense["category"])
print(expense["amount"])
```

Output:

```text
Food
500
```

Inside a list, each item is accessed the same way, after first reaching the dictionary through its index or through a loop:

```python
print(expenses[0]["category"])
```

Output:

```text
Food
```

---

## 4. Looping Through Expenses

To view every expense, the program loops through the list and reads each dictionary's values.

```python
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== ALL EXPENSES =====")
    for expense in expenses:
        print(f"{expense['category']} - {expense['amount']}")
```

Example output:

```text
===== ALL EXPENSES =====
Food - 500.0
Travel - 1200.0
Food - 300.0
```

`if not expenses:` checks whether the list is still empty, so the program doesn't print a blank section when nothing has been added yet.

---

## 5. Calculating Total Spending

Total spending is calculated by looping through every expense and adding up the `"amount"` value.

```python
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
```

Example:

```python
expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1200},
    {"category": "Food", "amount": 300},
]

print("Total spending:", calculate_total(expenses))
```

Output:

```text
Total spending: 2000
```

This reuses the same accumulator pattern from Day 10 and Day 13 (`total = 0`, then `total += ...` inside a loop).

---

## 6. Category-wise Spending

Category-wise spending groups the amounts by category instead of adding everything into one number.

```python
def category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals
```

Example:

```python
expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1200},
    {"category": "Food", "amount": 300},
]

print(category_totals(expenses))
```

Output:

```text
{'Food': 800, 'Travel': 1200}
```

### How it works, step by step

```text
Expense 1: Food, 500
    "Food" not in totals  →  totals["Food"] = 500

Expense 2: Travel, 1200
    "Travel" not in totals  →  totals["Travel"] = 1200

Expense 3: Food, 300
    "Food" already in totals  →  totals["Food"] += 300  →  800
```

Final result:

```python
{'Food': 800, 'Travel': 1200}
```

---

## 7. Using Dictionaries for Totals

A plain number can only store **one** total. To store a total **per category**, a dictionary is used instead, where:

- the **key** is the category name
- the **value** is the running total for that category

```python
totals = {
    "Food": 800,
    "Travel": 1200
}
```

This is the same idea as the character-frequency dictionary from Day 11 and Day 13 — one dictionary, many running counters, each identified by its own key.

---

## 8. Input Validation Using try/except

If the user types something that isn't a number for the amount, `float()` raises a `ValueError` and crashes the program unless it's handled.

```python
def add_expense(expenses):
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")
```

Example — invalid input:

```text
Enter category: Food
Enter amount: five hundred
Invalid amount. Please enter a number.
```

Example — valid input:

```text
Enter category: Food
Enter amount: 500
Expense added successfully.
```

The `try` block attempts the risky conversion. The `except ValueError` block only runs if that conversion fails, so the program keeps running instead of crashing. `return` exits the function early so an invalid expense is never appended to the list.

---

## 9. Full Project Code — Expense Tracker V2

```python
def add_expense(expenses):
    category = input("Enter category: ").strip()

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n===== ALL EXPENSES =====")
    for expense in expenses:
        print(f"{expense['category']} - {expense['amount']}")


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def category_totals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    return totals


def show_menu():
    print("\n===== EXPENSE TRACKER V2 =====")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Total spending")
    print("4. Category-wise spending")
    print("5. Exit")


def main():
    expenses = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Total spending:", calculate_total(expenses))

        elif choice == "4":
            print("Category-wise spending:", category_totals(expenses))

        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


main()
```

### Why a `while True` loop with menu numbers?

```text
show_menu()  →  prints the options
       ↓
input()      →  the user picks a number
       ↓
if/elif      →  runs the matching function
       ↓
loop again, until the user chooses "5" and break stops it
```

This is the same menu pattern used for V1, now calling the new list-of-dictionaries functions instead of the file-based ones.

---

## Project Work

Improved Expense Tracker to V2.

Features added:

- Add expense
- View all expenses
- Calculate total spending
- Calculate category-wise spending
- Exit menu
- Invalid amount handling

---

## Important Concepts

Each expense is stored as a dictionary:

```python
{
    "category": "Food",
    "amount": 500
}
```

All expenses are stored inside a list:

```python
expenses = []
```

Category totals are stored using a dictionary.

Example:

```python
{
    "Food": 800,
    "Travel": 1200
}
```

---

## Problems Faced

Write any errors I faced while building the project.

---

## What I Learned

I learned how lists and dictionaries can be combined to store and process real application data.

I also learned how to calculate totals for each category.

---

## Commands Used

```bash
python expense_tracker.py
```

```bash
git status
git add .
git commit -m "Complete Day 14 Expense Tracker V2"
git push
git status
```

Expected:

```text
nothing to commit, working tree clean
```

---

## Next Step

Day 15 — File Handling practice and deeper revision.
