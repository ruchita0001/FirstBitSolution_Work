# Create a class Book with members as bid,bname,price and author.Add following methods: 
# a. Constructor (Support both parameterized and parameterless) 
# b. Destructor 
# c. ShowBook

class Book:
    def __init__(self, bid=1110001, book_name='Java', price=540, author=None):
        self.bid = bid
        self.bname = book_name
        self.price = price
        self.author = author

    def showBook(self):
        return f"Book ID: {self.bid}\nBook Name: {self.bname}\nPrice: {self.price}\nAuthor: {self.author}"

    def __del__(self):
        print('Book object destroyed')

b1 = Book(1001, 'Python', 350, 'ABC')
print(b1.showBook())
del b1
print('---------------------------------------------------')

b2 = Book()
print(b2.showBook())
