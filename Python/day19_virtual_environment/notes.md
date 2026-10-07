# Day 19 Notes — pip + Virtual Environment

## Topics Learned

- Virtual environments
- venv
- pip
- pip install
- pip list
- pip freeze
- requirements.txt
- Activating and deactivating venv

---

## What is a Virtual Environment?

A virtual environment is an isolated Python environment for a project.

It allows a project to have its own Python packages without affecting other projects.

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate — Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Activate — Git Bash

```bash
source venv/Scripts/activate
```

### Deactivate

```bash
deactivate
```

---

## pip

`pip` is used to install and manage Python packages.

Example:

```bash
python -m pip install requests
```

### Check Installed Packages

```bash
python -m pip list
```

### pip freeze

```bash
python -m pip freeze
```

It shows installed packages and their versions.

---

## requirements.txt

Create it using:

```bash
python -m pip freeze > requirements.txt
```

Install from it using:

```bash
python -m pip install -r requirements.txt
```

---

## Practice Done

- Created a virtual environment
- Activated venv
- Installed requests
- Used requests in Python
- Checked installed packages
- Created requirements.txt
- Tested requirements.txt
- Deactivated venv

---

## Important Concepts

- venv keeps project packages isolated.
- pip installs Python packages.
- pip freeze shows installed packages and versions.
- requirements.txt records project dependencies.
- venv should not be pushed to GitHub.

---

## Problems Faced

Write any errors you encountered here.

---

## What I Learned

Today I learned how to create and manage a Python
virtual environment and install project dependencies
using pip.

---

## Commands Used

```bash
python -m venv venv
python -m pip install requests
python -m pip list
python -m pip freeze
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
deactivate
```

---

## GitHub

After testing everything:

```bash
git status
git add .
git commit -m "Complete Day 19 pip and virtual environment"
git push
git status
```

Expected:

```text
nothing to commit, working tree clean
```
