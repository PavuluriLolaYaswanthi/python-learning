# Test-Path

## Purpose

Checks whether a file or folder exists.

---

## Syntax

```powershell
Test-Path <path>
```

---

## Example

```powershell
Test-Path .\Python\day1_variables
```

Output

```text
True
```

The folder exists.

---

## Example 2

```powershell
Test-Path .\Python\day1_variables\.git
```

Output

```text
True
```

A nested Git repository exists.

---

## After Removing .git

```powershell
Test-Path .\Python\day1_variables\.git
```

Output

```text
False
```

The nested repository has been removed.

---

## When to Use

- Verify files
- Verify folders
- Check if `.git` exists
