# WAP to find sum of digits of a number.

n = int(input("Enter a number: "))

def sum_digit(n):
    sum = 0
    while(n>0):
        d = n%10
        sum += d
        n = n // 10
        
    return sum
res = sum_digit(n)
print(f"The sum of digit of {n} is {res}")
