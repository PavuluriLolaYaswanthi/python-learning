# git checkout

## Purpose

Switch branches or restore files.

---

## Switch Branch

```powershell
git checkout feature-login
```

---

## Switch Back

```powershell
git checkout main
```

---

## Restore File

```powershell
git checkout HEAD -- notes.md
```

---

## Restore Folder

```powershell
git checkout 337ed06 -- Python/day1_variables
```

---

## Difference Between checkout and switch

### checkout

- Switch branches
- Restore files
- Restore folders

### switch

- Switch branches only

---

## Recommendation

Modern Git recommends:

```powershell
git switch
```

for changing branches.

Use

```powershell
git checkout
```

mainly for restoring files or working with older repositories.
