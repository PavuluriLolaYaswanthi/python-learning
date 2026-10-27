CREATE TABLE day8_students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks REAL,
    city TEXT
);

INSERT INTO day8_students VALUES
(1, 'Ravi', 85, 'Guntur'),
(2, 'Priya', 92, 'Hyderabad'),
(3, 'Arjun', 68, 'Vijayawada'),
(4, 'Sneha', 88, 'Guntur'),
(5, 'Kiran', 55, NULL);

CREATE TABLE day8_expenses (
    expense_id INTEGER PRIMARY KEY,
    category TEXT,
    amount REAL
);

INSERT INTO day8_expenses VALUES
(1, 'Food', 250),
(2, 'Travel', 100),
(3, 'Food', 150),
(4, 'Shopping', 500),
(5, 'Travel', 200),
(6, 'Food', 100);


-- 1. Students above average marks (Ravi, Priya, Sneha)
SELECT name, marks
FROM day8_students
WHERE marks > (SELECT AVG(marks) FROM day8_students);

-- 2. Student(s) with the lowest marks (Kiran, 55)
SELECT name, marks
FROM day8_students
WHERE marks = (SELECT MIN(marks) FROM day8_students);

-- 3. Expenses greater than the average expense (Food 250, Shopping 500)
SELECT category, amount
FROM day8_expenses
WHERE amount > (SELECT AVG(amount) FROM day8_expenses);

-- 4. Grades: Ravi Very Good, Priya Excellent, Arjun Needs Improvement,
--    Sneha Very Good, Kiran Needs Improvement
SELECT name,
       CASE
           WHEN marks >= 90 THEN 'Excellent'
           WHEN marks >= 80 THEN 'Very Good'
           WHEN marks >= 70 THEN 'Good'
           ELSE 'Needs Improvement'
       END AS grade
FROM day8_students;

-- 5. Expense levels: Food 250 Medium, Travel 100 Low, Food 150 Low,
--    Shopping 500 High, Travel 200 Medium, Food 100 Low
SELECT category, amount,
       CASE
           WHEN amount >= 400 THEN 'High'
           WHEN amount >= 200 THEN 'Medium'
           ELSE 'Low'
       END AS expense_level
FROM day8_expenses;

-- 6. Students whose city is missing (Kiran)
SELECT * FROM day8_students WHERE city IS NULL;

-- 7. Students whose city is present (Ravi, Priya, Arjun, Sneha)
SELECT * FROM day8_students WHERE city IS NOT NULL;

-- 8. Name and city, 'Unknown' when missing (Kiran shows Unknown)
SELECT name, COALESCE(city, 'Unknown') AS city
FROM day8_students;

-- 9. Pass/Fail at 60 (only Kiran fails)
SELECT name,
       CASE
           WHEN marks >= 60 THEN 'Pass'
           ELSE 'Fail'
       END AS status
FROM day8_students;

-- 10. Total students and students with a city (5 and 4)
SELECT COUNT(*) AS total_students,
       COUNT(city) AS students_with_city
FROM day8_students;
