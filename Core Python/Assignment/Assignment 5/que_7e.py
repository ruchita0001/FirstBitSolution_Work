# (e) x − x²/3 + x³/5 − x⁴/7 + … n terms

x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0
sign = 1
den = 1

for i in range(1, n+1):
    sum += sign * (x ** i) / den
    sign *= -1
    den += 2

print("Sum of series =", sum)
