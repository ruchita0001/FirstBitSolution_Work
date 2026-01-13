#WAP find reverse of a number

def reverseNumber(num):
 
    rev = 0
    while(num > 0):
        d = num % 10
        rev = rev * 10 + d 
        num = num // 10

    return rev


num = int(input("Enter the Number : "))

res = reverseNumber(num)

print(f"Reverse of {num} = {res}")