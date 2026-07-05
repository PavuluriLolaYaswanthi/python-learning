# git init

## Purpose

Creates a new Git repository.

---

## Syntax

```powershell
git init
```

---

## Example

```powershell
cd python-learning
git init
```

---

## Output

```text
Initialized empty Git repository in ...
```

---

## What Happens?

Git creates a hidden folder.

```text
.git/
```

This folder stores:

- commits
- branches
- configuration
- history

---

## Verify

```powershell
Get-ChildItem -Force
```

You should see:

```text
.git
```

---

## Important

Run this command only once.

Initialize Git only in the project root.

Correct

```text
python-learning/
```

Wrong

```text
python-learning/Python/day1_variables/
```

Running git init inside another repository creates a nested repository.
