from SY.symarks import SYMarks
from TY.tymarks import TYMarks

class Student:

    def __init__(self, roll=0, name=''):
        self.roll = roll
        self.name = name
        self.sy = SYMarks()
        self.ty = TYMarks()

    def accept(self):
        self.roll = int(input('Enter Roll No: '))
        self.name = input('Enter Name: ')
        self.sy.accept()
        self.ty.accept()

    def calculate(self):
        total = self.sy.total() + self.ty.total()
        percentage = total / 5

        if percentage >= 70:
            grade = 'A'
        elif percentage >= 60:
            grade = 'B'
        elif percentage >= 50:
            grade = 'C'
        elif percentage >= 40:
            grade = 'Pass Class'
        else:
            grade = 'Fail'

        return total, percentage, grade

    def display(self):
        total, per, grade = self.calculate()

        print('\n--- Student Result ---')
        print('Roll No:', self.roll)
        print('Name:', self.name)
        print('Total Marks:', total)
        print('Percentage:', per)
        print('Grade:', grade)
