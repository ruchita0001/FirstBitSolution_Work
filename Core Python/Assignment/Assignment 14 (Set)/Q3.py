#WAP program to find all the unique words and count the frequency of occurrence from a given list of strings.
#Use Python set data type.

n = ['Riya Priya Raj', 'banana orange Raj']

words = ' '.join(n).split()
for w in set(words):
    print(w, ':', words.count(w))
