# Accept no. of passengers from user and per ticket cost. Then accept age of eachpassenger and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

n = int(input("Enter the number of Passengers : "))

total = 0 

for i in range(1, n+1):
    cost = int(input(f"Enter the Passenger {i} ticket cost : "))
    age = int(input(f"Enter the Passenger {i} Age : "))

    if age < 12:
        ticket = cost * 0.30
    elif age > 59:
        ticket = cost * 0.50
    else:
        ticket = cost

    total += ticket
    
print(f"Total amount of ticket to travel {n} passengers is {total}")