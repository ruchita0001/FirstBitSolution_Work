# Replace all Occurrences of ‘a’ with $ in a String
s = input('Enter a string: ')
result = ''

for ch in s:
    if ch == 'a':
        result = result + '$'
    else:
        result = result + ch

print('Updated String:', result)


               #Or
# s = input("Enter a string: ")
# new_string = s.replace('a', '$')
# print("Updated String:", new_string)
