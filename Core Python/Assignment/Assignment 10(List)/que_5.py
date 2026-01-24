#Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

li = [1, 2, 3, 2, 4, 2]
num = int(input())

count = 0
for i in li:
    if i == num:
        count += 1

if count > 0:
    print("Found", count, "times")
else:
    print("Not found")
