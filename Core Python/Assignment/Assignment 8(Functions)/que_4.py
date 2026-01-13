# Sum of all odd numbers between 1 to n

def sumOfOdd(n):
    sum = 0

    for i in range(1,n+1):
        if i % 2 != 0:
            sum += i 
        
    return sum 

n = int(input("Enter the value of n : "))

res = sumOfOdd(n)

print(f"Sum of odd numbers between 1 to {n} is {res}")