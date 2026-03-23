from student import Student

class EnggStudent(Student):

    def __init__(self, branch='', internalMarks=0):
        super().__init__()
        self.branch = branch
        self.internalMarks = internalMarks

    def accept(self):
        super().accept()
        self.branch = input('Enter Branch: ')
        self.internalMarks = int(input('Enter Internal Marks: '))

    def display(self):
        super().display()
        print('Branch:', self.branch)
        print('Internal Marks:', self.internalMarks)
        print('Rank:', self.calculateRank())

    def calculateRank(self):
        total = (self.percentage + self.internalMarks) / 2

        if total >= 75:
            return 'Excellent'
        elif total >= 60:
            return 'Very Good'
        else:
            return 'Good'

    def __str__(self):
        return f'ID: {self.studentId}, Name: {self.name}, Branch: {self.branch}, Marks: {self.percentage}, Internal: {self.internalMarks}'
