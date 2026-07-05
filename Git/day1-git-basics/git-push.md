# git push

## Purpose

Uploads local commits to GitHub.

---

## Syntax

```powershell
git push origin main
```

---

## Example

```powershell
git push origin main
```

---

## Workflow

Local Repository

↓

git push

↓

GitHub Repository

---

## Verify

Refresh GitHub.

Your latest commit should appear.

---

## Common Errors

### Authentication failed

Login again.

---

### Everything up-to-date

No new commits exist.

---

### Rejected

Someone pushed changes before you.

Run:

```powershell
git pull
```

then push again.

---

## Daily Workflow

```powershell
git status

git add .

git commit -m "Meaningful message"

git push origin main
```
