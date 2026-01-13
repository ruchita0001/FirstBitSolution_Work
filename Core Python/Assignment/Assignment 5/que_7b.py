# (b) N + N² + N³ + … + Nⁿ

N = int(input("Enter N: "))

sum = 0

for i in range(1, N+1):
    sum += N ** i

print("Sum of series =", sum)