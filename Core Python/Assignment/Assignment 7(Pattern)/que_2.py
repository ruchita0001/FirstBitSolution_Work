# pyramid of stars increasing then decreasing

* 
* * 
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

n = 5  
# Top half (increasing stars)
for i in range(1, n+1):
    print("* " * i)

# Bottom half (decreasing stars)
for i in range(n-1, 0, -1):
    print("* " * i)
