# git branch

## Purpose

Create, list, rename, and delete branches.

---

## View All Local Branches

```powershell
git branch
```

Example

```text
* main
```

The * indicates the current branch.

---

## Create a New Branch

```powershell
git branch feature-login
```

---

## Verify

```powershell
git branch
```

Output

```text
* main
  feature-login
```

---

## Rename Branch

```powershell
git branch -m old-name new-name
```

Example

```powershell
git branch -m feature-login login-page
```

---

## Delete Branch

```powershell
git branch -d feature-login
```

Delete forcefully

```powershell
git branch -D feature-login
```

---

## View All Branches

```powershell
git branch -a
```

---

## Best Practices

- Use descriptive names.
- Delete unused branches.
- Keep the main branch stable.
