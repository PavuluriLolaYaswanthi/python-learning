
-- 1. Count all students (5)
SELECT COUNT(*) AS total_students FROM students;

-- 2. Count Cybersecurity students (2)
SELECT COUNT(*) AS cybersecurity_students
FROM students
WHERE course = 'Cybersecurity';

-- 3. Total marks (425.5)
SELECT SUM(marks) AS total_marks FROM students;

-- 4. Average marks (85.1)
SELECT AVG(marks) AS average_marks FROM students;

-- 5. Lowest mark (78.5)
SELECT MIN(marks) AS lowest_marks FROM students;

-- 6. Highest mark (92.0)
SELECT MAX(marks) AS highest_marks FROM students;

-- 7. Total marks of CSE students (173.5)
SELECT SUM(marks) AS cse_total_marks
FROM students
WHERE course = 'CSE';

-- 8. Average marks of Cybersecurity students (86.75)
SELECT AVG(marks) AS cybersecurity_average
FROM students
WHERE course = 'Cybersecurity';

-- 9. Number of distinct courses (3)
SELECT COUNT(DISTINCT course) AS unique_courses FROM students;

-- 10. Count, average, lowest and highest in one query (5, 85.1, 78.5, 92.0)
SELECT
    COUNT(*) AS total_students,
    AVG(marks) AS average_marks,
    MIN(marks) AS lowest_marks,
    MAX(marks) AS highest_marks
FROM students;
