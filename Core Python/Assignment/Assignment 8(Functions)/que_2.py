# WAP to calculate area of circle

n = int(input("radius of circle: "))

def circle_area(r):
    area = 3.142 * (r**2)
    return area

res = circle_area(n)
print("Area of circl: ", res)
