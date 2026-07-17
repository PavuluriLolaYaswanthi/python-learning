# Remove a Git Submodule

## Step 1

Delete the nested repository.

```powershell
Remove-Item -Recurse -Force .\Python\day1_variables\.git
```

---

## Step 2

Remove the submodule reference.

```powershell
git rm --cached Python/day1_variables
```

---

## Step 3

Check status.

```powershell
git status
```

---

## Step 4

Add the folder again.

```powershell
git add Python/day1_variables
```

---

## Step 5

Commit.

```powershell
git commit -m "Convert submodule to normal folder"
```

---

## Step 6

Push.

```powershell
git push origin main
```

---

## Verify

Refresh GitHub.

The arrow icon disappears.

The folder becomes a normal folder.
