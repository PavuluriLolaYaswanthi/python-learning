-- 1. departments table
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE
);

-- 2. employees table with a foreign key
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 3. expenses table where amount must be greater than zero
CREATE TABLE expenses (
    expense_id INTEGER PRIMARY KEY,
    amount REAL NOT NULL CHECK (amount > 0)
);

-- 4. Add a payment_method column with default 'Cash'
ALTER TABLE expenses ADD COLUMN payment_method TEXT DEFAULT 'Cash';

-- 6. Junction table for students and courses
CREATE TABLE enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- 10. Each expense with its category name
SELECT expenses.expense_id, expense_categories.category_name, expenses.amount
FROM expenses
INNER JOIN expense_categories
    ON expenses.category_id = expense_categories.category_id;
