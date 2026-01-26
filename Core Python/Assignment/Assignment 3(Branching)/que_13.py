# WAP to input electricity unit charges and calculate total electricity bill according to the given condition:
    # For first 50 units Rs. 0.50/unit
    # For next 100 units Rs. 0.75/unit
    # For next 100 units Rs. 1.20/unit
    # For unit above 250 Rs. 1.50/unit
    # An additional surcharge of 20% is added to the bill
    
units = int(input("Enter number of units consumed: "))
bill = 0

if units <= 50:
    bill = units * 0.5
else:
    bill = 50 * 0.5
    if units <= 150:
        bill += (units - 50) * 0.75
    else:
        bill += 100 * 0.75
        if units <= 250:
            bill += (units - 150) * 1.2
        else:
            bill += 100 * 1.2
            bill += (units - 250) * 1.5
bill = bill + (0.2 * bill)
print("Total electricity bill: Rs.", bill)
