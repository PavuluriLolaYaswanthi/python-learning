-- 1. Age at least 22 AND marks above 85 (Ravi, Priya, Sneha)
SELECT * FROM students WHERE age >= 22 AND marks > 85;

-- 2. CSE OR Cybersecurity (Ravi, Priya, Sneha, Kiran)
SELECT * FROM students WHERE course = 'CSE' OR course = 'Cybersecurity';

-- 3. NOT studying AI (Ravi, Priya, Sneha, Kiran)
SELECT * FROM students WHERE NOT course = 'AI';

-- 4. Age 22 or younger AND marks at least 85 (Ravi, Sneha)
SELECT * FROM students WHERE age <= 22 AND marks >= 85;

-- 5. Marks above 80 OR age 21 (all five students)
SELECT * FROM students WHERE marks > 80 OR age = 21;

-- 6. Sort by age, youngest to oldest
SELECT * FROM students ORDER BY age ASC;

-- 7. Sort by marks, highest to lowest
SELECT * FROM students ORDER BY marks DESC;

-- 8. Two highest-scoring students (Priya, Sneha)
SELECT * FROM students ORDER BY marks DESC LIMIT 2;

-- 9. Cybersecurity students, marks lowest to highest (Kiran, Priya)
SELECT * FROM students
WHERE course = 'Cybersecurity'
ORDER BY marks ASC;

-- 10. Top two students aged at least 22 (Priya, Sneha)
SELECT * FROM students
WHERE age >= 22
ORDER BY marks DESC
LIMIT 2;
