# WAP to check if given number is Armstrong or not using recursive function.

def count_digits(n):
    if(n == 0):
        return 0
    return 1 + count_digits(n // 10)

def sum_pow(n, digits):
    if(n == 0):
        return 0
    digit = n % 10
    return (digit ** digits) + sum_pow(n // 10, digits)

def is_armstrong(n):
    digits = count_digits(n)
    return sum_pow(n, digits) == n

num = int(input("Enter number: "))

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
