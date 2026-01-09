# Write a program to enter P, T, R and calculate Compound Interest.

P = float(input("Enter Principal (₹): "))
T = float(input("Enter Time (years): "))
R = float(input("Enter Rate (% per year): "))

# Calculate compound interest
A = P * (1 + R/100) ** T
CI = A - P

# Print result
print("Compound Interest =", CI)