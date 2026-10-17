-- 1. Insert Meena
INSERT INTO students (student_id, name, age, course, marks)
VALUES (6, 'Meena', 22, 'AI', 90.0);

-- 2. Insert Rahul and Divya
INSERT INTO students (student_id, name, age, course, marks)
VALUES
    (7, 'Rahul', 21, 'CSE', 76.0),
    (8, 'Divya', 23, 'AI', 94.5);

-- 3. Change Priya's marks to 95
UPDATE students SET marks = 95 WHERE student_id = 2;
SELECT * FROM students WHERE student_id = 2;

-- 4. Change Arjun's course to Cybersecurity
UPDATE students SET course = 'Cybersecurity' WHERE student_id = 3;
SELECT * FROM students WHERE student_id = 3;

-- 5. Add 5 marks to every CSE student (Ravi, Sneha, Rahul)
SELECT * FROM students WHERE course = 'CSE';   -- preview
UPDATE students SET marks = marks + 5 WHERE course = 'CSE';
SELECT * FROM students WHERE course = 'CSE';   -- verify

-- 6. Delete the student with ID 8
SELECT * FROM students WHERE student_id = 8;   -- preview
DELETE FROM students WHERE student_id = 8;
SELECT * FROM students WHERE student_id = 8;   -- returns zero rows

-- 7. Delete students with marks below 70 (deletes zero rows with this data)
SELECT * FROM students WHERE marks < 70;       -- preview
DELETE FROM students WHERE marks < 70;

-- 8. Increase student 1's age by one year
UPDATE students SET age = age + 1 WHERE student_id = 1;
SELECT * FROM students WHERE student_id = 1;

-- 9. Preview who would be affected by deleting all AI students (no delete)
SELECT * FROM students WHERE course = 'AI';

-- 10. Safely change Sneha's marks to 91
SELECT student_id, name, marks FROM students WHERE student_id = 4;  -- preview
UPDATE students SET marks = 91 WHERE student_id = 4;
SELECT student_id, name, marks FROM students WHERE student_id = 4;  -- verify