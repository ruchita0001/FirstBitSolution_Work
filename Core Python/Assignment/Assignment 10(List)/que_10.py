#Remove all occurrences of an element

li = [10, 20, 30, 20, 40]
num = int(input("Enter number to remove: "))

new_list = []

for i in li:
    if i != num:
        new_list.append(i)

print("Updated List:", new_list)
