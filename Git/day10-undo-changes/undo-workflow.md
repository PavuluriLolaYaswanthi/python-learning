# Undo Changes Workflow

## Undo Unstaged Changes

```powershell
git diff

git restore README.md
```

---

## Unstage Files

```powershell
git reset README.md
```

---

## Undo Last Local Commit

```powershell
git reset --soft HEAD~1
```

---

## Permanently Remove Last Local Commit

```powershell
git reset --hard HEAD~1
```

---

## Undo a Pushed Commit

```powershell
git revert HEAD

git push origin main
```

---

## Complete Workflow

```powershell
git status

git diff

git restore README.md

git reset README.md

git reset --soft HEAD~1

git revert HEAD

git push origin main
```

---

## Best Practices

- Check `git status` before undoing changes.
- Use `git diff` to review changes.
- Use `git revert` for public/shared history.
- Reserve `git reset --hard` for situations where you are certain you want to discard local work.
