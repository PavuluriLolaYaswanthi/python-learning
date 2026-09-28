#squares of the numbers using dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squares = {
    number: number ** 2
    for number in numbers
}
print(squares)

# passed students using dictionary comprehension
marks = {"Alice": 90,"Bob": 55,"Charlie": 80,"David": 45}
passed ={
    name: mark
    for name, mark in marks.items()
    if mark >= 70
}
print(passed)

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