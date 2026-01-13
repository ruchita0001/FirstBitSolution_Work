# Enter number of students from user. For those many students accept marks of 5 subject marks from user and calculate percentage. Display all percentage and average percentage of students.

n = int(input("Enter the number of students : "))

total_perc = 0

for i in range(1,n+1):
    total = 0

    print("Enter the 5 subject marks of Student ",i)
    for j in range(1,6):
        m = int(input(f"Enter the marks of subject {j}  : "))
        total += m
       
    perc = (total / 500) * 100
    print(f"Percentage of Student {i} : {perc}%")

    total_perc += perc

avg = total_perc / n 
print(f"Avarage Percentage of {n} students is {avg}%")
    
