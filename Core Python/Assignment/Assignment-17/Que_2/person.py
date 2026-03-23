class Person:
    def __init__(self):
        self.name = ''
        self.age = 0

    def accept(self):
        self.name = input('Enter Name: ')
        self.age = int(input('Enter Age: '))

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)
