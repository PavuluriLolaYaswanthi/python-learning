# Git Branch Workflow

## Step 1

Check current branch.

```powershell
git branch
```

---

## Step 2

Create a new branch.

```powershell
git branch feature-login
```

---

## Step 3

Switch to the branch.

```powershell
git switch feature-login
```

or

```powershell
git checkout feature-login
```

---

## Step 4

Work on your feature.

Example

```text
Add login page
Fix bugs
Update UI
```

---

## Step 5

Check changes.

```powershell
git status
```

---

## Step 6

Commit changes.

```powershell
git add .

git commit -m "Add login feature"
```

---

## Step 7

Switch back to main.

```powershell
git switch main
```

---

## Step 8

Merge the feature branch.

```powershell
git merge feature-login
```

---

## Step 9

Delete the branch.

```powershell
git branch -d feature-login
```

---

## Complete Workflow

```powershell
git branch feature-login

git switch feature-login

git status

git add .

git commit -m "Add login feature"

git switch main

git merge feature-login

git branch -d feature-login
```

---

## Workflow Diagram

```text
main
 │
 │
 ├─────────────┐
 │             │
 │     feature-login
 │             │
 │        Development
 │             │
 └──── Merge ──┘
 │
main (updated)
```

---

## Best Practices

- Create one branch per feature.
- Commit frequently.
- Keep branch names meaningful.
- Merge only after testing.
- Delete branches after merging.
- Protect the `main` branch from direct development.
