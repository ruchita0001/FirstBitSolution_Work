#Python Program to Find the Intersection of Two Lists

def intersection_list(li1, li2):
    inter = []

    for i in li1:
        if i in li2 and i not in inter:
            inter.append(i)
    return inter


li1 = [10, 20, 30, 40]
li2 = [30, 40, 50]

res = intersection_list(li1, li2)
print('Intersection of two lists:', res)