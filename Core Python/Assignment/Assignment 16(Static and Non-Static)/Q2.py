# Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

#Ans: 
class Product:

    discount = 10 

    def __init__(self, pid=0, pname='', price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print('Product ID:', self.pid)
        print('Product Name:', self.pname)
        print('Price:', self.price)
        print('Quantity:', self.quantity)

    def applyDiscount(self):
        d = (self.price * Product.discount) / 100
        self.price = self.price - d

    def __del__(self):
        print('Product object destroyed')


p1 = Product(101, 'Laptop', 50000, 2)

p1.showProduct()

p1.applyDiscount()

print('After Discount:')
p1.showProduct()
