try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Numbers only")
else:
    print("You entered a valid number:", number)
finally:
    print("Execution completed.")