#Three lists – numbers, squares, cubes

numbers = [1, 2, 3, 4, 5]
squares = []
cubes = []

for i in numbers:
    squares.append(i * i)
    cubes.append(i * i * i)

print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
