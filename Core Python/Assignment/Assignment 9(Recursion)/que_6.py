#WAP to print Fibonacci series using recursion.

n = int(input("Enter number of terms: "))

def fib(n):
    if n == 1 or n == 2:  
        return 1
    return fib(n-1) + fib(n-2)

def print_fib(n, i=1):
    if i > n:
        return
    print(fib(i), end=" ")
    print_fib(n, i+1)

print_fib(n)
