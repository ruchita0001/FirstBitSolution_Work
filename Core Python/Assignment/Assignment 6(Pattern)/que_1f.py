# Program to print a pyramid pattern of numbers
        1 
      1 2 3 
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9


n = 5   # number of rows
for i in range(1, n+1):
    # printing spaces
    for space in range(n - i):
        print("  ", end="")

    # printing numbers
    for num in range(1, 2*i):
        print(num, end=" ")
    print()
