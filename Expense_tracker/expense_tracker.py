while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        category = input("Category: ")

        try:
            amount = float(input("Amount: "))

        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        with open("expenses.txt", "a") as file:
            file.write(f"{category} - {amount}\n")

        print("Expense Saved!")

    elif choice == "2":

        try:
            with open("expenses.txt", "r") as file:
                expenses = file.read()

                if expenses:
                    print("\nExpenses:")
                    print(expenses)
                else:
                    print("No expenses found.")

        except FileNotFoundError:
            print("No expenses found.")

    elif choice == "3":

        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid Choice. Please select 1, 2, or 3.")