# WAP to check if given number Strong Number.

n = int(input('Enter a number:'))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    
    fact = 1          # calculate factorial of digit
    for i in range(1, digit + 1):
        fact *= i
        
    sum += fact
    temp //= 10

if sum == n:
    print('Strong Number')
else:
    print('Not a Strong Number')