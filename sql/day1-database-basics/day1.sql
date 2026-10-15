CREATE TABLE courses(
    course_id INT PRIMARY KEY,
    course_name TEXT NOT NULL
);

CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL);

INSERT INTO students
    (student_id, name, age, course, marks)
VALUES
    (1, 'Ravi', 22, 'CSE', 85.5),
    (2, 'Priya', 23, 'Cybersecurity', 92.0),
    (3, 'Arjun', 21, 'AI', 78.5),
    (4, 'Sneha', 22, 'CSE', 88.0),
    (5, 'Kiran', 24, 'Cybersecurity', 81.5);

INSERT INTO students
    (student_id, name, age, course, marks)
VALUES(6,'Meena',22,'CSE', 90.0);

SELECT name,course FROM students;

SELECT * FROM students WHERE age>21;

SELECT COUNT(*) FROM students;