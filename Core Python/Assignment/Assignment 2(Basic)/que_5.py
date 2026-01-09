# WAP to calculate selling price of book based on cost price and discount.

#Formula:
#Selling Price = Cost Price − Discount

cost_price = int(input("Enter cost price: "))
discount = int(input("Enter discount: "))

selling_price = cost_price - discount

print("Selling Price =", selling_price)