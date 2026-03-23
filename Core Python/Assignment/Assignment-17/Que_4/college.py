from student import Student

class College:

    # ✅ Parameterized Constructor
    def __init__(self, size):
        self.students = []
        self.size = size

    #Add Student
    def addStudent(self, student):
        if len(self.students) < self.size:
            self.students.append(student)
            print('Student added successfully')
        else:
            print('College is full')

    #Get Student (by ID)
    def getStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                return s
        return None

    #Remove Student (by ID)
    def removeStudent(self, studentId):
        for s in self.students:
            if s.studentId == studentId:
                self.students.remove(s)
                print('Student removed')
                return
        print('Student not found')

    #Override __str__
    def __str__(self):
        result = '--- College Students ---\n'
        for s in self.students:
            result += str(s) + '\n'
        return result
