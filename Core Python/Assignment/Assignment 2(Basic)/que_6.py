# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

# Given:
# DA = 10% of basic
# TA = 12% of basic
# HRA = 15% of basic

basic = int(input("Enter basic salary: "))

da = (10 * basic) / 100
ta = (12 * basic) / 100
hra = (15 * basic) / 100

total_salary = basic + da + ta + hra

print("Total Salary =", total_salary)