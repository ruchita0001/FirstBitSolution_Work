#WAP that finds all pairs of elements in a list whose sum is equal to a given value.

n = [1, 2, 3, 4, 5, 6]
target = 7
seen = set()

for num in n:
    diff = target - num
    if diff in seen:
        print(diff, num)
    seen.add(num)
