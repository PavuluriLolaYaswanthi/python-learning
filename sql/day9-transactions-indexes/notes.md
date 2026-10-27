# SQL Day 9 — Transactions, Indexes, and Query Performance

## Topics Learned (Simple Explanation)

1. **Database transaction**
   A transaction is a group of database operations treated as one logical unit of work. Example: sending ₹200 means "take from Ravi" and "give to Priya". Both must happen, or neither.

2. **BEGIN TRANSACTION**
   Tells the database, "I'm starting a job. Don't make my changes permanent yet."

3. **COMMIT**
   Means "the job is done, save everything." After this, the changes are permanent.

4. **ROLLBACK**
   Means "something is wrong, cancel everything since BEGIN." The data goes back to how it was. It works only before COMMIT.

5. **ACID properties** (four rules that make transactions reliable)
   - **Atomicity:** all or nothing. No half-finished transfer.
   - **Consistency:** the rules are never broken (for example, no negative balance).
   - **Isolation:** two people working at the same time don't mess up each other's work.
   - **Durability:** once saved, the data stays saved, even if the system crashes.

6. **Index (CREATE INDEX)**
   An index helps a database locate rows more efficiently without examining every row in many common query patterns.

7. **DROP INDEX**
   Removes the index only. Your table and data stay safe.

8. **EXPLAIN QUERY PLAN**
   Asks SQLite, "How will you run this query?" It shows the plan before running it.

9. **SCAN vs SEARCH**
   - **SCAN:** the database reads through the rows one by one.
   - **SEARCH:** the database uses an index to go straight to the matching rows.
   A scan isn't always bad. For a small table, it can be just as fast.

## Practical Work

- Created accounts and orders tables.
- Transferred money between accounts using a transaction.
- Tested ROLLBACK to cancel uncommitted changes.
- Created and removed indexes.
- Searched orders using WHERE.
- Examined query plans with EXPLAIN QUERY PLAN.
- Completed 10 practice questions.

## Important Concepts

### Transactions

A transaction groups database operations into one logical unit of work.

| Command | Purpose |
| ------- | ------- |
| `BEGIN` | Start a transaction |
| `COMMIT` | Save the transaction's changes |
| `ROLLBACK` | Cancel uncommitted changes |

- Example: a ₹200 transfer from Ravi to Priya needs both the subtraction and the addition to succeed together. After commit: Ravi 800, Priya 1700, Arjun 800 (total stays ₹3,300).
- `ROLLBACK` only undoes uncommitted changes; it cannot undo a transaction that was already committed.

### ACID

- **Atomicity:** all or nothing.
- **Consistency:** transactions preserve database rules (e.g. no negative balance when a constraint forbids it).
- **Isolation:** concurrent transactions don't interfere improperly.
- **Durability:** committed changes persist, subject to the database's durability configuration and storage system.

### Indexes

- An index helps the database find rows without examining every row, like a book's index.
- Can speed up `WHERE`, join, and sorting operations.
- Cost: extra storage, and `INSERT`, `UPDATE`, and `DELETE` can get slower because indexes must be updated.
- Don't index every column; add indexes to columns you frequently search, join, or sort on, and check the query plan first.
- Primary keys are commonly indexed automatically (behavior depends on the database system).

```sql
CREATE INDEX idx_day9_orders_status ON day9_orders(status);
DROP INDEX idx_day9_orders_customer;   -- removes the index, not the data
```

### EXPLAIN QUERY PLAN

Shows how SQLite intends to run a query.

| Plan wording | General meaning |
| ------------ | --------------- |
| `SCAN` | Reads through a table or index |
| `SEARCH` | Looks up rows using a targeted access method |
| `USING INDEX` | Uses an index for the operation |

A scan isn't automatically bad: for small tables or queries returning most rows, it can be the best choice. Output varies by SQLite version, table size, and optimizer decisions.

Written answers:

- **9.** If a transaction is rolled back before it is committed, all its uncommitted changes are cancelled and the data returns to its last committed state.
- **10.** Atomicity (all or nothing), Consistency (rules and constraints are preserved), Isolation (concurrent transactions don't interfere improperly), Durability (committed changes persist).

Notes: question 4 fails with "index already exists" if you already created `idx_day9_orders_amount` in the lesson, and question 6 needs the status index to exist first. Verify balances before and after questions 1 and 2.

## Problems Faced

- Understanding when changes are committed or rolled back.
- Understanding the difference between a scan and an index search.
- Learning why indexes are useful but should not be added to every column.
- Some SQL editors don't run multi-statement transaction scripts, so run the statements individually.

## What I Learned

I learned how to protect database changes with transactions, how indexes can improve query performance, and how to inspect SQLite query plans.

## Next Day

Review SQL Days 1–9 and build a mini-project that combines filtering, aggregation, joins, constraints, subqueries, and transactions.
