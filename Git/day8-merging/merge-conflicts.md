# Merge Conflicts

## What is a Merge Conflict?

A merge conflict happens when Git cannot automatically combine changes.

This usually occurs when the same part of the same file has been modified in different branches.

---

## Example

### main branch

```python
print("Welcome")
```

### feature-login branch

```python
print("Welcome User")
```

Git doesn't know which version should be kept.

---

## Conflict Message

```text
CONFLICT (content): Merge conflict in app.py

Automatic merge failed.
Fix conflicts and then commit the result.
```

---

## Conflict Markers

Git marks conflicts inside the file.

```text
<<<<<<< HEAD

print("Welcome")

=======

print("Welcome User")

>>>>>>> feature-login
```

---

## Resolve the Conflict

Edit the file manually.

Choose the correct code.

Example

```python
print("Welcome User")
```

Remove all conflict markers.

---

## Save the File

Stage the resolved file.

```powershell
git add app.py
```

Commit the merge.

```powershell
git commit -m "Resolve merge conflict"
```

---

## Verify

```powershell
git status
```

Expected

```text
nothing to commit, working tree clean
```

---

## Avoid Merge Conflicts

- Pull the latest changes before starting work.
- Commit frequently.
- Merge regularly.
- Communicate with teammates.
- Work on different files whenever possible.

---

## Merge Conflict Workflow

```text
Create Branch

↓

Make Changes

↓

Commit Changes

↓

Switch to main

↓

Merge

↓

Conflict?

↓

Yes

↓

Resolve Conflict

↓

git add

↓

git commit

↓

Done
```

---

## Useful Commands

View current branch.

```powershell
git branch
```

Check repository status.

```powershell
git status
```

View commit history.

```powershell
git log --oneline
```

Abort a merge (if needed).

```powershell
git merge --abort
```

Continue after resolving the conflict.

```powershell
git add .

git commit -m "Resolve merge conflict"
```

---

## Best Practices

- Read the conflict markers carefully.
- Never delete code without understanding the changes.
- Test the application after resolving conflicts.
- Commit immediately after the conflict is resolved.
