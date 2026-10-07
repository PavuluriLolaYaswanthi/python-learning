from module import calculate_average, is_passed

marks = [80, 70, 90, 60]

average = calculate_average(marks)

print(f"Average: {average}")

if is_passed(marks):
    print("Student passed.")
else:
    print("Student failed.")