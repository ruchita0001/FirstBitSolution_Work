# Find the sum of three-digit number.

num = int(input("Enter a three-digit number: "))

a = num // 100        # first digit
b = (num // 10) % 10  # second digit
c = num % 10          # third digit

sum = a + b + c

print("Sum of digits =", sum)