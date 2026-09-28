# Day 13 Notes — Data Structure Problem Solving

## Topics Practiced

- Lists
- Dictionaries
- Strings
- Loops
- Conditions
- Functions
- List comprehensions
- Dictionary comprehensions
- Problem solving
- Debugging

---

## Problems Solved

1. Find largest number
2. Find smallest number
3. Sum of numbers
4. Count even numbers
5. Remove duplicates
6. Reverse a string
7. Count vowels
8. Count words
9. Check palindrome
10. Character frequency
11. Highest student marks
12. Average marks
13. Filter passing students
14. Word frequency
15. Filter expensive expenses
16. Second largest number
17. Common elements
18. Separate even and odd
19. Word length dictionary
20. Mini expense analysis

---

## Code

All 20 solutions are saved separately in `practice.py`.

---

## Important Concepts

### Dictionary methods: `.keys()`, `.values()`, `.items()`

A dictionary stores **key: value** pairs. These three methods decide what a loop receives.

| Method     | Gives you                     | Used In                |
| ---------- | ----------------------------- | ---------------------- |
| `.keys()`   | only the **key**              | looping over names     |
| `.values()` | only the **value**            | Problem 12 (average)   |
| `.items()`  | both the **key AND the value**| Problems 11, 13, 15    |

```python
marks = {"Alice": 90, "Bob": 55, "Charlie": 80}

print(marks.keys())
print(marks.values())
print(marks.items())
```

Output:

```text
dict_keys(['Alice', 'Bob', 'Charlie'])
dict_values([90, 55, 80])
dict_items([('Alice', 90), ('Bob', 55), ('Charlie', 80)])
```

Looping with each one:

```python
for name in marks.keys():
    print(name)              # Alice, Bob, Charlie

for mark in marks.values():
    print(mark)              # 90, 55, 80

for name, mark in marks.items():
    print(name, mark)        # Alice 90, Bob 55, Charlie 80
```

**When to use which**

- Need only the names → `.keys()`
- Need only the numbers (sum, average) → `.values()`
- Need to compare a value **and** remember whose it is (highest marks, filtering) → `.items()`

Looping directly over a dictionary gives the **keys**, so `for name in marks:` is the same as `for name in marks.keys():`.
This is why Problem 14 needs a list of words: looping over a dictionary only visits each key once, so every count stays 1.

---

### `float("inf")` — Infinity as a Starting Value

```python
lowest_marks = float("inf")   # infinity: bigger than any real mark
```

`float("inf")` is a special number that is **bigger than every other number**.
`float("-inf")` is the opposite: **smaller than every other number**.

```python
print(5 < float("inf"))        # True
print(-5 > float("-inf"))      # True
```

**Why use it?**

When finding the lowest value, the starting value must be larger than every real value. Then the first mark always replaces it:

```python
marks = {"Alice": 90, "Bob": 55, "David": 45}
lowest_marks = float("inf")

for name, mark in marks.items():
    if mark < lowest_marks:
        lowest_marks = mark

print(lowest_marks)
```

Output:

```text
45
```

Why not start with `0`?

```text
Starting with 0 for the lowest → no mark is smaller than 0 → the answer never updates (wrong).
Starting with 0 for the highest → fails if every number is negative (wrong).
```

| Finding      | Safe starting value                    |
| ------------ | -------------------------------------- |
| Lowest       | `float("inf")` or the first item       |
| Highest      | `float("-inf")` or the first item      |

---

## Patterns Used

| Pattern                        | Used In                |
| ------------------------------ | ---------------------- |
| Track a running max / min      | Problems 1, 2, 11, 16  |
| Running total (accumulator)    | Problems 3, 12, 20     |
| Counter variables              | Problems 4, 7, 8       |
| Build a new list with `append` | Problems 5, 17, 18     |
| Build a string in a loop       | Problems 6, 9          |
| Frequency dictionary           | Problems 10, 14        |
| Dictionary comprehension       | Problems 13, 15, 19    |
| `sorted()` with `lambda`       | Problem 19             |

---

## Dictionary Methods: `.keys()`, `.values()`, `.items()`

A dictionary stores **key → value** pairs. These three methods let a loop pick which part it needs.

| Method       | Gives you                    |
| ------------ | ---------------------------- |
| `.keys()`    | only the keys                |
| `.values()`  | only the values              |
| `.items()`   | both the key **and** the value |

```python
marks = {"Alice": 90, "Bob": 55, "Charlie": 80}

print(marks.keys())
print(marks.values())
print(marks.items())
```

Output:

```text
dict_keys(['Alice', 'Bob', 'Charlie'])
dict_values([90, 55, 80])
dict_items([('Alice', 90), ('Bob', 55), ('Charlie', 80)])
```

### Looping with each one

```python
for name in marks.keys():
    print(name)
```

```text
Alice
Bob
Charlie
```

```python
for mark in marks.values():
    print(mark)
```

```text
90
55
80
```

```python
for name, mark in marks.items():
    print(name, mark)
```

```text
Alice 90
Bob 55
Charlie 80
```

Looping directly over a dictionary (`for name in marks:`) is the same as looping over `.keys()`.

### Where I used them

| Method       | Used In                                                   |
| ------------ | --------------------------------------------------------- |
| `.values()`  | Problem 12 — only the marks were needed to calculate the average |
| `.items()`   | Problems 11, 13, 15 — both the name and the mark/amount were needed |
| keys only    | Problem 14 — this looped over keys, so every count was 1 |

Rule of thumb:

```text
Need only the key?    → .keys()
Need only the value?  → .values()
Need both?            → .items()
```

---

## `float("inf")` — Infinity as a Starting Value

```python
lowest_marks = float("inf")   # infinity: bigger than any real mark
```

`float("inf")` is a special number that is **larger than every other number**.

This makes it a safe starting value when looking for the **lowest** value:

```python
marks = {"Alice": 90, "Bob": 55, "Charlie": 80, "David": 45}
lowest_marks = float("inf")

for mark in marks.values():
    if mark < lowest_marks:
        lowest_marks = mark

print(lowest_marks)
```

Output:

```text
45
```

Why it works: the first mark (`90`) is always smaller than infinity, so it replaces the starting value, and the loop continues from there.

The opposite is `float("-inf")`, which is **smaller than every other number**. It is a safe starting value when looking for the **highest** value.

```python
highest_marks = float("-inf")
```

### Why not start with `0`?

Starting with `0` only works when every value is positive.

```python
numbers = [-5, -2, -9]
largest = 0

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

Output:

```text
0
```

This is wrong, because `0` is not in the list. Starting with `float("-inf")` (or with the first item, `numbers[0]`) fixes it.

| Goal              | Safe starting value                |
| ----------------- | ---------------------------------- |
| Find the lowest   | `float("inf")` or the first item   |
| Find the highest  | `float("-inf")` or the first item  |

---

## Functions I Practiced

- `count_even_numbers(numbers)` — returns how many even numbers are in a list (Problem 4)
- `find_largest(numbers)` — returns the largest number without using `max()` (Problem 1)
- `count_word_frequency(words)` — returns a dictionary of how many times each word appears (Problem 14)

Each function takes the data as a **parameter** and uses `return` to send the result back, so the result can be stored and reused. The code is in `practice.py`.

---

## Problems I Found Difficult

- **Problem 11 — Highest / lowest marks:** choosing the right starting value (`float("inf")`) and using `.items()` to get the name and the mark together
- **Problem 14 — Word frequency:** looping over a list of words instead of dictionary keys, and the `if word in dict` / `else` counting pattern
- **Problem 16 — Second largest / smallest:** updating both variables in the right order, and the `elif` branch that handles numbers between the two

---

## Errors I Faced

- Problem 10: forgot to print the frequency after building the dictionary
- Problem 12: calculated the average inside the loop instead of after it
- Problem 14: looped over dictionary keys instead of a list of words, so every count was 1
- Problems 11 and 16: starting with `0` breaks for negative numbers; use the first item or `float("-inf")` instead

---

## What I Learned

Today I practiced solving Python problems using lists,
dictionaries, strings, loops, conditions, functions,
and comprehensions.

I learned that solving problems requires breaking a
large problem into smaller steps before writing code.

---

## Key Takeaway

I should understand the problem first, create a simple
solution, test it, and then improve the code if necessary.

---

## Git Commands Used

```bash
git status
git add .
git commit -m "Complete Day 13 data structure problems"
git push
```