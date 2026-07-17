# Remove-Item

## Purpose

Deletes files or folders.

---

## Syntax

```powershell
Remove-Item <path>
```

---

## Delete Folder

```powershell
Remove-Item -Recurse -Force FolderName
```

---

## Delete Nested Git Repository

```powershell
Remove-Item -Recurse -Force .\Python\day1_variables\.git
```

---

## Options

### -Recurse

Deletes all files and subfolders.

### -Force

Deletes hidden and protected files.

---

## Verify

```powershell
Test-Path .\Python\day1_variables\.git
```

Output

```text
False
```

The folder has been deleted.

---

## Warning

`Remove-Item` permanently deletes files.

Always verify the path before running the command.
