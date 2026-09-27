

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
print("Student with highest marks:", highest_name, "with marks:", highest_marks)