# b. 1!+ 2! + 3! + 4!+..... + n!

def sumOfFactorialSeries(n):
    
    for i in range(1,n+1):
        sum = 0
        fact = 1

        for j in range(1,i+1):
            fact *= j
            sum += fact

    return sum

n = int(input("Enter the value of n : "))

res = sumOfFactorialSeries(n)

print(f"Sum of series of Factorial numbers upto {n} is {res}")