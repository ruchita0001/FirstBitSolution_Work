# WAP to find all the anagrams and group them together from a given list of strings.

s = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

d = {}

for w in s:
    k = ''.join(sorted(w))
    d.setdefault(k, []).append(w)

print(list(d.values()))
