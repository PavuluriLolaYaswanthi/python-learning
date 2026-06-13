# Day 1 Notes

## Topics Learned

- Variables
- Input/Output
- Data Types

## Practice Done

- Built simple calculator project
- Practiced taking user input
- Practiced printing output

## Important Concepts

- input() gives string
- int() converts to integer
- float() converts to decimal
- Variables store data
- print() displays output

## Problems Faced

- Forgot to convert input values to numbers
- Got errors while running Python file
- Learned how indentation works in Python

## What I Learned

Today I learned basic Python fundamentals like variables, input/output, and data types. I understood how user input works and how to convert strings into integers or floats. I also built my first calculator program using if-else conditions and mathematical operators.

## Git Commands Used — Day 1

### Initialize Git Repository

git init

### Check Current Status

git status

### Add All Files

git add .

### Commit Files

git commit -m "Day 1 Python basics and calculator"

### Configure Git Username

git config --global user.name "PavuluriLolaYaswanthi"

### Configure Git Email

git config --global user.email "<lolayaswanthipavuluri13@gmail.com>"

### Add GitHub Remote Repository

git remote add origin <https://github.com/PavuluriLolaYaswanthi/python-learning.git>

### Remove Wrong Remote

git remote remove origin

### Rename Branch to Main

git branch -M main

### Pull GitHub Changes

git pull origin main --allow-unrelated-histories

### Push Code to GitHub

git push -u origin main

### Force Push (Used for Cleaning Duplicate Commits)

git push origin main --force

### Remove Latest Commit But Keep Files

git reset --soft HEAD~1

### Run Python Files

python hello.py
python variables.py
python input_output.py
python data_types.py
python calculator.py

### Change Folder

cd python
cd day1_variables

## Git Notes – Recover Deleted Files and Folders

## View Commit History

Shows all commits related to a specific file or folder.

```powershell
git log --oneline -- Python/day1_variables
```

Example:

```text
337ed06 Day 2 Python practice
```

---

## Restore a Deleted Folder

Restore a folder from a previous commit.

```powershell
git checkout 337ed06 -- Python/day1_variables
```

Replace `337ed06` with the commit ID from your history.

---

## Verify Folder is Restored

```powershell
Get-ChildItem Python
```

or

```powershell
dir Python
```

You should see:

```text
day1_variables
day2_conditions
day3_loops
day4_functions
```

---

## Save the Restored Folder

After restoring, commit and push the changes.

```powershell
git add .
git commit -m "Restore day1_variables"
git push origin main
```

---

## View Recent Commits

```powershell
git log --oneline
```

Example:

```text
f8c61ca Remove day1_variables folder
337ed06 Day 2 Python practice
```

---

## Check Repository Status

```powershell
git status
```

Useful for checking:

- Modified files
- Deleted files
- Untracked files

---

## Check if a Folder Exists

```powershell
Test-Path .\Python\day1_variables
```

Output:

```text
True
```

Folder exists.

Output:

```text
False
```

Folder does not exist.

---

## Common Mistake

❌ Wrong:

```powershell
git checkout <commit-id> -- Python/day1_variables
```

PowerShell treats `<` and `>` specially and this is only a placeholder.

✅ Correct:

```powershell
git checkout 337ed06 -- Python/day1_variables
```

Always replace the placeholder with a real commit ID.

---

## Recovery Workflow

### 1. Find the commit

```powershell
git log --oneline -- Python/day1_variables
```

### 2. Restore the folder

```powershell
git checkout <commit-id> -- Python/day1_variables
```

### 3. Verify

```powershell
Get-ChildItem Python
```

### 4. Commit the restoration

```powershell
git add .
git commit -m "Restore deleted folder"
git push origin main
```

---

## Key Lesson

Git stores snapshots of your project history.

Even if a file or folder is deleted, you can usually recover it from a previous commit using:

```powershell
git checkout <commit-id> -- <path>
```
