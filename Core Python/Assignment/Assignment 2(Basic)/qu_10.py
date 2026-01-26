# WAP to reverse three-digit number.

num = int(input("Enter a three-digit number: "))

a = num // 100       
b = (num // 10) % 10 
c = num % 10         

reverse = (c * 100) + (b * 10) + a
print("Reversed number =", reverse)
