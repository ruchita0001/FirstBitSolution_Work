#Use a dictionary comprehension to count the length of each word in a sentence (take input from user)

text = input('Enter a sentence: ')
words = text.split()
result = {word: len(word) for word in words}
print('Word Length Dictionary:', result)
