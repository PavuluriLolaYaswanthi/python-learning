# Day 10 Notes — Modules + pip

## Topics Learned

- Modules
- import
- from ... import
- Built-in modules
- Third-party packages
- pip
- Virtual environments
- requirements.txt

---

## What is a Module?

A module is a Python file containing reusable code such as functions and variables.

Example:

```python
import mymodule
```

---

## Creating a Module

```python
def add(a, b):
    return a + b
```

The file can be imported into another Python program.

---

## Importing a Module

```python
import mymodule

print(mymodule.add(10, 20))
```

---

## Importing Specific Functions

```python
from mymodule import add

print(add(10, 20))
```

---

## Built-in Modules

Python provides many built-in modules.

Examples:

```python
import math
import random
```

Example:

```python
import math

print(math.sqrt(25))
```

---

## What is pip?

pip is Python's package installer.

It is used to install third-party Python packages.

Example:

```bash
python -m pip install requests
```

---

## Useful pip Commands

Check pip:

```bash
python -m pip --version
```

Install package:

```bash
python -m pip install requests
```

List packages:

```bash
python -m pip list
```

Show package information:

```bash
python -m pip show requests
```

Create requirements.txt:

```bash
python -m pip freeze > requirements.txt
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## Virtual Environment

A virtual environment provides an isolated environment for a Python project.

Create:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

---

## Important

Do not upload `.venv` to GitHub.

Add it to `.gitignore`:

```text
.venv/
__pycache__/
```

---

## Practice Done

- Created a custom Python module
- Imported a custom module
- Used built-in modules
- Installed a package using pip
- Practiced a virtual environment
- Learned about requirements.txt

---

## Problems Faced

- Understanding import syntax
- Understanding the difference between modules and packages
- Installing packages with pip
- Understanding virtual environments

---

## What I Learned

Today I learned how Python code can be organized into reusable modules and how external packages can be installed using pip. I also learned why virtual environments are used to keep project dependencies isolated.

---

## Interview Questions

### What is a module?

A module is a Python file containing reusable code.

### What is pip?

pip is Python's package installer used to install third-party packages.

### What is a virtual environment?

A virtual environment creates an isolated Python environment for a project.

### Why use requirements.txt?

It records project dependencies so they can be installed again easily.

---

## Commands Used

```bash
python --version
python -m pip --version

python -m pip install requests
python -m pip list
python -m pip show requests

python -m venv .venv

python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt

deactivate # if active we can deactivate
Remove-Item -Recurse -Force .venv #remove the .venv
```
