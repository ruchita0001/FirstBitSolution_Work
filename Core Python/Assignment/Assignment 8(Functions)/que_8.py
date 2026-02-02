#WAP find reverse of a number

n = int(input("Enter a number: "))

def rev_number(n):
    rev = 0
    while n > 0:
        d = n % 10
        rev = rev * 10 + d
        n = n // 10 
     
    return rev

res = rev_number(n)
print(f"Reverse of {n} = {res}")
