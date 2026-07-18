# Daily Git Workflow

## Before Starting Work

### 1. Navigate to Your Project

```powershell
cd <project-folder>
```

Example

```powershell
cd C:\Users\Administrator\Desktop\python-learning
```

---

### 2. Check the Current Branch

```powershell
git branch
```

Example Output

```text
* main
```

---

### 3. Check Repository Status

```powershell
git status
```

Expected Output

```text
nothing to commit, working tree clean
```

---

## Start a New Feature

### Create and Switch to a New Branch

```powershell
git switch -c feature-name
```

Example

```powershell
git switch -c day9-github-collaboration
```

---

## Work on Your Project

- Write code
- Create files
- Modify existing files
- Test your application

---

## Check Changes

```powershell
git status
```

Example Output

```text
Changes not staged for commit
```

---

## Stage Changes

Stage all files.

```powershell
git add .
```

Stage a specific file.

```powershell
git add README.md
```

---

## Create a Commit

```powershell
git commit -m "Meaningful commit message"
```

Example

```powershell
git commit -m "Complete Day 9 GitHub collaboration notes"
```

---

## Verify Commit

```powershell
git log --oneline -5
```

---

## Switch Back to Main

```powershell
git switch main
```

---

## Merge the Feature Branch

```powershell
git merge feature-name
```

Example

```powershell
git merge day9-github-collaboration
```

---

## Delete the Merged Branch

```powershell
git branch -d feature-name
```

Example

```powershell
git branch -d day9-github-collaboration
```

---

## Push Changes to GitHub

```powershell
git push origin main
```

---

## Verify Everything is Saved

```powershell
git status
```

Expected Output

```text
nothing to commit, working tree clean
```

---

# Complete Daily Workflow

```powershell
git branch

git status

git switch -c feature-name

# Work on your project

git status

git add .

git commit -m "Meaningful commit message"

git log --oneline -5

git switch main

git merge feature-name

git branch -d feature-name

git push origin main

git status
```

---

# Best Practices

- Start each new feature in a separate branch.
- Check `git status` before and after making changes.
- Commit frequently with clear and meaningful messages.
- Test your code before merging.
- Merge feature branches into `main` only after testing.
- Delete branches after they are merged.
- Push your latest changes to GitHub regularly.
- Verify your repository is clean before ending your work session.

---

# Typical Development Workflow

```text
Open Project
      │
      ▼
Check Status
      │
      ▼
Create Feature Branch
      │
      ▼
Write Code
      │
      ▼
Test Changes
      │
      ▼
git add
      │
      ▼
git commit
      │
      ▼
Switch to main
      │
      ▼
git merge
      │
      ▼
Delete Feature Branch
      │
      ▼
git push
      │
      ▼
Repository Updated on GitHub
```
