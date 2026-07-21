# git clone

## Purpose

Downloads a remote GitHub repository to your local computer.

---

## Syntax

```powershell
git clone <repository-url>
```

---

## Example

```powershell
git clone https://github.com/username/python-learning.git
```

---

## What Happens?

Git creates a local copy of the repository.

Example

```text
python-learning/
│
├── .git
├── README.md
├── Python/
└── Projects/
```

---

## Verify

```powershell
cd python-learning

git status
```

Expected

```text
On branch main

nothing to commit, working tree clean
```

---

## Best Practices

- Clone only once.
- Use `git pull` to update an existing repository.
