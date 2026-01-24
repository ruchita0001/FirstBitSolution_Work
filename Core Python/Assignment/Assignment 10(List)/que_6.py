#WAP to remove duplicates from the list.

li = [1, 2, 2, 3, 4, 3, 5]
new = []

for i in li:
    found = False
    for j in new:
        if i == j:
            found = True
            break
    if not found:
        new.append(i)

print(new)
