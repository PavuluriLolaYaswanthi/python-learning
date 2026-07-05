# git commit

## Purpose

Creates a permanent snapshot of your staged changes.

---

## Syntax

```powershell
git commit -m "message"
```

---

## Example

```powershell
git commit -m "Day 1 variables completed"
```

---

## Good Commit Messages

```text
Add Day 1 variables

Fix login bug

Update README

Complete expense tracker
```

---

## Bad Commit Messages

```text
abc

test

update

changes
```

---

## Verify

```powershell
git log --oneline
```

---

## Best Practice

Every meaningful change should have its own commit.
