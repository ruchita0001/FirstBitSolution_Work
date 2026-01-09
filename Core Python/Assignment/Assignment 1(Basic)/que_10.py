# Write a program to calculate area of an equilateral triangle.

# Input the side of the equilateral triangle
side = int(input("Enter the side of the equilateral triangle: "))

# Approximate value of square root of 3
sqrt3 = 1.732

# Calculate area using formula: (√3 / 4) * side^2
area = (sqrt3 / 4) * (side ** 2)

# Display the result
print("The area of the equilateral triangle is:", area)