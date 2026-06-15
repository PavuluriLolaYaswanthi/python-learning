expenses = []

while True:

    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        category = input("Enter Category: ")
        amount = float(input("Enter Amount: "))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense Added Successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\nExpenses List")

            for expense in expenses:
                print(
                    "Category:",
                    expense["category"],
                    "| Amount:",
                    expense["amount"]
                )

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Spending =", total)

    elif choice == "4":

        print("Thank You For Using Expense Tracker!")
        break

    else:

        print("Invalid Choice")