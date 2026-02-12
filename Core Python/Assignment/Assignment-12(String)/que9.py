#Calculate the Number of Words and the Number of Characters Present in a String

def countWordsAndChars(str1):
    
    charCount = len(str1)
    wordCount = len(str1.split())
    
    return wordCount, charCount

str1 = input('Enter a string: ')
words, chars = countWordsAndChars(str1)

print('Number of words:', words)
print('Number of characters:', chars)
