# Git Submodule Notes

## What is a Submodule?

A Git submodule is another Git repository stored inside a parent Git repository.

Instead of tracking the files inside the folder, Git tracks only a reference to another repository.

---

## Normal Repository Structure

```text
python-learning/
│
├── .git
│
├── Python/
│   ├── day1_variables/
│   ├── day2_conditions/
│   └── day3_loops/
```

Only one `.git` folder exists.

---

## Nested Repository Structure

```text
python-learning/
│
├── .git
│
└── Python/
    └── day1_variables/
        └── .git
```

Now Git thinks `day1_variables` is another repository.

---

## Why Did This Happen?

Because `git init` was executed inside:

```text
Python/day1_variables
```

instead of

```text
python-learning
```

---

## Result

GitHub displays an arrow (↪) instead of a normal folder.

Git tracks only the repository reference instead of the files.

---

## Key Lesson

Never run:

```powershell
git init
```

inside a folder that already belongs to another Git repository.
