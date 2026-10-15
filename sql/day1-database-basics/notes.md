# Day 1 — SQL Database Fundamentals

## Topics Learned

- What is a database?
- What is a table?
- Rows and columns
- Primary keys
- SQL data types: INTEGER, TEXT, REAL
- CREATE TABLE
- INSERT INTO
- SELECT *

## Key Definitions

- **Database:** An organized collection of information that can be stored, retrieved, and managed.
- **Table:** Stores related information in rows and columns (e.g. a `students` table).
- **Column:** One type of information, such as `name` or `age`.
- **Row:** One complete record, such as everything about one student.
- **Primary key:** A column (or set of columns) that uniquely identifies each row. It must be unique and cannot be NULL. A table has only one primary key.

## SQL Data Types Used

| Type | Stores | Example |
| ---- | ------ | ------- |
| INTEGER | Whole numbers | `age`, `student_id` |
| TEXT | Text/strings | `name`, `course` |
| REAL | Decimal numbers | `marks` |

## Practical Work

- Created a `students` table with `student_id` as the primary key.
- Inserted five student records.
- Retrieved all records using `SELECT *`.
- Practiced creating another table (`courses`).

### Commands Used

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
);

INSERT INTO students
    (student_id, name, age, course, marks)
VALUES
    (1, 'Ravi', 22, 'CSE', 85.5),
    (2, 'Priya', 23, 'Cybersecurity', 92.0),
    (3, 'Arjun', 21, 'AI', 78.5),
    (4, 'Sneha', 22, 'CSE', 88.0),
    (5, 'Kiran', 24, 'Cybersecurity', 81.5);

SELECT * FROM students;
```

## Practice Exercise Answers

```sql
-- 1. Create a courses table
CREATE TABLE courses (course_id INTEGER PRIMARY KEY, course_name TEXT NOT NULL);

-- 2. Insert Meena
INSERT INTO students (student_id, name, age, course, marks)
VALUES (6, 'Meena', 22, 'AI', 90);

-- 3. Display only name and course
SELECT name, course FROM students;

-- 4. Students older than 21
SELECT * FROM students WHERE age > 21;

-- 5. Count student records
SELECT COUNT(*) FROM students;
```

## Important Concepts

- A row represents one record.
- A column represents one attribute.
- A primary key uniquely identifies each record.
- NOT NULL prevents a column from accepting NULL values.
- `SELECT *` retrieves all columns.
- Two students can share a name, but never a `student_id`.

## Problems Faced

- Inserting a duplicate `student_id` fails because the primary key must be unique.
- Leaving out `name` fails because it is declared `NOT NULL`.
- Running `CREATE TABLE` twice gives a "table already exists" error.
- Missing commas, quotes around text values, or the closing semicolon cause syntax errors.

## What I Learned

I learned how databases organize information into tables and how to create a table, insert records, and retrieve data using SQL. I also understood why every table needs a primary key and how data types and constraints like NOT NULL keep the data clean.

## Next Day

Learn SELECT, WHERE, and comparison operators (`=`, `!=`, `>`, `<`, `>=`, `<=`) and practice 10 filtering queries.
