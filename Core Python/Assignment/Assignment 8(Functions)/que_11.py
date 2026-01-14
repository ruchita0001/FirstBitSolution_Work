# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

# To count number of digits
def count_digits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count


# To find power of a number
def power(base, exp):
    result = 1
    for i in range(exp):
        result = result * base
    return result


# To check Armstrong number
def check_armstrong(num):
    temp = num
    digits = count_digits(num)
    total = 0

    while temp > 0:
        rem = temp % 10
        total = total + power(rem, digits)
        temp = temp // 10

    if total == num:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


# Main program
n = int(input("Enter a number: "))
check_armstrong(n)

