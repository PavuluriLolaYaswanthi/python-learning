# git revert

## Purpose

Create a new commit that reverses the changes introduced by a previous commit.

---

## Revert the Last Commit

```powershell
git revert HEAD
```

---

## Revert a Specific Commit

```powershell
git revert <commit-id>
```

Example

```powershell
git revert a1b2c3d
```

---

## Verify

```powershell
git log --oneline
```

---

## Why Use Revert?

Unlike `git reset`, `git revert` preserves project history and is safe for shared repositories.

---

## Best Practices

- Use for commits that have already been pushed.
- Review the new revert commit before pushing.
