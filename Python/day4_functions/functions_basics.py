
def reverse_number(n):
    return str(n)[::-1]

number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)