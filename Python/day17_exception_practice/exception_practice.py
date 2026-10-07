# ValueError - right type, but an invalid value
try:
    num = int("abc")
except ValueError:
    print("Invalid Value - can't convert 'abc' to a number")


#ZeroDivisionError — dividing by zero
try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    result = number1 / number2
    print(f"Result: {result}")
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
    

#FileNotFoundError — File is not found
try:
    with open("data.txt", "r") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print("File does not exist.")

    
#IndexError  — List index doesn't exist
fruits = ["apple", "banana", "cherry"]
try:
    print(fruits[10])
except IndexError:
    print("That index doesn't exist in the list")

   
#KeyError — Key doesn't exist in the dictionary
student = {"name": "Alex", "age": 20}
try:
    print(student["grade"])
except KeyError:
    print("That key doesn't exist in the dictionary")
    

#TypeError — using the wrong type for an operation
try:
    result = "5" + 5
except TypeError:
    print("Can't add a string and an integer directly")
    

#AttributeError — calling a method that doesn't exist on that object
try:
    text = "hello"
    text.append("!")   # strings don't have .append(), that's a list method
except AttributeError:
    print("That method doesn't exist for this type")
    

#NameError — using a variable that was never defined
try:
    print(undefined_variable)
except NameError:
    print("That variable doesn't exist")
    
    
#ImportError / ModuleNotFoundError — importing a module that doesn't exist
try:
    import some_fake_module
except ModuleNotFoundError:
    print("That module isn't installed or doesn't exist")
    

#OverflowError — a number too large for Python to handle in a specific operation 
#(rare, but happens with things like huge exponents in certain math functions)
import math
try:
    print(math.exp(10000))   # way too large to represent as a float
except OverflowError:
    print("Number too large to calculate")
    
    
# Problem 1 — Age Input
try:
    age = int(input("Enter age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid number.")


# Problem 2 — Division
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Problem 3 — File Reader
filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")


# Problem 4 — List Index
fruits = ["Apple", "Banana", "Mango"]

try:
    index = int(input("Enter index: "))
    print(fruits[index])
except ValueError:
    print("Please enter a number.")
except IndexError:
    print("Index does not exist.")


# Problem 5 — Dictionary Key
student = {
    "name": "Yaswanthi",
    "marks": 90
}

key = input("Enter key: ")

try:
    print(student[key])
except KeyError:
    print("Key does not exist.")