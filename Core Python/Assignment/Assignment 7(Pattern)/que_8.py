# hollow mirrored number pyramid

# 1               1 
# 1 2           2 1 
# 1 2 3       3 2 1
# 1 2 3 4   4 3 2 1
# 1 2 3 4 5 4 3 2 1

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = " ")

    for j in range(i+1,6):
        print(" ",end = " ")

    for j in range(1,5-i):
        print(" ", end = " ")

    for j in range(i, 0, -1):
        if i < 5:
            print(j, end=" ")
        else:
            if j == 5:
                continue
            print(j, end=" ")
            
    print()
