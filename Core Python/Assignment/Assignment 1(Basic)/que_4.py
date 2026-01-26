# Write a program to enter P, T, R and calculate simple Interest.

P = int(input("Enter Principal: "))
T = int(input("Enter Time in years: "))
R = int(input("Enter Rate per annum: "))

SI = (P * T * R) / 100

print('Simple Interest:', SI)
