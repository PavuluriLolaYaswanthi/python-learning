# Day 21 Notes — Expense Tracker V3

## Topics Learned

- Separating application logic into modules
- Importing functions from another Python file
- Organising a Python project
- Saving and reading data from files
- Calculating total expenses
- Calculating category-wise spending
- Handling invalid user input
- Writing project documentation

---

## Project Files

```text
expense_tracker_v3/
├── main.py
├── expense.py
├── README.md
├── requirements.txt
├── .gitignore
└── data/
    └── expenses.txt
```

| File                | Purpose                              |
| ------------------- | ------------------------------------ |
| `main.py`           | Menu and user interaction            |
| `expense.py`        | Expense-related functions            |
| `data/expenses.txt` | Persistent expense records           |
| `README.md`         | Project documentation                |
| `requirements.txt`  | Project dependencies                 |
| `.gitignore`        | Files excluded from Git              |

---

## Features Implemented

- Add expense
- View expenses
- Calculate total expenses
- View category-wise spending
- Save expenses to a file
- Handle invalid amounts and menu choices

---

## Important Concepts

- `import` allows code from another module to be reused.
- Append mode (`"a"`) preserves existing records.
- Read mode (`"r"`) retrieves saved records.
- `try` and `except` help handle invalid input.
- Dictionaries can group and total expenses by category.
- Functions make code easier to organise and maintain.

### Importing from `expense.py`

```python
from expense import add_expense, view_expenses, calculate_total, category_totals
```

`main.py` handles the menu. `expense.py` does the work. Keeping them separate means each file has one job.

### Append vs read mode

```python
with open("data/expenses.txt", "a") as file:    # add a new record, keep old ones
    file.write(f"{category} - {amount}\n")

with open("data/expenses.txt", "r") as file:    # read all saved records
    content = file.read()
```

Using `"w"` instead of `"a"` would erase every old record each time.

---

## Problems Faced

- **Wrong function name in `category_totals`:** I used `calculate_total` where `category_totals` was needed, so the menu option for category-wise spending showed one overall total instead of one total per category. Fixed by calling `category_totals(expenses)` and printing each category with its own total.
- **`NameError` after moving code to `expense.py`:** a function worked in one file but failed in another because I forgot to add it to the `from expense import ...` line.
- **`FileNotFoundError` for `data/expenses.txt`:** the program crashed when the file or `data/` folder did not exist yet. Fixed by creating the folder and catching `FileNotFoundError` when reading.
- **Negative amounts were accepted:** `float()` accepts `-50`, so the amount had to be checked with an extra `if amount <= 0` after the `try/except`.
- **Amounts read from the file are strings:** `"250.0"` had to be converted with `float()` before adding it to a total.

> Delete any item above that you did not actually run into, and add anything I missed.

---

## What I Learned

I learned how to separate the menu from expense-related functions, organise a Python project into multiple files, preserve data using file handling, and calculate total and category-wise spending.

---

## Testing

Test data:

```text
Food - 250
Travel - 100
Food - 150
```

- Add Food expense of 250
- Add Travel expense of 100
- Add another Food expense of 150
- View expenses and verify all three records appear
- Calculate total and verify it is 500.00
- View category totals and verify Food = 400.00 and Travel = 100.00
- Enter text instead of an amount and verify the error is handled
- Enter a negative amount and verify it is rejected
- Exit, restart the application, and verify the saved records remain

Expected results:

```text
Total spending: 500.00

Category-wise spending:
Food: 400.00
Travel: 100.00
```

---

## GitHub Commands

```bash
git status
git add .
git commit -m "Organize expense tracker V3"
git push
git status
```

Expected:

```text
nothing to commit, working tree clean
```
