# View Commit History of a Folder

## Purpose

Displays commits related to a specific folder.

---

## Syntax

```powershell
git log --oneline -- <folder-name>
```

---

## Example

```powershell
git log --oneline -- Python/day1_variables
```

Output

```text
337ed06 Day 2 Python practice
```

---

## Why Use This?

Useful when:

- A folder is deleted.
- A file is modified.
- You need the commit ID for recovery.

---

## Restore Folder

Once you have the commit ID:

```powershell
git checkout 337ed06 -- Python/day1_variables
```

---

## Workflow

Find Commit

↓

Copy Commit ID

↓

Restore Folder

↓

Commit Changes

↓

Push to GitHub

---

## Recovery Commands

Restore

```powershell
git checkout 337ed06 -- Python/day1_variables
```

Save

```powershell
git add .

git commit -m "Restore day1_variables"

git push origin main
```

---

## Best Practice

Before restoring any deleted folder:

1. Find its commit history.

```powershell
git log --oneline -- Python/day1_variables
```

2. Restore the folder.

```powershell
git checkout <commit-id> -- Python/day1_variables
```

3. Commit the restored files.

4. Push to GitHub.
