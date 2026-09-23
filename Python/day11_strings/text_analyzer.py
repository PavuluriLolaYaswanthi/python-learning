text = input("Enter a text: ")

# analyze the text
characters = len(text)
words = len(text.split())
sentences = text.count('.') + text.count('!') + text.count('?')

# count uppercase and lowercase letters
uppercase_count = sum(1 for c in text if c.isupper())
lowercase_count = sum(1 for c in text if c.islower())

# display results
print(f"Characters: {characters}")
print(f"Words: {words}")
print(f"Sentences: {sentences}")
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")

#word search
word = input("Enter a word to search: ")

if word.lower() in text.lower():
    print("Word found!")
else:
    print("Word not found.")
    
#character frequency
fequency = {}
for char in text:
    if char != " ":
        if char in fequency:
            fequency[char] += 1
        else:
            fequency[char] = 1

print("Character frequency:")
for char, count in fequency.items():
    print(f"'{char}': {count}")