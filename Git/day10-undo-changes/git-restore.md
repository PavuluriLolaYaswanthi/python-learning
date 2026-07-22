# git restore

## Purpose

Discard changes made to files that have not been committed.

---

## Restore a File

```powershell
git restore README.md
```

---

## Restore Multiple Files

```powershell
git restore file1.py file2.py
```

---

## Restore All Files

```powershell
git restore .
```

---

## Restore a Staged File

```powershell
git restore --staged README.md
```

---

## Verify

```powershell
git status
```

---

## Best Practices

- Use before committing.
- Check changes with `git diff` first.
- Be careful, as discarded changes cannot be recovered unless committed.
