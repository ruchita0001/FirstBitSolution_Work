#Python Program to Form a New String where the First Character and the Last Character have been Exchanged

def swapFirstLast(s):
    
    if len(s) <= 1:
        return s
    
    newString = s[-1] + s[1:-1] + s[0]
    
    return newString

str1 = input('Enter a string: ')
res = swapFirstLast(str1)
print(res)
