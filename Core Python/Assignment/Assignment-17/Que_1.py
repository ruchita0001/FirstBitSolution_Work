class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    def setData(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))

    def displayData(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
        
class Student(Person):
    def __init__(self):
        super().__init__()
        self.studentId = 0
        self.percentage = 0.0

    def setStudentData(self):
        self.studentId = int(input('Enter Student ID: '))
        self.percentage = float(input('Enter Percentage: '))
        super().setData()

    def displayStudentData(self):
        print("Student ID:", self.studentId)
        super().displayData()
        print("Percentage:", self.percentage)
        
        
s1 = Student()
s1.setStudentData()
print('\n--- Student Details ---')
s1.displayStudentData()
