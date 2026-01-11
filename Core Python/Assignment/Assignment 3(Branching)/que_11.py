# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
    # a. Children below 12 = 30% discount 
    # b. Senior citizen (above 59) = 50% discount
    # c. Others need to pay full.

# Initialize total amount
total_amount = 0

# Loop to input age and ticket amount for 5 people
for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    ticket = float(input(f"Enter ticket amount for person {i+1}: "))

    # Apply discount based on age
    if age < 12:
        amount = ticket * 0.7      # 30% discount
    elif age > 59:
        amount = ticket * 0.5      # 50% discount
    else:
        amount = ticket            # No discount

    total_amount += amount

# Display total amount
print("Total amount to be paid for all 5 people:", total_amount)