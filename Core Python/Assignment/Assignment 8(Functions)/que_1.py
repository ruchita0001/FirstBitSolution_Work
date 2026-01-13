#Write a program to calculate area of rectangle

def rectangleArea(l,b):
    area = l * b
    return area

length = int(input("Enter the length of rectangle : "))
breadth = int(input("Enter the breadth of rectangle : "))

res = rectangleArea(length,breadth)
print("Area of rectangle : ", res)
