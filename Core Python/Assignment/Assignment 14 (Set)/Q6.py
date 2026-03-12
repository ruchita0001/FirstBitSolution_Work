#WAP to find the two numbers whose product is maximum among all the pairs in a given list of numbers.
#Use the Python set.

num = [1, 5, 3, 9, 2]

s = set(num)

a = max(s)
s.remove(a)
b = max(s)

print('Numbers:', a, b)
print('Maximum product:', a * b)
