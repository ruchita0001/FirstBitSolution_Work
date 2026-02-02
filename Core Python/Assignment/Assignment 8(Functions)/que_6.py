# WAP to find print the following Fibonacci series using functions:
# 1 1 2 3 5 8 n terms

n = int(input("Enter a number: "))

def fibonacci(n):
    a = 1
    b = 1
    print(a, b, end=" ")
    for i in range(3, n+1):
        c = a+b
        print(c, end=" ")
        a=b
        b=c

fibonacci(n)
