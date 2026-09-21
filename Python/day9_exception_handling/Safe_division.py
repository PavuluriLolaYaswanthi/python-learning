try:
    a=float(input("Enter the numerator: "))
    b=float(input("Enter the denominator: "))
    result=a/b
    print("The result is: ", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")