# Python Program to Detect if Two Strings are Anagrams

def check_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if sorted(s1) == sorted(s2):
        return 'Strings are Anagrams'
    else:
        return 'Strings are Not Anagrams'


str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

result = check_anagram(str1, str2)
print(result)
