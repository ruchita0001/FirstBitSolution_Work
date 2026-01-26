# Convert distance from feet and inches to meters and centimeters

feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))
total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54

meters = int(centimeters // 100)
remaining_cm = centimeters % 100
print("Distance is:", meters, "meters and", remaining_cm, "centimeters")
