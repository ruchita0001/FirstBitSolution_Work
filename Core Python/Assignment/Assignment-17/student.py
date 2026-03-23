class Student:

    def __init__(self, studentId=0, name='', age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def accept(self):
        self.studentId = int(input('Enter Student ID: '))
        self.name = input('Enter Name: ')
        self.age = int(input('Enter Age: '))
        self.percentage = float(input('Enter Percentage: '))

    def display(self):
        print('Student ID:', self.studentId)
        print('Name:', self.name)
        print('Age:', self.age)
        print('Percentage:', self.percentage)

    def calculateRank(self):
        if self.percentage >= 75:
            return 'Distinction'
        elif self.percentage >= 60:
            return 'First Class'
        else:
            return 'Pass'
