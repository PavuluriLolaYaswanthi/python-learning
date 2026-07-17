# Git Recovery Cheat Sheet

## Recover a Deleted Folder

### Find Commit History

```powershell
git log --oneline -- Python/day1_variables
```

---

### Restore Folder

```powershell
git checkout <commit-id> -- Python/day1_variables
```

Example

```powershell
git checkout 337ed06 -- Python/day1_variables
```

---

### Verify

```powershell
Get-ChildItem Python
```

---

### Save Changes

```powershell
git add .

git commit -m "Restore deleted folder"

git push origin main
```

---

## Recover a Deleted File

Find history.

```powershell
git log --oneline -- README.md
```

---

Restore file.

```powershell
git checkout <commit-id> -- README.md
```

---

Commit.

```powershell
git add .

git commit -m "Restore README"

git push origin main
```

---

## Important

Replace

```text
<commit-id>
```

with the actual commit hash.

Example

```text
337ed06
```
