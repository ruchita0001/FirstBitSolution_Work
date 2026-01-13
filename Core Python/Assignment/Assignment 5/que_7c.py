# (c) Geometric series (1 + 2 + 4 + 8 + … n terms)

n = int(input("Enter number of terms: "))

sum = 0
term = 1

for i in range(n):
    sum += term
    term = term * 2

print("Sum of geometric series =", sum)