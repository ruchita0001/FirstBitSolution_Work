# Python Program to Merge Two Lists and Sort it
li1 = [5, 2, 8]
li2 = [1, 9, 3]

def merge_and_sort(li1, li2):
    merged = []
    
    for i in li1:
        merged.append(i)
    for i in li2:
        merged.append(i)

    n = len(merged)
    for i in range(n):
        for j in range(0, n-i-1):
            if merged[j] > merged[j+1]:
                merged[j], merged[j+1] = merged[j+1], merged[j]

    return merged

result = merge_and_sort(li1, li2)
print("Merged and Sorted List:", result)
