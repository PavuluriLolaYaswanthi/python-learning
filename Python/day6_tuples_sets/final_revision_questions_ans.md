# tuples & sets

## 16. Final Revision Questions

### 1. What is the difference between a list and a tuple?

A **list** is mutable, which means we can modify its elements after creation. A **tuple** is immutable, which means we cannot modify its elements after creation.

```python
my_list = [10, 20, 30]
my_list[0] = 100
print(my_list)  # [100, 20, 30]

my_tuple = (10, 20, 30)
# my_tuple[0] = 100  # TypeError
```

### 2. What does immutable mean?

Immutable means that an object's contents cannot be changed after it is created.

**Example:** A tuple does not allow us to replace one of its elements.

```python
numbers = (10, 20, 30)
# numbers[1] = 50  # TypeError
```

### 3. Can a tuple contain duplicate values?

**Yes.** Tuples allow duplicate values.

```python
numbers = (10, 20, 10, 30, 20)
print(numbers)
```

Output:

```text
(10, 20, 10, 30, 20)
```

### 4. Why can't we access set elements using indexes?

Sets do not support positional indexing because they are unordered collections without guaranteed element positions.

```python
numbers = {10, 20, 30}
# print(numbers[0])  # TypeError
```

To access elements, we can iterate through the set:

```python
for number in numbers:
    print(number)
```

### 5. How can we remove duplicates from a list?

We can use `set()` to remove duplicates. However, the original order is not guaranteed.

```python
numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(set(numbers))
print(unique_numbers)
```

If we want to **preserve the original order**, use `dict.fromkeys()`:

```python
numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)
```

Output:

```text
[10, 20, 30, 40]
```

### 6. What is the difference between `remove()` and `discard()`?

Both methods remove an element from a set.

* `remove()` raises a `KeyError` if the element does not exist.
* `discard()` does not raise an error if the element does not exist.

```python
numbers = {10, 20, 30}

numbers.remove(20)
numbers.discard(50)

print(numbers)
```

Output:

```text
{10, 30}
```

### 7. What is the difference between union and intersection?

**Union** combines all unique elements from both sets.

**Intersection** returns only the elements common to both sets.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union
print(a & b)  # Intersection
```

Output:

```text
{1, 2, 3, 4, 5, 6}
{3, 4}
```

### 8. What does the difference operation return?

The difference operation returns elements that are in the first set but not in the second set.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a - b)
```

Output:

```text
{1, 2}
```

Note: `b - a` would return `{5, 6}`.

### 9. What is symmetric difference?

Symmetric difference returns elements that belong to either set but **not to both sets**.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a ^ b)
```

Output:

```text
{1, 2, 5, 6}
```

The common elements `3` and `4` are excluded.

### 10. How do you create an empty set in Python?

Use `set()` to create an empty set.

```python
empty_set = set()
print(type(empty_set))
```

Output:

```text
<class 'set'>
```

**Important:** `{}` creates an empty dictionary, not an empty set.
