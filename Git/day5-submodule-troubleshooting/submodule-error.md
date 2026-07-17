# Common Submodule Errors

## Error 1

```text
fatal: Pathspec 'Python/day1_variables/*' is in submodule 'Python/day1_variables'
```

### Cause

Git thinks the folder is another repository.

---

## Error 2

GitHub shows

```text
day1_variables ↪
```

instead of

```text
day1_variables/
```

### Cause

The folder is stored as a submodule.

---

## Error 3

Folder appears empty on GitHub.

### Cause

Git tracked only the submodule reference.

---

## Error 4

```text
nothing to commit
```

but files exist locally.

### Cause

Git is tracking the submodule instead of the files.

---

## Solution

Remove the submodule.

Then add the folder again as a normal folder.
