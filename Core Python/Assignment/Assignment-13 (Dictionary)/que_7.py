#Python Program to Remove the Given Key from a Dictionary
d = {1: 'Python', 2: 'SQL', 3: 'Java'}

key = int(input("Enter key to remove: "))

if key in d:
    del d[key]
    print("Updated Dictionary:", d)
else:
    print("Key not found")
