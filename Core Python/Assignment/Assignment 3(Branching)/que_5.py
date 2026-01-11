# WAP to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

# First check if triangle is valid
if (a + b > c) and (a + c > b) and (b + c > a):
    
    if a == b == c:
        print("The triangle is equilateral")
    elif a == b or b == c or a == c:
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")
        
else:
    print("The triangle is not valid")