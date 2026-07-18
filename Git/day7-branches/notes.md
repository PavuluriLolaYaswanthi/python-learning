# Git Branches Notes

## What is a Branch?

A branch is an independent line of development.

It allows you to work on new features or bug fixes without affecting the main project.

---

## Why Use Branches?

Without branches:

- All work happens on the main branch.
- Bugs can affect production.
- Team collaboration becomes difficult.

With branches:

- Work safely.
- Experiment freely.
- Develop multiple features simultaneously.
- Collaborate with teams.

---

## Default Branch

Most repositories use:

```text
main
```

Older repositories may use:

```text
master
```

---

## Example

```text
main
│
├── login-feature
│
├── payment-feature
│
└── bug-fix
```

Each branch is independent.

---

## Branch Workflow

main

↓

Create Branch

↓

Develop Feature

↓

Test

↓

Merge

↓

Delete Branch

---

## Benefits

- Parallel development
- Better collaboration
- Safe experimentation
- Easy rollback

---

## Best Practices

- One feature per branch.
- Keep branch names meaningful.
- Delete merged branches.
- Never work directly on main for large features.
