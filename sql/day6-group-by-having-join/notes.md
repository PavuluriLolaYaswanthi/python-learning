# Day 6 — GROUP BY, HAVING, and JOIN

## Topics Learned

1. `GROUP BY`
2. `HAVING`
3. Difference between `WHERE` and `HAVING`
4. `INNER JOIN`
5. `LEFT JOIN`
6. Aggregate functions with grouped data
7. Joining multiple tables
8. Combining `JOIN`, `GROUP BY`, and `HAVING`

## Important Concepts

### GROUP BY

Groups rows that have the same value in one or more columns so an aggregate can be calculated for each group.

```sql
SELECT category, SUM(amount) AS total_amount
FROM expenses
GROUP BY category;
```

In a grouped query, selected columns should be grouped columns or aggregate calculations.

### HAVING

Filters groups based on aggregate conditions.

```sql
SELECT course, AVG(marks) AS average_marks
FROM students
GROUP BY course
HAVING AVG(marks) > 85;
```

### WHERE vs HAVING

- `WHERE` filters individual rows before grouping.
- `HAVING` filters groups after grouping.
- Typed order: `WHERE` comes before `GROUP BY`; `HAVING` comes after it.

### INNER JOIN

Returns only rows with a match in both tables.

```sql
SELECT students.name, student_details.city
FROM students
INNER JOIN student_details
    ON students.student_id = student_details.student_id;
```

### LEFT JOIN

Returns every row from the left table plus matching rows from the right table. Missing matches give `NULL` on the right side (not 0 or an empty string).

```sql
SELECT students.name, student_details.city
FROM students
LEFT JOIN student_details
    ON students.student_id = student_details.student_id;
```

| Feature | `INNER JOIN` | `LEFT JOIN` |
| ------- | ------------ | ----------- |
| All rows from left table | No | Yes |
| Only matching rows | Yes | No |
| Missing match on the right | Row excluded | Right-side columns are `NULL` |

### Logical processing order (simplified)

`FROM / JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT / ORDER BY`

## Aggregate Functions

| Function | Purpose |
| -------- | ------- |
| `COUNT(*)` | Counts rows |
| `SUM(amount)` | Calculates a total |
| `AVG(marks)` | Calculates an average |
| `MIN(marks)` | Finds the minimum |
| `MAX(marks)` | Finds the maximum |

## Practical Work

- Grouped expenses by category.
- Calculated average marks by course.
- Counted students in each course.
- Filtered grouped results using `HAVING`.
- Combined the students and student_details tables.
- Used `LEFT JOIN` to identify missing details.
- Calculated totals for each expense payer.
- Completed 10 practice questions.23

## Important Results

- Food expenses total: 500
- Shopping expenses total: 500
- Travel expenses total: 300
- CSE average marks: 86.75
- Cybersecurity average marks: 86.75
- AI average marks: 78.5
- Ravi's recorded payments: 400
- Priya's recorded payments: 300
- Arjun's recorded payments: 500
- Only Sneha has no city in student_details; only expense 6 has no payment record.

## Problems Faced

- Understanding the difference between `WHERE` and `HAVING`.
- Understanding why `INNER JOIN` excludes unmatched rows.
- Understanding why `LEFT JOIN` returns `NULL`.
- Running the setup twice gives "table already exists"; use a fresh database.

## What I Learned

I learned how to group records and calculate summaries using SQL. I can filter grouped results with `HAVING` and combine related tables using `INNER JOIN` and `LEFT JOIN`. These skills help me generate reports from student records and expense data.

## Next Day

Day 7 — Foreign Keys, Constraints, Database Relationships, Normalization, and Revision.
