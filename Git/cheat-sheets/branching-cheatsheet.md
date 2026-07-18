# Git Branching Cheat Sheet

## View Branches

```powershell
git branch
```

---

## View Local and Remote Branches

```powershell
git branch -a
```

---

## Create Branch

```powershell
git branch feature-login
```

---

## Create and Switch

```powershell
git switch -c feature-login
```

---

## Switch Branch

```powershell
git switch feature-login
```

or

```powershell
git checkout feature-login
```

---

## Switch Back

```powershell
git switch main
```

---

## Rename Branch

```powershell
git branch -m old-name new-name
```

---

## Delete Branch

```powershell
git branch -d feature-login
```

Force Delete

```powershell
git branch -D feature-login
```

---

## Daily Branch Workflow

```powershell
git branch feature-login

git switch feature-login

git add .

git commit -m "Add login"

git switch main

git merge feature-login

git branch -d feature-login
```
