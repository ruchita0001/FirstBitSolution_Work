#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa.
#Use the Python set.

a = {1,2,3,4,5}
b = {2,3,6}

print('Missing in second set:', a - b)
print('Missing in first set:', b - a)
