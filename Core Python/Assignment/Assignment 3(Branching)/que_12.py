# WAP to check if given 3 digit number is a palindrome or not.

# Input a three-digit number
num = int(input("Enter a three-digit number: "))

# Extract digits
a = num // 100       # hundreds place
b = (num // 10) % 10 # tens place
c = num % 10         # units place

# Check palindrome
if a == c:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
