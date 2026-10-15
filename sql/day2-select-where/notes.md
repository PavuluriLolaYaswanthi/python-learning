# Day 2 — SELECT, WHERE and Comparison Operators

## Topics Learned

- SELECT statement
- Selecting specific columns
- WHERE clause
- Filtering records
- Comparison operators: `=`, `!=`, `>`, `<`, `>=`, `<=`
- Comparing text and numeric values

## Key Syntax

```sql
SELECT column_names
FROM table_name
WHERE condition;
```

- Column selection controls which information appears.
- Filtering (`WHERE`) controls which records appear.
- Order of clauses: `SELECT`, then `FROM`, then `WHERE`.

## Comparison Operators

| Operator | Meaning | Example |
| -------- | ------- | ------- |
| `=` | Equal to | `age = 22` |
| `!=` (or `<>`) | Not equal to | `course != 'CSE'` |
| `>` | Greater than | `marks > 85` |
| `<` | Less than | `age < 23` |
| `>=` | Greater than or equal to | `marks >= 88` |
| `<=` | Less than or equal to | `age <= 22` |

## Practical Work

- Practiced selecting individual columns.
- Filtered students by age, marks, and course.
- Completed 10 filtering exercises.

### Exercise Solutions

```sql
-- 1. Names of all students
SELECT name FROM students;

-- 2. Names and ages of students aged exactly 22 (Ravi, Sneha)
SELECT name, age FROM students WHERE age = 22;

-- 3. Marks greater than 80 (Ravi, Priya, Sneha, Kiran)
SELECT * FROM students WHERE marks > 80;

-- 4. Marks less than 85 (Arjun, Kiran)
SELECT * FROM students WHERE marks < 85;

-- 5. Not enrolled in Cybersecurity (Ravi, Arjun, Sneha)
SELECT * FROM students WHERE course != 'Cybersecurity';

-- 6. Aged 23 or older (Priya, Kiran)
SELECT * FROM students WHERE age >= 23;

-- 7. Marks 85 or lower (Arjun, Kiran)
SELECT * FROM students WHERE marks <= 85;

-- 8. Course exactly CSE (Ravi, Sneha)
SELECT * FROM students WHERE course = 'CSE';

-- 9. Marks exactly 92 (Priya)
SELECT * FROM students WHERE marks = 92;

-- 10. Names and marks where marks >= 88 (Priya, Sneha)
SELECT name, marks FROM students WHERE marks >= 88;
```

## Important Concepts

- `SELECT *` retrieves all columns.
- `WHERE` filters records based on a condition.
- `=` checks equality; `!=` checks inequality.
- `>` and `<` are strict comparisons that exclude the boundary value.
- `>=` and `<=` include the boundary value (Sneha's 88 qualifies for `marks >= 88`).
- Text values must be enclosed in single quotes, e.g. `'CSE'`.
- Ravi's 85.5 is not `<= 85`, so exercise 7 excludes him.

## Problems Faced

- Forgetting quotes around text (`course = CSE`) causes an error; it must be `'CSE'`.
- Using `=` when I meant `>` returns only exact matches.
- Putting `WHERE` before `FROM` causes a syntax error.
- Boundary mistakes: mixing up `>` vs `>=` and `<` vs `<=`.

## What I Learned

I learned how to retrieve specific columns and filter table records using SQL comparison operators, and how small differences like `>` versus `>=` change which rows are returned.

## Next Day

Learn AND, OR, NOT, ORDER BY, and LIMIT.
