# git fetch

## Purpose

Downloads the latest changes from the remote repository without modifying your working files.

---

## Syntax

```powershell
git fetch
```

---

## Example

```powershell
git fetch origin
```

---

## What Happens?

Git downloads:

- New commits
- New branches
- Updated references

Your current branch remains unchanged.

---

## Workflow

GitHub

↓

git fetch

↓

Local Repository Updated

↓

Working Directory Unchanged

---

## Verify

```powershell
git status
```

---

## Best Practices

Use `git fetch` to inspect incoming changes before merging them.
