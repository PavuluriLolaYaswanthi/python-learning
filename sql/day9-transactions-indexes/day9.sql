---## Exercise Solutions
---Sample data: `day9_accounts` has Ravi 1000, Priya 1500, Arjun 800. 
---`day9_orders` has 5 orders (Ravi 500 Pending, Priya 1200 Completed,Arjun 750 Pending, Sneha 900 Completed, Kiran 300 Pending).'''

CREATE TABLE day9_accounts (
    account_id INTEGER PRIMARY KEY,
    owner TEXT NOT NULL,
    balance REAL NOT NULL CHECK (balance >= 0)
);

INSERT INTO day9_accounts VALUES
(1, 'Ravi', 1000),
(2, 'Priya', 1500),
(3, 'Arjun', 800);

CREATE TABLE day9_orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL,
    amount REAL NOT NULL
);

INSERT INTO day9_orders VALUES
(1, 'Ravi', 'Pending', 500),
(2, 'Priya', 'Completed', 1200),
(3, 'Arjun', 'Pending', 750),
(4, 'Sneha', 'Completed', 900),
(5, 'Kiran', 'Pending', 300);


-- 1. Add ₹100 to Arjun's balance and commit
BEGIN TRANSACTION;
UPDATE day9_accounts SET balance = balance + 100 WHERE account_id = 3;
COMMIT;

-- 2. Subtract ₹50 from Ravi's balance, then cancel
BEGIN TRANSACTION;
UPDATE day9_accounts SET balance = balance - 50 WHERE account_id = 1;
SELECT * FROM day9_accounts;   -- shows the temporary change
ROLLBACK;
SELECT * FROM day9_accounts;   -- Ravi's balance is back to its previous value

-- 3. Pending orders (orders 1, 3, 5)
SELECT * FROM day9_orders WHERE status = 'Pending';

-- 4. Index on the amount column
CREATE INDEX idx_day9_orders_amount ON day9_orders(amount);

-- 5. Sneha's order (order 4, Completed, 900)
SELECT * FROM day9_orders WHERE customer_name = 'Sneha';

-- 6. Remove the status index
DROP INDEX idx_day9_orders_status;

-- 7. Query plan for orders over ₹700 (matches 1200, 750, 900)
--EXPLAIN QUERY PLAN
SELECT * FROM day9_orders WHERE amount > 700;

-- 8. Amounts between 400 and 1000 inclusive (orders 1, 3, 4)
SELECT * FROM day9_orders WHERE amount BETWEEN 400 AND 1000;
