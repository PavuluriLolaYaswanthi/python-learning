# git diff

## Purpose

Compare changes between files, commits, or branches.

---

## View Unstaged Changes

```powershell
git diff
```

---

## View Staged Changes

```powershell
git diff --staged
```

---

## Compare Two Commits

```powershell
git diff HEAD~1 HEAD
```

---

## Compare Two Branches

```powershell
git diff main feature-login
```

---

## Best Practices

- Run `git diff` before committing.
- Review staged changes with `git diff --staged`.
