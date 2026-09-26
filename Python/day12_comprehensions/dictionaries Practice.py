numbers = [1, 2, 3, 4, 5]
squares = {
    number: number ** 2
    for number in numbers
}
print(squares)


marks = {"Alice": 90,"Bob": 55,"Charlie": 80,"David": 45}
passed ={
    name: mark
    for name, mark in marks.items()
    if mark >= 70
}
print(passed)



