class Book:
    count = 0 
    def __init__(self, bid=0, bname='', price=0, author=''):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def showBook(self):
        print('Book ID:', self.bid)
        print('Book Name:', self.bname)
        print('Price:', self.price)
        print('Author:', self.author)

    def __del__(self):
        print('Book object destroyed')


b1 = Book(1,'Python',500,'Guido')
b2 = Book(2,'Java',400,'James')

b1.showBook()
b2.showBook()

print('Total objects created:', Book.count)
