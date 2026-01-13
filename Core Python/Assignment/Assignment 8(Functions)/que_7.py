# WAP to find sum of digits of a number.

def sumOfDigit(num):
    sum = 0

    while(num > 0):
        d = num % 10
        sum += d
        num = num // 10

    return sum


num = int(input("Enter the Number : "))

res = sumOfDigit(num)

print(f"The sum of digits of {num} is {res}")