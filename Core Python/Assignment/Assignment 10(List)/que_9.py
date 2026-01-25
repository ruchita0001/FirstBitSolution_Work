#Separate Even and Odd

li = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even list:", even)
print("Odd list:", odd)
