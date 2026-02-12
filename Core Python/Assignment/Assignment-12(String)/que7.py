#Calculate the Length of a String Without Using a Library Function

def findLength(str1):
    count = 0
    for ch in str1:
        count = count + 1
    return count
  
str1 = input('Enter a string: ')
res = findLength(str1)
print('Length of string is:', res)
