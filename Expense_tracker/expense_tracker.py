
from expense_utils import save_expense, read_expenses, calculate_total

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        category = input("Category: ")

        try:
            amount = float(input("Amount: "))

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue
        
        save_expense(category, amount)

        print("Expense Saved!")
    
    
    elif choice == "2":
        expenses = read_expenses()
        if expenses:
            print("\nRecorded Expenses:")
            print(expenses)
        else:
            print("No expenses recorded yet.")

    elif choice == "3":
        expenses = read_expenses()
        if expenses:
            total = calculate_total(expenses)
            print(f"\nTotal Expenses: {total:.2f}")
        else:
            print("No expenses recorded yet.")

    elif choice == "4":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice. Please select 1, 2, 3, or 4.")