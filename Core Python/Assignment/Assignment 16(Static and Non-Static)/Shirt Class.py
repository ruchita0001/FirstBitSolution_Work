class Shirt:

    sizePrice = {
        'small':0,
        'medium':10,
        'large':20,
        'xlarge':30
    }

    def __init__(self, sid=0, sname='', stype='', price=0, size='small'):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def applySizePrice(self):
        inc = Shirt.sizePrice[self.size]
        self.price = self.price + (self.price * inc)/100

    def showShirt(self):
        print(self.sid,self.sname,self.stype,self.size,self.price)

    def __del__(self):
        print('Shirt object destroyed')


s1 = Shirt(1,'Cotton','formal',1000,'large')

s1.applySizePrice()
s1.showShirt()
