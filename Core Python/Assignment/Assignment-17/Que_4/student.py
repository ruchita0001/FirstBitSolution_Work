class Student:

    def __init__(self, studentId=0, name='', age=0, percentage=0.0):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def __str__(self):
        return f'ID: {self.studentId}, Name: {self.name}, Age: {self.age}, Percentage: {self.percentage}'
