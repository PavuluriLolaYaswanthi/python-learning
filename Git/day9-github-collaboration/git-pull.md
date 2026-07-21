# git pull

## Purpose

Downloads changes from the remote repository and automatically merges them into your current branch.

---

## Syntax

```powershell
git pull origin main
```

---

## Example

```powershell
git pull origin main
```

---

## What Happens?

`git pull` performs two operations:

1. `git fetch`
2. `git merge`

---

## Workflow

GitHub

↓

git fetch

↓

git merge

↓

Updated Local Repository

---

## Verify

```powershell
git log --oneline
```

---

## Best Practices

- Pull before starting work.
- Resolve conflicts immediately if they occur.
