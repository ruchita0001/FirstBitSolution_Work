# WAP to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("The triangle is valid")
else:
    print("The triangle is not valid")