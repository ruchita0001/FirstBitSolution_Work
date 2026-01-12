# WAP to print all even numbers until n.

# Input the value of n
n = int(input('Enter a number: '))
print('Even numbers up to', n, 'are:')

# Loop from 1 to n
for i in range(1, n+1):
    if i % 2 == 0:  # Check if the number is divisible by 2
        print(i, end=' ')
