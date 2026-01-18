# WAP to find maximum and minimum element in a list.

lst = [12, 45, 7, 89, 23, 56]
max_val = lst[0]
min_val = lst[0]
for i in lst:
    if i > max_val:
        max_val = i
    if i < min_val:
        min_val = i

print("Maximum element is:", max_val)
print("Minimum element is:", min_val)


