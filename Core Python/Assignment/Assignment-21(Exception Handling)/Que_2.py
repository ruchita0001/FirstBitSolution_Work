class Television:

    def __init__(self):
        self.model = 0
        self.size = 0
        self.price = 0

    def accept(self):
        try:
            self.model = int(input('Enter Model Number: '))
            if len(str(self.model)) > 4:
                raise Exception('Model number must be 4 digits or less')

            self.size = int(input('Enter Screen Size (in inches): '))
            if self.size < 12 or self.size > 70:
                raise Exception('Screen size must be between 12 and 70')

            self.price = float(input('Enter Price: '))
            if self.price < 0 or self.price > 5000:
                raise Exception('Price must be between 0 and 5000')

        except Exception as e:
            print('Error:', e)
            print('Setting all values to 0')
            self.model = 0
            self.size = 0
            self.price = 0

    def display(self):
        print('\n--- Television Details ---')
        print('Model Number:', self.model)
        print('Screen Size:', self.size)
        print('Price:', self.price)


#Main
print('--- Enter Television Details ---')

t = Television()
t.accept()

t.display()
