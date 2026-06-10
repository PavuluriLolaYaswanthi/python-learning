# Day 3 Notes — Loops

## Topics Learned
- for loops
- while loops
- range()
- iteration
- repetition in programming

---

## What Is A Loop?
A loop is used to repeat code multiple times automatically.

Loops help reduce repetitive code and make programs efficient.

---

## Types of Loops Learned

### 1. for Loop
Used when the number of repetitions is known.

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

### 2. while Loop
Used when repetition depends on a condition.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Important Concepts

### range()
Used to generate sequence of numbers.

Examples:

```python
range(5)
```

Gives:

```text
0 1 2 3 4
```

---

```python
range(1, 6)
```

Gives:

```text
1 2 3 4 5
```

---

### count += 1

Shortcut for:

```python
count = count + 1
```

Used to update loop variable.

---

## Practice Done
- for loop examples
- while loop examples
- range() practice
- multiplication table generator

---

## Main Project Built
### Multiplication Generator

Program takes a number from user and prints multiplication table.

Example:

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

## Problems Faced
- Indentation mistakes
- Forgot loop stopping condition
- Confused about range ending value

---

## What I Learned
Today I learned how loops automate repeated tasks in programming. I practiced for loops, while loops, and range(). I understood iteration and built a multiplication generator project using loops.

---

## Commands Used

```bash
python for_loop.py
python while_loop.py
python range_loop.py
python multiplication_generator.py

git add .
git commit -m "Day 3 loops and multiplication generator"
git push
```