# Day 11 Notes — Strings

## Topics Learned

* Strings
* Creating strings
* String indexing
* Positive indexing
* Negative indexing
* String slicing
* `len()`
* `lower()`
* `upper()`
* `strip()`
* `replace()`
* `split()`
* `join()`
* `in`
* `not in`
* f-strings
* String iteration
* String counting
* Character frequency
* Text Analyzer project

---

## 1. What is a String?

A **string** is a sequence of characters used to store text.

Strings can be created using single quotes or double quotes.

```python
name = "Yaswanthi"
city = 'Guntur'
message = "Hello Python"
```

The data type of a string is `str`.

```python
name = "Python"

print(type(name))
```

Output:

```text
<class 'str'>
```

---

## 2. String Indexing

Each character in a string has an **index position**.

Python starts indexing from **0**.

Example:

```python
text = "Python"
```

Index positions:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

Example:

```python
text = "Python"

print(text[0])
print(text[1])
print(text[2])
```

Output:

```text
P
y
t
```

### Important

Python uses **zero-based indexing**.

That means the first character is at index `0`.

---

## 3. Negative Indexing

Python also supports indexing from the end of a string.

Example:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

Example:

```python
text = "Python"

print(text[-1])
print(text[-2])
```

Output:

```text
n
o
```

`-1` means the last character.

---

## 4. String Slicing

Slicing is used to extract a portion of a string.

Syntax:

```python
string[start:stop]
```

The `start` index is included.

The `stop` index is excluded.

Example:

```python
text = "Python"

print(text[0:3])
```

Output:

```text
Pyt
```

Why?

```text
P y t h o n
0 1 2 3 4 5
|-----|
0     3
```

Index `3` is not included.

### More Slicing Examples

```python
text = "Python"

print(text[0:2])
print(text[2:5])
print(text[:4])
print(text[2:])
```

Output:

```text
Py
tho
Pyth
thon
```

`[:4]` means:

```python
text[0:4]
```

`[2:]` means:

```python
text[2:len(text)]
```

---

## 5. `len()`

`len()` returns the number of characters in a string.

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

Spaces are also counted.

```python
text = "Hello World"

print(len(text))
```

`Hello World` contains 11 characters including the space.

---

## 6. `lower()`

`lower()` converts all alphabetic characters to lowercase.

```python
text = "PYTHON"

print(text.lower())
```

Output:

```text
python
```

It does not change the original string.

```python
text = "PYTHON"

text.lower()

print(text)
```

Output:

```text
PYTHON
```

To store the changed value:

```python
text = text.lower()
```

---

## 7. `upper()`

`upper()` converts alphabetic characters to uppercase.

```python
text = "python"

print(text.upper())
```

Output:

```text
PYTHON
```

Example:

```python
name = "yaswanthi"

name = name.upper()

print(name)
```

Output:

```text
YASWANTHI
```

---

## 8. `strip()`

`strip()` removes unnecessary spaces from the beginning and end of a string.

```python
text = "   Python   "

print(text.strip())
```

Output:

```text
Python
```

This is especially useful when taking input from users.

```python
name = input("Enter your name: ")

name = name.strip()

print(name)
```

---

## 9. `replace()`

`replace()` replaces one piece of text with another.

Syntax:

```python
string.replace(old, new)
```

Example:

```python
text = "I love Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

Output:

```text
I love Python
```

Another example:

```python
text = "I like apples"

text = text.replace("apples", "mangoes")

print(text)
```

Output:

```text
I like mangoes
```

---

## 10. `split()`

`split()` divides a string into smaller pieces and returns a **list**.

```python
text = "Python is easy"

words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy']
```

So `text.split()` converts `"Python is easy"` into `["Python", "is", "easy"]`.

This is very useful when counting words.

```python
text = "Python is easy to learn"

words = text.split()

print(len(words))
```

Output:

```text
5
```

---

## 11. `join()`

`join()` combines multiple strings into one string.

```python
words = ["Python", "is", "easy"]

text = " ".join(words)

print(text)
```

Output:

```text
Python is easy
```

Here `" ".join(words)` means join the words using a space.

### Using another separator

```python
words = ["Python", "SQL", "Git"]

result = ", ".join(words)

print(result)
```

Output:

```text
Python, SQL, Git
```

---

## 12. `split()` vs `join()`

### `split()` — String → List

```python
text = "Python is easy"

words = text.split()
```

Result:

```python
["Python", "is", "easy"]
```

### `join()` — List → String

```python
words = ["Python", "is", "easy"]

text = " ".join(words)
```

Result:

```text
Python is easy
```

Remember:

```text
split() → separates
join()  → combines
```

---

## 13. `in` Operator

The `in` operator checks whether something exists inside a string.

```python
text = "Python is easy"

print("Python" in text)
```

Output:

```text
True
```

```python
print("Java" in text)
```

Output:

```text
False
```

---

## 14. `not in`

`not in` checks whether something does **not** exist in a string.

```python
text = "Python is easy"

print("Java" not in text)
```

Output:

```text
True
```

```python
if "Python" in text:
    print("Python found")
```

---

## 15. f-Strings

f-strings are used to easily combine variables and text.

```python
name = "Yaswanthi"
age = 23

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Yaswanthi and I am 23 years old.
```

The important syntax is:

```python
f"Text {variable}"
```

```python
language = "Python"

print(f"I am learning {language}.")
```

Output:

```text
I am learning Python.
```

---

## 16. Strings and Loops

A string can be looped through character by character.

```python
text = "Python"

for char in text:
    print(char)
```

Output:

```text
P
y
t
h
o
n
```

Here, `char` represents one character at a time.

---

## 17. Counting Characters

We can use a loop to count characters.

```python
text = "hello"

count = 0

for char in text:
    count += 1

print(count)
```

Output:

```text
5
```

We can also simply use `len(text)`.

---

## 18. Character Frequency

A **frequency** tells us how many times something occurs.

Example: `hello`

Character frequency:

```text
h → 1
e → 1
l → 2
o → 1
```

We can use a dictionary.

```python
text = "hello"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)
```

Output:

```python
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

### How it works

Initially: `frequency = {}`

When we see `h`: `frequency["h"] = 1`

When we see `e`: `frequency["e"] = 1`

When we see the first `l`: `frequency["l"] = 1`

When we see the second `l`: `frequency["l"] += 1`

So: `frequency["l"] = 2`

---

## 19. Case-Insensitive Searching

Strings are case-sensitive.

```python
text = "Python"

print("python" in text)
```

Output:

```text
False
```

Because `Python` and `python` are different in terms of uppercase/lowercase.

We can use `lower()` to perform a case-insensitive search.

```python
text = "Python"

if "python" in text.lower():
    print("Word found")
```

Output:

```text
Word found
```

---

## 20. Counting Specific Characters

Python provides `count()`.

```python
text = "hello"

print(text.count("l"))
```

Output:

```text
2
```

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## 21. Counting Sentences

For a basic Text Analyzer, we can count periods:

```python
text = "Python is easy. Python is powerful."

sentences = text.count(".")

print(sentences)
```

Output:

```text
2
```

This is a simple approach for our project.

---

## 22. Text Analyzer Project

The Day 11 project is a **Text Analyzer**.

The program takes text from the user and analyzes it.

Basic features:

```text
Character count
Word count
Sentence count
```

```python
text = input("Enter some text: ")

characters = len(text)

words = len(text.split())

sentences = text.count(".")

print("\n===== TEXT ANALYZER =====")
print(f"Characters: {characters}")
print(f"Words: {words}")
print(f"Sentences: {sentences}")
```

Example input:

```text
Python is easy to learn.
```

The program analyzes the text and displays the counts.

---

## 23. Word Search

We can search for a word inside the text.

```python
word = input("Enter a word to search: ")

if word.lower() in text.lower():
    print("Word found!")
else:
    print("Word not found.")
```

### Why use `lower()`?

Suppose `text = "Python is easy"` and the user enters `python`.

Without `lower()`: `"python" in "Python is easy"` returns `False`.

With `word.lower() in text.lower()`, the comparison becomes
`python in python is easy`, so it returns `True`.

---

## 24. Character Frequency in Text Analyzer

We can add character frequency to the project.

```python
frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("\nCharacter Frequency:")

for char, count in frequency.items():
    print(f"{char}: {count}")
```

### Important

```python
if char != " ":
```

means: ignore spaces. Without it, the dictionary would also count spaces.

---

## 25. Important String Concepts

| Concept     | Meaning                          |
| ----------- | --------------------------------- |
| `str`       | String data type                 |
| `text[0]`   | Access first character           |
| `text[-1]`  | Access last character            |
| `text[1:4]` | Slice string                     |
| `len(text)` | Get length                       |
| `lower()`   | Convert to lowercase             |
| `upper()`   | Convert to uppercase             |
| `strip()`   | Remove beginning/end spaces      |
| `replace()` | Replace text                     |
| `split()`   | String → List                    |
| `join()`    | List → String                    |
| `in`        | Check if something exists        |
| `not in`    | Check if something doesn't exist |
| `count()`   | Count occurrences                |
| `f""`       | Formatted string                 |

---

## 26. Important Rules to Remember

**Rule 1 — Index starts at 0**

```python
text[0]
```

is the first character.

**Rule 2 — Negative index starts from -1**

```python
text[-1]
```

is the last character.

**Rule 3 — Slicing excludes the stop index**

```python
text[0:3]
```

includes indexes `0, 1, 2` but not `3`.

**Rule 4 — Strings are immutable**

You cannot directly change an individual character. This will not work:

```python
text = "Python"

text[0] = "J"
```

Instead, create a new string using methods such as:

```python
text = text.replace("P", "J")
```

**Rule 5 — String methods usually return a new string**

```python
text = "python"

text.upper()

print(text)
```

still prints `python`. To keep the result:

```python
text = text.upper()
```

---

## 27. Problems Faced

```text
- Initially confused about string indexing starting from 0.
- Initially confused about the stop index in slicing.
- Confused between split() and join().
- Forgot that strings are case-sensitive.
- Initially confused about how character frequency works with dictionaries.
```

---

## 28. What I Learned

I learned that strings are sequences of characters and that Python provides
many built-in operations and methods for working with text.

I learned how indexing and slicing work, including negative indexing.

I learned how to use common string methods such as `lower()`, `upper()`,
`strip()`, `replace()`, `split()`, `join()`, and `count()`.

I also learned how to search inside strings using `in` and `not in`.

I practiced looping through strings and using dictionaries to calculate
character frequency.

Finally, I used these concepts to build a Text Analyzer project.

---

## 29. Git Commands Used

```bash
git status
git add .
git commit -m "Complete Day 11 strings"
git push
```
