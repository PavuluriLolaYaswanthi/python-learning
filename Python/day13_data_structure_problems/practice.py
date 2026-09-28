

# problem 1 : largest number in a list without using max() function

numbers = [10, 25, 7, 40, 15]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print("The largest number is:", largest_number)

# problem 2 : smallest number in a list without using min() function

numbers = [10, 25, 7, 40, 15]
smallest_number = numbers[0]
for number in numbers:
    if number < smallest_number:
        smallest_number = number
print("The smallest number is:", smallest_number)

# problem 3 : sum of all numbers in a list without using sum() function

numbers = [10, 20, 30, 40]
total_sum = 0
for number in numbers:
    total_sum += number
print("The sum of all numbers is:", total_sum)

# problem 4 : count the number of even and odd numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8,9]
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 ==0:
        even_count += 1
    else:
        odd_count += 1
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)

# problem 5 : remove duplicates from a list without using set()

numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("List with duplicates removed:", unique_numbers)

# problem 6 : reverse a string using loop

text = "Python"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)

# problem 7 : count number of vowels in a string

text = "Hello, World!"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count +=1
print("Number of vowels in the string:", count)

# problem 8 : Count the number of words.

text = "Python is easy to learn"
count = 0
for char in text:
    if char == " ":
        count += 1
word_count = count + 1
print("Number of words in the string:", word_count)

# same problem 8 : Count the number of words.

text = "Python is easy to learn"
words = text.split()
print("Number of words in the string:", len(words))

# problem 9 : palindrome check for a string

text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
# problem 10 : character frequency count in a string

frequency = {}
text = input("Enter a string: ")
for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
print("Character frequency:")

# problem 11 : students with highest marks

marks = {"Alice": 90, "Bob": 55, "Charlie": 80, "David": 45}
highest_marks = 0
highest_name = None
for name, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_name = name
print(highest_name)
print(highest_marks)

# students with lowest marks

marks = {"Alice": 90, "Bob": 55, "Charlie": 80, "David": 45}
lowest_marks = float("inf")   # infinity: bigger than any real mark
lowest_name = None
for name, mark in marks.items():
    if mark < lowest_marks:
        lowest_marks = mark
        lowest_name = name
print(lowest_name)
print(lowest_marks)

# problem 12 : calculate average marks of students

marks = {"Alice": 90, "Bob": 55, "Charlie": 80, "David": 45}
total_marks = 0
for mark in marks.values():
    total_marks += mark
    average_marks = total_marks / len(marks)
print("Average marks of students:", average_marks)

# problem 13: filter the passed students from the dictionary

marks = {"Alice": 85,"Bob": 45,"Charlie": 75,"David": 30}
passed_students = {name: mark for name, mark in marks.items() if mark >= 50}
print("Passed students:", passed_students)

# problem 14: count word frequency

words = {
    "Food": 500,
    "Travel": 1500,
    "Shopping": 3000,
    "Bills": 800
}

word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
print("Word frequency:", word_frequency)

# problem 15: find expensive expenses

expenses = {
    "Food": 500,
    "Travel": 1500,
    "Shopping": 3000,
    "Bills": 800
}
expensive_expenses = {category: amount for category, amount in expenses.items() if amount > 1000}
print("Expensive expenses:", expensive_expenses)

# problem 16: second largest number in a list

numbers = [10, 25, 7, 40, 15]
largest = 0
second_largest = None
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number != largest:
        if second_largest is None or number > second_largest:
            second_largest = number
print("The second largest number is:", second_largest)

# second smallest number in a list

numbers = [10, 25, 7, 40, 15]
smallest = numbers[0]
second_smallest = None
for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number != smallest:
        if second_smallest is None or number < second_smallest:
            second_smallest = number
print("The second smallest number is:", second_smallest)

# problem 17: Common elements in two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for number in list1:
    if number in list2:
        common_elements.append(number)
print("Common elements in the two lists:", common_elements)

# unique elements in two lists

unique_elements = []
for number in list1:
    if number not in list2:
        unique_elements.append(number)
for number in list2:
    if number not in list1:
        unique_elements.append(number)
print("Unique elements in the two lists:", unique_elements)

# problem 18: separate even and odd numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

# problem 19: word length in dictionary

words = ["apple", "banana", "cherry", "date"]
word_length = {word: len(word) for word in words}
print("Word length in dictionary:", word_length)

# sort a list of dictionaries by a key

students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 22}
]
students_sorted = sorted(students, key=lambda x: x["age"])
print("Students sorted by age:", students_sorted)

# problem 20: Mini Expense Analysis

expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1200},
    {"category": "Food", "amount": 300},
    {"category": "Shopping", "amount": 2000}
]
total = 0
food_total = 0
for expense in expenses:
    total += expense["amount"]
    if expense["category"] == "Food":
        food_total += expense["amount"]
print("Total expenses:", total)
print("Total food expenses:", food_total)