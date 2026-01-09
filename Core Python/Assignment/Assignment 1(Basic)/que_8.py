# Write a program to convert days into years, weeks and days.

# Input total days
total_days = int(input("Enter the number of days: "))

# Calculate years, weeks, and remaining days
years = total_days // 365
remaining_days_after_years = total_days % 365

weeks = remaining_days_after_years // 7
days = remaining_days_after_years % 7

# Display the result
print("Days:", int(total_days))
print("Years:", int(years))
print("Weeks:", int(weeks))
print("Days:", int(days))
