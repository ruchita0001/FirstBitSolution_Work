# Convert distance from feet and inches to meters and centimeters

# Input distance in feet and inches
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

# Convert feet and inches to total inches 
total_inches = (feet * 12) + inches

# Convert inches to centimeters
centimeters = total_inches * 2.54

# Convert centimeters to meters and centimeters
meters = int(centimeters // 100)
remaining_cm = centimeters % 100

# Display result
print("Distance is:", meters, "meters and", remaining_cm, "centimeters")