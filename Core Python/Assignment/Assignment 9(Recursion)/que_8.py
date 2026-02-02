#WAP to check whether a number is prime or not using recursion.

num = int(input("Enter number: "))

def is_prime(n, i=None):
    if n <= 1:
        return False
    if i is None:
        i = n // 2  
    if i == 1:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i-1)

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")
