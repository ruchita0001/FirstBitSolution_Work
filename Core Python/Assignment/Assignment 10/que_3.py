#WAP to find the second largest element in the list.

li = [10, 5, 25, 8, 18]

largest = li[0]
second = li[0]

for i in li:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest =", second)
