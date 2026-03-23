class Complex:

    #Constructor
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    #Destructor
    def __del__(self):
        print('Object destroyed')

    #Overload + Operator
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)

    #Overload - Operator
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i)

    #Display
    def display(self):
        print(f'{self.real} + {self.imag}i')
