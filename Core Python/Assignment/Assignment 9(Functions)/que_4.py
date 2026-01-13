# WAP to find sum of n numbers using recursion.

def sumOfNumbers(n):
    if n == 0:
        return 0
    else:
        return n + sumOfNumbers(n-1)
    
n = int(input("Enter the value of of n :  "))
res = sumOfNumbers(n)
print(f"Sum of first {n} numbers = {res}")