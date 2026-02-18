#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

d = {}

n = int(input("Enter value of n: "))

for i in range(1, n+1):
    d[i] = i * i

print("Generated Dictionary:", d)
