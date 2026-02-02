# Sum of all odd numbers between 1 to n

n = int(input("Enter value of n: "))

def sum_odd(n):
    total=0
    for i in range(1, n+1):
        if i%2 != 0:
            total += i
    return total

print(f"sum of odd number {n} is {sum_odd(n)}")
