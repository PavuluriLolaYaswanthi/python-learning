# GitHub Collaboration Workflow

## Clone Repository

```powershell
git clone https://github.com/username/project.git
```

↓

## Navigate into the Project

```powershell
cd project
```

↓

## Pull Latest Changes

```powershell
git pull origin main
```

↓

## Create a Feature Branch

```powershell
git switch -c feature-login
```

↓

## Work on the Project

Modify files.

↓

## Stage Changes

```powershell
git add .
```

↓

## Commit Changes

```powershell
git commit -m "Add login feature"
```

↓

## Push the Branch

```powershell
git push origin feature-login
```

↓

## Open a Pull Request

Review the changes on GitHub and create a Pull Request.

↓

## Merge into Main

After approval, merge the Pull Request.

---

# Complete Workflow

```powershell
git clone <repository-url>

cd project

git pull origin main

git switch -c feature-login

git add .

git commit -m "Add login feature"

git push origin feature-login
```

---

## Best Practices

- Pull before starting new work.
- Create one branch per feature.
- Keep Pull Requests small and focused.
- Respond to code review comments.
- Delete merged branches after the Pull Request is merged.
