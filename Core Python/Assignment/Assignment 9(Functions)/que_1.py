# WAP to find sum of following series using recursive functions:
# i. 1! + 2! + 3! + 4! +..... + n!


def fact(n):
    if n == 0:
        return 1
    else:
        return  n * fact(n-1)
    
def sum(n):
    if n == 0:
        return 0
    else:
        return fact(n) + sum(n-1)
    
n = int(input("Enter the value of n: "))
res = sum(n)
print(f"Sum of Series of Factorial from 1 to {n} =  {res}")
