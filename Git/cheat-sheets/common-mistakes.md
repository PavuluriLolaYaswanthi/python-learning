# Common Git Mistakes

## Mistake 1

Running

```powershell
git init
```

inside a folder that already belongs to another Git repository.

### Wrong

```text
python-learning/
│
└── Python/
    └── day1_variables/
        └── git init ❌
```

### Correct

```text
python-learning/
│
└── git init ✅
```

---

## Mistake 2

Forgetting to check repository status.

Always run

```powershell
git status
```

before committing.

---

## Mistake 3

Forgetting to stage files.

```powershell
git add .
```

---

## Mistake 4

Writing poor commit messages.

❌ Bad

```text
update

abc

test
```

✅ Good

```text
Add Day 4 Functions

Fix Login Bug

Complete Expense Tracker
```

---

## Mistake 5

Forgetting to push.

```powershell
git push origin main
```

---

## Mistake 6

Deleting files without checking Git history.

Always check

```powershell
git log --oneline
```

before attempting recovery.

---

## Mistake 7

Ignoring Git error messages.

Read the error carefully.

Most Git errors clearly explain the problem.

Example

```text
fatal: Pathspec 'Python/day1_variables/*' is in submodule 'Python/day1_variables'
```

This tells you the folder is being treated as a submodule.

---

## Mistake 8

Creating multiple `.git` folders.

Correct

```text
python-learning/
│
├── .git
│
├── Python/
├── Git/
└── Projects/
```

Wrong

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

# Golden Rules

✅ One repository = One `.git` folder

✅ Run `git status` often

✅ Commit frequently

✅ Push regularly

✅ Use meaningful commit messages

✅ Read Git error messages carefully

✅ Keep your repository organized
