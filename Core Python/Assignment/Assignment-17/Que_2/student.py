from person import Person

class Student(Person):
    def __init__(self):
        super().__init__()
        self.studentId = 0
        self.percentage = 0.0

    def accept(self):
        self.studentId = int(input('Enter Student ID: '))
        self.percentage = float(input('Enter Percentage: '))
        super().accept()

    def display(self):
        print('Student ID:', self.studentId)
        super().display()
        print('Percentage:', self.percentage)

    def calculateRank(self):
        if self.percentage >= 75:
            return 'Distinction'
        elif self.percentage >= 60:
            return 'First Class'
        else:
            return 'Second Class'
