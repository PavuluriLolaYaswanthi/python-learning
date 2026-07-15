# Restore Deleted Folder

## Purpose

Recover an entire folder from a previous commit.

---

## Step 1

Find the commit.

```powershell
git log --oneline -- Python/day1_variables
```

Example

```text
337ed06 Day 2 Python Practice
```

---

## Step 2

Restore the folder.

```powershell
git checkout 337ed06 -- Python/day1_variables
```

Replace

```text
337ed06
```

with your commit ID.

---

## Step 3

Verify the folder.

```powershell
Get-ChildItem Python
```

or

```powershell
dir Python
```

Expected

```text
day1_variables
day2_conditions
day3_loops
day4_functions
```

---

## Step 4

Commit restored files.

```powershell
git add .
git commit -m "Restore deleted folder"
git push origin main
```

---

## Best Practice

Always verify the folder before committing.
