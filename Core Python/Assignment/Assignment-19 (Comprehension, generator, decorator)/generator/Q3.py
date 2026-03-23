#Write a generator function that mimics the behavior of the built-in range() function.
#The generator should take start, stop, and step arguments and yield numbers within the specified range.

def my_range(start, stop, step=1):

    if step == 0:
        print('Step cannot be zero')
        return

    if step > 0:
        while start < stop:
            yield start
            start += step
    else:
        while start > stop:
            yield start
            start += step


# Usage
for i in my_range(1, 10, 2):
    print(i, end=' ')
