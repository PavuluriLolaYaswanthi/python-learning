# Day 4 Notes — Functions

## Topics Learned
- Functions
- Parameters
- Arguments
- Return values
- Reusable code
- Unit Converter project

---

## What is a Function?

A function is a reusable block of code that performs a specific task.

Functions help:
- Reduce duplicate code
- Improve readability
- Organize programs
- Make debugging easier

---

## Important Concepts

### Function Definition

A function is created using the `def` keyword.

```python
def greet():
    print("Hello")
```

---

### Function Call

A function runs only when it is called.

```python
greet()
```

Output:

```text
Hello
```

---

### Parameters

Parameters are variables that receive values when a function is called.

```python
def greet(name):
    print(name)
```

---

### Arguments

Arguments are the actual values passed to a function.

```python
greet("Yaswanthi")
```

Here:

```text
Parameter = name
Argument = "Yaswanthi"
```

---

### Return

The `return` keyword sends a value back from a function.

```python
def add(a, b):
    return a + b
```

---

## Difference Between print() and return

### print()

- Displays output on the screen.
- Used for showing information to the user.
- Cannot easily reuse the output.

Example:

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

```text
30
```

---

### return

- Sends a value back from a function.
- Returned values can be stored in variables.
- Returned values can be reused in calculations and program logic.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

### Key Differences

| print() | return |
|----------|----------|
| Displays output on screen | Sends value back from function |
| Used for showing information | Used for calculations and logic |
| Cannot easily reuse output | Can store and reuse output |
| Does not return a value | Returns a value to the caller |

---

## Practice Done

- Created basic functions
- Practiced function calls
- Worked with parameters
- Worked with arguments
- Used return values
- Built a Unit Converter project

---

## Main Project Built

### Unit Converter

Features:
- KM to Miles conversion
- Celsius to Fahrenheit conversion
- Menu-based user input
- Functions used for each conversion

---

## Problems Faced

- Forgot to call functions
- Confused between parameters and arguments
- Confused between print() and return
- Indentation mistakes

---

## What I Learned

Today I learned how functions help organize code into reusable blocks. I practiced creating functions, calling functions, passing parameters and arguments, and using return values. I also learned the difference between print() and return and built a Unit Converter project using functions.

---

## Interview Questions

### What is a function?

A function is a reusable block of code that performs a specific task.

### What is the difference between a parameter and an argument?

- Parameter: Variable defined in a function.
- Argument: Actual value passed to a function.

### What is the difference between print() and return?

- `print()` displays output on the screen.
- `return` sends a value back from a function.
- Values returned using `return` can be stored in variables and reused later.
- `print()` is mainly for displaying information, while `return` is used for program logic and calculations.

---

## Commands Used

```bash
python functions_basics.py
python parameters.py
python return_values.py
python unit_converter.py

git add .
git commit -m "Day 4 functions and unit converter"
git push
```