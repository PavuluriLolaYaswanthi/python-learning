# Day 4 — SQL CRUD Operations

## Topics Learned

- CRUD: Create, Read, Update, Delete
- INSERT INTO (single row, multiple rows, selected columns)
- UPDATE and SET
- DELETE FROM
- WHERE conditions in data modification
- Safe database operations
- SELECT-based verification
- Transactions: BEGIN, COMMIT, ROLLBACK

## Practical Work

- Inserted individual student records.
- Inserted multiple records in one statement.
- Updated student marks and course information.
- Increased marks using arithmetic expressions.
- Deleted selected student records.
- Practiced previewing and verifying changes.
- Completed 10 SQL exercises.

## CRUD Summary

| Letter | Operation | SQL | Example |
| ------ | --------- | --- | ------- |
| C | Create | `INSERT` | `INSERT INTO students (student_id, name) VALUES (6, 'Meena');` |
| R | Read | `SELECT` | `SELECT * FROM students;` |
| U | Update | `UPDATE` | `UPDATE students SET marks = 95 WHERE student_id = 2;` |
| D | Delete | `DELETE` | `DELETE FROM students WHERE student_id = 6;` |

`CREATE TABLE` creates the table structure; `INSERT` adds records inside an existing table.

## Important Concepts

- **INSERT:** Always list column names explicitly. Columns left out get `NULL` if they allow it.
- **UPDATE:** `SET` changes values; `WHERE` picks which rows. `SET marks = marks + 5` uses the existing value.
- **DELETE:** Removes rows but keeps the table structure.
- **Dangerous queries:** `UPDATE students SET marks = 100;` changes every row, and `DELETE FROM students;` removes every row, because neither has a `WHERE` clause.

| Command | Effect |
| ------- | ------ |
| `DELETE FROM students WHERE student_id = 6;` | Deletes matching rows |
| `DELETE FROM students;` | Deletes all rows, keeps the table |
| `DROP TABLE students;` | Removes the table and its data |

### Safe SQL Workflow

1. **Preview** the target rows with `SELECT` using the same `WHERE`.
2. **Check** that they are exactly the rows you intend to change.
3. **Execute** the `INSERT`, `UPDATE`, or `DELETE`.
4. **Verify** the result with `SELECT`.

### Transactions

```sql
BEGIN TRANSACTION;
UPDATE students SET marks = 82 WHERE student_id = 3;
SELECT * FROM students WHERE student_id = 3;
ROLLBACK;  -- use COMMIT instead to save the change
```

- `BEGIN TRANSACTION` starts a transaction.
- `COMMIT` saves the changes.
- `ROLLBACK` cancels uncommitted changes.
- Transactions do not replace backups; practice on a practice database.

## Exercise Solutions

These run in order, so later results depend on earlier changes.s

Note for exercise 9: if you ran everything in order, Arjun is already Cybersecurity (exercise 4) and Divya was deleted (exercise 6), so only Meena is returned. On the original data, it would be Arjun alone before the inserts.

## Problems Faced

- Forgetting `WHERE` on `UPDATE` or `DELETE` would change or remove every row.
- Re-running `INSERT` statements fails because the `student_id` values already exist (primary key must be unique).
- Running the exercises in order means later results change (e.g. exercise 9).
- Some SQL editors handle multiple statements or transactions differently.

## What I Learned

I learned how to insert, retrieve, update, and delete database records. I also learned why WHERE conditions and verification queries are important for preventing accidental data changes.

## Next Day

Learn aggregate functions: COUNT, SUM, AVG, MIN, and MAX.
