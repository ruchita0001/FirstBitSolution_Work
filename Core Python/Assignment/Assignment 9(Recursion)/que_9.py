#WAP to calculate the m to the power n using recursion.

m = int(input("Enter base (m): "))
n = int(input("Enter power (n): "))

def power(m, n):
    if (n == 0):      
        return 1
    return m * power(m, n-1)

print("Result:", power(m, n))
