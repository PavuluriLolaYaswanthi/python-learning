def calculate_average(marks):

    total = 0

    for mark in marks:
        total += mark

    return total / len(marks)


def is_passed(marks):

    average = calculate_average(marks)

    return average >= 50