#Write a program to print list after removing even numbers.

def remove_even(li):
    new_list = []

    for i in li:
        if i % 2 != 0:
            new_list.append(i)

    print("List after removing even numbers:", new_list)

li = [1, 2, 3, 4, 5, 6, 7]
remove_even(li)
