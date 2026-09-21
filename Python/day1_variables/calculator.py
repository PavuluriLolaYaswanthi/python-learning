while True:
    num1 = float(input("Enter first number: "))
    operation = input("Choose (+, -, *, /, %, **, sq, exit): ")

    if operation == "exit":
        print("Goodbye!")
        break

    if operation == "sq":
        print("Result:", num1 ** 2)
        continue   # skip asking for num2, go straight to next loop

    num2 = float(input("Enter second number: "))

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        print("Result:", num1 / num2)
    elif operation == "%":
        print("Result:", num1 % num2)
    elif operation == "**":
        print("Result:", num1 ** num2)
    else:
        print("Invalid operation")