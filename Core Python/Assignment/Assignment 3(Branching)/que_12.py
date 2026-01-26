# WAP to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a three-digit number: "))

a = num // 100       
b = (num // 10) % 10 
c = num % 10         

if a == c:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
