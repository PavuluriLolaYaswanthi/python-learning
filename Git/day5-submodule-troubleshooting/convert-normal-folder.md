# Convert a Submodule into a Normal Folder

## Workflow

Nested Repository

↓

Delete .git Folder

↓

Remove Submodule Reference

↓

Add Folder

↓

Commit

↓

Push

↓

Normal Folder

---

## Commands

### Remove Nested Repository

```powershell
Remove-Item -Recurse -Force .\Python\day1_variables\.git
```

---

### Remove Submodule

```powershell
git rm --cached Python/day1_variables
```

---

### Add Folder Again

```powershell
git add Python/day1_variables
```

---

### Commit

```powershell
git commit -m "Convert submodule to normal folder"
```

---

### Push

```powershell
git push origin main
```

---

## Verify

GitHub should display:

```text
Python/
│
├── day1_variables/
├── day2_conditions/
├── day3_loops/
├── day4_functions/
```

No arrow (↪) should appear beside `day1_variables`.

---

## Lessons Learned

- One Git repository should normally contain only one `.git` folder.
- Never run `git init` inside an existing Git repository.
- Always check `git status` when something looks wrong.
- If GitHub shows an arrow icon (↪), check for a nested repository or submodule.
- Read Git error messages carefully—they usually point to the real problem.
