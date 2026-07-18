# Fast-Forward Merge

## What is a Fast-Forward Merge?

A Fast-Forward Merge happens when the target branch has not changed since the feature branch was created.

Git simply moves the branch pointer forward.

---

## Example

Before Merge

```text
A ---- B (main)
        \
         C ---- D (feature-login)
```

After Merge

```text
A ---- B ---- C ---- D (main)
```

No extra merge commit is created.

---

## Command

```powershell
git switch main

git merge feature-login
```

Git automatically performs a Fast-Forward Merge if possible.

---

## Advantages

- Cleaner commit history.
- No unnecessary merge commit.
- Faster merge process.

---

## When Does It Happen?

Fast-Forward Merge occurs when:

- No new commits exist on `main`.
- Only the feature branch contains new commits.

---

## Verify

```powershell
git log --oneline --graph
```

Expected Output

```text
* D Add Login Feature
* C Create Login Page
* B Initial Commit
```
