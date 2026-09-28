
#[expression for item in iterable if condition]

numbers = [i for i in range(1, 11)]
print(numbers)

# squares of the numbers using comprehensions
squares = [i**2 for i in range(1, 11)]
print(squares)

# Even numbers in list using comprehensions
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# odd numbers in list using comprehensions
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)

cubes using comprehensions
cubes = [number**3 for number in numbers]
print(cubes)

even or odd using comprehensions
result = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(result)

# uppercase names using comprehensions
names = ["Alice", "Bob", "Anita", "John", "Alex", "David"]
upper_names = [name.upper() for name in names]
print(upper_names)

# names starting with 'A' using comprehensions
result = [name for name in names if name.startswith("A")]
print(result)