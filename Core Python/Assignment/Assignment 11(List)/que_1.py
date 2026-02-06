#Python Program to Put Even and Odd elements of a List into two Different Lists

def even_odd_list(li):
    even =[]
    odd = []
    for i in range(len(li)):
        if(li[i] % 2 == 0):
            even.append(li[i])
        else:
            odd.append(li[i])

    print('Even elements:',even)
    print('Odd elements:',odd)


li = [10, 15, 22, 33, 40, 55]
even_odd_list(li)
