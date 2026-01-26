# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
    # a. Children below 12 = 30% discount 
    # b. Senior citizen (above 59) = 50% discount
    # c. Others need to pay full.

total_amount = 0
for i in range(1, 6):
    print("Person", i)
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))
    if age < 12:
        final = ticket - (ticket * 0.30)
        print("Child discount applied") 
    elif age > 59:
        final = ticket - (ticket * 0.50)
        print("Senior citizen discount applied") 
    else:
        final = ticket
        print("Full ticket price")
    print("Amount to pay:", final)
    total_amount += final

print("Total amount for all 5 people =", total_amount)
