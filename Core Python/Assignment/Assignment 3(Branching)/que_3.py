# WAP to input angles of a triangle and check whether triangle is valid or not.

# Rule:
# Sum of all three angles = 180°
# Each angle > 0

angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

# Check validity
if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1 + angle2 + angle3 == 180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")
