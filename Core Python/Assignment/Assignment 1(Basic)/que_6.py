# WAP to input two angles from user and find third angle of the triangle.

# Input two angles
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))

# Calculate third angle
angle3 = 180 - (angle1 + angle2)

# Display result
print("The third angle of the triangle is:", angle3)