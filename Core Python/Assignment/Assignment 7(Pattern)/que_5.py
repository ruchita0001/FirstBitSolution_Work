# hollow number pyramid with last row full
    1
   1 2 
  1   3
 1     4
1 2 3 4 5


n = 5 
# Top hollow numbers
for i in range(1, n):
    print(" " * (n - i), end="") 
    print(1, end="") 
    if i > 1:
        print(" " * (2*i - 3), end="")
        print(i, end=" ")
    print() 

# Bottom row (full numbers)
for i in range(1, n+1):
    print(i, end=" ") 
