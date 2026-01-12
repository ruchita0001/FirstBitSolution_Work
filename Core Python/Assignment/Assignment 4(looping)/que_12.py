# Write a program to check if given number is Armstrong number or not.

from string import digits


n = int(input('Enter a number: '))
sum = 0
temp = n

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == n:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
    