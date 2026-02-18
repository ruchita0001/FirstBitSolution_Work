##Python Program to Concatenate Two Dictionaries Into One
d1 = {1:'a',2:'b'}
d2 = {3:'c',4:'d'}
new_dict = {}

for elem in d1:
    new_dict[elem]=d1[elem]

for elem in d2:
    new_dict[elem]=d2[elem]

print(new_dict)
