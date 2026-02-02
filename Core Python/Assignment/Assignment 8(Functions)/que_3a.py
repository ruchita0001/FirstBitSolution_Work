# WAP to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# a. 1+ 2 + 3 + 4+..... + n
n = int(input("Enter value of n: "))

def sum_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print("Sum of numbers: ",sum_n(n))

#print(f"Sum of number {n} is {sum_n(n)}")
