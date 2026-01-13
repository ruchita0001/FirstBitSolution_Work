# Pascal’s Triangle

rows = 4

for i in range(rows):
    print(" " * (rows - i - 1), end="")  # Leading spaces
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)  # Next number in Pascal's Triangle
    print()
