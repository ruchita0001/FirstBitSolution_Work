from student import Student

class MedicalStudent(Student):

    #Parameterized Constructor
    def __init__(self, studentId=0, name='', age=0, percentage=0.0, specialization='', marksOfInternship=0):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    #Accept Method
    def accept(self):
        super().accept()
        self.specialization = input('Enter Specialization: ')
        self.marksOfInternship = int(input('Enter Internship Marks: '))

    #Display Method
    def display(self):
        super().display()
        print('Specialization:', self.specialization)
        print('Internship Marks:', self.marksOfInternship)
        print('Rank:', self.calculateRank())

    #Override Method
    def calculateRank(self):
        total = (self.percentage + self.marksOfInternship) / 2

        if total >= 75:
            return 'Excellent'
        elif total >= 60:
            return 'Very Good'
        else:
            return 'Good'
