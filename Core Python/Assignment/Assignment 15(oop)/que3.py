# Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc).
# Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    def __init__(self, sid=202, sname='Girls style', type='Formal', price=2500, size='Free'):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def showBook(self):  
        return f'Shirt ID: {self.sid}\nShirt Name: {self.sname}\nType: {self.type}\nPrice: {self.price}\nSize: {self.size}'

    def __del__(self):
        print('Shirt object destroyed')
        
        
s1 = Shirt(201, 'Office Wear', 'Formal', 1200, 'Large')
print(s1.showBook())
del s1
print('#-----------//*//---------#')

p2 = Shirt()
print(p2.showBook())
