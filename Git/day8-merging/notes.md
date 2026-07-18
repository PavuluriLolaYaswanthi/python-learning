# Git Merge Notes

## What is Git Merge?

Git Merge combines changes from one branch into another.

Usually, changes are merged into the `main` branch after a feature is completed.

---

## Why Use Merge?

Imagine a team working on different features.

Developer A

```text
Login Feature
```

Developer B

```text
Payment Feature
```

Developer C

```text
Dashboard
```

Each developer works on a separate branch.

Once completed, all branches are merged into `main`.

---

## Merge Workflow

```text
main
 │
 ├──────────────┐
 │              │
 │      feature-login
 │              │
 │      Development
 │              │
 └────── Merge ─┘
 │
main (updated)
```

---

## Types of Merge

- Fast-Forward Merge
- Three-Way Merge
- Merge Conflict

---

## Benefits

- Combines completed work
- Keeps project organized
- Enables team collaboration
- Maintains project history

---

## Best Practices

- Merge only tested code.
- Pull the latest changes before merging.
- Keep feature branches short-lived.
- Delete branches after successful merging.
