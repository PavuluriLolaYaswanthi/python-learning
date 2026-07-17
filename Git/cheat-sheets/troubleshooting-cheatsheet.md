# Git Troubleshooting Cheat Sheet

## Check Repository Status

```powershell
git status
```

---

## Check Remote Repository

```powershell
git remote -v
```

---

## View Commit History

```powershell
git log --oneline
```

---

## View Folder History

```powershell
git log --oneline -- Python/day1_variables
```

---

## Check if Folder Exists

```powershell
Test-Path .\Python\day1_variables
```

---

## Show Hidden Files

```powershell
Get-ChildItem -Force
```

---

## Find All .git Folders

```powershell
Get-ChildItem -Recurse -Force -Directory -Filter .git
```

---

## Delete Nested Repository

```powershell
Remove-Item -Recurse -Force .\Python\day1_variables\.git
```

---

## Remove Submodule

```powershell
git rm --cached Python/day1_variables
```

---

## Add Folder Again

```powershell
git add Python/day1_variables
```

---

## Commit

```powershell
git commit -m "Convert submodule to normal folder"
```

---

## Push

```powershell
git push origin main
```

---

## Display Folder Structure

```powershell
tree /f
```

---

## Check .gitmodules

```powershell
type .gitmodules
```

---

## View .gitignore

```powershell
Get-Content .gitignore
```
