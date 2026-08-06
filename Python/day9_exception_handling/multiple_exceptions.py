try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ValueError:
    print("Numbers only ")
except ZeroDivisionError:
    print("Cannot divide by zero")