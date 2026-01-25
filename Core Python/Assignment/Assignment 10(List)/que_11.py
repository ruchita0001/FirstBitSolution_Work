#Numbers divisible by m and n

li = [10, 15, 20, 30, 40, 60]
m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in li:
    if i % m == 0 and i % n == 0:
        print(i, "is divisible by both")
