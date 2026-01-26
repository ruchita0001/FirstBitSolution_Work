# Program to Find the Roots of a Quadratic Equation

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = b*b - 4*a*c  

r1 = (-b + D**0.5) / (2*a)
r2 = (-b - D**0.5) / (2*a)

print("Root 1 =", r1)
print("Root 2 =", r2)
