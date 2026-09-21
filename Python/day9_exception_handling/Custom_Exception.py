#Custom Exception (stretch goal)
#Create your own exception class called NegativeNumberError. 
# Write a function that raises it if the user enters a negative number, then catch and handle it.
class NegativeNumberError(Exception):
    pass
def check_positive_number():
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            raise NegativeNumberError("Negative number entered!")
        except NegativeNumberError as e:
            print(e)
        except ValueError:
            print("Please enter a valid number.")
        else:
            print("You entered a positive number:", num)
check_positive_number()