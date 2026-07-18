# Common Git Mistakes

This document lists common mistakes beginners make while learning Git and how to avoid them.

---

# Mistake 1

## Running `git init` Inside an Existing Repository

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

### Why?

A Git project should normally contain only **one `.git` folder** at its root.

Running `git init` inside a tracked folder creates a nested repository, which Git treats as a submodule.

---

# Mistake 2

## Forgetting to Check Repository Status

Always check the status before and after making changes.

```powershell
git status
```

This helps identify:

- Modified files
- Deleted files
- Untracked files
- Staged files

---

# Mistake 3

## Working Directly on the `main` Branch

❌ Avoid making large changes directly on `main`.

### Better Approach

```powershell
git switch -c feature-login
```

Develop your feature in a separate branch, then merge it into `main`.

---

# Mistake 4

## Forgetting to Stage Changes

Git only commits staged files.

```powershell
git add .
```

Always stage your changes before committing.

---

# Mistake 5

## Writing Poor Commit Messages

### Bad Examples

```text
update

abc

test

changes
```

### Good Examples

```text
Add Day 8 merge notes

Fix login validation bug

Complete expense tracker project

Update README documentation
```

Write commit messages that clearly describe your changes.

---

# Mistake 6

## Forgetting to Push Changes

Your commits remain only on your local machine until you push them.

```powershell
git push origin main
```

Push your work regularly to GitHub.

---

# Mistake 7

## Deleting Files Without Checking Git History

If a file or folder is accidentally deleted:

```powershell
git log --oneline
```

Find the commit where it existed and restore it using:

```powershell
git checkout <commit-id> -- <path>
```

---

# Mistake 8

## Ignoring Git Error Messages

Read Git errors carefully.

Example:

```text
fatal: Pathspec 'Python/day1_variables/*' is in submodule 'Python/day1_variables'
```

This clearly indicates that Git is treating the folder as a submodule.

Understanding the message helps identify the correct solution.

---

# Mistake 9

## Forgetting to Switch to the Correct Branch

Before making changes, check your current branch.

```powershell
git branch
```

The current branch is marked with an asterisk (`*`).

Example:

```text
* feature-login
  main
```

---

# Mistake 10

## Merging Untested Code

Always test your feature before merging it into the `main` branch.

Recommended workflow:

```powershell
git switch main

git merge feature-login

git branch -d feature-login
```

---

# Mistake 11

## Not Resolving Merge Conflicts Properly

Do not simply delete conflict markers.

Review both versions, choose the correct changes, and then:

```powershell
git add .

git commit -m "Resolve merge conflict"
```

---

# Mistake 12

## Deleting a Branch Before Merging

Deleting a branch without merging can result in lost work.

Merge first:

```powershell
git merge feature-login
```

Then delete:

```powershell
git branch -d feature-login
```

---

# Mistake 13

## Creating Multiple `.git` Folders

### Correct

```text
python-learning/
│
├── .git
├── Python/
├── Projects/
└── Git/
```

### Wrong

```text
python-learning/
│
├── .git
│
└── Python/
    └── day1_variables/
        └── .git
```

A single project should normally contain only one Git repository.

---

# Golden Rules

✅ Initialize Git only once at the project root.

✅ Check `git status` frequently.

✅ Create a new branch for each feature or bug fix.

✅ Commit small, meaningful changes.

✅ Write clear commit messages.

✅ Test your code before merging.

✅ Merge feature branches into `main` only after testing.

✅ Delete feature branches after merging.

✅ Push your changes regularly.

✅ Read Git error messages carefully.

✅ Keep your repository clean and organized.

✅ Maintain one `.git` folder per project.
