-- 1. Total spending per category (Food 500, Shopping 500, Travel 300)
SELECT category, SUM(amount) AS total_amount
FROM expenses
GROUP BY category;

-- 2. Students per course (AI 1, CSE 2, Cybersecurity 2)
SELECT course, COUNT(*) AS student_count
FROM students
GROUP BY course;

-- 3. Categories with total greater than 300 (Food 500, Shopping 500)
SELECT category, SUM(amount) AS total_amount
FROM expenses
GROUP BY category
HAVING SUM(amount) > 300;

-- 4. Courses with average marks at least 85 (CSE 86.75, Cybersecurity 86.75)
SELECT course, AVG(marks) AS average_marks
FROM students
GROUP BY course
HAVING AVG(marks) >= 85;

-- 5. Marks >= 80, grouped by course, at least two students
--    (CSE 2 / 86.75, Cybersecurity 2 / 86.75)
SELECT course, COUNT(*) AS student_count, AVG(marks) AS average_marks
FROM students
WHERE marks >= 80
GROUP BY course
HAVING COUNT(*) >= 2;

-- 6. Names and cities, matching records only
--    (Ravi Guntur, Priya Hyderabad, Arjun Vijayawada, Kiran Guntur)
SELECT students.name, student_details.city
FROM students
INNER JOIN student_details
    ON students.student_id = student_details.student_id;

-- 7. Every student and city, including missing ones
--    (same four rows as above, plus Sneha with NULL)
SELECT students.name, student_details.city
FROM students
LEFT JOIN student_details
    ON students.student_id = student_details.student_id;

-- 8. Total paid by each person (Arjun 500, Priya 300, Ravi 400)
SELECT expense_payments.paid_by, SUM(expenses.amount) AS total_paid
FROM expenses
INNER JOIN expense_payments
    ON expenses.expense_id = expense_payments.expense_id
GROUP BY expense_payments.paid_by;

-- 9. Payers whose total exceeds 300 (Arjun 500, Ravi 400)
SELECT expense_payments.paid_by, SUM(expenses.amount) AS total_paid
FROM expenses
INNER JOIN expense_payments
    ON expenses.expense_id = expense_payments.expense_id
GROUP BY expense_payments.paid_by
HAVING SUM(expenses.amount) > 300;

-- 10. Every expense and its payer, including expense 6 (paid_by NULL)
SELECT expenses.expense_id, expenses.category, expenses.amount,
       expense_payments.paid_by
FROM expenses
LEFT JOIN expense_payments
    ON expenses.expense_id = expense_payments.expense_id;
    