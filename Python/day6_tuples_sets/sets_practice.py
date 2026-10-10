# problem1
numbers = [10, 20, 10, 30, 20, 40, 10]
unique = []
for n in numbers:
  if n not in unique:
    unique.append(n)
print(unique)

# with inbuilt set function
numbers = [10, 20, 10, 30, 20, 40, 10]
unique = set(numbers)
print(unique)

# print the unique numbers in sorted order
numbers = {10, 20, 10, 30, 20, 40, 10}
unique = list(dict.fromkeys(numbers))
print(unique)

# problem2
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a|b # can be written as c = a.union(b)
print(c) # union of a and b

# intersection of a and b
d = a&b # can be written as d = a.intersection(b)
print(d)

# difference of a and b
e = a-b # can be written as e = a.difference(b)
print(e)

# symmetric difference of a and b
f = a^b # can be written as f = a.symmetric_difference(b)   
print(f)