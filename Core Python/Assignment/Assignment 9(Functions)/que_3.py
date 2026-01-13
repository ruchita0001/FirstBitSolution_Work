# WAP to reverse a given number using recursive function.

def reverseNumber(num,rev=0):
    if num == 0:
        return rev
    else:
        return reverseNumber(num // 10, rev * 10 + (num % 10))
    

num = int(input("Enter the Number : "))
res = reverseNumber(num)
print(f"Reverse of {num} = {res}")