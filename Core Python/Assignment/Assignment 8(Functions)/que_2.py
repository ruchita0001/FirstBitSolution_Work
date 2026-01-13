# WAP to calculate area of circle

def circleArea(r):
    area = 3.142 * (r**2)
    return area


radius = int(input("Enter radius of circle : "))
res = circleArea(radius)
print("Area of circle : ", res)