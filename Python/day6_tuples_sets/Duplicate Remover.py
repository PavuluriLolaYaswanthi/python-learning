user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
print("Original list:", numbers)
unique_numbers = list(dict.fromkeys(numbers))
print("List after removing duplicates:", unique_numbers)