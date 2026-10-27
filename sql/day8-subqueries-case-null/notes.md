# SQL Day 8 — Subqueries, CASE, and NULL

## Topics Learned

1. **Subqueries**
   - A query inside another SQL query.
   - Using subqueries with `WHERE`.
   - Using `AVG()`, `MAX()`, and `MIN()` in subqueries.
   - Using `IN` with a subquery.
2. **CASE Statements**
   - `CASE`, `WHEN`, `THEN`, `ELSE`, and `END`.
   - Creating grades and categories from conditions.
   - Similarity between SQL `CASE` and Python `if-elif-else`.
3. **NULL Values**
   - NULL represents a missing or unknown value.
   - `IS NULL` checks for missing values.
   - `IS NOT NULL` checks for present values.
   - `COALESCE()` provides a fallback value.
   - `COUNT(column)` ignores NULL values, while `COUNT(*)` counts rows.

## Practical Work

- Created `day8_students` and `day8_expenses` tables.
- Found students scoring above average.
- Found students with the highest or lowest marks.
- Classified students using CASE.
- Categorized expenses using CASE.
- Found missing city values.
- Used COALESCE() to display a default city.
- Completed 10 SQL practice questions.

## Important Concepts

### Subqueries

- The inner query runs first and supplies a value to the outer query.
- A subquery used with `=`, `>`, or `<` should return a single value; use `IN` when it can return several.

```sql
SELECT name, marks
FROM day8_students
WHERE marks > (SELECT AVG(marks) FROM day8_students);
```

Average marks = 77.6, so this returns Ravi (85), Priya (92), and Sneha (88).

### CASE

- Works like Python `if / elif / else` and creates a result column without changing stored data.
- `WHEN` conditions are checked in order and the first match wins, so put the highest thresholds first.

```sql
CASE
    WHEN marks >= 90 THEN 'Excellent'
    WHEN marks >= 80 THEN 'Very Good'
    ELSE 'Needs Improvement'
END AS grade
```

### NULL

- NULL means missing or unknown; it is not 0, an empty string, or the text `'NULL'`.
- Use `IS NULL` / `IS NOT NULL`, never `= NULL`.
- `COALESCE(city, 'Unknown')` returns the first non-NULL argument (output only, stored data unchanged).
- `AVG()` ignores NULLs; `COUNT(*)` counts all rows; `COUNT(column)` counts non-NULL values.

## Problems Faced

- Understanding how the inner query supplies a value to the outer query.
- Ordering CASE conditions correctly (highest threshold first).
- Understanding why NULL requires `IS NULL` instead of `=`.
- Remembering that `COUNT(column)` skips NULLs but `COUNT(*)` does not.

## What I Learned

I learned how to use subqueries to compare records with aggregate results, CASE to create conditional output, and NULL functions to handle missing information.

## Next Day

Practice SQL Days 1–8 and learn transactions, including BEGIN, COMMIT, and ROLLBACK.
