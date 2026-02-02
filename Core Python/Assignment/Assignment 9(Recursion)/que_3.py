# WAP to reverse a given number using recursive function.

num = int(input("Enter the Number : "))

def rev_num(n, rev=0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit
    return rev_num(n // 10, rev)

res = rev_num(num)
print(f"Reverse of {num} is {res}")
