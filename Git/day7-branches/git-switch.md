# git switch

## Purpose

Switch from one branch to another.

---

## Syntax

```powershell
git switch branch-name
```

---

## Example

```powershell
git switch feature-login
```

---

## Create and Switch

```powershell
git switch -c feature-login
```

Equivalent to:

```powershell
git branch feature-login
git switch feature-login
```

---

## Switch Back

```powershell
git switch main
```

---

## Why Use git switch?

Before Git 2.23, developers used:

```powershell
git checkout
```

Now Git provides:

```powershell
git switch
```

which is easier and safer.

---

## Best Practice

Use

```powershell
git switch
```

only for changing branches.
