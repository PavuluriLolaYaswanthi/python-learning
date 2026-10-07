while True:

    print("\n===== SAFE CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Calculator closed.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice.")
        continue

    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2

        elif choice == "2":
            result = num1 - num2

        elif choice == "3":
            result = num1 * num2

        elif choice == "4":
            result = num1 / num2

    except ValueError:
        print("Invalid input. Enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    else:
        print(f"Result: {result}")