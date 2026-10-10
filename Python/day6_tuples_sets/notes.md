# Day 9 – Tuples and Sets

## 1. Topics Learned

* Tuples
* Tuple indexing and slicing
* Tuple methods: `count()` and `index()`
* Sets
* Adding and removing set elements
* Removing duplicates
* Set operations: union, intersection, difference, and symmetric difference
* Differences between lists, tuples, and sets

---

## 2. What Is a Tuple?

A tuple is a collection of elements that is **ordered and immutable**.

Immutable means that the elements of a tuple cannot be changed after the tuple is created.

### Example

```python
student = ("Yaswanthi", 23, 9.12)

print(student)
print(student[0])
print(student[1])
print(student[2])
```

### Output

```text
('Yaswanthi', 23, 9.12)
Yaswanthi
23
9.12
```

### Important points

* Tuples use parentheses `()`.
* Tuples allow duplicate values.
* Tuples support indexing and slicing.
* Tuples cannot be modified after creation.
* Tuples are useful for storing fixed collections of data.

---

## 3. Tuple Indexing

Indexing is used to access individual elements.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[0])
print(numbers[2])
print(numbers[-1])
```

### Output

```text
10
30
50
```

* Positive indexing starts from `0`.
* Negative indexing starts from `-1` at the end.

---

## 4. Tuple Slicing

Slicing is used to access a portion of a tuple.

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

### Output

```text
(20, 30, 40)
```

The starting index is included, but the ending index is excluded.

---

## 5. Tuple Methods

### `count()`

Returns how many times a value occurs.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

Output:

```text
3
```

### `index()`

Returns the index of the first occurrence of a value.

```python
numbers = (10, 20, 30)

print(numbers.index(20))
```

Output:

```text
1
```

---

## 6. What Is a Set?

A set is a collection of **unique elements**. It automatically removes duplicate values.

### Example

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

The set contains only `10`, `20`, and `30`. The order of elements is not guaranteed.

### Important points

* Sets are written using curly braces `{}` with elements inside.
* Sets do not allow duplicate elements.
* Sets are mutable, so elements can be added or removed.
* Sets do not support indexing or slicing.
* Sets are useful for removing duplicates and performing set operations.

**Important:** An empty set is created using `set()`, not `{}`. Empty curly braces create an empty dictionary.

```python
empty_set = set()
empty_dictionary = {}
```

---

## 7. Adding and Removing Set Elements

### `add()`

Adds an element to a set.

```python
fruits = {"apple", "banana"}

fruits.add("mango")

print(fruits)
```

### `remove()`

Removes an element. Raises a `KeyError` if the element does not exist.

```python
fruits = {"apple", "banana", "mango"}

fruits.remove("banana")

print(fruits)
```

### `discard()`

Removes an element if it exists. Does not raise an error if it is missing.

```python
fruits = {"apple", "banana"}

fruits.discard("orange")

print(fruits)
```

---

## 8. Removing Duplicates from a List

There are two common ways to remove duplicate values from a list.

### Method 1: Using `set()`

A set removes duplicate values, but it does not guarantee that the original list order is preserved.

```python
numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

The result contains only the unique numbers, but their order may differ from the original list.

### Method 2: Using `dict.fromkeys()`

`dict.fromkeys()` creates a dictionary using the list elements as keys. Since dictionary keys are unique and dictionaries preserve insertion order, this method removes duplicates while **keeping the original order**.

```python
numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

### Output

```text
[10, 20, 30, 40]
```

### How does it work?

**Step 1:** Start with the original list.

```python
numbers = [10, 20, 10, 30, 20, 40, 10]
```

**Step 2:** Create a dictionary using `dict.fromkeys(numbers)`.

```python
print(dict.fromkeys(numbers))
```

Output:

```text
{10: None, 20: None, 30: None, 40: None}
```

Each number becomes a dictionary key. Duplicate keys are automatically removed, and the first insertion order is preserved.

**Step 3:** Convert the dictionary keys back into a list.

```python
unique_numbers = list(dict.fromkeys(numbers))
```

Output:

```text
[10, 20, 30, 40]
```

### Important Concepts

* `set(numbers)` removes duplicates but does not guarantee original order.
* `dict.fromkeys(numbers)` creates unique dictionary keys in insertion order.
* `list(dict.fromkeys(numbers))` converts those keys back into a list, preserving the original order of the first occurrences.
* Dictionary keys must be hashable; this method works for ordinary numbers and strings.

### Which method should I use?

| Requirement                                   | Method                         |
| --------------------------------------------- | ------------------------------ |
| Remove duplicates; order does not matter      | `list(set(numbers))`           |
| Remove duplicates and preserve original order | `list(dict.fromkeys(numbers))` |

**Key takeaway:** Use `list(dict.fromkeys(numbers))` when you want to remove duplicates without changing the order of the remaining elements.

## 9. Set Operations

Consider these two sets:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

### Union

Combines all unique elements from both sets.

```python
print(a | b)
print(a.union(b))
```

Result: `{1, 2, 3, 4, 5, 6}`

### Intersection

Returns elements common to both sets.

```python
print(a & b)
print(a.intersection(b))
```

Result: `{3, 4}`

### Difference

Returns elements present in the first set but not in the second.

```python
print(a - b)
print(a.difference(b))
```

Result: `{1, 2}`

### Symmetric Difference

Returns elements present in either set, but not in both.

```python
print(a ^ b)
print(a.symmetric_difference(b))
```

Result: `{1, 2, 5, 6}`

---

## 10. List vs Tuple vs Set

| Feature      | List                  | Tuple            | Set                 |
| ------------ | --------------------- | ---------------- | ------------------- |
| Syntax       | `[]`                  | `()`             | `{}`                |
| Ordered      | Yes                   | Yes              | No guaranteed order |
| Duplicates   | Allowed               | Allowed          | Not allowed         |
| Mutable      | Yes                   | No               | Yes                 |
| Indexing     | Yes                   | Yes              | No                  |
| Main purpose | Changeable collection | Fixed collection | Unique elements     |

### When should I use each?

* **List:** When I need to store and modify a collection of items.
* **Tuple:** When I need to store a collection that should not be modified.
* **Set:** When I need unique elements or want to compare collections using set operations.

---

## 12. Problems Faced

* Understanding the difference between mutable and immutable collections.
* Remembering that sets do not support indexing.
* Understanding the difference between union and intersection.
* Remembering that set element order is not guaranteed.

## 13. Important Concepts

* A tuple is ordered and immutable.
* A set stores unique elements.
* Lists and tuples support indexing; sets do not.
* `count()` counts occurrences in a tuple.
* `index()` finds the first occurrence of a value in a tuple.
* `add()` adds an element to a set.
* `remove()` raises an error if the element is absent; `discard()` does not.
* Union combines unique elements.
* Intersection finds common elements.
* Difference finds elements in one set but not the other.
* Symmetric difference finds elements that are not shared.

## 14. What I Learned

I learned how to create and access tuples, use tuple methods, create and modify sets, remove duplicates, and perform set operations. I also learned when to choose a list, tuple, or set based on the requirements of a program.

## 15. GitHub Commands

```bash
git status
git add .
git commit -m "Complete Day 9 tuples and sets practice"
git push
git status
```

## 16. Final Revision Questions

1. What is the difference between a list and a tuple?
2. What does immutable mean?
3. Can a tuple contain duplicate values?
4. Why can't we access set elements using indexes?
5. How can we remove duplicates from a list?
6. What is the difference between `remove()` and `discard()`?
7. What is the difference between union and intersection?
8. What does the difference operation return?
9. What is symmetric difference?
10. How do you create an empty set in Python?
