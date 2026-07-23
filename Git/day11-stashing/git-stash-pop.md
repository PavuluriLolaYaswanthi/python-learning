# git stash pop

## Purpose

Restore the most recent stash and remove it from the stash list.

---

## Syntax

```powershell
git stash pop
```

---

## Workflow

```powershell
git stash

git switch main

# Work

git switch feature-login

git stash pop
```

---

## Verify

```powershell
git status
```
