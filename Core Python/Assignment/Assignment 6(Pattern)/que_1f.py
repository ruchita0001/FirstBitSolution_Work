# Program to print a pyramid pattern of numbers

n = 5   # number of rows
for i in range(1, n+1):
    # printing spaces
    for space in range(n - i):
        print("  ", end="")

    # printing numbers
    for num in range(1, 2*i):
        print(num, end=" ")

    print()