# WAP to print all numbers in a range divisible by a given number.

start = int(input('Enter start of range: '))
end = int(input('Enter end of range: '))
num = int(input('Enter the number to divide by: '))

for i in range(start, end + 1):
    if i % num == 0:
        print(i, end=" ")
