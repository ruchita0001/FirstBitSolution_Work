#WAP to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

n = [1,2,3,4,5,6]
t = 10
s = set(n)

for i in n:
    for j in n:
        k = t - i - j
        if k in s and i < j < k:
            print(i, j, k)
