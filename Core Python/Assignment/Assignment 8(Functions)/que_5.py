# Sum of all prime numbers between 1 to n

n = int(input("Enter value of n: "))

def sum_prime(n):
    total = 0
    for num in range(2, n+1):
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        
        if prime:
            total += num
    
    return total

print("sum of prime numbers: ", sum_prime(n))
