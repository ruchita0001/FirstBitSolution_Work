#Count the Number of Vowels in a String

def countVowels(str1):
    
    count = 0
    for ch in str1:
        if ch in 'aeiouAEIOU':
            count = count + 1
    return count

str1 = input('Enter a string: ')
print(countVowels(str1))
