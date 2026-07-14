# git log

## Purpose

Displays the commit history of the repository.

---

## Syntax

```powershell
git log
```

---

## Short History

```powershell
git log --oneline
```

---

## Last Five Commits

```powershell
git log --oneline -5
```

---

## Example

```powershell
git log --oneline
```

Output

```text
337ed06 Day 2 Python practice

2d43ab1 Day 1 Variables

f8a3d11 Initial Commit
```

---

## Explanation

Each line contains:

Commit ID

Commit Message

Example

```text
337ed06 Day 2 Python practice
```

Where

337ed06 → Commit ID

Day 2 Python practice → Commit Message

---

## Why Use git log?

- View project history
- Find commit IDs
- Restore deleted files
- Debug changes

---

## Common Options

View complete history

```powershell
git log
```

Short history

```powershell
git log --oneline
```

Last 5 commits

```powershell
git log --oneline -5
```

---

## Best Practice

Use

```powershell
git log --oneline
```

daily to review your commits.
