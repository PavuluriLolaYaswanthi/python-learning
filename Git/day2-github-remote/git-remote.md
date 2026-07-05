# git remote

## Purpose

Displays or manages remote repositories connected to your local repository.

---

## Syntax

View remote repositories

```powershell
git remote -v
```

---

## Example

```powershell
git remote -v
```

Example Output

```text
origin  https://github.com/username/python-learning.git (fetch)

origin  https://github.com/username/python-learning.git (push)
```

---

## What Does This Mean?

### origin

The nickname of the remote repository.

---

### fetch

Downloads changes from GitHub.

Does NOT modify your local files.

---

### push

Uploads your commits to GitHub.

---

## Add a Remote Repository

```powershell
git remote add origin https://github.com/username/python-learning.git
```

Use this only once after creating a GitHub repository.

---

## Verify Remote

```powershell
git remote -v
```

Expected Output

```text
origin  https://github.com/username/python-learning.git (fetch)

origin  https://github.com/username/python-learning.git (push)
```

---

## Remove a Remote

```powershell
git remote remove origin
```

---

## Rename a Remote

```powershell
git remote rename origin github
```

---

## Common Errors

### No Remote Configured

```text
fatal: No remote repository specified.
```

Solution

Add a remote.

```powershell
git remote add origin <repository-url>
```

---

### Remote Already Exists

```text
error: remote origin already exists.
```

Solution

Remove the old remote.

```powershell
git remote remove origin
```

Then add the correct one.

---

## Best Practices

- Connect only one GitHub repository to one local project.
- Verify the remote using `git remote -v`.
- Keep the remote URL updated if the repository is renamed.
- Use meaningful repository names.

---

## Summary

Command

```powershell
git remote -v
```

Purpose

Shows all remote repositories connected to your project.

Command

```powershell
git remote add origin <repository-url>
```

Purpose

Connects a local repository to GitHub.

Command

```powershell
git remote remove origin
```

Purpose

Removes the existing remote.

Command

```powershell
git remote rename origin github
```

Purpose

Renames the remote repository alias.
