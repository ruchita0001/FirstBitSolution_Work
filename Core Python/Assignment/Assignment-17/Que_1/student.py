class Student:

    #Parameterized Constructor
    def __init__(self, studentId=0, name='', age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    #Accept Method
    def accept(self):
        self.studentId = int(input('Enter Student ID: '))
        self.name = input('Enter Name: ')
        self.age = int(input('Enter Age: '))
        self.percentage = float(input('Enter Percentage: '))

    #Display Method
    def display(self):
        print('Student ID:', self.studentId)
        print('Name:', self.name)
        print('Age:', self.age)
        print('Percentage:', self.percentage)
        print('Rank:', self.calculateRank())

    #CalculateRank Method
    def calculateRank(self):
        if self.percentage >= 75:
            return 'Distinction'
        elif self.percentage >= 60:
            return 'First Class'
        elif self.percentage >= 50:
            return 'Second Class'
        else:
            return 'Fail'

    #Override __str__ Method
    def __str__(self):
        return f'ID: {self.studentId}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}'
