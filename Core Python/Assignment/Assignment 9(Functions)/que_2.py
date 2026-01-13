# WAP to check if given number is Armstrong or not using recursive function.

def count_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_digits(num // 10)
    

def check_armstrong(num,digit):
    if num == 0:
        return 0
    else:
        return ((num % 10) ** digit) + check_armstrong(num // 10,digit)
    
num = int(input("Enter the number : "))

digit = count_digits(num)
sum = check_armstrong(num,digit)

if num == sum:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is an not Armstrong Number")