#WAP to check if entered number is a palindrome or not.

n = int(input("Enter a number: "))

def is_palindrome(n):
    original = n
    rev = 0
    
    while n>0:
        digit = n % 10
        rev + rev * 10 + digit
        n = n // 10
        
    if original == rev:
        return True
    else:
        return False

if is_palindrome(n):
    print("Palindrome number")
else:
    print("Not a Palindrome number")
