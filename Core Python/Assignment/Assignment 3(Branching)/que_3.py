# WAP to input angles of a triangle and check whether triangle is valid or not.

a = int(input("Enter angle a:"))
b = int(input("Enter angle b:"))
c = int(input("Enter angle c:"))

if a + b + c == 180 and a>0 and b>0 and c>0:
    print("The triangle is valid")
else:
    print("The triangle is not valid")
