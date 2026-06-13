fruits = ["Apple", "Banana", "Orange"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits = ["Apple", "Banana"]

fruits.append("Orange") # add element

fruits.remove("Banana") # delete element
print(fruits)

print(len(fruits)) # len of the list

fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)