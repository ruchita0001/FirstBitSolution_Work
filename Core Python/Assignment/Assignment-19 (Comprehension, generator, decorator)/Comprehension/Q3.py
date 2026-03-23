# Count the number of spaces in a string (take input from user)

text = input('Enter a string: ')

space_count = sum(1 for ch in text if ch == ' ')

print('Number of spaces:', space_count)
