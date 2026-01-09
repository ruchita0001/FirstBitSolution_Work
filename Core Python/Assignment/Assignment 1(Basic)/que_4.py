# Write a program to enter P, T, R and calculate simple Interest.

# SI = (P * T * R) / 100
# Where P = Principal, T = Time (in years), R = Rate (per annum)

P = int(input("Enter Principal (P): "))
T = int(input("Enter Time in years (T): "))
R = int(input("Enter Rate per annum (R): "))

# Calculate Simple Interest
Simple_Interest = (P * T * R) / 100

print('Simple_Interest:', Simple_Interest)