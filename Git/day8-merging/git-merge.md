# git merge

## Purpose

Combines one branch into another.

---

## Syntax

```powershell
git merge <branch-name>
```

---

## Example

Switch to the main branch.

```powershell
git switch main
```

Merge the feature branch.

```powershell
git merge feature-login
```

---

## Complete Workflow

```powershell
git branch feature-login

git switch feature-login

# Make changes

git add .

git commit -m "Add login feature"

git switch main

git merge feature-login
```

---

## Verify Merge

```powershell
git log --oneline
```

You should see the merge commit or updated history.

---

## Delete Merged Branch

```powershell
git branch -d feature-login
```

---

## Best Practices

- Merge into `main`.
- Test before merging.
- Delete merged branches.
