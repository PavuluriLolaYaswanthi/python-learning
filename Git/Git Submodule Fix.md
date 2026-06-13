# Git Submodule Fix

## Error

```text
fatal: Pathspec 'folder/*' is in submodule 'folder'
```

## Cause

The folder was accidentally initialized as a separate Git repository and became a submodule.

## Fix

```powershell
git rm --cached Python/day1_variables
git add Python/day1_variables
git commit -m "Convert submodule to normal folder"
git push origin main
```

## Check for Submodules

```powershell
type .gitmodules
```

If a folder appears here, Git treats it as a submodule.

## Lesson

Never run:

```powershell
git init
```

inside a project folder that already belongs to another Git repository
