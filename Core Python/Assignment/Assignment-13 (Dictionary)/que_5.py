#Python Program to Sum All the Items in a Dictionary
d = {1: 100, 2: 200, 3: 300}

total = 0

for i in d:
    total = total + d[i]

print("Sum of values:", total)
