# git reset

## Purpose

Move the current branch to a previous commit or unstage files.

---

## Unstage a File

```powershell
git reset README.md
```

---

## Unstage All Files

```powershell
git reset
```

---

## Soft Reset

Keeps changes but removes the commit.

```powershell
git reset --soft HEAD~1
```

---

## Mixed Reset (Default)

Removes the commit and unstages the changes.

```powershell
git reset HEAD~1
```

---

## Hard Reset

Removes the commit and deletes local changes.

```powershell
git reset --hard HEAD~1
```

---

## Verify

```powershell
git status
```

---

## Warning

`git reset --hard` permanently deletes uncommitted local changes.
