#WAP to print list after removing even numbers.

li = [10, 15, 20, 25, 30]
odd = []

for i in li:
    if (i % 2 != 0):
        odd.append(i)

print("List after removing even numbers:", odd)
