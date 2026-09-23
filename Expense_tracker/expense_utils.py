def save_expense(category, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{category} - {amount}\n")
def read_expenses():
    try:
        with open("expenses.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""
def calculate_total(expenses):
    total = 0.0
    for line in expenses.splitlines():
        if " - " in line:
            category, amount = line.split(" - ", 1)
            try:
                total += float(amount)
            except ValueError:
                pass
    return total