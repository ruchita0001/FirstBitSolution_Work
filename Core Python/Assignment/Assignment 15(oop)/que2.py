# 2. Create a class Product with members as pid,pname,price and quantity.
# Add following methods: 
# d. Constructor (Support both parameterized and parameterless) 
# e. Destructor 
# f. ShowBook

class Product:
    def __init__(self, pid=None, pname=None, price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showBook(self):   
        return f'Product ID: {self.pid}\nProduct Name: {self.pname}\nPrice: {self.price}\nQuantity: {self.quantity}'

    def __del__(self):
        print('Product object destroyed')

p1 = Product(101, 'Mouse', 500, 10)
print(p1.showBook())
del p1
print('############################')

p2 = Product()
print(p2.showBook())
