# WAP to find the second largest element in the list.
li = [40, 90, 60, 20, 80, 10, 70]

max = li[0]
smax = 0
tmax = 0
for i in range(1, len(li)):
    if (li[i] > max):
        smax = max
        max = li[i]
    elif(li[i] > smax):
        smax = li[i]
    
print('maximum element is:', max)
print('second maximum element is:', smax)
