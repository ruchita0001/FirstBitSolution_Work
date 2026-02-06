# Python Program to Sort the List According to the Second Element in Sublist

def sort_by_second(li):
    n = len(li)

    for i in range(n):
        for j in range(0, n-i-1):
            if li[j][1] > li[j+1][1]:
                li[j], li[j+1] = li[j+1], li[j]

    return li


li = [[1, 3], [4, 1], [2, 2], [5, 0]]

result = sort_by_second(li)
print("Sorted List:", result)
