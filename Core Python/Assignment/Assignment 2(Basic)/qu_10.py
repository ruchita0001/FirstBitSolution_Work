# WAP to reverse three-digit number.

num = int(input("Enter a three-digit number: "))

a = num // 100        # first digit
b = (num // 10) % 10  # middle digit
c = num % 10          # last digit

reverse = (c * 100) + (b * 10) + a

print("Reversed number =", reverse)