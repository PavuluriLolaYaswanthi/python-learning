# Day 3 — SQL Logical Operators, Sorting and Limiting

## Topics Learned

- `AND`
- `OR`
- `NOT`
- Combining multiple conditions with parentheses
- `ORDER BY`
- `ASC` and `DESC`
- Sorting by multiple columns
- `LIMIT`
- Combining filtering, sorting, and limiting

## Practical Work

- Filtered students using multiple conditions.
- Retrieved students matching either of two conditions.
- Excluded students using NOT.
- Sorted records by age and marks.
- Retrieved the top-scoring students using LIMIT.
- Completed 10 SQL practice exercises.

## Important Concepts

| Keyword | Meaning | Effect |
| ------- | ------- | ------ |
| `AND` | All conditions must be true | Narrows results |
| `OR` | At least one condition must be true | Broadens results |
| `NOT` | Reverses a condition | Excludes matching rows |
| `ORDER BY` | Sorts by one or more columns | `ASC` (default) or `DESC` |
| `LIMIT` | Restricts the number of rows returned | Use with `ORDER BY` for top-N |

- `AND` is evaluated before `OR`. Use parentheses to make grouping clear, e.g. `(course = 'CSE' OR course = 'AI') AND marks > 80`.
- `NOT course = 'CSE'` and `course != 'CSE'` give the same result here, but neither returns rows where `course` is `NULL`.
- With multiple sort columns, SQL sorts by the first, then uses the next to break ties: `ORDER BY course ASC, marks DESC`.
- Without `ORDER BY`, `LIMIT` returns rows in no guaranteed order.

### Query Clause Order

`SELECT` → `FROM` → `WHERE` → `ORDER BY` → `LIMIT`

## Example Query

```sql
SELECT name, marks
FROM students
WHERE age >= 22
ORDER BY marks DESC
LIMIT 2;
```

This finds students aged 22 or older, sorts them by marks from highest to lowest, and returns the top two.

## Problems Faced

- Forgetting parentheses when mixing `AND` and `OR` gives unexpected rows because `AND` runs first.
- Writing `LIMIT` before `ORDER BY` causes a syntax error; the order is `WHERE`, `ORDER BY`, `LIMIT`.
- Using `LIMIT` without `ORDER BY` returns rows in an unreliable order.
- Mixing up `ASC` and `DESC` when looking for top scores.

## What I Learned

I learned how to combine SQL conditions, exclude records, sort query results, and limit the number of rows returned. I also practiced combining WHERE, ORDER BY, and LIMIT in one query.

## Next Day

Learn INSERT, UPDATE, DELETE, and safe CRUD operations.
