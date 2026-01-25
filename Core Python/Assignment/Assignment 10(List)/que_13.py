#WAAP to print list after removing even numbers.

li = [1, 2, 3, 4, 5, 6]
new_list = []

for i in li:
    if i % 2 != 0:
        new_list.append(i)

print("After removing even:", new_list)
