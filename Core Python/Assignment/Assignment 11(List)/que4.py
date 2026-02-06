#Python Program to Find the Second Largest Number in a List Using Bubble Sort

li = [60, 40, 50, 10, 30, 20]

def second_largest(li):
    n = len(li)
    for i in range(n):
        for j in range(0, n - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

    return li[n - 2]

res = second_largest(li)
print("Second Largest Element:", res)