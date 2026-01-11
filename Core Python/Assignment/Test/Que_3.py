# WAP to accept distance in km and convert it into meters and centimeters both.

# Accept distance in kilometers
km = float(input("Enter distance in kilometers: "))

# Convert to meters and centimeters
meters = km * 1000
centimeters = km * 100000

# Display result
print("Distance in meters:", meters)
print("Distance in centimeters:", centimeters)
