# Undo Changes Notes

## Why Do We Need Undo Commands?

While working on a project, mistakes are common.

Examples:

- Modified the wrong file.
- Added unwanted changes.
- Committed incorrect code.
- Need to restore an older version.
- Accidentally staged files.

Git provides different commands depending on what you want to undo.

---

## Undo Commands

- git restore
- git reset
- git revert
- git diff

---

## Which Command Should You Use?

| Situation | Command |
|-----------|----------|
| Discard unstaged changes | git restore |
| Remove staged files | git reset |
| Undo a commit locally | git reset |
| Undo a pushed commit | git revert |
| Compare changes | git diff |

---

## Best Practices

- Prefer `git revert` for commits that have already been pushed.
- Use `git reset --hard` carefully because it permanently removes local changes.
- Review differences with `git diff` before discarding changes.
