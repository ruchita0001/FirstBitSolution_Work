# c. 1^1 + 2^2 + 3^3+ ...... n^n

n = int(input("Enter value of n: "))

def sum_pow(n):
    sum=0
    for i in range(1, n+1):
        sum += i**i
    return sum

print(f"Sum of power of series {n} is {sum_pow(n)}")
