#Find all of the words in a string that are less than 5 letters (take input from user)

text = input('Enter a string: ')
words = text.split()
res = [word for word in words if len(word) < 5]
print('Words less than 5 letters:', res)
