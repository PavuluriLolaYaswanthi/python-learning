# git stash

## Purpose

Temporarily save all modified and staged changes.

---

## Syntax

```powershell
git stash
```

---

## Example

```powershell
git stash
```

Output

```text
Saved working directory and index state
```

---

## Create a Named Stash

```powershell
git stash push -m "Login feature"
```

---

## Verify

```powershell
git stash list
```

---

## Best Practices

- Give meaningful names.
- Stash only temporary work.
