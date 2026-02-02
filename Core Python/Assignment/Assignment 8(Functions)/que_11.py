# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

n = int(input("Enter number: "))

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def sum_pow(n, digits):
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total

def is_armstrong(n):
    digits = count_digits(n)
    result = sum_pow(n, digits)
    return result == n
    
    
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
