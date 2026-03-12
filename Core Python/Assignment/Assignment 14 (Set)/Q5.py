# WAP to find the longest common prefix of all strings. Use the Python set.

strings = ['flower', 'flow', 'flight']

prefix = ''

for i in range(len(strings[0])):
    temp = set()
    
    for s in strings:
        if i < len(s):
            temp.add(s[i])
    
    if len(temp) == 1:
        prefix += temp.pop()
    else:
        break

print('Longest common prefix:', prefix)
