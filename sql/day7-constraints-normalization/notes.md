# SQL Day 7 — Foreign Keys, Constraints, Relationships and Normalization

## Topics Learned

1. Primary keys and foreign keys
2. NOT NULL and UNIQUE constraints
3. CHECK and DEFAULT constraints
4. One-to-one relationships
5. One-to-many relationships
6. Many-to-many relationships
7. Junction tables
8. First Normal Form (1NF)
9. Second Normal Form (2NF)
10. Third Normal Form (3NF)
11. Referential integrity
12. Normalized student and expense databases

## Important Concepts

### Primary Key

Uniquely identifies each row in a table.

```sql
student_id INTEGER PRIMARY KEY
```

### Foreign Key

A column that refers to a key in another table. Each non-NULL value must match an existing row in the referenced (parent) table.

```sql
FOREIGN KEY (course_id) REFERENCES courses(course_id)
```

- Insert parent rows (e.g. `courses`) before child rows (e.g. `students`).
- SQLite only enforces foreign keys when `PRAGMA foreign_keys = ON;` is set for the connection. Check with `PRAGMA foreign_keys;` (1 means on).

### Constraints

| Constraint | What it does |
| ---------- | ------------ |
| `PRIMARY KEY` | Uniquely identifies each row |
| `FOREIGN KEY` | Requires a matching referenced record (when non-NULL) |
| `NOT NULL` | Prevents a column from being NULL |
| `UNIQUE` | Prevents duplicate non-NULL values (multiple NULLs are allowed in SQLite) |
| `CHECK` | Requires values to satisfy a condition, e.g. `CHECK (amount > 0)` |
| `DEFAULT` | Supplies a value when an insert omits the column |

Constraints protect the database no matter which program or user inserts the data.

### Relationships

| Type | Meaning | Typical implementation |
| ---- | ------- | ---------------------- |
| One-to-one (1:1) | One record relates to one record | Foreign key with `UNIQUE` |
| One-to-many (1:N) | One course has many students | Foreign key on the "many" table |
| Many-to-many (M:N) | Students take many courses and courses have many students | Junction table such as `enrollments` |

A junction table with `PRIMARY KEY (student_id, course_id)` prevents the same student-course pair from being inserted twice.

### Normalization

| Normal form | Idea |
| ----------- | ---- |
| 1NF | One value per cell; no repeating groups (no `'CSE, AI'` in one cell) |
| 2NF | Every non-key attribute depends on the whole composite key (no partial dependency) |
| 3NF | No non-key attribute depends on another non-key attribute (no transitive dependency) |

Goal: store each fact once, in the right table, and connect tables with keys. This avoids repeated data, inconsistent updates, and awkward inserts or deletes.

## Practical Work

- Created `courses` and `students` tables.
- Added foreign-key relationships.
- Tested invalid foreign-key values.
- Tested primary-key, NOT NULL, and CHECK constraints.
- Created an `enrollments` junction table.
- Normalized expense categories into a separate table.
- Joined expenses with their categories.
- Completed 10 practice questions.

## Important SQL Commands

```sql
PRAGMA foreign_keys = ON;

SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
    ON students.course_id = courses.course_id;
```

Total spending by category (normalized tables): Food 400, Shopping 500, Travel 100.

```sql
SELECT expense_categories.category_name,
       SUM(expenses.amount) AS total_amount
FROM expenses
INNER JOIN expense_categories
    ON expenses.category_id = expense_categories.category_id
GROUP BY expense_categories.category_name;
```

Written answers:

- **5.** The insert fails because department 999 does not exist (assuming foreign-key enforcement is on and the value is non-NULL).
- **7.** One-to-many (1:N); store `course_id` as a foreign key in `students`.
- **8.** Storing `'CSE, AI, Cybersecurity'` in one cell violates 1NF. Use separate rows, usually through an `enrollments` junction table.
- **9.** `student_name` depending only on `student_id` is a partial dependency (2NF violation). Move it into the `students` table.

## What I Learned

I learned how to connect related database tables using foreign keys, protect records with constraints, model one-to-many and many-to-many relationships, and reduce unnecessary data duplication through normalization.

## Problems Faced

- Understanding primary keys versus foreign keys.
- Understanding why invalid foreign-key references fail (and that `PRAGMA foreign_keys = ON;` must be set).
- Understanding how junction tables work.
- Distinguishing 1NF, 2NF, and 3NF.

## Next Steps

- Revise SQL Days 1–7.
- Practice creating tables with constraints.
- Practice JOIN and GROUP BY queries.
- Build a small relational database for an expense tracker.
