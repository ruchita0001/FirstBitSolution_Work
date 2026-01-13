#WAP to check if entered number is a palindrome or not.

def reverseNumber(num):
    temp = num
    rev = 0
    while(num > 0):
        d = num % 10
        rev = rev * 10 + d 
        num = num // 10

    if temp == rev:
        return "Number is palindrome"
    else:
        return "Number is not palindrome"



num = int(input("Enter the Number : "))

print(reverseNumber(num))