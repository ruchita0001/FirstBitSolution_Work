#Write a program to create three lists of numbers, their squares and cubes

def square_cube_list(li):
    sq = []
    cube = []

    for i in li:
        sq.append(i * i)
        cube.append(i * i * i)

    print("Numbers:", li)
    print("Squares:", sq)
    print("Cubes:", cube)


li = [1, 2, 3, 4, 5]
square_cube_list(li)