class Product:

    discount = 10   # static variable

    def __init__(self, pid=0, pname='', price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def applyDiscount(self):
        d = (self.price * Product.discount)/100
        self.price = self.price - d

    def showProduct(self):
        print(self.pid, self.pname, self.price, self.quantity)

    def __del__(self):
        print('Product object destroyed')


p1 = Product(101,'Laptop',50000,2)

p1.applyDiscount()
p1.showProduct()
