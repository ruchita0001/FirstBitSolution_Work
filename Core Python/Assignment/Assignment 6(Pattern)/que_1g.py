# Alphabet pyramid pattern

n = 5   # number of rows

for i in range(1, n+1):

    # printing spaces
    for space in range(n - i):
        print("  ", end="")

    # printing alphabets
    for alpha in range(1, 2*i):
        print(chr(65 + alpha - 1), end=" ")

    print()
