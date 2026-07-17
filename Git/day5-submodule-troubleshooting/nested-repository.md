# Nested Git Repository

## What is a Nested Repository?

A nested repository is a Git repository created inside another Git repository.

Example:

```text
python-learning/
│
├── .git
│
└── Python/
    └── day1_variables/
        └── .git
```

---

## Why is it a Problem?

Git treats the folder as a separate repository.

Instead of adding the files, Git stores only a reference.

---

## How to Detect It

### Check for Hidden .git Folder

```powershell
Test-Path .\Python\day1_variables\.git
```

Output

```text
True
```

A nested repository exists.

---

### List All .git Folders

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

## Solution

Delete the nested `.git` folder.

```powershell
Remove-Item -Recurse -Force .\Python\day1_variables\.git
```

Verify

```powershell
Test-Path .\Python\day1_variables\.git
```

Expected

```text
False
```
