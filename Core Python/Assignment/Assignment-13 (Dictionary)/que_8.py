#Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
st = input("Enter string: ")

words = st.split()

d = {}

for i in words:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print("Word Frequency:", d)
