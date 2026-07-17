# Daily Git Workflow

## Before Starting Work

Check repository status.

```powershell
git status
```

---

## After Completing Work

Stage all changes.

```powershell
git add .
```

---

Create a commit.

```powershell
git commit -m "Meaningful commit message"
```

Example

```powershell
git commit -m "Complete Day 5 Lists and Dictionaries"
```

---

Push changes to GitHub.

```powershell
git push origin main
```

---

## Complete Daily Workflow

```powershell
git status

git add .

git commit -m "Meaningful commit message"

git push origin main
```

---

## Before Closing Your Project

Verify everything is saved.

```powershell
git status
```

Expected

```text
nothing to commit, working tree clean
```

---

## Best Practices

- Commit frequently.
- Use meaningful commit messages.
- Push your work at the end of each session.
- Check `git status` before and after committing.
