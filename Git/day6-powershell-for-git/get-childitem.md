# Get-ChildItem

## Purpose

Displays files and folders.

---

## Syntax

```powershell
Get-ChildItem
```

---

## Show Current Folder

```powershell
Get-ChildItem
```

---

## Show Python Folder

```powershell
Get-ChildItem Python
```

---

## Show Everything Recursively

```powershell
Get-ChildItem -Recurse
```

---

## Show Hidden Files

```powershell
Get-ChildItem -Force
```

---

## Show Hidden Files Recursively

```powershell
Get-ChildItem -Recurse -Force
```

---

## Find All Git Repositories

```powershell
Get-ChildItem -Recurse -Force -Directory -Filter .git
```

Expected

```text
python-learning\.git
```

Wrong

```text
python-learning\.git
python-learning\Python\day1_variables\.git
```

---

## When to Use

- View files
- View folders
- Find hidden `.git` folders
- Check repository contents
