# Remove the Characters of Odd Index Values in a String
def removeOddIndex(str1):
    return str1[::2]

str1 = input('Enter a string: ')
print(removeOddIndex(str1))
