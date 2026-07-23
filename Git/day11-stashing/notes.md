# Git Stash Notes

## What is Git Stash?

Git Stash temporarily saves your uncommitted changes so that you can work on something else without committing incomplete code.

Git removes the changes from your working directory and stores them in a temporary stack called the stash.

---

## Why Use Git Stash?

Example:

You are developing a login feature.

Suddenly your manager asks you to fix a production bug.

Instead of committing unfinished code:

- Stash your work
- Switch branches
- Fix the bug
- Return later
- Restore your work

---

## Workflow

Working Directory

↓

git stash

↓

Clean Working Directory

↓

Switch Branch

↓

Finish Other Work

↓

git stash pop

↓

Continue Development

---

## Benefits

- Keeps history clean
- No unnecessary commits
- Safe temporary storage
- Easy branch switching

---

## Best Practices

- Use stash for short-term work.
- Use commits for completed work.
- Name stashes for easier identification.
