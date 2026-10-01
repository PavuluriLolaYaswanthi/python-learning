# write the file
 
with open("student.txt", "w") as file:
    file.write("Name: Lola Yaswanthi\n")
    file.write("Age: 20\n")   
print("file created successfully")

# Read the file

with open("student.txt", "r") as file:
    content = file.read()
print("\nFile Content:")
print(content)

# append to the file

with open("student.txt", "a") as file:
    file.write("Topic: File Handling\n")
print("New information added.")

# Read line by line

with open("student.txt", "r") as file:
    print("\nReading line by line:")
    for line in file:
        print(line.strip())