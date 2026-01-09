# Program to Find the Roots of a Quadratic Equation

# Input values
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Calculate discriminant
d = b*b - 4*a*c

# Check conditions
if d < 0:
    print("Roots are imaginary")
else:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print("Roots are:", x1, "and", x2)  