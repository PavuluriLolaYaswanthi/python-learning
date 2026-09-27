
#[expression for item in iterable if condition]

numbers = [i for i in range(1, 11)]
print(numbers)

squares = [i**2 for i in range(1, 11)]
print(squares)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

cubes = [number**3 for number in numbers]
print(cubes)

result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(result)

names = ["Alice", "Bob", "Anita", "John", "Alex", "David"]
upper_names = [name.upper() for name in names]
print(upper_names)

result = [name for name in names if name.startswith("A")]
print(result)


# Expense Tracker Challenge

expenses = {
    "Food": 500,
    "Travel": 1200,
    "Shopping": 3000,
    "Bills": 800
}

filtered_expenses = {
    category: amount
    for category, amount in expenses.items()
    if amount > 700
}

print(filtered_expenses)


#sample pattern for dictionary comprehension
"""new_dictionary = {
    key: value
    for key, value in old_dictionary.items()
    if condition
}
"""
