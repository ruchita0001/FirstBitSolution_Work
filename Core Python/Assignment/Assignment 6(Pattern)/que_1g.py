# Alphabet pyramid pattern
        A 
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I


n = 5   
for i in range(1, n+1):
    for space in range(n - i):
        print("  ", end="")
    for alpha in range(1, 2*i):
        print(chr(65 + alpha - 1), end=" ")
    print()
