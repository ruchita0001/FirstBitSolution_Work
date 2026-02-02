#WAP to reverse a number using recursion.

num = int(input("Enter number: "))

def reverse_num(n, rev=0):
    if (n == 0):           
        return rev

    d = n % 10
    rev = rev * 10 + d
    return reverse_num(n // 10, rev)

print("Reversed number:", reverse_num(num))
