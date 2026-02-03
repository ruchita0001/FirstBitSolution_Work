#Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

li = [10, 20, 30, 20, 40]
num = int(input("Enter number: "))

count = 0
for i in li:
    if (i == num):
        count += 1

if (count > 0):
    print("Present", count, "times")
else:
    print("Not Present")
