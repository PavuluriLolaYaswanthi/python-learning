# Commit History Notes

## What is Commit History?

Every time you create a commit, Git saves a snapshot of your project.

These snapshots form the project's history.

---

## Why is Commit History Important?

Commit history allows you to:

- Track project progress
- See who made changes
- Recover deleted files
- Restore previous versions
- Debug problems

---

## Commit History Workflow

Working Directory

↓

git add

↓

git commit

↓

Commit History

↓

GitHub

---

## What Information Does a Commit Contain?

Every commit stores:

- Commit ID (Hash)
- Author
- Date
- Commit Message

Example

```text
337ed06 Day 2 Python practice
```

Where

337ed06 → Commit ID

Day 2 Python practice → Commit Message

---

## Why Commit Messages Matter

Good

```text
Add Day 4 Functions

Fix Login Bug

Complete Expense Tracker
```

Bad

```text
update

abc

test
```

---

## Best Practices

- Commit often.
- Use meaningful commit messages.
- Keep commits small and focused.
- Never use random commit messages.

---

## Summary

Commit history acts like a timeline of your project.

If something goes wrong, you can always go back to a previous commit.
