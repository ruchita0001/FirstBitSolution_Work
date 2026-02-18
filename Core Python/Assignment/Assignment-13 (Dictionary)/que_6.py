#Python Program to Multiply All the Items in a Dictionary
d = {1: 2, 2: 3, 3: 4}

mul = 1

for i in d:
    mul = mul * d[i]

print("Multiplication of values:", mul)
