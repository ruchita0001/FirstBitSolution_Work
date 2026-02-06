#Python Program to Sort a List According to the Length of the Elements within the list.

li = ['apple', 'kiwi', 'banana', 'fig', 'grapes']

def sort_by_length(li):
    n = len(li)

    for i in range(n):
        for j in range(0, n - i - 1):
            if len(li[j]) > len(li[j + 1]):
                li[j], li[j + 1] = li[j + 1], li[j]

    return li

res = sort_by_length(li)
print('Sorted List:', res)
