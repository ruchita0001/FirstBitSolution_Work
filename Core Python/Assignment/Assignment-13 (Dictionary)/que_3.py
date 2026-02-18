#Python Program to Check if a Given Key Exists in a Dictionary or Not
d = {1: 'Python', 2: 'SQL', 3: 'Java'}

key = int(input("Enter key to check: "))

if key in d:
    print("Key exists in dictionary")
else:
    print("Key does not exist")
