# number pyramid with mirrored numbers
#         1 
#       2 3 2 
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5


n = 5  
for i in range(1, n+1):
    print(" " * (n - i) * 2, end="")

    num = i
    for j in range(i):
        print(num, end=" ")
        num += 1
      
    num -= 2
    for j in range(i-1):
        print(num, end=" ")
        num -= 1

    print()  
