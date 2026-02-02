# WAP to find sum of n numbers using recursion.

def sum_n(n):
    if (n == 1):
        return 1
    return n + sum_n(n-1)  

n = int(input("Enter the value of n:  "))

res = sum_n(n)
print(f"Sum of first {n} numbers = {res}")
