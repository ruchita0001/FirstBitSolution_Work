#Implement a generator function that yields palindrome numbers.
#Palindromes are numbers that read the same backward as forward
#(e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindrome_generator():
    num = 0

    while True:
        if str(num) == str(num)[::-1]:
            yield num
        num += 1


# Usage (limit control manually)
gen = palindrome_generator()

for _ in range(15):   # first 15 palindrome numbers
    print(next(gen), end=' ')
