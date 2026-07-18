# Git Merge Cheat Sheet

## Merge Branch

```powershell
git switch main

git merge feature-login
```

---

## View History

```powershell
git log --oneline
```

---

## Graph View

```powershell
git log --oneline --graph
```

---

## Abort Merge

```powershell
git merge --abort
```

---

## Resolve Conflict

```powershell
git add .

git commit -m "Resolve merge conflict"
```

---

## Delete Merged Branch

```powershell
git branch -d feature-login
```

---

## Merge Workflow

```powershell
git switch main

git merge feature-login

git branch -d feature-login
```
