# WAP to find sum of digits using recursion.

num = int(input("Enter number: "))
def sum_digits(n):
    if n == 0:      
        return 0
    return (n % 10) + sum_digits(n // 10)

res = sum_digits(num) 
print(f"Sum of digits {num} is {res}")
