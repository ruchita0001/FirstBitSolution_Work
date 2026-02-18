#Python Program to Add a Key-Value Pair to the Dictionary
d = {1: 'Python', 2: 'SQL'}

key = int(input("Enter key: "))
value = input("Enter value: ")

d[key] = value

print("Updated Dictionary:", d)
