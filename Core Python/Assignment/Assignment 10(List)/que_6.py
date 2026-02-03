#WAP to remove duplicates from the list.

li = [10, 20, 10, 30, 20, 40]
new = []

for i in li:
    found = False
    for j in new:
        if (i == j):
            found = True
            break
    if not found:
        new.append(i)

print("After removing duplicates:", new)
