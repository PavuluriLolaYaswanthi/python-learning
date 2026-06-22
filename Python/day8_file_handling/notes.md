# Day 8 Notes — File Handling

## Topics Learned

- File Handling
- Read Files
- Write Files
- Append Files
- File Modes

---

## What is File Handling?

File handling allows programs to store and retrieve data from files.

Without file handling, data is lost when the program closes.

---

## File Modes

| Mode | Purpose |
|--------|----------|
| r | Read |
| w | Write |
| a | Append |
| x | Create File |

---

## Writing to a File

```python
with open("notes.txt", "w") as file:
    file.write("Hello Python")
```

---

## Reading a File

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

---

## Appending to a File

```python
with open("notes.txt", "a") as file:
    file.write("\nNew Data")
```

---

## Practice Done

- Created files
- Wrote data to files
- Read file contents
- Appended new data
- Built Expense Tracker with file storage

---

## Problems Faced

- Forgot file modes
- File not found errors
- Forgetting to close files

---

## What I Learned

Today I learned how to store data permanently using files. I practiced reading, writing, and appending data and upgraded my Expense Tracker to save expenses in a text file.

---

## Interview Questions

### What is file handling?

File handling allows programs to read from and write to files.

### Difference between w and a?

- w overwrites file content.
- a adds content to the end of the file.

### Why use with open()?

It automatically closes the file and is safer.

---

## Commands Used

```bash
python write_file.py
python read_file.py
python append_file.py
python expense_file_tracker.py

git add .
git commit -m "Day 8 file handling"
git push
```