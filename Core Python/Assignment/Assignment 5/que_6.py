# Write a program to print first n prime numbers.

n = int(input("Enter the value of n to print prime numbers : "))

print(f"The first {n} prime numbers are : ")

count = 0
i = 2

while(count < n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i,end=" ")
        count += 1
        
    i += 1
