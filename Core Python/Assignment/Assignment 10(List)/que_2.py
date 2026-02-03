# WAP to find maximum and minimum element in a list.

li = [40, 10, 60, 20, 80]

max = li[0]
min = li[0]

for i in range(1, len(li)):
    if (li[i] > max):
        max = li[i]
    if (li[i] < min):
        min = li[i]

print("Max =", max)
print("Min =", min)
