# Git Recovery Workflow

## Recover a Deleted Folder

### Find History

```powershell
git log --oneline -- Python/day1_variables
```

↓

### Restore Folder

```powershell
git checkout 337ed06 -- Python/day1_variables
```

↓

### Verify

```powershell
Get-ChildItem Python
```

↓

### Save Changes

```powershell
git add .
git commit -m "Restore deleted folder"
git push origin main
```

---

# Recover a Deleted File

### Find History

```powershell
git log --oneline -- README.md
```

↓

### Restore

```powershell
git checkout 337ed06 -- README.md
```

↓

### Verify

```powershell
dir
```

↓

### Commit

```powershell
git add .
git commit -m "Restore README"
git push origin main
```

---

# Common Mistakes

## Wrong

```powershell
git checkout <commit-id> -- folder
```

Typing `<commit-id>` literally causes an error.

---

## Correct

```powershell
git checkout 337ed06 -- Python/day1_variables
```

---

## Important Notes

- Always replace `<commit-id>` with the actual commit hash.
- Verify files after recovery.
- Commit the restored files.
- Push changes to GitHub.

---

# Quick Recovery Cheat Sheet

## Folder

```powershell
git log --oneline -- Python/day1_variables

git checkout 337ed06 -- Python/day1_variables

git add .

git commit -m "Restore deleted folder"

git push origin main
```

---

## File

```powershell
git log --oneline -- README.md

git checkout 337ed06 -- README.md

git add .

git commit -m "Restore deleted file"

git push origin main
```
