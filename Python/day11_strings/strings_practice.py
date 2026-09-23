name = "Python"
print(name[0])  # Output: P
print(name[-1])  # Output: n
print(len(name))  # Output: 6

text = "hello world"
print(text.upper())  # Output: HELLO WORLD
print(text.lower())  # Output: hello world

text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)  # Output: I love Python


text = "Python is powerful"
print("Python" in text)  # Output: True

name = "   Python   "
print(name.strip())  # Output: Python

text = "Python is easy to learn"
print(text.split())  # Output: ['Python', 'is', 'easy', 'to', 'learn']

words = ["Python", "SQL", "Git"]
print(" ".join(words))  # Output: Python SQL Git

text = "Python Programming"
print(text[:6])  # Output: Python
print(text[7:18])  # Output: Programming