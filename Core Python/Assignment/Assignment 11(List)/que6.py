#Python Program to Find the Union of two Lists

def union_list(li1, li2):
    union = []
    
    for i in li1:
        if i not in union:
            union.append(i)
            
    for i in li2:
        if i not in union:
            union.append(i)

    return union


li1 = [10, 20, 30, 40]
li2 = [30, 50, 60]

res = union_list(li1, li2)
print("Union of two lists:", res)
