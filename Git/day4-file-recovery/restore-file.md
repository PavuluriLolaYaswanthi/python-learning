# Restore Deleted File

## Purpose

Recover a single file from a previous commit.

---

## Step 1

Find commit history.

```powershell
git log --oneline -- README.md
```

---

## Step 2

Restore the file.

```powershell
git checkout 337ed06 -- README.md
```

---

## Step 3

Verify.

```powershell
Get-ChildItem
```

or

```powershell
dir
```

---

## Step 4

Save changes.

```powershell
git add .
git commit -m "Restore README"
git push origin main
```

---

## Example

Restore notes.md

```powershell
git checkout 337ed06 -- notes.md
```

Restore README.md

```powershell
git checkout 337ed06 -- README.md
```

---

## Best Practice

Recover only the file you need instead of restoring the entire project.
