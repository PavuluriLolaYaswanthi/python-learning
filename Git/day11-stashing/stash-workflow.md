# Git Stash Workflow

## Scenario

You are working on a feature.

↓

A critical bug is reported.

↓

Save your unfinished work.

```powershell
git stash push -m "Login Feature"
```

↓

Switch Branch

```powershell
git switch hotfix
```

↓

Fix Bug

↓

Commit Changes

↓

Switch Back

```powershell
git switch feature-login
```

↓

Restore Work

```powershell
git stash pop
```

↓

Continue Development

---

## Complete Workflow

```powershell
git stash push -m "Login Feature"

git switch hotfix

git add .

git commit -m "Fix production bug"

git switch feature-login

git stash pop
```
