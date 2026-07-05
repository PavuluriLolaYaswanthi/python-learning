# git add

## Purpose

Moves changes from the Working Directory to the Staging Area.

---

## Syntax

Add everything

```powershell
git add .
```

Add one file

```powershell
git add notes.md
```

Add one folder

```powershell
git add Python/day1_variables
```

---

## Workflow

Working Directory

↓

git add

↓

Staging Area

---

## Verify

```powershell
git status
```

Files appear under

```text
Changes to be committed
```

---

## Common Mistake

Forgetting to run

```powershell
git add .
```

before committing.
