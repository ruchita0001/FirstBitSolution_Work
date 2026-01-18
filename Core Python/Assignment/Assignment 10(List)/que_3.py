# WAP to find the second largest element in the list.
lst = [12, 45, 7, 89, 23, 56]

largest = lst[0]
second_largest = lst[0]

for num in lst:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element is:", second_largest)
