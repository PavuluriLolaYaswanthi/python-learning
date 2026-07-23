# git stash apply

## Purpose

Restore a stash without deleting it.

---

## Syntax

```powershell
git stash apply
```

Restore a specific stash.

```powershell
git stash apply stash@{1}
```

---

## Difference

apply

- Restores the stash
- Keeps it in the stash list

pop

- Restores the stash
- Removes it from the stash list
