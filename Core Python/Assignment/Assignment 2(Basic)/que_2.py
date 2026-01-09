# Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# Input temperature in Celsius
# Formula: C/5 = (F-32)/9
# Rearranged: F = (C * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

# Display result using f-string
print(f"{celsius}°C = {fahrenheit}°F")