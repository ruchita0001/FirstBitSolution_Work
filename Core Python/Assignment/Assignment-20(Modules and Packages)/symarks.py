class SYMarks:

    def __init__(self, computer=0, maths=0, electronics=0):
        self.computer = computer
        self.maths = maths
        self.electronics = electronics

    def accept(self):
        self.computer = int(input('Enter SY Computer Marks: '))
        self.maths = int(input('Enter SY Maths Marks: '))
        self.electronics = int(input('Enter SY Electronics Marks: '))

    def total(self):
        return self.computer + self.maths + self.electronics
