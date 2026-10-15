-- 1. Names of all students
SELECT name FROM students;

-- 2. Names and ages of students aged exactly 22 (Ravi, Sneha)
SELECT name, age FROM students WHERE age = 22;

-- 3. Marks greater than 80 (Ravi, Priya, Sneha, Kiran)
SELECT * FROM students WHERE marks > 80;

-- 4. Marks less than 85 (Arjun, Kiran)
SELECT * FROM students WHERE marks < 85;

-- 5. Not enrolled in Cybersecurity (Ravi, Arjun, Sneha)
SELECT * FROM students WHERE course != 'Cybersecurity';

-- 6. Aged 23 or older (Priya, Kiran)
SELECT * FROM students WHERE age >= 23;

-- 7. Marks 85 or lower (Arjun, Kiran)
SELECT * FROM students WHERE marks <= 85;

-- 8. Course exactly CSE (Ravi, Sneha)
SELECT * FROM students WHERE course = 'CSE';

-- 9. Marks exactly 92 (Priya)
SELECT * FROM students WHERE marks = 92;

-- 10. Names and marks where marks >= 88 (Priya, Sneha)
SELECT name, marks FROM students WHERE marks >= 88;