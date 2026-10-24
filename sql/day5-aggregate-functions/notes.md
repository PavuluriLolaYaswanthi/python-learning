# Day 5 — SQL Aggregate Functions

## Topics Learned

- Aggregate functions
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
- COUNT(DISTINCT column)
- Aggregate functions with WHERE
- Column aliases using AS
- Handling NULL values in aggregate calculations

## Practical Work

- Counted student records.
- Calculated total marks.
- Calculated average marks.
- Found minimum and maximum marks.
- Counted distinct courses.
- Filtered aggregate calculations by course.
- Combined five aggregate functions in one query.
- Completed 10 practice exercises.

## Aggregate Functions Summary

| Function | Purpose | Result on original data |
| -------- | ------- | ----------------------- |
| `COUNT(*)` | Counts all rows | 5 |
| `SUM(marks)` | Adds up values | 425.5 |
| `AVG(marks)` | Average of non-NULL values | 85.1 |
| `MIN(marks)` | Smallest value | 78.5 |
| `MAX(marks)` | Largest value | 92.0 |

## Important Concepts

- **COUNT:** `COUNT(*)` counts every row; `COUNT(column)` counts only non-NULL values; `COUNT(DISTINCT column)` counts unique non-NULL values.
- **SUM:** Adds numeric values, e.g. total marks = 85.5 + 92.0 + 78.5 + 88.0 + 81.5 = 425.5.
- **AVG:** Sum divided by the number of non-NULL values (425.5 / 5 = 85.1). A NULL is ignored, not treated as 0.
- **MIN / MAX:** Return the lowest and highest value; both ignore NULLs and also work on text.
- **WHERE:** Filters rows before the aggregate is calculated.
- **AS:** Gives a result column a readable name.
- **NULL behaviour:** If there are no non-NULL values, `SUM`, `AVG`, `MIN`, and `MAX` return NULL, and `COUNT` returns 0.

## Example Query

```sql
SELECT
    COUNT(*) AS total_students,
    SUM(marks) AS total_marks,
    AVG(marks) AS average_marks,
    MIN(marks) AS lowest_marks,
    MAX(marks) AS highest_marks
FROM students;
```

| total_students | total_marks | average_marks | lowest_marks | highest_marks |
| -------------- | ----------- | ------------- | ------------ | ------------- |
| 5 | 425.5 | 85.1 | 78.5 | 92.0 |

## Problems Faced

- If Day 4 changed the data (inserts, updates, deletes), the results won't match the expected numbers until the original five records are restored.
- Confusing `COUNT(*)` with `COUNT(column)` when NULLs are present.
- Forgetting quotes around text in `WHERE`, such as `course = 'CSE'`.
- Assuming `AVG()` treats NULL as 0; it skips NULLs instead.

## What I Learned

I learned how to summarize database records using aggregate functions. I can calculate counts, totals, averages, minimums, and maximums and apply filters to analyze specific groups of records.

## Next Day

Learn GROUP BY, HAVING, and JOIN.
