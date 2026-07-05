# GitHub Remote Notes

## What is a Remote Repository?

A remote repository is a copy of your Git repository stored on a server.

Example:

GitHub

GitLab

Bitbucket

---

## Why Use a Remote Repository?

Remote repositories help you:

- Backup your code
- Collaborate with other developers
- Share projects
- Access code from multiple devices

---

## Local Repository vs Remote Repository

### Local Repository

Stored on your computer.

Example:

```text
C:\Users\Administrator\Desktop\python-learning
```

---

### Remote Repository

Stored on GitHub.

Example:

```text
https://github.com/username/python-learning
```

---

## Workflow

```text
Local Repository

↓

Commit Changes

↓

Push

↓

GitHub Repository
```

---

## What is origin?

Origin is the default name given to your GitHub repository.

Example

```text
origin
```

Instead of typing:

```text
https://github.com/username/python-learning.git
```

Git lets you use:

```text
origin
```

---

## Common Remote Commands

View remote

```powershell
git remote -v
```

Add remote

```powershell
git remote add origin <repository-url>
```

Remove remote

```powershell
git remote remove origin
```

Rename remote

```powershell
git remote rename origin github
```

---

## Daily Workflow

```text
Edit Files

↓

git status

↓

git add .

↓

git commit

↓

git push origin main
```

---

## Key Terms

Repository

A Git project.

Local Repository

Repository stored on your computer.

Remote Repository

Repository stored online.

Origin

Default name of the remote repository.

Main

Default branch.
